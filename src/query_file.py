import time
import requests
from pathlib import Path
from ckanapi import RemoteCKAN
import pandas as pd
import numpy as np
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed

_TEMPO_LIMITE = 30
_MAX_TENTATIVAS = 5
_LIMIT_MAXIMO_REGISTROS_POR_PAGINA = 5000  # Blocos seguros para arquivos grandes (>1GB)
_LIMIT_NULOS_POR_COLUNA = 50
_LIMIT_DISTINTOS_POR_COLUNA = 50
_MAX_WORKERS = 2  # Número seguro de subprocessos paralelos para evitar bloqueios/rate-limit na API

# Tentativa de importação das bibliotecas para conversão de PDF
try:
  import markdown
  from weasyprint import HTML
  SUPORTE_PDF = True
except ImportError:
  SUPORTE_PDF = False


def _baixar_pagina_com_retry(rc, res_id, limit, offset, pagina_atual):
  """Função auxiliar isolada para executar o loop de retry com tqdm por página."""
  sucesso_requisicao = False
  inicio_req = time.time()
  ds_res = None

  with tqdm(total=_MAX_TENTATIVAS, desc=f"   Tentativa (pág. {pagina_atual})", leave=False) as pbar_req:
    for tentativa in range(1, _MAX_TENTATIVAS + 1):
      if time.time() - inicio_req > _TEMPO_LIMITE:
        break
      try:
        ds_res = rc.action.datastore_search(
            resource_id=res_id,
            limit=limit,
            offset=offset
        )
        sucesso_requisicao = True
        pbar_req.set_postfix(status="Sucesso!")
        pbar_req.update(_MAX_TENTATIVAS - pbar_req.n)
        break
      except requests.exceptions.RequestException:
        pbar_req.set_postfix(status=f"Falha (Tentativa {tentativa})")
        pbar_req.update(1)
        time.sleep(2)
      except Exception:
        pbar_req.set_postfix(status="Erro Inesperado")
        break

  return sucesso_requisicao, ds_res


def baixar_e_analisar_arquivo_grande(res_id, portal_url="https://dados.es.gov.br/"):
  """Conecta-se ao CKAN e baixa os dados utilizando paginação segura e loop de retry[cite: 6]."""
  rc = RemoteCKAN(portal_url)
  offset = 0
  all_records = []
  pagina_atual = 1
  colunas_referencia = None
  erros_estrutura = []

  print(f"\n🔍 Iniciando extração e auditoria estrutural do recurso: {res_id}")

  with tqdm(desc=f"📥 Baixando arquivo {res_id[:8]}", unit="reg") as pbar:
    while True:
      sucesso_requisicao, ds_res = _baixar_pagina_com_retry(
          rc, res_id, _LIMIT_MAXIMO_REGISTROS_POR_PAGINA, offset, pagina_atual
      )

      if not sucesso_requisicao:
        erros_estrutura.append(f"Timeout ou falha de rede na página {pagina_atual} (offset {offset}).")
        print(f"\n❌ [Erro Crítico] Falha ao acessar o recurso {res_id} na página {pagina_atual} após {_MAX_TENTATIVAS} tentativas.")
        break

      records = ds_res.get("records", [])
      fields = ds_res.get("fields", [])

      if not records:
        break

      colunas_pagina = [f["id"] for f in fields if f["id"] != "_id"]
      if colunas_referencia is None:
        colunas_referencia = set(colunas_pagina)
      else:
        colunas_atual_set = set(colunas_pagina)
        if colunas_referencia != colunas_atual_set:
          erros_estrutura.append(f"Divergência estrutural detectada na página {pagina_atual}: as colunas diferem do lote inicial.")

      all_records.extend(records)
      pbar.update(len(records))
      pbar.set_postfix(pagina=pagina_atual, total_acumulado=len(all_records))

      if len(records) < _LIMIT_MAXIMO_REGISTROS_POR_PAGINA:
        break

      offset += _LIMIT_MAXIMO_REGISTROS_POR_PAGINA
      pagina_atual += 1

  if not all_records:
    print("⚠️ Nenhum registro retornado para este arquivo.")
    return None, 0, [], erros_estrutura

  df = pd.DataFrame(all_records)
  if "_id" in df.columns:
    df = df.drop(columns=["_id"])

  total_linhas = len(df)
  colunas_ordenadas = sorted(df.columns)

  return df, total_linhas, colunas_ordenadas, erros_estrutura


def _calcular_estatisticas_bloco(args):
  """Função executada em subprocesso isolado para calcular estatísticas parciais

  de um subconjunto de colunas, evitando overflow numérico e garantindo consistência.
  """
  dados_dict, colunas_subset = args
  df_sub = pd.DataFrame(dados_dict)
  total_linhas_global = len(df_sub)
  resultados = {}

  for col in colunas_subset:
    try:
      serie = df_sub[col]
      nulos = int(serie.isna().sum())

      try:
        serie_val_str = serie.astype(str).str.strip().str.replace(',', '.', regex=False)
        zeros = int((pd.to_numeric(serie_val_str, errors='coerce') == 0.0).sum())
      except Exception:
        zeros = int((serie == 0).sum())

      distintos = int(serie.nunique(dropna=True))
      perc_nulos = (nulos / total_linhas_global * 100) if total_linhas_global > 0 else 0
      perc_zeros = (zeros / total_linhas_global * 100) if total_linhas_global > 0 else 0

      provavel_enum = (distintos <= _LIMIT_DISTINTOS_POR_COLUNA or (distintos / total_linhas_global < 0.05)) if total_linhas_global > 0 else False
      alerta_caso_1 = (nulos > _LIMIT_NULOS_POR_COLUNA) or (zeros > _LIMIT_NULOS_POR_COLUNA)
      alerta_caso_2 = (distintos > _LIMIT_DISTINTOS_POR_COLUNA)

      serie_limpa = serie.dropna()
      stats_col = None

      if len(serie_limpa) > 0:
        serie_str = serie_limpa.astype(str).str.strip().str.replace(',', '.', regex=False)
        serie_num = pd.to_numeric(serie_str, errors='coerce')

        if serie_num.notna().all() and len(serie_num) > 0:
          serie_num = serie_num.astype(np.float64)
          stats_col = {
              "tipo_estatistica": "numerica",
              "minimo": float(serie_num.min()),
              "maximo": float(serie_num.max()),
              "media": round(float(serie_num.mean()), 2),
              "mediana": float(serie_num.median()),
              "desvio_padrao": round(float(serie_num.std(ddof=0)), 2) if len(serie_num) > 1 else 0.0
          }
        else:
          tamanhos = serie_limpa.astype(str).str.len().astype(np.int64)
          if len(tamanhos) > 0:
            stats_col = {
                "tipo_estatistica": "texto",
                "min_length": int(tamanhos.min()),
                "max_length": int(tamanhos.max()),
                "mean_length": round(float(tamanhos.mean()), 2),
                "std_length": round(float(tamanhos.std(ddof=0)), 2) if len(tamanhos) > 1 else 0.0
            }

      resultados[col] = {
          "valores_nulos": nulos,
          "valores_zeros": zeros,
          "porcentagem_nulos": round(perc_nulos, 2),
          "porcentagem_zeros": round(perc_zeros, 2),
          "valores_distintos": distintos,
          "provavel_enum": provavel_enum,
          "alerta_caso_1": alerta_caso_1,
          "alerta_caso_2": alerta_caso_2,
          "estatisticas_coluna": stats_col,
          "status_analise": "sucesso"
      }
    except Exception:
      resultados[col] = {"status_analise": "insuficiente"}

  return resultados


def processar_estatisticas_paralelas(df, colunas_ordenadas):
  """Divide as colunas em blocos para execução paralela em subprocessos."""
  analise_colunas = {}
  num_workers = min(_MAX_WORKERS, len(colunas_ordenadas)) if colunas_ordenadas else 1
  if num_workers < 1:
    return analise_colunas

  chunks = np.array_split(colunas_ordenadas, num_workers)
  dados_dict = df.to_dict(orient='list')

  print(f"⚡ Processando estatísticas em paralelo usando {num_workers} subprocessos...")

  with ProcessPoolExecutor(max_workers=num_workers) as executor:
    futures = [
        executor.submit(_calcular_estatisticas_bloco, (dados_dict, list(chunk)))
        for chunk in chunks if len(chunk) > 0
    ]

    for future in as_completed(futures):
      try:
        res_parcial = future.result()
        analise_colunas.update(res_parcial)
      except Exception as e:
        print(f"⚠️ Erro em subprocesso de cálculo: {e}")

  return analise_colunas


def identificar_colunas_mesmas_estatisticas(analise_colunas):
  """Agrupa colunas que possuem exatamente as mesmas métricas e estatísticas

  de dados, auxiliando na detecção de colunas duplicadas com nomes diferentes.
  """
  mapa_stats = {}
  for col_nome, metricas in analise_colunas.items():
    if metricas.get("status_analise") == "sucesso":
      stats_dict = metricas.get("estatisticas_coluna")
      stats_items = frozenset(stats_dict.items()) if stats_dict else None
      sig = (
          metricas.get("valores_nulos"),
          metricas.get("valores_zeros"),
          metricas.get("porcentagem_nulos"),
          metricas.get("porcentagem_zeros"),
          metricas.get("valores_distintos"),
          stats_items
      )
      mapa_stats.setdefault(sig, []).append(col_nome)

  colunas_mesmas_estatisticas = [cols for cols in mapa_stats.values() if len(cols) > 1]
  return colunas_mesmas_estatisticas


def gerar_relatorio_arquivo_unico(
    res_id,
    nome_arquivo_saida="relatorio_arquivo_unico.md",
    caminho_saida="./generated",
    portal_url="https://dados.es.gov.br/"
):
  """Executa a extração, confere estrutura, processa métricas em subprocessos,

  verifica colunas duplicadas/mesmas estatísticas e salva o relatório.
  """
  df, total_linhas, colunas_ordenadas, erros_estrutura = baixar_e_analisar_arquivo_grande(res_id, portal_url)

  if df is None or total_linhas == 0:
    print("❌ Impossível gerar relatório devido à ausência de dados.")
    return

  # Processamento paralelo em subprocessos
  analise_colunas = processar_estatisticas_paralelas(df, colunas_ordenadas)

  # Identificação de colunas com as mesmas estatísticas (possíveis duplicadas)
  colunas_mesmas_stats = identificar_colunas_mesmas_estatisticas(analise_colunas)

  # Montagem do Relatório em Markdown
  linhas = []
  linhas.append(f"# Relatório de Auditoria de Arquivo Único (Grande Porte)")
  linhas.append(f"\n- **ID do Recurso:** `{res_id}`")
  linhas.append(f"- **Total de Linhas Auditadas:** `{total_linhas}`")
  linhas.append(f"- **Total de Colunas:** `{len(colunas_ordenadas)}`\n")
  linhas.append("---")

  # Seção de Erros de Estrutura
  linhas.append("\n## 🛠️ Conferência de Erros na Estrutura do Arquivo\n")
  if erros_estrutura:
    linhas.append("> **⚠️ Foram encontrados os seguintes problemas estruturais:**\n")
    for err in erros_estrutura:
      linhas.append(f"> - ❌ {err}")
  else:
    linhas.append("> ✅ **Nenhum erro estrutural detectado.** A integridade e consistência das colunas foram mantidas em todas as páginas.\n")
  linhas.append("---")

  # Seção de Qualidade de Colunas
  linhas.append("\n## 📋 Qualidade e Estatísticas das Colunas\n")
  for idx, (col_name, metricas) in enumerate(analise_colunas.items(), 1):
    if not metricas or metricas.get("status_analise") == "insuficiente":
      linhas.append(f"{idx}. `{col_name}` ➔ *Erro ao processar métricas da coluna.*")
    else:
      tags = []
      if metricas.get("provavel_enum"):
        tags.append("🟢 [Enum]")
      if metricas.get("alerta_caso_1"):
        tags.append("⚠️ [Caso 1: >50 Nulos/Zeros]")
      if metricas.get("alerta_caso_2"):
        tags.append("⚠️ [Caso 2: >50 Distintos]")
      
      tag_str = " " + " ".join(tags) if tags else ""
      stats = metricas.get("estatisticas_coluna")
      stats_str = ""
      
      if stats:
        if stats["tipo_estatistica"] == "numerica":
          stats_str = f" | 📊 **Numérica:** [Mín: {stats['minimo']}, Máx: {stats['maximo']}, Média: {stats['media']}, DesvPad: {stats['desvio_padrao']}]"
        else:
          stats_str = f" | 📝 **Texto:** [Tam Mín: {stats['min_length']}, Tam Máx: {stats['max_length']}, Média: {stats['mean_length']}]"

      linhas.append(
          f"{idx}. `{col_name}` ➔ "
          f"Nulos: **{metricas.get('porcentagem_nulos')}%** | "
          f"Zeros: **{metricas.get('porcentagem_zeros')}%** | "
          f"Distintos: **{metricas.get('valores_distintos')}**{tag_str}{stats_str}"
      )

  # Adiciona a verificação de colunas com exatamente as mesmas estatísticas
  if colunas_mesmas_stats:
    linhas.append("\n---")
    linhas.append("\n> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**\n")
    for grupo_cols in colunas_mesmas_stats:
      linhas.append(f"> - `{'`, `'.join(grupo_cols)}`\n")

  conteudo_md = "\n".join(linhas)

  # Salvando os arquivos gerados
  try:
    diretorio = Path(caminho_saida)
    diretorio.mkdir(parents=True, exist_ok=True)

    caminho_completo_md = diretorio / nome_arquivo_saida
    caminho_completo_md.write_text(conteudo_md, encoding="utf-8")
    print(f"\n📄 Relatório Markdown salvo com sucesso em: '{caminho_completo_md}'")

    if SUPORTE_PDF:
      conteudo_html = markdown.markdown(conteudo_md, extensions=["fenced_code", "tables"])
      html_completo = f"""
          <!DOCTYPE html>
          <html lang="pt-BR">
          <head>
              <meta charset="UTF-8">
              <style>
                  body {{ font-family: Helvetica, Arial, sans-serif; margin: 30px; color: #333; line-height: 1.5; font-size: 13px; }}
                  h1 {{ color: #004080; border-bottom: 2px solid #004080; padding-bottom: 5px; font-size: 20px; }}
                  h2 {{ color: #0059b3; margin-top: 25px; font-size: 16px; }}
                  hr {{ border: 0; border-top: 1px solid #ddd; margin: 15px 0; }}
                  code {{ background: #f6f8fa; padding: 2.3px 4px; border-radius: 3px; font-size: 11px; }}
              </style>
          </head>
          <body>
              {conteudo_html}
          </body>
          </html>
          """
      caminho_completo_pdf = diretorio / Path(nome_arquivo_saida).with_suffix(".pdf").name
      HTML(string=html_completo).write_pdf(caminho_completo_pdf)
      print(f"📑 Relatório PDF gerado com sucesso em: '{caminho_completo_pdf}'")

  except Exception as e:
    print(f"❌ Erro ao salvar os arquivos de relatório: {e}")


if __name__ == "__main__":
  _EXEMPLO_RESOURCE_ID = "2dc2d874-0d72-4c01-b8a0-ecb6f392d6e4"
  gerar_relatorio_arquivo_unico(
      res_id=_EXEMPLO_RESOURCE_ID,
      nome_arquivo_saida="relatorio_arquivo_gigante.md"
  )