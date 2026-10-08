from queries import agrupar_recursos_dataset, analisar_colunas_por_periodo

# Exemplo de uso com o ID fornecido:
if __name__ == "__main__":
  #dataset_id = "3210df25-0dfe-414b-aed4-844ddcdf87bb"
  dataset_id = "99e16b13-0e6f-4504-8544-00de842ab1fd"  # Substitua pelo ID do dataset desejado
  resultado_agrupado = agrupar_recursos_dataset(dataset_id)
  resultado_analisado = analisar_colunas_por_periodo(resultado_agrupado)
  # Exibindo o resultado formatado
  import json

  print(json.dumps(resultado_analisado, indent=2, ensure_ascii=False))