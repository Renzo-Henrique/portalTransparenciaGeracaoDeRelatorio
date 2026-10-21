# Auditoria Automatizada de Datasets CKAN - Portal da Transparência

Este repositório contém uma ferramenta em Python projetada para automatizar a auditoria estrutural, estatística e de metadados de datasets baseados em portais **CKAN** (como o Portal da Transparência do Estado do Espírito Santo). O sistema agrupa recursos temporais, avalia variações de colunas, audita metadados e calcula métricas de qualidade, gerando relatórios formatados em **Markdown (.md)**, **PDF (.pdf)** e códigos auxiliares em **LaTeX (.tex)**.

---

## 🚀 Arquitetura e Principais Módulos

* **`src/main.py`** (ou `main_2.py`): Script principal que define os IDs dos datasets alvo (como Receitas, Despesas e Contratos) e aciona a geração automatizada de relatórios.
* **`src/queries_metadata.py`**: Realiza a auditoria de metadados dos arquivos do dataset, identificando arquivos desatualizados (> 1 mês), comparando chaves estruturais par a par entre grupos (numerados sequencialmente como `001`, `002`, etc.) e detectando chaves internas com valores idênticos.
* **`src/queries_headers.py`**: Conecta-se via `ckanapi`, filtra arquivos CSV, agrupa recursos por período cronológico e analisa variações estruturais de cabeçalhos e colunas.
* **`src/queries_data.py`**: Realiza amostragem de dados via paginação (com teto de segurança e seed fixa), processa métricas avançadas via `pandas` (nulos, zeros, valores distintos, detecção de enums e estatísticas numéricas/textuais) e aponta colunas duplicadas com nomes diferentes.
* **`src/latex_table.py`**: Converte a estrutura de mapeamento de colunas e períodos diretamente para código LaTeX (`longtable`), facilitando a inclusão em relatórios acadêmicos e técnicos.

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

Para analisar uma base de dados específica do portal da transparência, obtenha o UUID/ID do dataset desejado diretamente na URL do portal CKAN.

Abra o script principal (`src/main.py` ou `main_2.py`) e adicione/ajuste as chamadas de geração:

```python
if __name__ == "__main__":
  # Executa a análise completa para os datasets configurados
  analise_completa()

```

### 4. Executando o Script

Execute a automação através do comando:

```bash
python3 src/main.py >generated/erros.txt

```

Os relatórios consolidados serão salvos automaticamente na pasta `./generated`.

---

## 📖 Como Interpretar os Relatórios

A ferramenta gera três tipos principais de relatórios por base de dados auditada. Veja abaixo como realizar a leitura de cada um deles:

### 1. Relatório de Metadados (`*_metadados.md` / `*.pdf`)

* **Análise de Arquivos Desatualizados:** Identifica rapidamente quais recursos possuem datas de criação ou última modificação superiores a 1 mês em relação ao período atual, alertando sobre defasagens de publicação.
* **Comparação Par a Par entre Grupos:** Mostra de forma cruzada (ex: Grupo `001` vs Grupo `002`) quais chaves estruturais de metadados estão presentes em um grupo e ausentes no outro.
* **Chaves de Metadados do Grupo:** Lista de forma limpa e em um único parágrafo todas as propriedades customizadas e metadados que caracterizam aquele grupo de arquivos.
* **Avisos de Chaves Internas Iguais:** Aponta quando chaves estruturais diferentes dentro de um mesmo arquivo possuem o mesmo valor (ex: `id` e `resource_id`), informando por meio de avisos se o valor difere entre os arquivos ou se permanece idêntico para todos.

### 2. Relatório Estrutural de Cabeçalhos (`*_headers.md` / `*.pdf`)

* **Agrupamento por nome de Arquivo:** Agrupa os arquivos por nomes similares (nomes iguais se retirados os dígitos do arquivo).
* **Evolução Cronológica por Período:** Cria subgrupos por blocos temporais em que a estrutura de colunas permaneceu inalterada.
* **Diferenciação Estrutural:** Aponta exatamente quantas colunas foram adicionadas, removidas ou alteradas em relação ao período imediatamente anterior.
* **Mapeamento de Arquivos e Listagem:** Lista os recursos CKAN vinculados a cada período e traz uma seção expansível (`<details>`) contendo a lista completa de colunas presentes.

### 3. Relatório de Qualidade de Dados (`*_dados.md` / `*.pdf`)

* **Métricas Estatísticas Avançadas:** Exibe contagem e porcentagem de valores nulos e zeros, além da quantidade de valores distintos por coluna.
* **Marcações e Alertas Automáticos:**
* 🟢 `[Enum]`: Indica colunas com características de dados enumerados.
* ⚠️ `[Caso 1: >50 Nulos/Zeros]` e `[Caso 2: >50 Distintos]`: Disparam alertas automáticos de qualidade.
* 📊 **Estatísticas Numéricas / 📝 Texto:** Apresentam mínimo, máximo, média, mediana e desvio padrão (para colunas numéricas) ou comprimentos mínimo, máximo e médio (para colunas de texto).


* **Detecção de Colunas Duplicadas:** Inclui um aviso ao final de cada período listando quais colunas possuem **exatamente as mesmas estatísticas de dados**, auxiliando na identificação de colunas repetidas que possuem nomes diferentes.

