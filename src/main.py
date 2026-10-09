from queries_headers import *
from queries_data import *
import json

_RECEITAS_ID = "3210df25-0dfe-414b-aed4-844ddcdf87bb"
_DESPESAS_ID = "99e16b13-0e6f-4504-8544-00de842ab1fd"
_PREFIXO_ARQUIVO_SAIDA = "analise"

def analise_completa():
  gerar_analise_das_colunas_headers(dataset_id = _RECEITAS_ID, nome_arquivo_saida=f"{_PREFIXO_ARQUIVO_SAIDA}_receitas_headers.md", caminho_saida = "./generated")
  gerar_analise_das_colunas_dados(dataset_id = _RECEITAS_ID, nome_arquivo_saida=f"{_PREFIXO_ARQUIVO_SAIDA}_receitas_dados.md", caminho_saida = "./generated")
  gerar_analise_das_colunas_headers(dataset_id = _DESPESAS_ID, nome_arquivo_saida=f"{_PREFIXO_ARQUIVO_SAIDA}_despesas_headers.md", caminho_saida = "./generated")
  gerar_analise_das_colunas_dados(dataset_id = _DESPESAS_ID, nome_arquivo_saida=f"{_PREFIXO_ARQUIVO_SAIDA}_despesas_dados.md", caminho_saida = "./generated")

# Exemplo de uso com o ID fornecido:
if __name__ == "__main__":
  # # Substitua pelo ID do dataset desejado
  # dataset_id = _DESPESAS_ID
  # # Substitua pelo nome do arquivo de saída desejado
  # prefixo_arquivo_saida = _PREFIXO_ARQUIVO_SAIDA

  # # Gerar análise das colunas e salvar em arquivos Markdown e PDF
  # gerar_analise_das_colunas_headers(dataset_id = dataset_id, nome_arquivo_saida=f"{prefixo_arquivo_saida}_headers.md", caminho_saida = "./generated")
  # # Gerar análise das colunas de dados e salvar em arquivo Markdown e PDF
  # analise_enriquecida = gerar_analise_das_colunas_dados(dataset_id = dataset_id, nome_arquivo_saida=f"{prefixo_arquivo_saida}_dados.md", caminho_saida = "./generated")
  
  # Se você quiser ver a análise enriquecida no console, descomente a linha abaixo:
  # print(json.dumps(analise_enriquecida, indent=2, ensure_ascii=False))

  analise_completa()