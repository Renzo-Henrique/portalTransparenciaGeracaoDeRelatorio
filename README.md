# Auditoria Automatizada de Datasets CKAN - Portal da Transparência

Este repositório contém uma ferramenta em Python projetada para automatizar a auditoria estrutural e estatística de datasets baseados em portais **CKAN** (como o Portal da Transparência do Estado do Espírito Santo). O script agrupa recursos temporais, avalia variações de colunas e executa análises estatísticas de qualidade (contagem de nulos, zeros, valores distintos e detecção de enums) gerando relatórios formatados em **Markdown (.md)** e **PDF (.pdf)**.

---

## 🚀 Arquitetura e Principais Módulos

* **`src/main.py`**: Script principal que define os IDs dos datasets alvo (como Receitas e Despesas) e aciona as funções de geração de relatórios de cabeçalhos e dados estatísticos.


* **`src/queries_headers.py`**: Realiza a conexão via `ckanapi`, consulta os metadados do pacote, filtra arquivos CSV, agrupa recursos por prefixo textual removendo extensões e dígitos numéricos, e analisa colunas por período cronológico.


* **`src/queries_data.py`**: Realiza a amostragem de dados via paginação (limitada a no máximo 30.000 registros utilizando uma `seed` fixa para reprodutibilidade), processa métricas por meio do `pandas` com proteções robustas contra travamentos e gera os relatórios detalhados.



---

## 🛠️ Como Utilizar o Código

Siga os passos abaixo para configurar o ambiente e executar a análise de uma base de dados específica do portal:

### 1. Pré-requisitos

Certifique-se de possuir o **Python 3** instalado em sua máquina.

### 2. Configuração do Ambiente Virtual e Instalação de Dependências

Abra o terminal na pasta raiz do projeto e execute os seguintes comandos:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```

### 3. Configurando a Base de Alvo (`src/main.py`)

Para analisar uma base de dados específica do portal da transparência, você pode obter o UUID/ID do dataset desejado diretamente na URL da página do dataset no portal CKAN.

Abra o arquivo `src/main.py` e altere a constante correspondente ou adicione um novo identificador na chamada principal:

```python
if __name__ == "__main__":
  # Insira o ID (UUID) do dataset do portal CKAN que deseja auditar
  dataset_id = "seu-dataset-uuid-aqui"
  prefixo_arquivo_saida = "relatorio_auditoria"

  # Gera a análise estrutural de cabeçalhos e colunas
  gerar_analise_das_colunas_headers(dataset_id=dataset_id, nome_arquivo_saida=f"{prefixo_arquivo_saida}_headers.md", caminho_saida="./generated")
  
  # Gera a análise detalhada de qualidade de dados (nulos, zeros e enums)
  analise_enriquecida = gerar_analise_das_colunas_dados(dataset_id=dataset_id, nome_arquivo_saida=f"{prefixo_arquivo_saida}_dados.md", caminho_saida="./generated")

```

### 4. Executando o Script

Após configurar o ID do dataset desejado, execute o script de automação através do comando:

```bash
python3 src/main.py

```

Os relatórios consolidados em **Markdown** e **PDF** serão gerados automaticamente dentro da pasta `./generated` informada no código.