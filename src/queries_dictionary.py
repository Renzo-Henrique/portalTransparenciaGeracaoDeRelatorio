import os
from pathlib import Path
from ckanapi import RemoteCKAN
import requests
import io

# Tentativa de importação da biblioteca para leitura de PDF
try:
  import pypdf
  SUPORTE_PYPDF = True
except ImportError:
  SUPORTE_PYPDF = False

# Tentativa de importação das bibliotecas para conversão de relatório em PDF
try:
  import markdown
  from weasyprint import HTML
  SUPORTE_PDF_GEN = True
except ImportError:
  SUPORTE_PDF_GEN = False


def obter_dicionario_pdf_dataset(dataset_id, portal_url="https://dados.es.gov.br/"):
  """Consulta um dataset no CKAN, filtra recursos PDF, valida a existência

  de exatamente um arquivo PDF na base, baixa o conteúdo e extrai o texto.
  """
  rc = RemoteCKAN(portal_url)
  recursos_pdf = []

  try:
    # 1. Obtém os detalhes do dataset via CKAN API
    dataset = rc.action.package_show(id=dataset_id)
    recursos = dataset.get("resources", [])

    for recurso in recursos:
      formato = recurso.get("format", "").upper()
      url_recurso = recurso.get("url", "")
      
      # Filtra recursos cujo formato seja PDF ou cuja URL termine em .pdf
      if formato == "PDF" or url_recurso.lower().endswith(".pdf"):
        res_id = recurso.get("id")
        res_name = recurso.get("name")

        if not res_name and url_recurso:
          res_name = url_recurso.split("/")[-1].split("?")[0]

        if not res_name:
          res_name = f"recurso_{res_id}.pdf"

        recursos_pdf.append({
            "id": res_id,
            "name": res_name,
            "url": url_recurso
        })

  except Exception as e:
    raise RuntimeError(
        f"Falha ao conectar com o CKAN ou recuperar os metadados do dataset {dataset_id}. "
        f"Motivo técnico: {e}"
    )

  qtd_pdfs = len(recursos_pdf)

  # 2. Verificação rigorosa: exige exatamente UM arquivo PDF na base
  if qtd_pdfs == 0:
    raise FileNotFoundError(
        f"Erro: Nenhum arquivo PDF foi encontrado no dataset '{dataset_id}' do portal. "
        "A base de dados precisa conter exatamente um dicionário de dados em formato PDF."
    )
  elif qtd_pdfs > 1:
    nomes_encontrados = [r["name"] for r in recursos_pdf]
    raise ValueError(
        f"Erro: Foram encontrados {qtd_pdfs} arquivos PDF no dataset ({nomes_encontrados}). "
        "O sistema requer e espera exatamente um arquivo PDF para realizar a extração com segurança."
    )

  recurso_alvo = recursos_pdf[0]
  pdf_url = recurso_alvo["url"]
  pdf_nome = recurso_alvo["name"]

  print(f"[Info] Arquivo PDF único identificado no CKAN: '{pdf_nome}'")

  if not SUPORTE_PYPDF:
    raise ImportError(
        "A biblioteca 'pypdf' não está instalada no ambiente. "
        "Instale-a via 'pip install pypdf' para processar o conteúdo do PDF."
    )

  # 3. Download do arquivo PDF diretamente da URL do CKAN
  try:
    response = requests.get(pdf_url, timeout=30)
    response.raise_for_status()
    pdf_file = io.BytesIO(response.content)
  except Exception as req_err:
    raise RuntimeError(
        f"Não foi possível baixar o arquivo PDF '{pdf_nome}' a partir da URL fornecida pelo CKAN ({pdf_url}). "
        f"Motivo da falha de rede/download: {req_err}"
    )

  # 4. Extração de texto página por página
  conteudo_extraido = []
  try:
    reader = pypdf.PdfReader(pdf_file)
    for i, pagina in enumerate(reader.pages):
      texto = pagina.extract_text()
      if texto:
        conteudo_extraido.append({"pagina": i + 1, "texto": texto})
  except Exception as pdf_err:
    raise RuntimeError(
        f"Não foi possível extrair o texto do arquivo PDF '{pdf_nome}'. "
        f"Motivo do erro no parser do PDF: {pdf_err}"
    )

  if not conteudo_extraido:
    raise ValueError(
        f"O arquivo PDF '{pdf_nome}' foi baixado com sucesso, mas nenhum conteúdo textual "
        "pôde ser extraído. O documento pode ser uma imagem escaneada sem camada OCR ativada."
    )

  return pdf_nome, conteudo_extraido


def gerar_relatorio_dicionario_pdf(
    dataset_id,
    portal_url="https://dados.es.gov.br/",
    nome_arquivo_saida="dicionario_analisado.md",
    caminho_saida="./generated",
):
  """Invoca obter_dicionario_pdf_dataset para coletar os dados do PDF no CKAN

  e gera os relatórios em .md e .pdf estruturados com os achados.
  """
  try:
    # Invoca a obtenção e validação do dicionário diretamente do CKAN
    dataset_nome, dados_pdf = obter_dicionario_pdf_dataset(dataset_id, portal_url)
  except Exception as e:
    print(f"\n[Erro] Falha ao obter o dicionário de dados do dataset {dataset_id}: {e}")
    return None

  linhas = []
  linhas.append("# Relatório de Auditoria e Extração do Dicionário de Dados (CKAN)")
  linhas.append(
      "\nEste documento apresenta os achados e o conteúdo estruturado extraído "
      "do arquivo PDF de dicionário de dados validado e baixado diretamente do portal CKAN.\n"
  )
  linhas.append("---")
  linhas.append(f"\n- **Recurso PDF Analisado:** `{dataset_nome}`")
  linhas.append("- **Status da Validação:** 1 arquivo PDF único detectado e processado com sucesso.\n")
  linhas.append("---")

  linhas.append("\n## 📋 Conteúdo Detalhado por Página\n")

  for item in dados_pdf:
    linhas.append(f"\n### 📄 Página {item['pagina']}\n")
    linhas.append("```text")
    linhas.append(item['texto'])
    linhas.append("```\n")
    linhas.append("---")

  conteudo_md = "\n".join(linhas)

  try:
    diretorio = Path(caminho_saida)
    diretorio.mkdir(parents=True, exist_ok=True)

    # Salva a versão .md
    caminho_completo_md = diretorio / nome_arquivo_saida
    caminho_completo_md.write_text(conteudo_md, encoding="utf-8")
    print(f"Relatório .md gerado com sucesso em: '{caminho_completo_md}'")

    # Salva a versão .pdf (se disponível)
    if SUPORTE_PDF_GEN:
      conteudo_html = markdown.markdown(
          conteudo_md, extensions=["fenced_code", "tables"]
      )
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
                  pre {{ background: #f6f8fa; padding: 10px; border-radius: 4px; font-size: 10px; white-space: pre-wrap; word-wrap: break-word; }}
                  code {{ background: #f6f8fa; padding: 2px 4px; border-radius: 3px; font-size: 11px; }}
              </style>
          </head>
          <body>
              {conteudo_html}
          </body>
          </html>
          """
      caminho_completo_pdf = diretorio / Path(nome_arquivo_saida).with_suffix(".pdf").name
      HTML(string=html_completo).write_pdf(caminho_completo_pdf)
      print(f"Relatório .pdf gerado com sucesso em: '{caminho_completo_pdf}'")
    else:
      print("Aviso: Bibliotecas 'markdown' ou 'weasyprint' não encontradas. Apenas o arquivo .md foi criado.")

  except Exception as e:
    print(f"Erro ao salvar os arquivos de relatório do dicionário: {e}")

  return conteudo_md