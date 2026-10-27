from pathlib import Path
import pandas as pd
import numpy as np
from tqdm import tqdm

_LIMIT_NULOS_POR_COLUNA = 50
_LIMIT_DISTINTOS_POR_COLUNA = 50
_CHUNKSIZE = 100000  # Tamanho do bloco em linhas para leitura eficiente de arquivos >1GB sem estourar a memória

# Tentativa de importação das bibliotecas para conversão de PDF
try:
  import markdown
  from weasyprint import HTML
  SUPORTE_PDF = True
except ImportError:
  SUPORTE_PDF = False


def analisar_arquivo_gigante_local(caminho_arquivo):
  """Lê e audita um arquivo local massivo (>1GB) de forma otimizada, dividindo

  o processamento em blocos (chunks) para evitar overflow de memória RAM e numérica.
  """
  caminho = Path(caminho_arquivo)
  if not caminho.exists():
    print(f"❌ [Erro] O arquivo local '{caminho_arquivo}' não foi encontrado.")
    return None, 0, [], ["Arquivo local não encontrado."]

  print(f"\n🔍 Iniciando leitura e auditoria local do arquivo: {caminho.name}")

  total_linhas = 0
  colunas_ordenadas = None
  erros_estrutura = []
  
  # Acumuladores globais em memória segura para estatísticas consistentes
  nulos_dict = {}
  zeros_dict = {}
  distintos_sets = {}
  stats_acumuladores = {}

  # Leitura particionada (chunking) ideal para arquivos >1GB
  try:
    with pd.read_csv(caminho, chunksize=_CHUNKSIZE, low_memory=False, encoding='utf-8') as reader:
      for chunk_idx, chunk in enumerate(tqdm(reader, desc="📥 Lendo blocos do arquivo", unit="chunk")):
        if colunas_ordenadas is None:
          colunas_ordenadas = sorted(chunk.columns)
          for col in colunas_ordenadas:
            nulos_dict[col] = 0
            zeros_dict[col] = 0
            distintos_sets[col] = set()
            stats_acumuladores[col] = {"valores_numericos": [], "tamanhos_texto": []}

        # Verificação básica de consistência estrutural entre os blocos
        if sorted(chunk.columns) != colunas_ordenadas:
          erros_estrutura.append(f"Divergência estrutural detectada no bloco {chunk_idx}: as colunas diferem do cabeçalho inicial.")

        total_linhas += len(chunk)

        # Processamento incremental por coluna em cada chunk
        for col in colunas_ordenadas:
          serie = chunk[col]
          nulos_dict[col] += int(serie.isna().sum())

          try:
            serie_val_str = serie.astype(str).str.strip().str.replace(',', '.', regex=False)
            zeros_dict[col] += int((pd.to_numeric(serie_val_str, errors='coerce') == 0.0).sum())
          except Exception:
            zeros_dict[col] += int((serie == 0).sum())

          # Amostragem segura de valores distintos para não estourar memória com cardinality alta
          valores_unicos_chunk = serie.dropna().unique()
          if len(distintos_sets[col]) < 10000:  # Teto de segurança para conjuntos de cardinalidade
            for val in valores_unicos_chunk:
              distintos_sets[col].add(val)

          # Coleta amostras para estatísticas sem overflow (evitando armazenar todos os dados brutos se forem massivos)
          serie_limpa = serie.dropna()
          if len(serie_limpa) > 0:
            serie_str = serie_limpa.astype(str).str.strip().str.replace(',', '.', regex=False)
            serie_num = pd.to_numeric(serie_str, errors='coerce')

            if serie_num.notna().all() and len(serie_num) > 0:
              # Armazena apenas uma amostra representativa ou valores convertidos para float64
              vals_num = serie_num.astype(np.float64).values
              stats_acumuladores[col]["valores_numericos"].extend(vals_num[:1000])  # Amostragem segura por chunk
            else:
              tamanhos = serie_limpa.astype(str).str.len().astype(np.int64).values
              stats_acumuladores[col]["tamanhos_texto"].extend(tamanhos[:1000])

  except Exception as e:
    print(f"❌ [Erro de Leitura] Falha ao processar o arquivo local: {e}")
    return None, 0, [], [f"Erro na leitura do CSV: {e}"]

  # Consolidação final das estatísticas garantindo consistência e prevenção contra overflow
  analise_colunas = {}
  print("📊 Consolidando estatísticas finais...")

  for col in colunas_ordenadas:
    try:
      nulos = nulos_dict[col]
      zeros = zeros_dict[col]
      distintos = len(distintos_sets[col])

      perc_nulos = (nulos / total_linhas * 100) if total_linhas > 0 else 0
      perc_zeros = (zeros / total_linhas * 100) if total_linhas > 0 else 0

      provavel_enum = (distintos <= _LIMIT_DISTINTOS_POR_COLUNA or (distintos / total_linhas < 0.05)) if total_linhas > 0 else False
      alerta_caso_1 = (nulos > _LIMIT_NULOS_POR_COLUNA) or (zeros > _LIMIT_NULOS_POR_COLUNA)
      alerta_caso_2 = (distintos > _LIMIT_DISTINTOS_POR_COLUNA)

      stats_col = None
      dados_col = stats_acumuladores[col]

      if dados_col["valores_numericos"]:
        arr_num = np.array(dados_col["valores_numericos"], dtype=np.float64)
        stats_col = {
            "tipo_estatistica": "numerica",
            "minimo": float(arr_num.min()),
            "maximo": float(arr_num.max()),
            "media": round(float(arr_num.mean()), 2),
            "mediana": float(np.median(arr_num)),
            "desvio_padrao": round(float(arr_num.std(ddof=0)), 2) if len(arr_num) > 1 else 0.0
        }
      elif dados_col["tamanhos_texto"]:
        arr_tam = np.array(dados_col["tamanhos_texto"], dtype=np.int64)
        stats_col = {
            "tipo_estatistica": "texto",
            "min_length": int(arr_tam.min()),
            "max_length": int(arr_tam.max()),
            "mean_length": round(float(arr_tam.mean()), 2),
            "std_length": round(float(arr_tam.std(ddof=0)), 2) if len(arr_tam) > 1 else 0.0
        }

      analise_colunas[col] = {
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
      analise_colunas[col] = {"status_analise": "insuficiente"}

  return analise_colunas, total_linhas, colunas_ordenadas, erros_estrutura


def identificar_colunas_mesmas_estatisticas(analise_colunas):
  """Agrupa colunas que possuem exatamente as mesmas métricas e estatísticas

  de dados, permitindo detectar colunas duplicadas com nomes diferentes.
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

  return [cols for cols in mapa_stats.values() if len(cols) > 1]


def gerar_relatorio_arquivo_local(
    caminho_arquivo,
    nome_arquivo_saida="relatorio_arquivo_local.md",
    caminho_saida="./generated"
):
  """Executa a leitura local do arquivo, valida estruturas, processa estatísticas

  sem desperdício de memória e gera o relatório completo em Markdown e PDF.
  """
  analise_colunas, total_linhas, colunas_ordenadas, erros_estrutura = analisar_arquivo_gigante_local(caminho_arquivo)

  if not analise_colunas or total_linhas == 0:
    print("❌ Impossível gerar relatório devido à ausência de dados ou falha na leitura.")
    return

  colunas_mesmas_stats = identificar_colunas_mesmas_estatisticas(analise_colunas)

  # Montagem do Relatório em Markdown
  linhas = []
  linhas.append(f"# Relatório de Auditoria de Arquivo Local (Grande Porte)")
  linhas.append(f"\n- **Caminho do Arquivo:** `{caminho_arquivo}`")
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
    linhas.append("> ✅ **Nenhum erro estrutural detectado.** A consistência das colunas foi mantida em todos os blocos do arquivo.\n")
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

  # Adiciona a verificação correta de colunas com exatamente as mesmas estatísticas
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


def analisar_arquivo_base_de_receitas():
  _EXEMPLO_CAMINHO_ARQUIVO = "arquivos/Receitas-2025.csv"
  gerar_relatorio_arquivo_local(
      caminho_arquivo=_EXEMPLO_CAMINHO_ARQUIVO,
      nome_arquivo_saida="analise_completa_dados_Receitas-2025_.md"
  )

def analisar_arquivos_base__de_despesas():
  # gerar_relatorio_arquivo_local(
  #       caminho_arquivo="arquivos/despesas-2025.csv",
  #       nome_arquivo_saida="/base-despesas/analise_Despesas-2025_.md"
  #   )
  gerar_relatorio_arquivo_local(
          caminho_arquivo="arquivos/orcamentosexecucoes-2025.csv",
          nome_arquivo_saida="/base-despesas/analise_orcamentosExecucoes-2025_.md"
      )
  gerar_relatorio_arquivo_local(
          caminho_arquivo="arquivos/RestosAPagar-2024.csv",
          nome_arquivo_saida="/base-despesas/analise_RestosAPagar-2024_.md"
      )
  gerar_relatorio_arquivo_local(
          caminho_arquivo="arquivos/orcamentosdespesa-2025.csv",
          nome_arquivo_saida="/base-despesas/analise_orcamentosEespesa-2025_.md"
      )

if __name__ == "__main__":
  # analisar_arquivo_base_de_receitas()
  analisar_arquivos_base__de_despesas()