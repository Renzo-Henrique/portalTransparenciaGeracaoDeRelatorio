# Auditoria Automatizada de Datasets CKAN - Portal da Transparência

Este repositório contém uma ferramenta em Python projetada para automatizar a auditoria estrutural, estatística e de metadados de datasets baseados em portais **CKAN** (como o Portal da Transparência do Estado do Espírito Santo), além de suportar a auditoria de **arquivos locais massivos (>1GB)**[cite: 7]. O sistema agrupa recursos temporais, avalia variações de colunas, audita metadados e calcula métricas avançadas de qualidade, gerando relatórios formatados em **Markdown (.md)**, **PDF (.pdf)** e códigos auxiliares em **LaTeX (.tex)**[cite: 1].

---

## 🚀 Arquitetura e Principais Módulos

* **`src/main.py`**: Script principal que define os IDs dos datasets alvo (como Receitas, Despesas e Contratos) e aciona a geração automatizada de relatórios consolidados por base[cite: 3].
* **`src/queries_metadata.py`**: Realiza a auditoria de metadados dos arquivos do dataset, identificando arquivos desatualizados (> 1 mês), comparando chaves estruturais par a par entre grupos (numerados sequencialmente como `001`, `002`, etc.) e detectando chaves internas com valores idênticos[cite: 6].
* **`src/queries_headers.py`**: Conecta-se via `ckanapi`, filtra arquivos CSV, agrupa recursos por período cronológico e analisa variações estruturais de cabeçalhos e colunas (removidas, alteradas e mantidas)[cite: 5].
* **`src/queries_data.py`**: Realiza amostragem de dados via paginação (com teto de segurança e seed fixa), processa métricas avançadas via `pandas` (nulos, zeros, valores distintos, detecção de enums e estatísticas numéricas/textuais) e aponta colunas duplicadas com nomes diferentes[cite: 4].
* **`src/query_file.py`**: Realiza a leitura e auditoria otimizada de **arquivos locais massivos (>1GB)** por meio de processamento em blocos (`chunking`), prevenindo estouros de memória (RAM) e validando a consistência estrutural entre blocos[cite: 7].
* **`src/latex_table.py`**: Converte a estrutura de mapeamento de colunas e períodos diretamente para código LaTeX (`longtable`), facilitando a inclusão em relatórios acadêmicos e técnicos[cite: 2].

---

## 🛠️ Como Utilizar o Código

Siga os passos abaixo para configurar o ambiente e executar a análise de uma base de dados específica do portal ou de um arquivo local:

### 1. Pré-requisitos

Certifique-se de possuir o **Python 3** instalado em sua máquina[cite: 1].

### 2. Configuração do Ambiente Virtual e Instalação de Dependências

Abra o terminal na pasta raiz do projeto e execute os seguintes comandos[cite: 1]:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```

### 3. Configurando a Base de Alvo (`src/main.py`)

Para analisar bases de dados do portal da transparência, obtenha os UUIDs/IDs dos datasets desejados e configure-os no script principal (`src/main.py`):

```python
if __name__ == "__main__":
  # Executa a análise completa para os datasets configurados
  analise_completa_de_bases()

```

### 4. Executando o Script

Execute a automação através do comando:

```bash
python3 src/main.py >generated/erros.txt

```

Para auditar um **arquivo local massivo** isoladamente, utilize o módulo `query_file.py`:

```bash
python3 src/query_file.py

```

Os relatórios consolidados serão salvos automaticamente na pasta `./generated`.

---

## 📖 Como Interpretar os Relatórios

A ferramenta gera diferentes tipos de relatórios focados em metadados, estrutura, qualidade de dados e arquivos locais:

### 1. Relatório de Metadados (`*_metadados.md` / `*.pdf`)

* **Análise de Arquivos Desatualizados:** Identifica recursos com datas de criação ou última modificação superiores a 1 mês.


* **Comparação Par a Par entre Grupos:** Cruzamento estrutural (ex: Grupo `001` vs `002`) para identificar chaves presentes em um grupo e ausentes no outro.


* **Chaves de Metadados e Avisos Internos:** Lista propriedades customizadas e aponta quando chaves internas diferentes possuem o mesmo valor (informando se os valores diferem ou permanecem idênticos entre os arquivos).



### 2. Relatório Estrutural de Cabeçalhos (`*_headers.md` / `*.pdf`)

* **Evolução Cronológica por Período:** Agrupa arquivos por blocos temporais de estabilidade estrutural.


* **Diferenciação Estrutural:** Aponta exata contagem e listagem de colunas adicionadas, removidas ou mantidas em relação ao período anterior.


* **Listagem Expansível:** Seções colapsáveis (`<details>`) com o mapeamento completo das colunas de cada período.



### 3. Relatório de Qualidade de Dados (`*_dados.md` / `*.pdf` ou arquivo local)

* **Métricas Estatísticas Avançadas:** Contagem e porcentagem de valores nulos e zeros, além de valores distintos.


* **Marcações e Alertas Automáticos:**
* 🟢 `[Enum]`: Colunas com características de dados enumerados.


* ⚠️ `[Caso 1: >50 Nulos/Zeros]` e `[Caso 2: >50 Distintos]`: Alertas automáticos de qualidade.


* 📊 **Estatísticas Numéricas / 📝 Texto:** Mínimo, máximo, média, mediana e desvio padrão (numéricos) ou métricas de comprimento de string.




* **Detecção de Colunas Duplicadas:** Aponta colunas que possuem **exatamente as mesmas estatísticas de dados** sob nomes diferentes.

