import os
import re
from ckanapi import RemoteCKAN


def agrupar_recursos_dataset(
    dataset_id, portal_url="https://dados.es.gov.br/"
):
  """Consulta um dataset no CKAN e agrupa seus recursos por prefixo de nome

  (removendo extensões e dígitos, preservando o case).
  """
  rc = RemoteCKAN(portal_url)
  grupos = {}

  try:
    # Obtém os detalhes do dataset
    dataset = rc.action.package_show(id=dataset_id)
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
    print(f"Erro ao processar o dataset {dataset_id}: {e}")
    return {}


def analisar_colunas_por_periodo(
    dicionario_agrupado, portal_url="https://dados.es.gov.br/"
):
  """Analisa os recursos agrupados, extrai os anos, verifica as colunas via Datastore,

  agrupa os períodos consecutivos com a mesma estrutura e inclui a lista e a
  quantidade
  de colunas diferentes em relação ao grupo anterior.
  """
  rc = RemoteCKAN(portal_url)
  resultado_final = {}

  for chave_principal, lista_recursos in dicionario_agrupado.items():
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
    prev_cols_set = None

    for ano, rec in recursos_com_ano:
      res_id = rec["id"]
      colunas = []

      try:
        # limit=0 busca apenas a estrutura/metadados dos campos sem baixar os dados
        ds_res = rc.action.datastore_search(resource_id=res_id, limit=0)
        fields = ds_res.get("fields", [])
        # Extrai os nomes das colunas (ignorando o campo interno '_id' do CKAN)
        colunas = [f["id"] for f in fields if f["id"] != "_id"]
      except Exception:
        # Se o recurso não estiver no datastore ou falhar, mantém lista vazia
        pass

      # Ordena alfabeticamente a lista de colunas atual
      colunas_ordenadas = sorted(colunas)
      colunas_tuple = tuple(colunas_ordenadas)
      colunas_set = set(colunas_ordenadas)

      if current_group is None:
        current_group = {
            "PeriodoInicio": ano if ano != 0 else None,
            "PeriodoFim": ano if ano != 0 else None,
            "QtdColunas": len(colunas_ordenadas),
            "ColunasAtual": colunas_ordenadas,
            "signature": colunas_tuple,
            "diff": [],
            "qtd_diff": 0,
        }
        prev_cols_set = colunas_set
      else:
        # Se mantiver exatamente as mesmas colunas do grupo anterior, estende o período fim
        if current_group["signature"] == colunas_tuple:
          if ano != 0:
            current_group["PeriodoFim"] = ano
        else:
          # Mudou a estrutura: calcula quais colunas diferem e a quantidade
          diff_cols = sorted(list(prev_cols_set ^ colunas_set))
          qtd_diff = len(diff_cols)

          # Salva o grupo anterior completo com a quantidade de diferenças
          grupos_colunas.append({
              "PeriodoInicio": current_group["PeriodoInicio"],
              "PeriodoFim": current_group["PeriodoFim"],
              "QtdColunas": current_group["QtdColunas"],
              "ColunasAtual": current_group["ColunasAtual"],
              "QtdColunasDiferentesAoAnterior": current_group["qtd_diff"],
              "ColunasDiferentesAoAnterior": current_group["diff"],
          })

          # Atualiza a referência anterior e inicia um novo grupo
          prev_cols_set = set(current_group["ColunasAtual"])
          current_group = {
              "PeriodoInicio": ano if ano != 0 else None,
              "PeriodoFim": ano if ano != 0 else None,
              "QtdColunas": len(colunas_ordenadas),
              "ColunasAtual": colunas_ordenadas,
              "signature": colunas_tuple,
              "qtd_diff": qtd_diff,
              "diff": diff_cols,
          }

    # Adiciona o último grupo remanescente
    if current_group is not None:
      grupos_colunas.append({
          "PeriodoInicio": current_group["PeriodoInicio"],
          "PeriodoFim": current_group["PeriodoFim"],
          "QtdColunas": current_group["QtdColunas"],
          "ColunasAtual": current_group["ColunasAtual"],
          "QtdColunasDiferentesAoAnterior": current_group["qtd_diff"],
          "ColunasDiferentesAoAnterior": current_group["diff"],
      })

    resultado_final[chave_principal] = grupos_colunas

  return resultado_final