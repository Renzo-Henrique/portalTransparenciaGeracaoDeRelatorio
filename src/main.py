from queries_headers import *
from queries_data import *
from queries_metadata import *
from query_file import *

_RECEITAS_ID = "3210df25-0dfe-414b-aed4-844ddcdf87bb"
_DESPESAS_ID = "99e16b13-0e6f-4504-8544-00de842ab1fd"
_CONTRATOS_ID = "36f4bfc0-48f2-4cf9-a812-5249724da742"
_PREFIXO_ARQUIVO_SAIDA = "analise"

def analise_completa_da_base(id, nome_base):
  gerar_analise_metadados(dataset_id = id, nome_arquivo_saida=f"{_PREFIXO_ARQUIVO_SAIDA}_{nome_base}_metadados.md", caminho_saida = "./generated")
  gerar_analise_das_colunas_headers(dataset_id = id, nome_arquivo_saida=f"{_PREFIXO_ARQUIVO_SAIDA}_{nome_base}_headers.md", caminho_saida = "./generated")
  gerar_analise_das_colunas_dados(dataset_id = id, nome_arquivo_saida=f"{_PREFIXO_ARQUIVO_SAIDA}_{nome_base}_dados.md", caminho_saida = "./generated")


def analise_completa_de_bases():
  analise_completa_da_base(_RECEITAS_ID, "receitas")
  analise_completa_da_base(_DESPESAS_ID, "despesas")
  analise_completa_da_base(_CONTRATOS_ID, "contratos")



# Exemplo de uso com o ID fornecido:
if __name__ == "__main__":

  analise_completa_de_bases()