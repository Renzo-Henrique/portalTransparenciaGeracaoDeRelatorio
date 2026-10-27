# Relatório de Análise Estrutural de Dados - CKAN

Este documento apresenta um resumo consolidado das bases de dados, evolução dos períodos,
variações de colunas e mapeamento de arquivos obtidos do portal de transparência.

---

##  Grupo Principal: `Receitas-`

### 🔹 Período: 2004 até 2015
- **Quantidade Total de Colunas:** `21`
- *Colunas removidas (estavam no anterior, mas não agora):* Nenhuma
- *Colunas alteradas/adicionadas (estão agora, mas não no anterior):* Nenhuma
- *Colunas mantidas (estavam no anterior e continuam agora):* N/A (Primeiro período)

**Arquivos/Recursos Vinculados:**

  - 📄 `Receitas-2004.csv` *(ID: `b6a19383-b5c0-4e03-8da0-c398e69a1b25`)*

  - 📄 `Receitas-2005.csv` *(ID: `73aba44c-bf9a-4d27-8857-e0fa4d5ee90c`)*

  - 📄 `Receitas-2006.csv` *(ID: `022bc3e1-0c64-4bc8-96c7-9867e96b2fa3`)*

  - 📄 `Receitas-2007.csv` *(ID: `8b5f5124-4e08-4cef-bfc6-1a94a180452b`)*

  - 📄 `Receitas-2008.csv` *(ID: `f5d276e6-74d8-411c-a99f-5ab9ddfab940`)*

  - 📄 `Receitas-2009.csv` *(ID: `d2423087-21bf-4cb3-b846-2eddb43ee0e4`)*

  - 📄 `Receitas-2010.csv` *(ID: `6ff68743-0b00-4d22-a5c2-400bf32ea260`)*

  - 📄 `Receitas-2011.csv` *(ID: `f81fa1ba-ad88-4d3b-a4f4-f6bb7e09fd96`)*

  - 📄 `Receitas-2012.csv` *(ID: `533d9285-ce6a-42b7-a90b-70e201e52f5e`)*

  - 📄 `Receitas-2013.csv` *(ID: `86b1b10f-5457-4c5f-8d9a-3885703033c6`)*

  - 📄 `Receitas-2014.csv` *(ID: `4648ee95-b4a2-4189-8db7-8678ab5a9ef9`)*

  - 📄 `Receitas-2015.csv` *(ID: `29181137-01d7-416d-8c74-934b89e0a49b`)*


<details>
<summary><b>Ver lista completa de colunas neste período (21 colunas)</b></summary>


```text
alinea, ano, categoriaEconomica, codAlinea, codCategoriaEconomica, codEspecie, codOrigem, codRubrica, codSubalinea, codUnidadeGestora, codigoDetalhamentoFonteAux, data, especie, mes, origem, previsto, realizado, recolhido, rubrica, subalinea, unidadeGestora
```
</details>

---
### 🔹 Período: 2018 até 2021
- **Quantidade Total de Colunas:** `37`
	- *Colunas removidas (estavam no anterior, mas não agora):* 19
	`alinea`, `categoriaEconomica`, `codAlinea`, `codCategoriaEconomica`, `codEspecie`, `codOrigem`, `codRubrica`, `codSubalinea`, `codUnidadeGestora`, `data`, `especie`, `mes`, `origem`, `previsto`, `realizado`, `recolhido`, `rubrica`, `subalinea`, `unidadeGestora`
	- *Colunas alteradas/adicionadas (estão agora, mas não no anterior):* 35
	`codigoAlinea`, `codigoCategoria`, `codigoDetalhamentoFonte`, `codigoEspecie`, `codigoFonte`, `codigoGrupoFonte`, `codigoIdUso`, `codigoNatureza`, `codigoOrigem`, `codigoRubrica`, `codigoSubAlinea`, `codigoUG`, `codigoUGEmitente`, `contaContabil`, `dataContabilizacao`, `dataEmissao`, `descricaoAlinea`, `descricaoCategoria`, `descricaoContaContabil`, `descricaoDetalhamentoFonte`, `descricaoEspecie`, `descricaoFonte`, `descricaoGrupoFonte`, `descricaoIdUso`, `descricaoNatureza`, `descricaoOrigem`, `descricaoRubrica`, `descricaoSubAlinea`, `descricaoUG`, `descricaoUGEmitente`, `documento`, `tipo`, `tipoLancamento`, `valorArrecadada`, `valorPrevista`
	- *Colunas mantidas (estavam no anterior e continuam agora):* 2
	`ano`, `codigoDetalhamentoFonteAux`

**Arquivos/Recursos Vinculados:**

  - 📄 `Receitas-2018.csv` *(ID: `5e28c8e6-464f-40ce-8c39-403a3d1344c8`)*

  - 📄 `Receitas-2019.csv` *(ID: `e25110cb-31bf-47e2-aa6b-121e3ae6d3e3`)*

  - 📄 `Receitas-2020.csv` *(ID: `254b1dbd-4eb0-429c-9a67-f5dc827d2d57`)*

  - 📄 `Receitas-2021.csv` *(ID: `927c1391-5b16-4ba1-ade7-c474264bbb38`)*


<details>
<summary><b>Ver lista completa de colunas neste período (37 colunas)</b></summary>


```text
ano, codigoAlinea, codigoCategoria, codigoDetalhamentoFonte, codigoDetalhamentoFonteAux, codigoEspecie, codigoFonte, codigoGrupoFonte, codigoIdUso, codigoNatureza, codigoOrigem, codigoRubrica, codigoSubAlinea, codigoUG, codigoUGEmitente, contaContabil, dataContabilizacao, dataEmissao, descricaoAlinea, descricaoCategoria, descricaoContaContabil, descricaoDetalhamentoFonte, descricaoEspecie, descricaoFonte, descricaoGrupoFonte, descricaoIdUso, descricaoNatureza, descricaoOrigem, descricaoRubrica, descricaoSubAlinea, descricaoUG, descricaoUGEmitente, documento, tipo, tipoLancamento, valorArrecadada, valorPrevista
```
</details>

---
### 🔹 Período: 2022
- **Quantidade Total de Colunas:** `47`
	- *Colunas removidas (estavam no anterior, mas não agora):* 6
	`codigoAlinea`, `codigoRubrica`, `codigoSubAlinea`, `descricaoAlinea`, `descricaoRubrica`, `descricaoSubAlinea`
	- *Colunas alteradas/adicionadas (estão agora, mas não no anterior):* 16
	`codigoDetalhamento1`, `codigoDetalhamento2`, `codigoDetalhamento3`, `codigoTipo`, `descricaoDetalhamento1`, `descricaoDetalhamento2`, `descricaoDetalhamento3`, `descricaoTipo`, `valorArrecadadaBruta`, `valorArrecadadaDeducao`, `valorArrecadadaLiquida`, `valorPrevistaBruta`, `valorPrevistaDeducao`, `valorPrevistaLiquida`, `valorRecolhida`, `valorRecolhidaBruta`
	- *Colunas mantidas (estavam no anterior e continuam agora):* 31
	`ano`, `codigoCategoria`, `codigoDetalhamentoFonte`, `codigoDetalhamentoFonteAux`, `codigoEspecie`, `codigoFonte`, `codigoGrupoFonte`, `codigoIdUso`, `codigoNatureza`, `codigoOrigem`, `codigoUG`, `codigoUGEmitente`, `contaContabil`, `dataContabilizacao`, `dataEmissao`, `descricaoCategoria`, `descricaoContaContabil`, `descricaoDetalhamentoFonte`, `descricaoEspecie`, `descricaoFonte`, `descricaoGrupoFonte`, `descricaoIdUso`, `descricaoNatureza`, `descricaoOrigem`, `descricaoUG`, `descricaoUGEmitente`, `documento`, `tipo`, `tipoLancamento`, `valorArrecadada`, `valorPrevista`

**Arquivos/Recursos Vinculados:**

  - 📄 `Receitas-2022.csv` *(ID: `72356e99-d084-45b4-9fd5-8347803cd68a`)*


<details>
<summary><b>Ver lista completa de colunas neste período (47 colunas)</b></summary>


```text
ano, codigoCategoria, codigoDetalhamento1, codigoDetalhamento2, codigoDetalhamento3, codigoDetalhamentoFonte, codigoDetalhamentoFonteAux, codigoEspecie, codigoFonte, codigoGrupoFonte, codigoIdUso, codigoNatureza, codigoOrigem, codigoTipo, codigoUG, codigoUGEmitente, contaContabil, dataContabilizacao, dataEmissao, descricaoCategoria, descricaoContaContabil, descricaoDetalhamento1, descricaoDetalhamento2, descricaoDetalhamento3, descricaoDetalhamentoFonte, descricaoEspecie, descricaoFonte, descricaoGrupoFonte, descricaoIdUso, descricaoNatureza, descricaoOrigem, descricaoTipo, descricaoUG, descricaoUGEmitente, documento, tipo, tipoLancamento, valorArrecadada, valorArrecadadaBruta, valorArrecadadaDeducao, valorArrecadadaLiquida, valorPrevista, valorPrevistaBruta, valorPrevistaDeducao, valorPrevistaLiquida, valorRecolhida, valorRecolhidaBruta
```
</details>

---
### 🔹 Período: 2023
- **Quantidade Total de Colunas:** `56`
	- *Colunas removidas (estavam no anterior, mas não agora):* 47
	`ano`, `codigoCategoria`, `codigoDetalhamento1`, `codigoDetalhamento2`, `codigoDetalhamento3`, `codigoDetalhamentoFonte`, `codigoDetalhamentoFonteAux`, `codigoEspecie`, `codigoFonte`, `codigoGrupoFonte`, `codigoIdUso`, `codigoNatureza`, `codigoOrigem`, `codigoTipo`, `codigoUG`, `codigoUGEmitente`, `contaContabil`, `dataContabilizacao`, `dataEmissao`, `descricaoCategoria`, `descricaoContaContabil`, `descricaoDetalhamento1`, `descricaoDetalhamento2`, `descricaoDetalhamento3`, `descricaoDetalhamentoFonte`, `descricaoEspecie`, `descricaoFonte`, `descricaoGrupoFonte`, `descricaoIdUso`, `descricaoNatureza`, `descricaoOrigem`, `descricaoTipo`, `descricaoUG`, `descricaoUGEmitente`, `documento`, `tipo`, `tipoLancamento`, `valorArrecadada`, `valorArrecadadaBruta`, `valorArrecadadaDeducao`, `valorArrecadadaLiquida`, `valorPrevista`, `valorPrevistaBruta`, `valorPrevistaDeducao`, `valorPrevistaLiquida`, `valorRecolhida`, `valorRecolhidaBruta`
	- *Colunas alteradas/adicionadas (estão agora, mas não no anterior):* 56
	`Alinea`, `Ano`, `ArrecadadaBruta`, `ArrecadadaDeducao`, `ArrecadadaLiquida`, `CategoriaEconomica`, `CodAlinea`, `CodCategoriaEconomica`, `CodDetalhamento1`, `CodDetalhamento2`, `CodDetalhamento3`, `CodEspecie`, `CodNatureza`, `CodOrigem`, `CodRubrica`, `CodSubalinea`, `CodTipo`, `CodUnidadeGestora`, `CodigoContaContabil`, `CodigoDetalhamentoFonte`, `CodigoDetalhamentoFonteAux`, `CodigoFonte`, `CodigoGrupoFonte`, `CodigoIdUso`, `CodigoUGEmitente`, `ContaContabil`, `Data`, `DataContabilizacao`, `DataEmissao`, `Detalhamento1`, `Detalhamento2`, `Detalhamento3`, `DetalhamentoFonte`, `Documento`, `Especie`, `Fonte`, `GrupoFonte`, `Id`, `IdUso`, `Mes`, `Natureza`, `Origem`, `PrevistaBruta`, `PrevistaDeducao`, `PrevistaLiquida`, `Previsto`, `Realizado`, `RecolhidaBruta`, `Recolhido`, `Rubrica`, `Subalinea`, `Tipo`, `TipoArquivo`, `TipoLancamento`, `UGEmitente`, `UnidadeGestora`
- *Colunas mantidas (estavam no anterior e continuam agora):* Nenhuma

**Arquivos/Recursos Vinculados:**

  - 📄 `Receitas-2023.csv` *(ID: `d59902ff-41e5-4b61-a50d-9cf0769c74af`)*


<details>
<summary><b>Ver lista completa de colunas neste período (56 colunas)</b></summary>


```text
Alinea, Ano, ArrecadadaBruta, ArrecadadaDeducao, ArrecadadaLiquida, CategoriaEconomica, CodAlinea, CodCategoriaEconomica, CodDetalhamento1, CodDetalhamento2, CodDetalhamento3, CodEspecie, CodNatureza, CodOrigem, CodRubrica, CodSubalinea, CodTipo, CodUnidadeGestora, CodigoContaContabil, CodigoDetalhamentoFonte, CodigoDetalhamentoFonteAux, CodigoFonte, CodigoGrupoFonte, CodigoIdUso, CodigoUGEmitente, ContaContabil, Data, DataContabilizacao, DataEmissao, Detalhamento1, Detalhamento2, Detalhamento3, DetalhamentoFonte, Documento, Especie, Fonte, GrupoFonte, Id, IdUso, Mes, Natureza, Origem, PrevistaBruta, PrevistaDeducao, PrevistaLiquida, Previsto, Realizado, RecolhidaBruta, Recolhido, Rubrica, Subalinea, Tipo, TipoArquivo, TipoLancamento, UGEmitente, UnidadeGestora
```
</details>

---
### 🔹 Período: 2024 até 2025
- **Quantidade Total de Colunas:** `47`
	- *Colunas removidas (estavam no anterior, mas não agora):* 56
	`Alinea`, `Ano`, `ArrecadadaBruta`, `ArrecadadaDeducao`, `ArrecadadaLiquida`, `CategoriaEconomica`, `CodAlinea`, `CodCategoriaEconomica`, `CodDetalhamento1`, `CodDetalhamento2`, `CodDetalhamento3`, `CodEspecie`, `CodNatureza`, `CodOrigem`, `CodRubrica`, `CodSubalinea`, `CodTipo`, `CodUnidadeGestora`, `CodigoContaContabil`, `CodigoDetalhamentoFonte`, `CodigoDetalhamentoFonteAux`, `CodigoFonte`, `CodigoGrupoFonte`, `CodigoIdUso`, `CodigoUGEmitente`, `ContaContabil`, `Data`, `DataContabilizacao`, `DataEmissao`, `Detalhamento1`, `Detalhamento2`, `Detalhamento3`, `DetalhamentoFonte`, `Documento`, `Especie`, `Fonte`, `GrupoFonte`, `Id`, `IdUso`, `Mes`, `Natureza`, `Origem`, `PrevistaBruta`, `PrevistaDeducao`, `PrevistaLiquida`, `Previsto`, `Realizado`, `RecolhidaBruta`, `Recolhido`, `Rubrica`, `Subalinea`, `Tipo`, `TipoArquivo`, `TipoLancamento`, `UGEmitente`, `UnidadeGestora`
	- *Colunas alteradas/adicionadas (estão agora, mas não no anterior):* 47
	`ano`, `codigoCategoria`, `codigoDetalhamento1`, `codigoDetalhamento2`, `codigoDetalhamento3`, `codigoDetalhamentoFonte`, `codigoDetalhamentoFonteAux`, `codigoEspecie`, `codigoFonte`, `codigoGrupoFonte`, `codigoIdUso`, `codigoNatureza`, `codigoOrigem`, `codigoTipo`, `codigoUG`, `codigoUGEmitente`, `contaContabil`, `dataContabilizacao`, `dataEmissao`, `descricaoCategoria`, `descricaoContaContabil`, `descricaoDetalhamento1`, `descricaoDetalhamento2`, `descricaoDetalhamento3`, `descricaoDetalhamentoFonte`, `descricaoEspecie`, `descricaoFonte`, `descricaoGrupoFonte`, `descricaoIdUso`, `descricaoNatureza`, `descricaoOrigem`, `descricaoTipo`, `descricaoUG`, `descricaoUGEmitente`, `documento`, `tipo`, `tipoLancamento`, `valorArrecadada`, `valorArrecadadaBruta`, `valorArrecadadaDeducao`, `valorArrecadadaLiquida`, `valorPrevista`, `valorPrevistaBruta`, `valorPrevistaDeducao`, `valorPrevistaLiquida`, `valorRecolhida`, `valorRecolhidaBruta`
- *Colunas mantidas (estavam no anterior e continuam agora):* Nenhuma

**Arquivos/Recursos Vinculados:**

  - 📄 `Receitas-2024.csv` *(ID: `9ba06f4d-5c0e-4160-bad3-1a325e432496`)*

  - 📄 `Receitas-2025.csv` *(ID: `2dc2d874-0d72-4c01-b8a0-ecb6f392d6e4`)*


<details>
<summary><b>Ver lista completa de colunas neste período (47 colunas)</b></summary>


```text
ano, codigoCategoria, codigoDetalhamento1, codigoDetalhamento2, codigoDetalhamento3, codigoDetalhamentoFonte, codigoDetalhamentoFonteAux, codigoEspecie, codigoFonte, codigoGrupoFonte, codigoIdUso, codigoNatureza, codigoOrigem, codigoTipo, codigoUG, codigoUGEmitente, contaContabil, dataContabilizacao, dataEmissao, descricaoCategoria, descricaoContaContabil, descricaoDetalhamento1, descricaoDetalhamento2, descricaoDetalhamento3, descricaoDetalhamentoFonte, descricaoEspecie, descricaoFonte, descricaoGrupoFonte, descricaoIdUso, descricaoNatureza, descricaoOrigem, descricaoTipo, descricaoUG, descricaoUGEmitente, documento, tipo, tipoLancamento, valorArrecadada, valorArrecadadaBruta, valorArrecadadaDeducao, valorArrecadadaLiquida, valorPrevista, valorPrevistaBruta, valorPrevistaDeducao, valorPrevistaLiquida, valorRecolhida, valorRecolhidaBruta
```
</details>

---
### 🔹 Período: 2026
- **Quantidade Total de Colunas:** `56`
	- *Colunas removidas (estavam no anterior, mas não agora):* 47
	`ano`, `codigoCategoria`, `codigoDetalhamento1`, `codigoDetalhamento2`, `codigoDetalhamento3`, `codigoDetalhamentoFonte`, `codigoDetalhamentoFonteAux`, `codigoEspecie`, `codigoFonte`, `codigoGrupoFonte`, `codigoIdUso`, `codigoNatureza`, `codigoOrigem`, `codigoTipo`, `codigoUG`, `codigoUGEmitente`, `contaContabil`, `dataContabilizacao`, `dataEmissao`, `descricaoCategoria`, `descricaoContaContabil`, `descricaoDetalhamento1`, `descricaoDetalhamento2`, `descricaoDetalhamento3`, `descricaoDetalhamentoFonte`, `descricaoEspecie`, `descricaoFonte`, `descricaoGrupoFonte`, `descricaoIdUso`, `descricaoNatureza`, `descricaoOrigem`, `descricaoTipo`, `descricaoUG`, `descricaoUGEmitente`, `documento`, `tipo`, `tipoLancamento`, `valorArrecadada`, `valorArrecadadaBruta`, `valorArrecadadaDeducao`, `valorArrecadadaLiquida`, `valorPrevista`, `valorPrevistaBruta`, `valorPrevistaDeducao`, `valorPrevistaLiquida`, `valorRecolhida`, `valorRecolhidaBruta`
	- *Colunas alteradas/adicionadas (estão agora, mas não no anterior):* 56
	`Alinea`, `Ano`, `ArrecadadaBruta`, `ArrecadadaDeducao`, `ArrecadadaLiquida`, `CategoriaEconomica`, `CodAlinea`, `CodCategoriaEconomica`, `CodDetalhamento1`, `CodDetalhamento2`, `CodDetalhamento3`, `CodEspecie`, `CodNatureza`, `CodOrigem`, `CodRubrica`, `CodSubalinea`, `CodTipo`, `CodUnidadeGestora`, `CodigoContaContabil`, `CodigoDetalhamentoFonte`, `CodigoDetalhamentoFonteAux`, `CodigoFonte`, `CodigoGrupoFonte`, `CodigoIdUso`, `CodigoUGEmitente`, `ContaContabil`, `Data`, `DataContabilizacao`, `DataEmissao`, `Detalhamento1`, `Detalhamento2`, `Detalhamento3`, `DetalhamentoFonte`, `Documento`, `Especie`, `Fonte`, `GrupoFonte`, `Id`, `IdUso`, `Mes`, `Natureza`, `Origem`, `PrevistaBruta`, `PrevistaDeducao`, `PrevistaLiquida`, `Previsto`, `Realizado`, `RecolhidaBruta`, `Recolhido`, `Rubrica`, `Subalinea`, `Tipo`, `TipoArquivo`, `TipoLancamento`, `UGEmitente`, `UnidadeGestora`
- *Colunas mantidas (estavam no anterior e continuam agora):* Nenhuma

**Arquivos/Recursos Vinculados:**

  - 📄 `Receitas-2026.csv` *(ID: `dcefa0ca-7e31-4b53-b6bd-0e559ef42d43`)*


<details>
<summary><b>Ver lista completa de colunas neste período (56 colunas)</b></summary>


```text
Alinea, Ano, ArrecadadaBruta, ArrecadadaDeducao, ArrecadadaLiquida, CategoriaEconomica, CodAlinea, CodCategoriaEconomica, CodDetalhamento1, CodDetalhamento2, CodDetalhamento3, CodEspecie, CodNatureza, CodOrigem, CodRubrica, CodSubalinea, CodTipo, CodUnidadeGestora, CodigoContaContabil, CodigoDetalhamentoFonte, CodigoDetalhamentoFonteAux, CodigoFonte, CodigoGrupoFonte, CodigoIdUso, CodigoUGEmitente, ContaContabil, Data, DataContabilizacao, DataEmissao, Detalhamento1, Detalhamento2, Detalhamento3, DetalhamentoFonte, Documento, Especie, Fonte, GrupoFonte, Id, IdUso, Mes, Natureza, Origem, PrevistaBruta, PrevistaDeducao, PrevistaLiquida, Previsto, Realizado, RecolhidaBruta, Recolhido, Rubrica, Subalinea, Tipo, TipoArquivo, TipoLancamento, UGEmitente, UnidadeGestora
```
</details>

---

##  Grupo Principal: `receitas`

### 🔹 Período: 2016 até 2017
- **Quantidade Total de Colunas:** `21`
- *Colunas removidas (estavam no anterior, mas não agora):* Nenhuma
- *Colunas alteradas/adicionadas (estão agora, mas não no anterior):* Nenhuma
- *Colunas mantidas (estavam no anterior e continuam agora):* N/A (Primeiro período)

**Arquivos/Recursos Vinculados:**

  - 📄 `receitas2016.csv` *(ID: `4e32b780-939e-4472-b166-00631f3b8244`)*

  - 📄 `receitas2017.csv` *(ID: `fb0e5556-7f1b-4f08-b62f-6a2080faf5b3`)*


<details>
<summary><b>Ver lista completa de colunas neste período (21 colunas)</b></summary>


```text
alinea, ano, categoriaEconomica, codAlinea, codCategoriaEconomica, codEspecie, codOrigem, codRubrica, codSubalinea, codUnidadeGestora, codigoDetalhamentoFonteAux, data, especie, mes, origem, previsto, realizado, recolhido, rubrica, subalinea, unidadeGestora
```
</details>

---

##  Grupo Principal: `DividaAtiva`

### 🔹 Período: None
- **Quantidade Total de Colunas:** `9`
- *Colunas removidas (estavam no anterior, mas não agora):* Nenhuma
- *Colunas alteradas/adicionadas (estão agora, mas não no anterior):* Nenhuma
- *Colunas mantidas (estavam no anterior e continuam agora):* N/A (Primeiro período)

**Arquivos/Recursos Vinculados:**

  - 📄 `DividaAtiva.csv` *(ID: `016bbc36-15fb-476b-b249-d9726426c82c`)*


<details>
<summary><b>Ver lista completa de colunas neste período (9 colunas)</b></summary>


```text
Ano, CpfCnpj, DataInscricao, Id, NomeDevedor, NumeroCDA, NumeroProcesso, ValorReal, ValorVRTE
```
</details>

---