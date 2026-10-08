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