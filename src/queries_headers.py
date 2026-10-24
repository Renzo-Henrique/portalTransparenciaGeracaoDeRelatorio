import os
import requests
import re
import sys
import time
from tqdm import tqdm
from pathlib import Path
from ckanapi import RemoteCKAN

_TEMPO_LIMITE = 20
_MAX_TENTATIVAS = 5

def agrupar_recursos_dataset(
    dataset_id, portal_url="https://dados.es.gov.br/"
):
  """Consulta um dataset no CKAN e agrupa seus recursos por prefixo de nome (removendo extensões e dígitos, preservando o case).
  """
  rc = RemoteCKAN(portal_url)
  grupos = {}

  
  tentativa = 1
  dataset = None
  sucesso_requisicao = False

  # Loop de retry utilizando tqdm para monitorar as tentativas de requisição do dataset
  with tqdm(total=_MAX_TENTATIVAS, desc=f"   [{dataset_id}] Conectando ao Dataset", leave=False) as pbar:
    inicio_rec = time.time()

    for tentativa in range(1, _MAX_TENTATIVAS + 1):
      if time.time() - inicio_rec > _TEMPO_LIMITE:
        break
      try:
        dataset = rc.action.package_show(id=dataset_id)
        sucesso_requisicao = True
        pbar.set_postfix(status="Sucesso!")
        pbar.update(_MAX_TENTATIVAS - pbar.n) # Completa a barra em caso de sucesso
        break
      except requests.exceptions.RequestException as e:
        pbar.set_postfix(status=f"Falha (Tentativa {tentativa})")
        pbar.update(1)
        time.sleep(1)
      except Exception as e:
        print(f"\n❌ [Erro na API] Erro não recuperável ao buscar o dataset {dataset_id}: {e}")
        break

  # Se estourar o tempo limite de 20s por falha de rede, retorna dicionário vazio
  if not sucesso_requisicao:
    print(
        f"❌ [Timeout / Pulado] A requisição do dataset {dataset_id} falhou após {_TEMPO_LIMITE}s de tentativas de rede. Pulando..."
    )
    return {}


  try:
    # Obtém os detalhes do dataset
    recursos = dataset.get("resources", [])

    for recurso in recursos:
      if recurso.get("format") != "CSV":
        continue  # Ignora recursos que não são CSV
      res_id = recurso.get("id")
      res_name = recurso.get("name")

      # Fallback caso o recurso não tenha nome cadastrado: tenta extrair da URL
      if not res_name and recurso.get("url"):
        res_name = recurso.get("url").split("/")[-1].split("?")[0]

      if not res_name:
        res_name = f"recurso_{res_id}"

      # 1. Remove a extensão do arquivo (ex: .csv, .xlsx)
      base_name, _ = os.path.splitext(res_name)

      # 2. Remove todos os dígitos numéricos para unificar anos/versões (ex: receitas2020 -> receitas)
      # O case é preservado (sensível a maiúsculas/minúsculas)
      group_key = re.sub(r"\d+", "", base_name)

      # Monta o dicionário do elemento
      item = {"id": res_id, "name": res_name}

      # Adiciona ao grupo correspondente
      if group_key not in grupos:
        grupos[group_key] = []
      grupos[group_key].append(item)

    return grupos

  except Exception as e:
    print(f"❌ [Erro na API] Erro inesperado ao buscar o recurso {res_id}: {e}")
    return {}


def analisar_colunas_por_periodo(
    dicionario_agrupado, portal_url="https://dados.es.gov.br/"
):
  """Analisa os recursos agrupados, extrai os anos, verifica as colunas via Datastore,

  agrupa os períodos consecutivos com a mesma estrutura e calcula separadamente
  as colunas removidas, alteradas e as que se mantiveram em relação ao grupo anterior.
  """
  rc = RemoteCKAN(portal_url)
  resultado_final = {}

  for chave_principal, lista_recursos in tqdm(dicionario_agrupado.items(), desc="Headers: Grupos Principais:"):
    recursos_com_ano = []

    # 1. Extrai o ano de cada arquivo para ordenação cronológica
    for rec in lista_recursos:
      name = rec["name"]
      match = re.search(r"(19\d{2}|20\d{2})", name)
      ano = int(match.group(1)) if match else 0
      recursos_com_ano.append((ano, rec))

    # Ordena os recursos pelo ano (e pelo nome caso não tenha ano)
    recursos_com_ano.sort(key=lambda x: (x[0], x[1]["name"]))

    grupos_colunas = []
    current_group = None

    # Etapa 1: Cria os blocos brutos de períodos consecutivos com a mesma estrutura
    desc_recursos = f"   [{chave_principal}] Verificando recursos"
    for ano, rec in tqdm(recursos_com_ano, desc=desc_recursos, leave=False):
      res_id = rec["id"]
      res_name = rec["name"]
      colunas = []

      # Mecanismo de Retry com limite para a requisição de headers
      
      tentativa_rec = 1
      ds_res = None
      sucesso_rec = False
      with tqdm(total=_MAX_TENTATIVAS, desc=f"      Recurso {res_id[:6]}...", leave=False) as pbar_rec:

        inicio_rec = time.time()
        for tentativa_rec in range(1, _MAX_TENTATIVAS + 1):

          if time.time() - inicio_rec > _TEMPO_LIMITE:
            break
          try:
            ds_res = rc.action.datastore_search(resource_id=res_id, limit=0)
            sucesso_rec = True
            pbar_rec.set_postfix(status="Sucesso!")
            pbar_rec.update(_MAX_TENTATIVAS - pbar_rec.n)
            break
          except requests.exceptions.RequestException as e:
            pbar_rec.set_postfix(status=f"Retry {tentativa_rec}")
            pbar_rec.update(1)
            time.sleep(2)
          except Exception as e:
            pbar_rec.set_postfix(status="Erro Estrutural")
            break

      # Se estourar as tentativas por falha de rede, pula este recurso específico
      if not sucesso_rec:
        print(
            f"\n❌ [Timeout / Pulado] O recurso {res_id} (`{res_name}`) falhou após {_MAX_TENTATIVAS} tentativas. Pulando..."
        )
        continue


      try:
        fields = ds_res.get("fields", [])
        colunas = [f["id"] for f in fields if f["id"] != "_id"]
      except Exception as e:
        print(f"⚠️ [Erro de Processamento] Falha ao extrair colunas do recurso {res_id}: {e}")
        colunas = []

      colunas_ordenadas = sorted(colunas)
      colunas_tuple = tuple(colunas_ordenadas)
      info_arquivo = {"id": res_id, "name": res_name}

      if current_group is None:
        current_group = {
            "PeriodoInicio": ano if ano != 0 else None,
            "PeriodoFim": ano if ano != 0 else None,
            "QtdColunas": len(colunas_ordenadas),
            "ColunasAtual": colunas_ordenadas,
            "signature": colunas_tuple,
            "ArquivosPeriodo": [info_arquivo],
        }
      else:
        # Se mantiver as mesmas colunas, estende o período fim e acumula o arquivo
        if current_group["signature"] == colunas_tuple:
          if ano != 0:
            current_group["PeriodoFim"] = ano
          current_group["ArquivosPeriodo"].append(info_arquivo)
        else:
          # Mudou a estrutura: salva o grupo atual e inicia um novo
          grupos_colunas.append(current_group)
          current_group = {
              "PeriodoInicio": ano if ano != 0 else None,
              "PeriodoFim": ano if ano != 0 else None,
              "QtdColunas": len(colunas_ordenadas),
              "ColunasAtual": colunas_ordenadas,
              "signature": colunas_tuple,
              "ArquivosPeriodo": [info_arquivo],
          }

    # Adiciona o último grupo remanescente
    if current_group is not None:
      grupos_colunas.append(current_group)

    # Etapa 2: Calcula separadamente as colunas removidas, alteradas e mantidas em relação ao grupo [i - 1]
    grupos_finais = []
    for i, grupo in enumerate(grupos_colunas):
      colunas_atuais_set = set(grupo["ColunasAtual"])

      if i == 0:
        colunas_removidas = []
        colunas_alteradas = []
        colunas_mantidas = []
      else:
        colunas_anteriores_set = set(grupos_colunas[i - 1]["ColunasAtual"])
        # Colunas removidas: estavam no anterior, mas não estão no atual
        colunas_removidas = sorted(list(colunas_anteriores_set - colunas_atuais_set))
        # Colunas alteradas/adicionadas: estão no atual, mas não estavam no anterior
        colunas_alteradas = sorted(list(colunas_atuais_set - colunas_anteriores_set))
        # Colunas mantidas: estavam no anterior e continuam no atual (interseção)
        colunas_mantidas = sorted(list(colunas_anteriores_set.intersection(colunas_atuais_set)))

      grupos_finais.append({
          "PeriodoInicio": grupo["PeriodoInicio"],
          "PeriodoFim": grupo["PeriodoFim"],
          "QtdColunas": grupo["QtdColunas"],
          "ColunasAtual": grupo["ColunasAtual"],
          "ColunasRemovidas": colunas_removidas,
          "ColunasAlteradas": colunas_alteradas,
          "ColunasMantidas": colunas_mantidas,
          "ArquivosPeriodo": grupo["ArquivosPeriodo"],
      })

    resultado_final[chave_principal] = grupos_finais

  return resultado_final

# Tentativa de importação das bibliotecas para conversão de PDF
try:
  import markdown
  from weasyprint import HTML

  SUPORTE_PDF = True
except ImportError:
  SUPORTE_PDF = False


def gerar_analise_das_colunas_headers(
    dataset_id,
    nome_arquivo_saida="colunas_analisadas.md",
    caminho_saida="./",
):
  """Gera um arquivo .md e sua versão correspondente em .pdf em um caminho

  específico para facilitar a análise humana do retorno da função.
  """
  resultado_agrupado = agrupar_recursos_dataset(dataset_id)
  analise_dict = analisar_colunas_por_periodo(resultado_agrupado)

  linhas = []

  linhas.append("# Relatório de Análise Estrutural de Dados - CKAN")
  linhas.append(
      "\nEste documento apresenta um resumo consolidado das bases de dados,"
      " evolução dos períodos,\nvariações de colunas e mapeamento de arquivos"
      " obtidos do portal de transparência.\n"
  )
  linhas.append("---")

  # 1. Monta todo o conteúdo do relatório primeiro perpassando os dados
  for chave_principal, grupos in analise_dict.items():
    linhas.append(f"\n##  Grupo Principal: `{chave_principal}`\n")

    for i, grupo in enumerate(grupos, start=1):
      periodo_inicio = grupo.get("PeriodoInicio")
      periodo_fim = grupo.get("PeriodoFim")
      periodo_str = (
          f"{periodo_inicio}"
          if periodo_inicio == periodo_fim
          else f"{periodo_inicio} até {periodo_fim}"
      )

      linhas.append(f"### 🔹 Período: {periodo_str}")
      linhas.append(f"- **Quantidade Total de Colunas:** `{grupo.get('QtdColunas')}`")

      # Colunas removidas
      colunas_removidas = grupo.get("ColunasRemovidas", [])
      if colunas_removidas:
        linhas.append(
            f"\t- *Colunas removidas (estavam no anterior, mas não agora):* {len(colunas_removidas)}\n\t`"
            + "`, `".join(colunas_removidas)
            + "`"
        )
      else:
        linhas.append(
            "- *Colunas removidas (estavam no anterior, mas não agora):* Nenhuma"
        )

      # Colunas alteradas / adicionadas
      colunas_alteradas = grupo.get("ColunasAlteradas", [])
      if colunas_alteradas:
        linhas.append(
            f"\t- *Colunas alteradas/adicionadas (estão agora, mas não no anterior):* {len(colunas_alteradas)}\n\t`"
            + "`, `".join(colunas_alteradas)
            + "`"
        )
      else:
        linhas.append(
            "- *Colunas alteradas/adicionadas (estão agora, mas não no anterior):* Nenhuma"
        )

      # Colunas mantidas
      colunas_mantidas = grupo.get("ColunasMantidas", [])
      if colunas_mantidas:
        linhas.append(
            f"\t- *Colunas mantidas (estavam no anterior e continuam agora):* {len(colunas_mantidas)}\n\t`"
            + "`, `".join(colunas_mantidas)
            + "`"
        )
      else:
        # Se for o primeiro período, não há anterior para comparar
        if i == 1:
          linhas.append(
              "- *Colunas mantidas (estavam no anterior e continuam agora):* N/A (Primeiro período)"
          )
        else:
          linhas.append(
              "- *Colunas mantidas (estavam no anterior e continuam agora):* Nenhuma"
          )

      # Arquivos do período
      linhas.append("\n**Arquivos/Recursos Vinculados:**\n")
      arquivos = grupo.get("ArquivosPeriodo", [])
      if arquivos:
        for arq in arquivos:
          linhas.append(
              f"  - 📄 `{arq.get('name')}` *(ID: `{arq.get('id')}`)*\n"
          )
      else:
        linhas.append("  - *Nenhum arquivo listado.*")

      # Lista atual de colunas colapsável
      colunas_atual = grupo.get("ColunasAtual", [])
      linhas.append(
          "\n<details>\n<summary><b>Ver lista completa de colunas neste"
          f" período ({len(colunas_atual)} colunas)</b></summary>\n"
      )
      linhas.append("\n```text")
      linhas.append(", ".join(colunas_atual))
      linhas.append("```\n</details>\n")
      linhas.append("---")

  conteudo_md = "\n".join(linhas)

  # 2. Salva os arquivos UMA ÚNICA VEZ após todo o texto ser compilado
  try:
    diretorio = Path(caminho_saida)
    diretorio.mkdir(parents=True, exist_ok=True)

    # Salva a versão .md
    caminho_completo_md = diretorio / nome_arquivo_saida
    caminho_completo_md.write_text(conteudo_md, encoding="utf-8")
    #print(f"Arquivo .md gerado com sucesso em: '{caminho_completo_md}'")

    # Salva a versão .pdf (se disponível)
    if SUPORTE_PDF:
      conteudo_html = markdown.markdown(
          conteudo_md, extensions=["fenced_code", "tables"]
      )

      html_completo = f"""
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{ font-family: Helvetica, Arial, sans-serif; margin: 30px; color: #333; line-height: 1.5; font-size: 14px; }}
                    h1 {{ color: #004080; border-bottom: 2px solid #004080; padding-bottom: 5px; font-size: 22px; }}
                    h2 {{ color: #0059b3; margin-top: 25px; font-size: 18px; }}
                    h3 {{ color: #222; font-size: 15px; margin-top: 15px; }}
                    hr {{ border: 0; border-top: 1px solid #ddd; margin: 15px 0; }}
                    pre {{ background: #f6f8fa; padding: 10px; border-radius: 4px; font-size: 11px; white-space: pre-wrap; }}
                    code {{ background: #f6f8fa; padding: 2px 4px; border-radius: 3px; font-size: 12px; }}
                    details {{ background: #fafafa; padding: 8px; border: 1px solid #e1e4e8; border-radius: 4px; margin-top: 8px; }}
                    summary {{ font-weight: bold; color: #0059b3; cursor: pointer; }}
                </style>
            </head>
            <body>
                {conteudo_html}
            </body>
            </html>
            """

      nome_arquivo_pdf = Path(nome_arquivo_saida).with_suffix(".pdf").name
      caminho_completo_pdf = diretorio / nome_arquivo_pdf

      HTML(string=html_completo).write_pdf(caminho_completo_pdf)
      #print(f"Arquivo .pdf gerado com sucesso em: '{caminho_completo_pdf}'")
    else:
      print(
          "Aviso: Bibliotecas 'markdown' ou 'weasyprint' não encontradas."
          " Apenas o arquivo .md foi criado."
      )

  except Exception as e:
    print(f"Erro ao salvar os arquivos de relatório: {e}")

  return analise_dict