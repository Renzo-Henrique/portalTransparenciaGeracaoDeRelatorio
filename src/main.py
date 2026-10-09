from queries_headers import *
from queries_data import *
import json

_RECEITAS_ID = "3210df25-0dfe-414b-aed4-844ddcdf87bb"
_DESPESAS_ID = "99e16b13-0e6f-4504-8544-00de842ab1fd"
_PREFIXO_ARQUIVO_SAIDA = "analise"


# Exemplo de uso com o ID fornecido:
if __name__ == "__main__":
  # Substitua pelo ID do dataset desejado
  dataset_id = _DESPESAS_ID
  # Substitua pelo nome do arquivo de saída desejado
  prefixo_arquivo_saida = _PREFIXO_ARQUIVO_SAIDA

  gerar_analise_das_colunas_headers(dataset_id = dataset_id, nome_arquivo_saida=f"{prefixo_arquivo_saida}_headers.md", caminho_saida = "./generated")
  analise_enriquecida = gerar_analise_das_colunas_dados(dataset_id = dataset_id, nome_arquivo_saida=f"{prefixo_arquivo_saida}_dados.md", caminho_saida = "./generated")
  

  print(json.dumps(analise_enriquecida, indent=2, ensure_ascii=False))