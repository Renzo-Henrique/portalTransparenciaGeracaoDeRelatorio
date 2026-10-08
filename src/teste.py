from queries_headers import gerar_analise_das_colunas

# Exemplo de uso com o ID fornecido:
if __name__ == "__main__":
  #dataset_id = "3210df25-0dfe-414b-aed4-844ddcdf87bb"
  dataset_id = "99e16b13-0e6f-4504-8544-00de842ab1fd"  # Substitua pelo ID do dataset desejado
  resultado_obtido = gerar_analise_das_colunas(dataset_id = dataset_id, caminho_saida = "./generated")
  # Exibindo o resultado formatado
  import json

  #print(json.dumps(resultado_analisado, indent=2, ensure_ascii=False))