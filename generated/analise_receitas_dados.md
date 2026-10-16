# Relatório de Análise Estrutural e Qualidade de Dados - CKAN

Este documento apresenta um resumo consolidado das bases de dados por período, evolução das colunas, métricas de qualidade e estatísticas numéricas consolidadas com marcação de alertas (Caso 1: Nulos/Zeros > 50 e Caso 2: Distintos > 50).

---

## 📂 Grupo Principal: `receitas`

### 🔹 Período: 2004 até 2017
- **Quantidade Total de Colunas:** `21`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`receitas2004.csv`** *(ID: `b6a19383-b5c0-4e03-8da0-c398e69a1b25`)*
  - 📄 **`receitas2005.csv`** *(ID: `73aba44c-bf9a-4d27-8857-e0fa4d5ee90c`)*
  - 📄 **`receitas2006.csv`** *(ID: `022bc3e1-0c64-4bc8-96c7-9867e96b2fa3`)*
  - 📄 **`receitas2007.csv`** *(ID: `8b5f5124-4e08-4cef-bfc6-1a94a180452b`)*
  - 📄 **`receitas2008.csv`** *(ID: `f5d276e6-74d8-411c-a99f-5ab9ddfab940`)*
  - 📄 **`receitas2009.csv`** *(ID: `d2423087-21bf-4cb3-b846-2eddb43ee0e4`)*
  - 📄 **`receitas2010.csv`** *(ID: `6ff68743-0b00-4d22-a5c2-400bf32ea260`)*
  - 📄 **`receitas2011.csv`** *(ID: `f81fa1ba-ad88-4d3b-a4f4-f6bb7e09fd96`)*
  - 📄 **`receitas2012.csv`** *(ID: `533d9285-ce6a-42b7-a90b-70e201e52f5e`)*
  - 📄 **`receitas2013.csv`** *(ID: `86b1b10f-5457-4c5f-8d9a-3885703033c6`)*
  - 📄 **`receitas2014.csv`** *(ID: `4648ee95-b4a2-4189-8db7-8678ab5a9ef9`)*
  - 📄 **`receitas2015.csv`** *(ID: `29181137-01d7-416d-8c74-934b89e0a49b`)*
  - 📄 **`receitas2016.csv`** *(ID: `4e32b780-939e-4472-b166-00631f3b8244`)*
  - 📄 **`receitas2017.csv`** *(ID: `fb0e5556-7f1b-4f08-b62f-6a2080faf5b3`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `alinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **517** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 154, Tam Média: 38.7, DesvPad Tam: 16.57]

  2. `ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2004.0, Máx: 2017.0, Média: 2012.27, Mediana: 2012.0, DesvPad: 2.83]

  3. `categoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.62, DesvPad Tam: 3.2]

  4. `codAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **525** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111204.0, Máx: 990000.0, Média: 196179.33, Mediana: 132503.0, DesvPad: 184635.29]

  5. `codCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9.0, Média: 1.52, Mediana: 1.0, DesvPad: 1.83]

  6. `codEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **104** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 990.0, Média: 195.88, Mediana: 132.0, DesvPad: 184.66]

  7. `codOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **50** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 99.0, Média: 19.38, Mediana: 13.0, DesvPad: 18.47]

  8. `codRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **196** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 9900.0, Média: 1961.52, Mediana: 1325.0, DesvPad: 1846.35]

  9. `codSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1072** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120410.0, Máx: 99000000.0, Média: 19617951.86, Mediana: 13250301.0, DesvPad: 18463527.72]

  10. `codUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **227** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 50901.0, Máx: 800103.0, Média: 627372.72, Mediana: 800102.0, DesvPad: 219182.46]

  11. `codigoDetalhamentoFonteAux` ➔ Nulos: **100.0%** (53936 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  12. `data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **113** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  13. `especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **73** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 48, Tam Média: 19.73, DesvPad Tam: 9.91]

  14. `mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 12.0, Média: 6.72, Mediana: 7.0, DesvPad: 3.63]

  15. `origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 43, Tam Média: 20.69, DesvPad Tam: 3.52]

  16. `previsto` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **88.67%** (47824 zeros) | Distintos: **5102** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -1816461336.0, Máx: 2055529299.0, Média: 3225948.92, Mediana: 0.0, DesvPad: 51643788.01]

  17. `realizado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **5.06%** (2731 zeros) | Distintos: **49016** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -702637561.45, Máx: 2207722670.74, Média: 3109164.27, Mediana: 49350.815, DesvPad: 27129377.59]

  18. `recolhido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (53936 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  19. `rubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **200** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 79, Tam Média: 31.85, DesvPad Tam: 9.47]

  20. `subalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **967** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 142, Tam Média: 34.83, DesvPad Tam: 13.71]

  21. `unidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **177** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 89, Tam Média: 37.94, DesvPad Tam: 13.82]

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


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `codigoNatureza`, `codigoSubAlinea`


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

  2. `codigoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.09, Mediana: 1.0, DesvPad: 0.74]

  3. `codigoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **90** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7923.0, Média: 1295.41, Mediana: 1114.0, DesvPad: 792.6]

  4. `codigoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **171** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 792399.0, Média: 129582.9, Mediana: 111450.0, DesvPad: 79254.54]

  5. `codigoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **209** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 7923990.0, Média: 1295829.81, Mediana: 1114501.0, DesvPad: 792545.42]

  6. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **48.95%** (24476 zeros) | Distintos: **148** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 900000.0, Média: 16203.61, Mediana: 1.0, DesvPad: 58925.94]

  7. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **333** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.000675, Média: 459.92, Mediana: 500.0, DesvPad: 186.59]

  8. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 129.2, Mediana: 111.0, DesvPad: 79.26]

  9. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **111** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.0, Média: 459.9, Mediana: 500.0, DesvPad: 186.58]

  10. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 8.0, Média: 4.51, Mediana: 5.0, DesvPad: 1.85]

  11. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **19.98%** (9992 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4.0, Média: 0.8, Mediana: 1.0, DesvPad: 0.4]

  12. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **258** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79239901.0, Média: 12958299.62, Mediana: 11145011.0, DesvPad: 7925454.05]

  13. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 12.8, Mediana: 11.0, DesvPad: 7.91]

  14. `codigoTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **258** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79239901.0, Média: 12958299.62, Mediana: 11145011.0, DesvPad: 7925454.05]

  15. `codigoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **164** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 726183.4, Mediana: 800102.0, DesvPad: 175628.58]

  16. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **194** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 719414.76, Mediana: 800102.0, DesvPad: 186988.54]

  17. `contaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621390000.0, Média: 465314248.05, Mediana: 621200000.0, DesvPad: 234791130.07]

  18. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **29312** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  19. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1169** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.29, DesvPad Tam: 2.33]

  21. `descricaoContaContabil` ➔ Nulos: **30.52%** (15259 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 19.23, DesvPad Tam: 7.17]

  22. `descricaoDetalhamento1` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **43** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 142, Tam Média: 52.69, DesvPad Tam: 17.71]

  23. `descricaoDetalhamento2` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **94** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 145, Tam Média: 56.95, DesvPad Tam: 13.9]

  24. `descricaoDetalhamento3` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **118** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 154, Tam Média: 112.36, DesvPad Tam: 52.43]

  25. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **240** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 185, Tam Média: 47.52, DesvPad Tam: 24.2]

  26. `descricaoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 84, Tam Média: 12.15, DesvPad Tam: 10.87]

  27. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **75** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 141, Tam Média: 34.35, DesvPad Tam: 12.06]

  28. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 50, Tam Média: 43.96, DesvPad Tam: 12.11]

  29. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 39, Tam Média: 31.79, DesvPad Tam: 3.61]

  30. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **157** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 116.72, DesvPad Tam: 45.79]

  31. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 39.3, DesvPad Tam: 8.43]

  32. `descricaoTipo` ➔ Nulos: **0.0%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **156** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 116.72, DesvPad Tam: 45.79]

  33. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **100** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 37.5, DesvPad Tam: 8.47]

  34. `descricaoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **110** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 20.15, DesvPad Tam: 6.46]

  35. `documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.04%** (19 zeros) | Distintos: **14448** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  36. `tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 18, Tam Média: 16.04, DesvPad Tam: 1.28]

  37. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  38. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  39. `valorArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **79.81%** (39905 zeros) | Distintos: **9079** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -122363213.04, Máx: 122363213.04, Média: 53649.59, Mediana: 0.0, DesvPad: 2368382.61]

  40. `valorArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **96.07%** (48036 zeros) | Distintos: **1873** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -48583192.37, Máx: 10070104.99, Média: -15323.87, Mediana: 0.0, DesvPad: 662814.75]

  41. `valorArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **76.07%** (38036 zeros) | Distintos: **10606** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -180000000.0, Máx: 357518954.24, Média: 89774.1, Mediana: 0.0, DesvPad: 4964182.35]

  42. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  43. `valorPrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.95%** (49975 zeros) | Distintos: **26** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 669467432.0, Média: 22061.98, Mediana: 0.0, DesvPad: 3092630.87]

  44. `valorPrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.99%** (49995 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: -11453638.0, Máx: 0.0, Média: -361.32, Mediana: 0.0, DesvPad: 54569.98]

  45. `valorPrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.83%** (49916 zeros) | Distintos: **78** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -172865464.0, Máx: 1983274603.0, Média: 101956.33, Mediana: 0.0, DesvPad: 11775905.5]

  46. `valorRecolhida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  47. `valorRecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **48.27%** (24137 zeros) | Distintos: **21230** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -85001407.33, Máx: 84544358.68, Média: 42516.86, Mediana: 0.0, DesvPad: 2201216.29]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `codigoNatureza`, `codigoTipo`

> - `valorArrecadada`, `valorPrevista`, `valorRecolhida`


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

  3. `ArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **86.0%** (34402 zeros) | Distintos: **4776** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -3736209.87, Máx: 13551083.08, Média: 6776.11, Mediana: 0.0, DesvPad: 176961.1]

  4. `ArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **95.52%** (38207 zeros) | Distintos: **1761** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -86279.82, Máx: 84869.51, Média: -847.69, Mediana: 0.0, DesvPad: 6456.61]

  5. `ArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **70.69%** (28277 zeros) | Distintos: **9951** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -5916549.75, Máx: 34907227.6, Média: 420.29, Mediana: 0.0, DesvPad: 398413.49]

  6. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.2, DesvPad Tam: 1.94]

  7. `CodAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **61** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 761101.0, Média: 126369.2, Mediana: 111450.0, DesvPad: 65791.72]

  8. `CodCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.06, Mediana: 1.0, DesvPad: 0.61]

  9. `CodDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **32** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7611.0, Média: 1263.28, Mediana: 1114.0, DesvPad: 657.97]

  10. `CodDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **61** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 761101.0, Média: 126369.2, Mediana: 111450.0, DesvPad: 65791.72]

  11. `CodDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **75** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 7611010.0, Média: 1263692.83, Mediana: 1114501.0, DesvPad: 657917.2]

  12. `CodEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **20** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 761.0, Média: 125.98, Mediana: 111.0, DesvPad: 65.79]

  13. `CodNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **101** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 76110101.0, Média: 12636929.75, Mediana: 11145011.0, DesvPad: 6579171.87]

  14. `CodOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 76.0, Média: 12.47, Mediana: 11.0, DesvPad: 6.56]

  15. `CodRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **32** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7611.0, Média: 1263.28, Mediana: 1114.0, DesvPad: 657.97]

  16. `CodSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **101** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 76110101.0, Média: 12636929.75, Mediana: 11145011.0, DesvPad: 6579171.87]

  17. `CodTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **101** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 76110101.0, Média: 12636929.75, Mediana: 11145011.0, DesvPad: 6579171.87]

  18. `CodUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **32** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 30901.0, Máx: 800102.0, Média: 732161.7, Mediana: 800102.0, DesvPad: 157289.63]

  19. `CodigoContaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621350000.0, Média: 439753968.61, Mediana: 621200000.0, DesvPad: 244211970.85]

  20. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **43.69%** (17474 zeros) | Distintos: **58** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 900000.0, Média: 21150.62, Mediana: 2.0, DesvPad: 72085.46]

  21. `CodigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **108** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.00011, Média: 542.51, Mediana: 500.000003, DesvPad: 101.2]

  22. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **36** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 542.49, Mediana: 500.0, DesvPad: 101.19]

  23. `CodigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 5.0, Máx: 8.0, Média: 5.36, Mediana: 5.0, DesvPad: 0.86]

  24. `CodigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.04%** (18 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2.0, Média: 1.0, Mediana: 1.0, DesvPad: 0.02]

  25. `CodigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **70** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 714674.1, Mediana: 800102.0, DesvPad: 179331.18]

  26. `ContaContabil` ➔ Nulos: **35.58%** (14230 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 21.69, DesvPad Tam: 10.17]

  27. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **46** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  28. `DataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26580** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  29. `DataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **987** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  30. `Detalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 142, Tam Média: 52.67, DesvPad Tam: 18.11]

  31. `Detalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **61** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 144, Tam Média: 56.15, DesvPad Tam: 13.85]

  32. `Detalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **75** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 154, Tam Média: 111.52, DesvPad Tam: 53.26]

  33. `DetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 173, Tam Média: 52.52, DesvPad Tam: 21.23]

  34. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.04%** (16 zeros) | Distintos: **12803** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  35. `Especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **17** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 59, Tam Média: 11.94, DesvPad Tam: 10.45]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **36** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 140, Tam Média: 37.02, DesvPad Tam: 13.63]

  37. `GrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 50, Tam Máx: 50, Tam Média: 50.0, DesvPad Tam: 0.0]

  38. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **40000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 403491956.0, Máx: 608071310.0, Média: 485877503.75, Mediana: 465973374.5, DesvPad: 83000833.54]

  39. `IdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 33, Tam Média: 29.99, DesvPad Tam: 0.38]

  40. `Mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 12.0, Média: 6.35, Mediana: 6.0, DesvPad: 3.28]

  41. `Natureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **102** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 115.79, DesvPad Tam: 46.68]

  42. `Origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 39.26, DesvPad Tam: 8.53]

  43. `PrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (40000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  44. `PrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (40000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  45. `PrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (40000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  46. `Previsto` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Realizado` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `RecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **47.78%** (19114 zeros) | Distintos: **14990** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -2105477.95, Máx: 5974037.02, Média: 6933.23, Mediana: 0.0, DesvPad: 145935.26]

  49. `Recolhido` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  50. `Rubrica` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Subalinea` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  52. `Tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **102** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 115.79, DesvPad Tam: 46.68]

  53. `TipoArquivo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 18, Tam Média: 16.15, DesvPad Tam: 1.36]

  54. `TipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  55. `UGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 19.53, DesvPad Tam: 7.1]

  56. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **32** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 87, Tam Média: 36.64, DesvPad Tam: 7.22]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `Alinea`, `Previsto`, `Realizado`, `Recolhido`, `Rubrica`, `Subalinea`

> - `CodAlinea`, `CodDetalhamento2`

> - `CodDetalhamento1`, `CodRubrica`

> - `CodNatureza`, `CodSubalinea`, `CodTipo`

> - `Natureza`, `Tipo`

> - `PrevistaBruta`, `PrevistaDeducao`, `PrevistaLiquida`


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

  4. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2506** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 350.0, Máx: 90069.0, Média: 47653.66, Mediana: 49892.5, DesvPad: 24318.88]

  5. `NomeDevedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **576** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 83, Tam Média: 34.1, DesvPad Tam: 12.34]

  6. `NumeroCDA` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2506** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 30.0, Máx: 7502.0, Média: 3773.18, Mediana: 3914.5, DesvPad: 2253.38]

  7. `NumeroProcesso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2506** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 14638304.0, Máx: 72572175.0, Média: 65512581.8, Mediana: 69318624.5, DesvPad: 9538608.79]

  8. `ValorReal` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2402** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 182.69, Máx: 706254913.65, Média: 2121533.7, Mediana: 116239.405, DesvPad: 22287092.17]

  9. `ValorVRTE` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (2506 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

---