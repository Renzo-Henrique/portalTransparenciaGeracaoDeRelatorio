# Relatório de Auditoria e Extração do Dicionário de Dados (CKAN)

Este documento apresenta os achados e o conteúdo estruturado extraído do arquivo PDF de dicionário de dados validado e baixado diretamente do portal CKAN.

---

- **Recurso PDF Analisado:** `Dicionario de Dados`
- **Status da Validação:** 1 arquivo PDF único detectado e processado com sucesso.

---

## 📋 Conteúdo Detalhado por Página


### 📄 Página 1

```text
 
GOVERNO DO ESTADO DO ESPÍRITO SANTO 
Dados Abertos 
Dicionário de Dados 
• Versão: 1.0 
• Autor: Gilmar Hartwig 
• Data: 13/07/2021 
 
Receitas 
Descrição dos campos 
Campo Tipo Descrição 
CodigoUG numeric Código da Unidade Gestora 
DescricaoUG text Descrição da Unidade Gestora 
ContaContabil 
numeric Corresponde ao código da conta contábil, do 
plano de contas do SIGEFES, da qual foi 
extraído o dado. 
DescricaoContaContabil 
text Corresponde ao título da conta contábil, do 
plano de contas do SIGEFES, da qual foi 
extraído o dado. 
CodigoNatureza numeric Código Natureza 
DescricaoNatureza 
text Agrupamento que identifica a origem dos 
recursos, se orçamentários ou extra-
orçamentários. Busca identificar a origem dos 
recursos segundo o fato gerador. Constituem 
receitas orçamentárias os valores constantes 
da lei orçamentária, enquanto as extra-
orçamentárias são todas aquelas 
provenientes de qualquer arrecadação que 
não figure no orçamento e, 
consequentemente, toda arrecadação que 
não constitui renda do Estado. 
CodigoCategoria numeric Código categoria 
DescricaoCategoria 
text A Lei Federal nº 4.320/64, em seu artigo 11, 
classifica a receita orçamentária em duas 
categorias econômicas: Receitas Correntes e 
Receitas de Capital. (*1) 
CodigoOrigem numeric Código origem 
DescricaoOrigem 
text É o detalhamento das Categorias 
Econômicas, que tem por objetivo identificar 
a natureza da procedência das receitas, no 
momento em que ingressam no Orçamento 
Público (*2) 
CodigoEspecie numeric Código espécie 
DescricaoEspecie 
text É o nível de classificação vinculado à Origem 
que permite qualificar com maior detalhe o 
fato gerador dos ingressos das receitas. Por 
exemplo, dentro da Origem Receita 
Tributária, podemos identificar as espécies 
“impostos, taxas e contribuições de melhoria 
```

---

### 📄 Página 2

```text
 
GOVERNO DO ESTADO DO ESPÍRITO SANTO 
CodigoRubrica numeric Código rubrica 
DescricaoRubrica 
text É o detalhamento das espécies de receita. A 
Rubrica busca identificar dentro de cada 
Espécie de receita, uma qualificação mais 
específica. Agrega determinadas receitas com 
características próprias e semelhantes entre 
si. 
CodigoAlinea numeric Código alínea 
DescricaoAlinea 
text É o detalhamento que identifica o nome da 
receita propriamente dita, registrando a 
entrada de recursos financeiros. 
CodigoSubAlinea numeric Código Sub alínea 
DescricaoSubAlinea 
text Constitui o nível mais analítico da receita, 
utilizado quando há necessidade de se 
detalhar a Alínea com maior especificidade 
CodigoIdUso numeric Código ID Uso 
DescricaoIdUso 
text Identificador de despesa que indica se os 
recursos compõem contrapartida nacional de 
empréstimos ou de doações, ou se são 
destinados a outras aplicações, constando da 
LOA e dos créditos adicionais. 
CodigoFonte numeric Código Fonte 
DescricaoFonte 
text Indica a origem ou procedência do dinheiro 
arrecadado. Esta classificação combina o 
critério origem do dinheiro às despesas 
orçamentárias. Esta vinculação visa 
demonstrar o montante de dinheiro que já 
está comprometido com o atendimento de 
determinadas finalidades, e aquele que pode 
ser livremente alocado 
CodigoGrupoFonte numeric Código do Grupo Fonte 
DescricaoGrupoFonte 
text Classificação criada para assegurar que 
receitas vinculadas por lei a finalidade 
específica sejam exclusivamente aplicadas 
em programas e ações que visem à 
consecução desse objetivo 
CodigoDetalhamentoFonte numeric - 
CodigoDetalhamentoFonteAux 
text Corresponde ao código do Detalhamento da 
Fonte, utilizado no SIGEFES para registrar a 
receita. 
DescricaoDetalhamentoFonte 
numeric Corresponde ao título do Detalhamento da 
Fonte, utilizado no SIGEFES para registrar a 
receita. 
ValorPrevista text Valor de arrecadação prevista pelo Governo 
ValorArrecadada numeric Valor efetivamente arrecadado pelo Governo 
DataEmissao text Data de emissão do documento fiscal 
DataContabilizacao numeric Data de contabilização do documento fiscal 
Documento text Número do documento fiscal 
CodigoUGEmitente 
numeric Código da Unidade Gestora emitente do 
documento 
DescricaoUGEmitente text Unidade Gestora emitente do documento 
Tipo numeric Tipo da receita (previsto ou realizad 
id text Código interno de sistema 
```

---

### 📄 Página 3

```text
 
GOVERNO DO ESTADO DO ESPÍRITO SANTO 
Ano numeric Ano que foi efetivada a receita 
 
(*1)  
Receitas Correntes: são arrecadadas dentro do exercício financeiro, aumentam as 
disponibilidades financeiras do Estado, em geral com efeito positivo sobre o Patrimônio 
Líquido e constituem instrumento para financiar os objetivos definidos nos programas e ações 
orçamentários, com vistas a satisfazer finalidades públicas.  
Receitas de Capital: também aumentam as disponibilidades financeiras do Estado e são 
instrumentos de financiamento dos programas e ações orçamentários, a fim de se atingirem as 
finalidades públicas. Porém, de forma diversa das Receitas Correntes, as Receitas de Capital 
em geral não provocam efeito sobre o Patrimônio Líquido. 
(*2)  
Os códigos da Origem para as receitas correntes e de capital, de acordo com a Lei no 4.320, de 
1964, são: 
RECEITAS CORRENTES  
1. Receita Tributária 
2. Receita de Contribuições 
3. Receita Patrimonial 
4. Receita Agropecuária 
5. Receita Industrial 
6. Receita de Serviços 
7. Transferências Correntes 
9. Outras Receitas Correntes 
RECEITAS DE CAPITAL  
1. Operações de Crédito  
2. Alienação de Bens  
3. Amortização de Empréstimos  
4. Transferências de Capital  
5. Outras Receitas de Capital  
Informações Adicionais 
 
```

---