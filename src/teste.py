from queries_headers import *
from queries_data import *

# Exemplo de uso com o ID fornecido:
if __name__ == "__main__":
  #dataset_id = "3210df25-0dfe-414b-aed4-844ddcdf87bb"
  dataset_id = "99e16b13-0e6f-4504-8544-00de842ab1fd"  # Substitua pelo ID do dataset desejado
  #resultado_obtido = gerar_analise_das_colunas(dataset_id = dataset_id, caminho_saida = "./generated")
  # Exibindo o resultado formatado
  # 1. Agrupa os recursos do dataset
  #dicionario_agrupado = agrupar_recursos_dataset(dataset_id)

  # 2. Faz a análise estrutural por períodos e diferenças
  #analise_dict =analisar_colunas_por_periodo(dicionario_agrupado)

  # 3. EnriquecE o dicionário com as métricas de nulos e enums por arquivo
  #analise_enriquecida = enriquecer_analise_com_qualidade(analise_dict)


  analise_enriquecida = gerar_analise_das_colunas(dataset_id = dataset_id, nome_arquivo_saida="colunasAnalisadasCompletamente.md", caminho_saida = "./generated")
  import json

  print(json.dumps(analise_enriquecida, indent=2, ensure_ascii=False))