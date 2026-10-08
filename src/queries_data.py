import os
from pathlib import Path
from ckanapi import RemoteCKAN
import pandas as pd
from tqdm import tqdm

from queries_headers import agrupar_recursos_dataset, analisar_colunas_por_periodo

# Tentativa de importação das bibliotecas para conversão de PDF
try:
  import markdown
  from weasyprint import HTML
  SUPORTE_PDF = True
except ImportError:
  SUPORTE_PDF = False


def analisar_qualidade_colunas_recurso(res_id, portal_url="https://dados.es.gov.br/"):
  """Analisa estatísticas de um recurso limitando a no máximo 50.000 registros
  amostrados aleatoriamente (com seed fixa), sem excesso de logs para garantir
  máxima performance e evitar travamentos de I/O.
  """
  rc = RemoteCKAN(portal_url)

  try:
    # 1. Paginação limitada a no máximo 50.000 registros
    limit = 10000
    max_registros = 50000
    offset = 0
    all_records = []

    while len(all_records) < max_registros:
      try:
        current_limit = min(limit, max_registros - len(all_records))
        ds_res = rc.action.datastore_search(resource_id=res_id, limit=current_limit, offset=offset)
      except Exception:
        break

      records = ds_res.get("records", [])
      if not records:
        break
      all_records.extend(records)

      if len(records) < current_limit or len(all_records) >= max_registros:
        break
      offset += current_limit

    if not all_records:
      return None, 0, []

    # 2. Carrega no DataFrame e aplica amostragem aleatória por seed
    df = pd.DataFrame(all_records)
    if "_id" in df.columns:
      df = df.drop(columns=["_id"])

    if len(df) > max_registros:
      df = df.sample(n=max_registros, random_state=42)

    total_linhas = len(df)
    colunas_ordenadas = sorted(df.columns)

    return df, total_linhas, colunas_ordenadas

  except Exception:
    return None, 0, []


def enriquecer_analise_com_qualidade(analise_dict, portal_url="https://dados.es.gov.br/"):
  """Varre o dicionário utilizando 3 níveis de TQDM:
  1. Grupos Principais
  2. Períodos de tempo
  3. Arquivos do Período
  """
  for chave_principal, grupos in tqdm(analise_dict.items(), desc="1. Grupos Principais"):
    for grupo in tqdm(grupos, desc="   2. Períodos de tempo", leave=False):
      arquivos = grupo.get("ArquivosPeriodo", [])
      
      if arquivos:
        analises_arquivos = {}
        
        # Nível 3: Iteração sobre os arquivos do período
        for arq in tqdm(arquivos, desc="      3. Arquivos do Período", leave=False):
          res_id = arq.get("id")
          if not res_id:
            continue
            
          df, total_linhas, colunas_ordenadas = analisar_qualidade_colunas_recurso(res_id, portal_url)
          
          if df is None or total_linhas == 0:
            continue

          analise_colunas = {}
          
          for col in colunas_ordenadas:
            try:
              serie = df[col]
              
              nulos = int(serie.isna().sum())
              try:
                zeros = int((serie == 0).sum())
              except Exception:
                zeros = 0

              distintos = int(serie.nunique(dropna=True))

              caso_1 = (nulos > 50) or (zeros > 50)
              caso_2 = (distintos > 50)

              perc_nulos = (nulos / total_linhas * 100) if total_linhas > 0 else 0
              provavel_enum = (
                  (distintos <= 20 or (distintos / total_linhas < 0.01))
                  if total_linhas > 0
                  else False
              )

              analise_colunas[col] = {
                  "total_linhas": total_linhas,
                  "valores_nulos": nulos,
                  "valores_zeros": zeros,
                  "porcentagem_nulos": round(perc_nulos, 2),
                  "valores_distintos": distintos,
                  "provavel_enum": provavel_enum,
                  "alerta_caso_1": caso_1,
                  "alerta_caso_2": caso_2,
                  "status_analise": "sucesso"
              }

            except Exception:
              analise_colunas[col] = {
                  "total_linhas": total_linhas,
                  "valores_nulos": 0,
                  "valores_zeros": 0,
                  "porcentagem_nulos": 0.0,
                  "valores_distintos": 0,
                  "provavel_enum": False,
                  "alerta_caso_1": False,
                  "alerta_caso_2": False,
                  "status_analise": "insuficiente",
                  "mensagem": "Obtiveram-se registros estatisticamente suficientes que não comprovam essa hipótese."
              }

          analises_arquivos[res_id] = analise_colunas
        
        grupo["analiseDeColunasPorArquivo"] = analises_arquivos

        # Consolidação das colunas agrupadas por período de tempo
        analise_periodo = {}
        colunas_acumuladas = {}
        for res_id, cols_dict in analises_arquivos.items():
          for col_nome, metrics in cols_dict.items():
            if col_nome not in colunas_acumuladas:
              colunas_acumuladas[col_nome] = []
            colunas_acumuladas[col_nome].append(metrics)

        for col_nome, metrics_list in colunas_acumuladas.items():
          valid_metrics = [m for m in metrics_list if m.get("status_analise") == "sucesso"]
          if valid_metrics:
            avg_linhas = sum(m["total_linhas"] for m in valid_metrics) // len(valid_metrics)
            avg_nulos = sum(m["valores_nulos"] for m in valid_metrics) // len(valid_metrics)
            avg_zeros = sum(m["valores_zeros"] for m in valid_metrics) // len(valid_metrics)
            avg_perc_nulos = round(sum(m["porcentagem_nulos"] for m in valid_metrics) / len(valid_metrics), 2)
            avg_distintos = sum(m["valores_distintos"] for m in valid_metrics) // len(valid_metrics)
            
            provavel_enum = any(m["provavel_enum"] for m in valid_metrics)
            caso_1 = any(m["alerta_caso_1"] for m in valid_metrics)
            caso_2 = any(m["alerta_caso_2"] for m in valid_metrics)

            analise_periodo[col_nome] = {
                "total_linhas": avg_linhas,
                "valores_nulos": avg_nulos,
                "valores_zeros": avg_zeros,
                "porcentagem_nulos": avg_perc_nulos,
                "valores_distintos": avg_distintos,
                "provavel_enum": provavel_enum,
                "alerta_caso_1": caso_1,
                "alerta_caso_2": caso_2,
                "status_analise": "sucesso"
            }
          else:
            analise_periodo[col_nome] = metrics_list[0]

        grupo["analiseDeColunasPorPeriodo"] = analise_periodo

  return analise_dict


def gerar_analise_das_colunas(
    dataset_id,
    nome_arquivo_saida="colunasAnalisadas.md",
    caminho_saida="./",
):
  """Gera os arquivos .md e .pdf com base na análise estrutural e de qualidade por período."""
  resultado_agrupado = agrupar_recursos_dataset(dataset_id)
  analise_dict = analisar_colunas_por_periodo(resultado_agrupado)
  analise_dict = enriquecer_analise_com_qualidade(analise_dict)

  linhas = []
  linhas.append("# Relatório de Análise Estrutural e Qualidade de Dados - CKAN")
  linhas.append(
      "\nEste documento apresenta um resumo consolidado das bases de dados por período, "
      "evolução das colunas e métricas de qualidade consolidadas por período de tempo "
      "com marcação de alertas (Caso 1: Nulos/Zeros > 50 e Caso 2: Distintos > 50).\n"
  )
  linhas.append("---")

  for chave_principal, grupos in analise_dict.items():
    linhas.append(f"\n## 📂 Grupo Principal: `{chave_principal}`\n")

    for grupo in grupos:
      periodo_inicio = grupo.get("PeriodoInicio")
      periodo_fim = grupo.get("PeriodoFim")
      periodo_str = (
          f"{periodo_inicio}"
          if periodo_inicio == periodo_fim
          else f"{periodo_inicio} até {periodo_fim}"
      )

      linhas.append(f"### 🔹 Período: {periodo_str}")
      linhas.append(f"- **Quantidade Total de Colunas:** `{grupo.get('QtdColunas')}`")

      diff_cols = grupo.get("ColunasDiferentesAoAnterior", [])
      if diff_cols:
        linhas.append(f"  - *Colunas removidas/alteradas:* `" + "`, `".join(diff_cols) + "`")
      else:
        linhas.append("  - *Colunas removidas/alteradas:* Nenhuma")

      arquivos = grupo.get("ArquivosPeriodo", [])
      if arquivos:
        linhas.append("\n**Arquivos Vinculados ao Período:**")
        for arq in arquivos:
          res_id = arq.get("id")
          linhas.append(f"  - 📄 **`{arq.get('name')}`** *(ID: `{res_id}`)*")

      linhas.append("\n**Análise de Qualidade das Colunas (Consolidada por Período):**")
      analise_cols = grupo.get("analiseDeColunasPorPeriodo", {})
      
      if analise_cols:
        for idx, (col_nome, metricas) in enumerate(analise_cols.items(), 1):
          if metricas.get("status_analise") == "insuficiente":
            linhas.append(
                f"  {idx}. `{col_nome}` ➔ *{metricas.get('mensagem')}*"
            )
          else:
            tags = []
            if metricas.get("provavel_enum"):
              tags.append("🟢 [Enum]")
            if metricas.get("alerta_caso_1"):
              tags.append("⚠️ [Caso 1: >50 Nulos/Zeros]")
            if metricas.get("alerta_caso_2"):
              tags.append("⚠️ [Caso 2: >50 Distintos]")
            
            tag_str = " " + " ".join(tags) if tags else ""

            linhas.append(
                f"  {idx}. `{col_nome}` ➔ "
                f"Nulos: **{metricas.get('porcentagem_nulos')}%** "
                f"({metricas.get('valores_nulos')} nulos, {metricas.get('valores_zeros', 0)} zeros) | "
                f"Distintos: **{metricas.get('valores_distintos')}**{tag_str}\n"
            )
      else:
        linhas.append("  - *Nenhuma métrica obtida para este período.*")

      linhas.append("---")

  conteudo_md = "\n".join(linhas)

  try:
    diretorio = Path(caminho_saida)
    diretorio.mkdir(parents=True, exist_ok=True)

    caminho_completo_md = diretorio / nome_arquivo_saida
    caminho_completo_md.write_text(conteudo_md, encoding="utf-8")
    print(f"Arquivo .md gerado com sucesso em: '{caminho_completo_md}'")

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
                  h3 {{ color: #222; font-size: 14px; margin-top: 15px; }}
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
      print(f"Arquivo .pdf gerado com sucesso em: '{caminho_completo_pdf}'")

  except Exception as e:
    print(f"Erro ao salvar os arquivos de relatório: {e}")

  return analise_dict