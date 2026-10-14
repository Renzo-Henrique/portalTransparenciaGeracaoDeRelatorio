# Relatório de Análise Estrutural e Qualidade de Dados - CKAN

Este documento apresenta um resumo consolidado das bases de dados por período, evolução das colunas, métricas de qualidade e estatísticas numéricas consolidadas com marcação de alertas (Caso 1: Nulos/Zeros > 50 e Caso 2: Distintos > 50).

---

## 📂 Grupo Principal: `receitas`

### 🔹 Período: 2004 até 2008
- **Quantidade Total de Colunas:** `21`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`receitas2004.csv`** *(ID: `b6a19383-b5c0-4e03-8da0-c398e69a1b25`)*
  - 📄 **`receitas2005.csv`** *(ID: `73aba44c-bf9a-4d27-8857-e0fa4d5ee90c`)*
  - 📄 **`receitas2006.csv`** *(ID: `022bc3e1-0c64-4bc8-96c7-9867e96b2fa3`)*
  - 📄 **`receitas2007.csv`** *(ID: `8b5f5124-4e08-4cef-bfc6-1a94a180452b`)*
  - 📄 **`receitas2008.csv`** *(ID: `f5d276e6-74d8-411c-a99f-5ab9ddfab940`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `alinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **160** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 31, Tam Média: 25.08, DesvPad Tam: 5.18]

  2. `ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2004.0, Máx: 2008.0, Média: 2005.98, Mediana: 2006.0, DesvPad: 1.4]

  3. `categoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 32, Tam Média: 18.16, DesvPad Tam: 0.98]

  4. `codAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **177** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111204.0, Máx: 980000.0, Média: 171390.0, Mediana: 160020.0, DesvPad: 98981.58]

  5. `codCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9.0, Média: 1.2, Mediana: 1.0, DesvPad: 0.96]

  6. `codEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **40** | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 980.0, Média: 171.1, Mediana: 160.0, DesvPad: 98.99]

  7. `codOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **20** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 98.0, Média: 16.84, Mediana: 16.0, DesvPad: 9.86]

  8. `codRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **72** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 9800.0, Média: 1713.45, Mediana: 1600.0, DesvPad: 989.8]

  9. `codSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **371** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120410.0, Máx: 98000000.0, Média: 17139019.24, Mediana: 16002000.0, DesvPad: 9898156.3]

  10. `codUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **85** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 50901.0, Máx: 800102.0, Média: 521626.68, Mediana: 450284.0, DesvPad: 226271.67]

  11. `codigoDetalhamentoFonteAux` ➔ Nulos: **100.0%** (2420 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  12. `data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  13. `especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **35** | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 32, Tam Média: 22.0, DesvPad Tam: 8.42]

  14. `mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 12.0, Máx: 12.0, Média: 12.0, Mediana: 12.0, DesvPad: 0.0]

  15. `origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **18** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 32, Tam Média: 21.66, DesvPad Tam: 3.2]

  16. `previsto` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **41.82%** (1012 zeros) | Distintos: **1089** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -612385430.0, Máx: 2055529299.0, Média: 17977598.81, Mediana: 20000.0, DesvPad: 104070878.66]

  17. `realizado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **27.31%** (661 zeros) | Distintos: **1747** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -702637561.45, Máx: 2207722670.74, Média: 17172273.73, Mediana: 30462.555, DesvPad: 108821704.7]

  18. `recolhido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (2420 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  19. `rubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 31, Tam Média: 26.09, DesvPad Tam: 5.97]

  20. `subalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **361** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 45, Tam Média: 34.31, DesvPad Tam: 10.53]

  21. `unidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **62** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 18, Tam Média: 7.2, DesvPad Tam: 2.94]

---
### 🔹 Período: 2009
- **Quantidade Total de Colunas:** `0`
  - *Colunas removidas/alteradas:* `alinea`, `ano`, `categoriaEconomica`, `codAlinea`, `codCategoriaEconomica`, `codEspecie`, `codOrigem`, `codRubrica`, `codSubalinea`, `codUnidadeGestora`, `codigoDetalhamentoFonteAux`, `data`, `especie`, `mes`, `origem`, `previsto`, `realizado`, `recolhido`, `rubrica`, `subalinea`, `unidadeGestora`

**Arquivos Vinculados ao Período:**
  - 📄 **`receitas2009.csv`** *(ID: `d2423087-21bf-4cb3-b846-2eddb43ee0e4`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  - *Nenhuma métrica obtida para este período.*
---
### 🔹 Período: 2010 até 2017
- **Quantidade Total de Colunas:** `21`
  - *Colunas removidas/alteradas:* `alinea`, `ano`, `categoriaEconomica`, `codAlinea`, `codCategoriaEconomica`, `codEspecie`, `codOrigem`, `codRubrica`, `codSubalinea`, `codUnidadeGestora`, `codigoDetalhamentoFonteAux`, `data`, `especie`, `mes`, `origem`, `previsto`, `realizado`, `recolhido`, `rubrica`, `subalinea`, `unidadeGestora`

**Arquivos Vinculados ao Período:**
  - 📄 **`receitas2010.csv`** *(ID: `6ff68743-0b00-4d22-a5c2-400bf32ea260`)*
  - 📄 **`receitas2011.csv`** *(ID: `f81fa1ba-ad88-4d3b-a4f4-f6bb7e09fd96`)*
  - 📄 **`receitas2012.csv`** *(ID: `533d9285-ce6a-42b7-a90b-70e201e52f5e`)*
  - 📄 **`receitas2013.csv`** *(ID: `86b1b10f-5457-4c5f-8d9a-3885703033c6`)*
  - 📄 **`receitas2014.csv`** *(ID: `4648ee95-b4a2-4189-8db7-8678ab5a9ef9`)*
  - 📄 **`receitas2015.csv`** *(ID: `29181137-01d7-416d-8c74-934b89e0a49b`)*
  - 📄 **`receitas2016.csv`** *(ID: `4e32b780-939e-4472-b166-00631f3b8244`)*
  - 📄 **`receitas2017.csv`** *(ID: `fb0e5556-7f1b-4f08-b62f-6a2080faf5b3`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `alinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **371** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 154, Tam Média: 40.26, DesvPad Tam: 19.13]

  2. `ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2010.0, Máx: 2017.0, Média: 2013.89, Mediana: 2013.0, DesvPad: 1.98]

  3. `categoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.73, DesvPad Tam: 3.45]

  4. `codAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **423** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111204.0, Máx: 990000.0, Média: 209631.93, Mediana: 132503.0, DesvPad: 203625.18]

  5. `codCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9.0, Média: 1.64, Mediana: 1.0, DesvPad: 2.03]

  6. `codEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **88** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 990.0, Média: 209.34, Mediana: 132.0, DesvPad: 203.65]

  7. `codOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **43** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 99.0, Média: 20.73, Mediana: 13.0, DesvPad: 20.37]

  8. `codRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **162** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 9900.0, Média: 2096.03, Mediana: 1325.0, DesvPad: 2036.25]

  9. `codSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **855** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120410.0, Máx: 99000000.0, Média: 20963212.47, Mediana: 13250399.0, DesvPad: 20362516.67]

  10. `codUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **178** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 60101.0, Máx: 800103.0, Média: 620447.79, Mediana: 800102.0, DesvPad: 219575.47]

  11. `codigoDetalhamentoFonteAux` ➔ Nulos: **100.0%** (34307 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  12. `data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **90** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  13. `especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 48, Tam Média: 20.15, DesvPad Tam: 9.73]

  14. `mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 12.0, Média: 6.44, Mediana: 6.0, DesvPad: 3.46]

  15. `origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 43, Tam Média: 20.85, DesvPad Tam: 3.66]

  16. `previsto` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **91.69%** (31456 zeros) | Distintos: **2494** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -1816461336.0, Máx: 2046565000.0, Média: 2786606.39, Mediana: 0.0, DesvPad: 54660477.88]

  17. `realizado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **4.12%** (1412 zeros) | Distintos: **31576** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -155382354.55, Máx: 689185290.92, Média: 2759383.62, Mediana: 45790.6, DesvPad: 16384203.13]

  18. `recolhido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (34307 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  19. `rubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **149** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 79, Tam Média: 31.31, DesvPad Tam: 9.84]

  20. `subalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **801** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 142, Tam Média: 35.88, DesvPad Tam: 14.99]

  21. `unidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **112** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 89, Tam Média: 39.65, DesvPad Tam: 12.89]

---
### 🔹 Período: 2018 até 2021
- **Quantidade Total de Colunas:** `37`
  - *Colunas removidas/alteradas:* `alinea`, `categoriaEconomica`, `codAlinea`, `codCategoriaEconomica`, `codEspecie`, `codOrigem`, `codRubrica`, `codSubalinea`, `codUnidadeGestora`, `codigoAlinea`, `codigoCategoria`, `codigoDetalhamentoFonte`, `codigoEspecie`, `codigoFonte`, `codigoGrupoFonte`, `codigoIdUso`, `codigoNatureza`, `codigoOrigem`, `codigoRubrica`, `codigoSubAlinea`, `codigoUG`, `codigoUGEmitente`, `contaContabil`, `data`, `dataContabilizacao`, `dataEmissao`, `descricaoAlinea`, `descricaoCategoria`, `descricaoContaContabil`, `descricaoDetalhamentoFonte`, `descricaoEspecie`, `descricaoFonte`, `descricaoGrupoFonte`, `descricaoIdUso`, `descricaoNatureza`, `descricaoOrigem`, `descricaoRubrica`, `descricaoSubAlinea`, `descricaoUG`, `descricaoUGEmitente`, `documento`, `especie`, `mes`, `origem`, `previsto`, `realizado`, `recolhido`, `rubrica`, `subalinea`, `tipo`, `tipoLancamento`, `unidadeGestora`, `valorArrecadada`, `valorPrevista`

**Arquivos Vinculados ao Período:**
  - 📄 **`receitas2018.csv`** *(ID: `5e28c8e6-464f-40ce-8c39-403a3d1344c8`)*
  - 📄 **`receitas2019.csv`** *(ID: `e25110cb-31bf-47e2-aa6b-121e3ae6d3e3`)*
  - 📄 **`receitas2020.csv`** *(ID: `254b1dbd-4eb0-429c-9a67-f5dc827d2d57`)*
  - 📄 **`receitas2021.csv`** *(ID: `927c1391-5b16-4ba1-ade7-c474264bbb38`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2018.0, Máx: 2021.0, Média: 2019.5, Mediana: 2019.5, DesvPad: 1.12]

  2. `codigoAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **137** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111204.0, Máx: 792299.0, Média: 192888.19, Mediana: 133201.0, DesvPad: 162459.06]

  3. `codigoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.44, Mediana: 1.0, DesvPad: 1.56]

  4. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **81.19%** (32477 zeros) | Distintos: **37** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 922.0, Média: 7.91, Mediana: 0.0, DesvPad: 52.76]

  5. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.05%** (20 zeros) | Distintos: **161** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 675.000002, Média: 234.36, Mediana: 271.0, DesvPad: 63.93]

  6. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 192.58, Mediana: 133.0, DesvPad: 162.52]

  7. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.05%** (20 zeros) | Distintos: **57** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 675.0, Média: 234.36, Mediana: 271.0, DesvPad: 63.93]

  8. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.05%** (20 zeros) | Distintos: **5** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 6.0, Média: 1.74, Mediana: 2.0, DesvPad: 0.44]

  9. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **97.72%** (39087 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5.0, Média: 0.09, Mediana: 0.0, DesvPad: 0.59]

  10. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **331** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120410.0, Máx: 79229900.0, Média: 19288845.21, Mediana: 13320199.0, DesvPad: 16245900.05]

  11. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 19.05, Mediana: 13.0, DesvPad: 16.25]

  12. `codigoRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7922.0, Média: 1928.49, Mediana: 1332.0, DesvPad: 1624.61]

  13. `codigoSubAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **331** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120410.0, Máx: 79229900.0, Média: 19288845.21, Mediana: 13320199.0, DesvPad: 16245900.05]

  14. `codigoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **96** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 20101.0, Máx: 800102.0, Média: 279413.27, Mediana: 310201.0, DesvPad: 162082.22]

  15. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **118** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 282328.2, Mediana: 310201.0, DesvPad: 165219.44]

  16. `contaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 521110000.0, Máx: 621390000.0, Média: 615669129.0, Mediana: 621200000.0, DesvPad: 22881642.52]

  17. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23465** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  18. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1061** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  19. `descricaoAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **126** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 154, Tam Média: 39.65, DesvPad Tam: 24.02]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 19.39, DesvPad Tam: 4.94]

  21. `descricaoContaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 43, Tam Média: 18.86, DesvPad Tam: 5.79]

  22. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **174** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 174, Tam Média: 23.94, DesvPad Tam: 12.76]

  23. `descricaoEspecie` ➔ Nulos: **17.19%** (6876 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **21** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 39, Tam Média: 21.07, DesvPad Tam: 11.56]

  24. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **65** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 111, Tam Média: 23.7, DesvPad Tam: 8.76]

  25. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 49, Tam Média: 23.46, DesvPad Tam: 2.69]

  26. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 21, Tam Máx: 96, Tam Média: 38.61, DesvPad Tam: 2.73]

  27. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **340** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 152, Tam Média: 43.26, DesvPad Tam: 22.83]

  28. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 26, Tam Média: 20.24, DesvPad Tam: 2.83]

  29. `descricaoRubrica` ➔ Nulos: **30.33%** (12130 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **35** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 74, Tam Média: 30.77, DesvPad Tam: 8.57]

  30. `descricaoSubAlinea` ➔ Nulos: **21.4%** (8559 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **267** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 152, Tam Média: 42.72, DesvPad Tam: 22.54]

  31. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **161** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 87, Tam Média: 29.57, DesvPad Tam: 26.11]

  32. `descricaoUGEmitente` ➔ Nulos: **0.13%** (53 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **216** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 87, Tam Média: 30.0, DesvPad Tam: 26.25]

  33. `documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12140** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  34. `tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 10, Tam Média: 9.89, DesvPad Tam: 0.46]

  35. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  36. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **5.54%** (2214 zeros) | Distintos: **30197** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -37883149.01, Máx: 38894780.44, Média: 31265.26, Mediana: 965.335, DesvPad: 721945.48]

  37. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **94.47%** (37787 zeros) | Distintos: **1942** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -335784072.0, Máx: 2413081000.0, Média: 996352.95, Mediana: 0.0, DesvPad: 23882606.7]

---
### 🔹 Período: 2022 até 2026
- **Quantidade Total de Colunas:** `47`
  - *Colunas removidas/alteradas:* `codigoAlinea`, `codigoDetalhamento1`, `codigoDetalhamento2`, `codigoDetalhamento3`, `codigoRubrica`, `codigoSubAlinea`, `codigoTipo`, `descricaoAlinea`, `descricaoDetalhamento1`, `descricaoDetalhamento2`, `descricaoDetalhamento3`, `descricaoRubrica`, `descricaoSubAlinea`, `descricaoTipo`, `valorArrecadadaBruta`, `valorArrecadadaDeducao`, `valorArrecadadaLiquida`, `valorPrevistaBruta`, `valorPrevistaDeducao`, `valorPrevistaLiquida`, `valorRecolhida`, `valorRecolhidaBruta`

**Arquivos Vinculados ao Período:**
  - 📄 **`receitas2022.csv`** *(ID: `72356e99-d084-45b4-9fd5-8347803cd68a`)*
  - 📄 **`receitas2023.csv`** *(ID: `d59902ff-41e5-4b61-a50d-9cf0769c74af`)*
  - 📄 **`receitas2024.csv`** *(ID: `9ba06f4d-5c0e-4160-bad3-1a325e432496`)*
  - 📄 **`receitas2025.csv`** *(ID: `2dc2d874-0d72-4c01-b8a0-ecb6f392d6e4`)*
  - 📄 **`receitas2026.csv`** *(ID: `58349543-d608-4bb6-b4a7-6483e9d2e3fb`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2022.0, Máx: 2026.0, Média: 2024.0, Mediana: 2024.0, DesvPad: 1.41]

  2. `codigoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.1, Mediana: 1.0, DesvPad: 0.74]

  3. `codigoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7923.0, Média: 1296.64, Mediana: 1114.0, DesvPad: 795.21]

  4. `codigoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **170** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 792399.0, Média: 129705.1, Mediana: 111450.0, DesvPad: 79515.56]

  5. `codigoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **207** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 7923990.0, Média: 1297051.81, Mediana: 1114501.0, DesvPad: 795155.56]

  6. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **48.79%** (24395 zeros) | Distintos: **150** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 900000.0, Média: 16303.01, Mediana: 1.0, DesvPad: 59152.14]

  7. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **348** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.000675, Média: 460.24, Mediana: 500.0, DesvPad: 186.06]

  8. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 129.33, Mediana: 111.0, DesvPad: 79.52]

  9. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **111** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.0, Média: 460.22, Mediana: 500.0, DesvPad: 186.05]

  10. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 8.0, Média: 4.51, Mediana: 5.0, DesvPad: 1.85]

  11. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **19.95%** (9976 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4.0, Média: 0.8, Mediana: 1.0, DesvPad: 0.41]

  12. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **257** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79239901.0, Média: 12970519.71, Mediana: 11145011.0, DesvPad: 7951555.5]

  13. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 12.81, Mediana: 11.0, DesvPad: 7.94]

  14. `codigoTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **257** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79239901.0, Média: 12970519.71, Mediana: 11145011.0, DesvPad: 7951555.5]

  15. `codigoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **161** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 724585.85, Mediana: 800102.0, DesvPad: 176607.36]

  16. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **191** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 717561.01, Mediana: 800102.0, DesvPad: 188414.1]

  17. `contaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **17** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621390000.0, Média: 462087411.89, Mediana: 621200000.0, DesvPad: 236107636.15]

  18. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **29466** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  19. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1169** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.3, DesvPad Tam: 2.34]

  21. `descricaoContaContabil` ➔ Nulos: **31.15%** (15573 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 19.39, DesvPad Tam: 7.42]

  22. `descricaoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **43** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 142, Tam Média: 52.66, DesvPad Tam: 17.77]

  23. `descricaoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **96** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 145, Tam Média: 56.95, DesvPad Tam: 14.04]

  24. `descricaoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **119** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 154, Tam Média: 112.17, DesvPad Tam: 52.5]

  25. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **253** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 185, Tam Média: 47.53, DesvPad Tam: 24.21]

  26. `descricaoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 84, Tam Média: 12.18, DesvPad Tam: 10.86]

  27. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **75** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 141, Tam Média: 34.44, DesvPad Tam: 12.11]

  28. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 50, Tam Média: 43.97, DesvPad Tam: 12.1]

  29. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 39, Tam Média: 31.78, DesvPad Tam: 3.62]

  30. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **158** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 116.57, DesvPad Tam: 45.85]

  31. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 39.23, DesvPad Tam: 8.49]

  32. `descricaoTipo` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **157** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 116.57, DesvPad Tam: 45.85]

  33. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **95** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 89, Tam Média: 37.62, DesvPad Tam: 8.7]

  34. `descricaoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **105** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 20.07, DesvPad Tam: 6.54]

  35. `documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.03%** (17 zeros) | Distintos: **14501** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  36. `tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 18, Tam Média: 16.03, DesvPad Tam: 1.27]

  37. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  38. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  39. `valorArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **84.33%** (42165 zeros) | Distintos: **7126** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -77685138.12, Máx: 109787939.65, Média: 36715.0, Mediana: 0.0, DesvPad: 1586033.89]

  40. `valorArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **96.82%** (48409 zeros) | Distintos: **1522** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -48583192.37, Máx: 1152899.22, Média: -9028.48, Mediana: 0.0, DesvPad: 445804.46]

  41. `valorArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **82.07%** (41035 zeros) | Distintos: **8079** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -180000000.0, Máx: 357518954.24, Média: 88171.52, Mediana: 0.0, DesvPad: 4932917.06]

  42. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  43. `valorPrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.95%** (49976 zeros) | Distintos: **26** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 669467432.0, Média: 21986.31, Mediana: 0.0, DesvPad: 3092585.11]

  44. `valorPrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  45. `valorPrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.83%** (49916 zeros) | Distintos: **79** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -172865464.0, Máx: 1983274603.0, Média: 101956.33, Mediana: 0.0, DesvPad: 11775905.5]

  46. `valorRecolhida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  47. `valorRecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **57.0%** (28499 zeros) | Distintos: **17944** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -85001407.33, Máx: 84544358.68, Média: 39177.96, Mediana: 0.0, DesvPad: 2188475.47]

---

## 📂 Grupo Principal: `Receitas-`

### 🔹 Período: 2023 até 2026
- **Quantidade Total de Colunas:** `56`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Receitas-2023.csv`** *(ID: `0fea9fda-9e19-4268-9a1e-e1ace5dcce3d`)*
  - 📄 **`Receitas-2024.csv`** *(ID: `e08d6239-0fc0-400c-8c69-256f7f2ff5fd`)*
  - 📄 **`Receitas-2025.csv`** *(ID: `b499bf46-4df3-4fb7-a526-99c53c6c0902`)*
  - 📄 **`Receitas-2026.csv`** *(ID: `dcefa0ca-7e31-4b53-b6bd-0e559ef42d43`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Alinea` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2023.0, Máx: 2026.0, Média: 2024.5, Mediana: 2024.5, DesvPad: 1.12]

  3. `ArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **87.39%** (34957 zeros) | Distintos: **4323** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -3736209.87, Máx: 13551083.08, Média: 6205.06, Mediana: 0.0, DesvPad: 176235.96]

  4. `ArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **94.55%** (37819 zeros) | Distintos: **2137** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -190892.09, Máx: 84869.51, Média: -908.24, Mediana: 0.0, DesvPad: 7044.88]

  5. `ArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **64.69%** (25876 zeros) | Distintos: **12144** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -117641911.39, Máx: 69098934.06, Média: -18029.79, Mediana: 0.0, DesvPad: 1270082.44]

  6. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.2, DesvPad Tam: 1.94]

  7. `CodAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **64** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 761101.0, Média: 126204.49, Mediana: 111450.0, DesvPad: 65860.34]

  8. `CodCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.06, Mediana: 1.0, DesvPad: 0.61]

  9. `CodDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7611.0, Média: 1261.63, Mediana: 1114.0, DesvPad: 658.65]

  10. `CodDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **64** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 761101.0, Média: 126204.49, Mediana: 111450.0, DesvPad: 65860.34]

  11. `CodDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **77** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 7611010.0, Média: 1262045.63, Mediana: 1114501.0, DesvPad: 658603.39]

  12. `CodEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **18** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 761.0, Média: 125.82, Mediana: 111.0, DesvPad: 65.86]

  13. `CodNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **104** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 76110101.0, Média: 12620457.82, Mediana: 11145011.0, DesvPad: 6586033.75]

  14. `CodOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 76.0, Média: 12.46, Mediana: 11.0, DesvPad: 6.57]

  15. `CodRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7611.0, Média: 1261.63, Mediana: 1114.0, DesvPad: 658.65]

  16. `CodSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **104** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 76110101.0, Média: 12620457.82, Mediana: 11145011.0, DesvPad: 6586033.75]

  17. `CodTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **104** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 76110101.0, Média: 12620457.82, Mediana: 11145011.0, DesvPad: 6586033.75]

  18. `CodUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 735340.86, Mediana: 800102.0, DesvPad: 159801.04]

  19. `CodigoContaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621350000.0, Média: 456015004.7, Mediana: 621200000.0, DesvPad: 238710180.64]

  20. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **43.68%** (17473 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 900000.0, Média: 18922.03, Mediana: 2.0, DesvPad: 70843.13]

  21. `CodigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **108** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.00011, Média: 541.12, Mediana: 500.000003, DesvPad: 100.47]

  22. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **36** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 541.1, Mediana: 500.0, DesvPad: 100.47]

  23. `CodigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 5.0, Máx: 8.0, Média: 5.35, Mediana: 5.0, DesvPad: 0.86]

  24. `CodigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.04%** (18 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2.0, Média: 1.0, Mediana: 1.0, DesvPad: 0.02]

  25. `CodigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **70** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 717853.26, Mediana: 800102.0, DesvPad: 181843.91]

  26. `ContaContabil` ➔ Nulos: **32.39%** (12955 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 21.98, DesvPad Tam: 10.46]

  27. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **46** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  28. `DataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26109** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  29. `DataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **983** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  30. `Detalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **28** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 142, Tam Média: 52.91, DesvPad Tam: 17.86]

  31. `Detalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **64** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 144, Tam Média: 56.32, DesvPad Tam: 13.28]

  32. `Detalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **77** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 154, Tam Média: 111.48, DesvPad Tam: 53.03]

  33. `DetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 173, Tam Média: 52.54, DesvPad Tam: 21.13]

  34. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.03%** (12 zeros) | Distintos: **12391** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  35. `Especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **15** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 59, Tam Média: 11.86, DesvPad Tam: 10.57]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **36** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 140, Tam Média: 36.19, DesvPad Tam: 10.08]

  37. `GrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 50, Tam Máx: 50, Tam Média: 50.0, DesvPad Tam: 0.0]

  38. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **40000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 403491956.0, Máx: 606465554.0, Média: 485476064.75, Mediana: 465973374.5, DesvPad: 82410673.6]

  39. `IdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 33, Tam Média: 29.99, DesvPad Tam: 0.38]

  40. `Mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 12.0, Média: 6.33, Mediana: 6.0, DesvPad: 3.29]

  41. `Natureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **105** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 116.03, DesvPad Tam: 46.63]

  42. `Origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 39.59, DesvPad Tam: 8.17]

  43. `PrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (40000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  44. `PrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (40000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  45. `PrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (40000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  46. `Previsto` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Realizado` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `RecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **53.37%** (21348 zeros) | Distintos: **13403** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -2105477.95, Máx: 5974037.02, Média: 7685.19, Mediana: 0.0, DesvPad: 176710.6]

  49. `Recolhido` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  50. `Rubrica` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Subalinea` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  52. `Tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **105** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 116.03, DesvPad Tam: 46.63]

  53. `TipoArquivo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 18, Tam Média: 16.35, DesvPad Tam: 1.41]

  54. `TipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  55. `UGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 19.79, DesvPad Tam: 6.9]

  56. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 87, Tam Média: 37.21, DesvPad Tam: 7.65]

---

## 📂 Grupo Principal: `DividaAtiva`

### 🔹 Período: None
- **Quantidade Total de Colunas:** `9`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`DividaAtiva.csv`** *(ID: `016bbc36-15fb-476b-b249-d9726426c82c`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2015.0, Máx: 2015.0, Média: 2015.0, Mediana: 2015.0, DesvPad: 0.0]

  2. `CpfCnpj` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **677** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 18, Tam Média: 17.96, DesvPad Tam: 0.44]

  3. `DataInscricao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **223** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  4. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2506** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 175.0, Máx: 90133.0, Média: 43559.36, Mediana: 40719.0, DesvPad: 26655.36]

  5. `NomeDevedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **576** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 83, Tam Média: 34.11, DesvPad Tam: 12.34]

  6. `NumeroCDA` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2506** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 30.0, Máx: 7502.0, Média: 3773.18, Mediana: 3914.5, DesvPad: 2253.38]

  7. `NumeroProcesso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2506** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 14638304.0, Máx: 72572175.0, Média: 65512581.8, Mediana: 69318624.5, DesvPad: 9538608.79]

  8. `ValorReal` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2404** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 181.21, Máx: 701099582.27, Média: 2111177.61, Mediana: 115837.595, DesvPad: 22150853.84]

  9. `ValorVRTE` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (2506 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

---