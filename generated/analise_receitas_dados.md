# Relatório de Análise Estrutural e Qualidade de Dados - CKAN

Este documento apresenta um resumo consolidado das bases de dados por período, evolução das colunas, métricas de qualidade e estatísticas numéricas consolidadas com marcação de alertas (Caso 1: Nulos/Zeros > 50 e Caso 2: Distintos > 50). Foram utilizados apenas `10000 registros por recurso`

---

## 📂 Grupo Principal: `Receitas-`

### 🔹 Período: 2004 até 2015
- **Quantidade Total de Colunas:** `21`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Receitas-2004.csv`** *(ID: `b6a19383-b5c0-4e03-8da0-c398e69a1b25`)*
  - 📄 **`Receitas-2005.csv`** *(ID: `73aba44c-bf9a-4d27-8857-e0fa4d5ee90c`)*
  - 📄 **`Receitas-2006.csv`** *(ID: `022bc3e1-0c64-4bc8-96c7-9867e96b2fa3`)*
  - 📄 **`Receitas-2007.csv`** *(ID: `8b5f5124-4e08-4cef-bfc6-1a94a180452b`)*
  - 📄 **`Receitas-2008.csv`** *(ID: `f5d276e6-74d8-411c-a99f-5ab9ddfab940`)*
  - 📄 **`Receitas-2009.csv`** *(ID: `d2423087-21bf-4cb3-b846-2eddb43ee0e4`)*
  - 📄 **`Receitas-2010.csv`** *(ID: `6ff68743-0b00-4d22-a5c2-400bf32ea260`)*
  - 📄 **`Receitas-2011.csv`** *(ID: `f81fa1ba-ad88-4d3b-a4f4-f6bb7e09fd96`)*
  - 📄 **`Receitas-2012.csv`** *(ID: `533d9285-ce6a-42b7-a90b-70e201e52f5e`)*
  - 📄 **`Receitas-2013.csv`** *(ID: `86b1b10f-5457-4c5f-8d9a-3885703033c6`)*
  - 📄 **`Receitas-2014.csv`** *(ID: `4648ee95-b4a2-4189-8db7-8678ab5a9ef9`)*
  - 📄 **`Receitas-2015.csv`** *(ID: `29181137-01d7-416d-8c74-934b89e0a49b`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `alinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **424** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 112, Tam Média: 36.87, DesvPad Tam: 11.24]

  2. `ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2004.0, Máx: 2015.0, Média: 2011.48, Mediana: 2012.0, DesvPad: 2.26]

  3. `categoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.56, DesvPad Tam: 3.0]

  4. `codAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **498** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 6, Tam Média: 6.0, DesvPad Tam: 0.05]

  5. `codCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9.0, Média: 1.54, Mediana: 1.0, DesvPad: 1.88]

  6. `codEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **101** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 4, Tam Média: 3.0, DesvPad Tam: 0.02]

  7. `codOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **50** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 2, Tam Máx: 4, Tam Média: 2.0, DesvPad Tam: 0.05]

  8. `codRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **193** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 4, Tam Média: 4.0, DesvPad Tam: 0.0]

  9. `codSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **985** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 8, Tam Média: 8.0, DesvPad Tam: 0.09]

  10. `codUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **195** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 50901.0, Máx: 800103.0, Média: 640855.09, Mediana: 800102.0, DesvPad: 216097.55]

  11. `codigoDetalhamentoFonteAux` ➔ Nulos: **100.0%** (46293 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  12. `data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  13. `especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 48, Tam Média: 19.38, DesvPad Tam: 9.97]

  14. `mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 12.0, Média: 6.76, Mediana: 7.0, DesvPad: 3.64]

  15. `origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 43, Tam Média: 20.55, DesvPad Tam: 3.57]

  16. `previsto` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **88.16%** (40812 zeros) | Distintos: **4676** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -1699765235.0, Máx: 2055529299.0, Média: 3000746.79, Mediana: 0.0, DesvPad: 49393953.96]

  17. `realizado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **4.98%** (2305 zeros) | Distintos: **42310** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -702637561.45, Máx: 2207722670.74, Média: 2909258.71, Mediana: 49766.26, DesvPad: 28399378.65]

  18. `recolhido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (46293 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  19. `rubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **162** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 79, Tam Média: 32.29, DesvPad Tam: 9.07]

  20. `subalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **719** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 112, Tam Média: 33.39, DesvPad Tam: 11.68]

  21. `unidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **158** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 89, Tam Média: 37.35, DesvPad Tam: 13.45]

---
### 🔹 Período: 2018 até 2021
- **Quantidade Total de Colunas:** `37`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Receitas-2018.csv`** *(ID: `5e28c8e6-464f-40ce-8c39-403a3d1344c8`)*
  - 📄 **`Receitas-2019.csv`** *(ID: `e25110cb-31bf-47e2-aa6b-121e3ae6d3e3`)*
  - 📄 **`Receitas-2020.csv`** *(ID: `254b1dbd-4eb0-429c-9a67-f5dc827d2d57`)*
  - 📄 **`Receitas-2021.csv`** *(ID: `927c1391-5b16-4ba1-ade7-c474264bbb38`)*

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
### 🔹 Período: 2022
- **Quantidade Total de Colunas:** `47`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Receitas-2022.csv`** *(ID: `72356e99-d084-45b4-9fd5-8347803cd68a`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2022.0, Máx: 2022.0, Média: 2022.0, Mediana: 2022.0, DesvPad: 0.0]

  2. `codigoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.1, Mediana: 1.0, DesvPad: 0.78]

  3. `codigoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7922.0, Média: 1298.01, Mediana: 1114.0, DesvPad: 828.41]

  4. `codigoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 792299.0, Média: 129842.99, Mediana: 111450.0, DesvPad: 82835.65]

  5. `codigoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **76** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 7922990.0, Média: 1298430.72, Mediana: 1114501.0, DesvPad: 828356.5]

  6. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **60.79%** (6079 zeros) | Distintos: **29** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 312700.0, Média: 130.64, Mediana: 0.0, DesvPad: 5416.99]

  7. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **68** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 301.0, Média: 133.6, Mediana: 101.000002, DesvPad: 57.02]

  8. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **21** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 129.46, Mediana: 111.0, DesvPad: 82.84]

  9. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **31** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 301.0, Média: 133.6, Mediana: 101.0, DesvPad: 57.02]

  10. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 3.0, Média: 1.14, Mediana: 1.0, DesvPad: 0.34]

  11. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.82%** (9982 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4.0, Média: 0.01, Mediana: 0.0, DesvPad: 0.17]

  12. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **92** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79229901.0, Média: 12984308.87, Mediana: 11145011.0, DesvPad: 8283564.92]

  13. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 12.82, Mediana: 11.0, DesvPad: 8.27]

  14. `codigoTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **92** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79229901.0, Média: 12984308.87, Mediana: 11145011.0, DesvPad: 8283564.92]

  15. `codigoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **52** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 20101.0, Máx: 800102.0, Média: 723823.36, Mediana: 800102.0, DesvPad: 182876.61]

  16. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **67** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 20101.0, Máx: 800102.0, Média: 719534.85, Mediana: 800102.0, DesvPad: 190607.6]

  17. `contaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621350000.0, Média: 519541477.8, Mediana: 621200000.0, DesvPad: 203718321.52]

  18. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4090** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  19. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **267** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.32, DesvPad Tam: 2.46]

  21. `descricaoContaContabil` ➔ Nulos: **19.92%** (1992 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 18.87, DesvPad Tam: 6.63]

  22. `descricaoDetalhamento1` ➔ Nulos: **0.02%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **28** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 142, Tam Média: 53.27, DesvPad Tam: 17.39]

  23. `descricaoDetalhamento2` ➔ Nulos: **0.02%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 144, Tam Média: 56.79, DesvPad Tam: 13.68]

  24. `descricaoDetalhamento3` ➔ Nulos: **0.02%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **70** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 154, Tam Média: 113.3, DesvPad Tam: 52.17]

  25. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **65** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 107, Tam Média: 26.86, DesvPad Tam: 18.46]

  26. `descricaoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 59, Tam Média: 11.88, DesvPad Tam: 10.61]

  27. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **31** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 109, Tam Média: 25.84, DesvPad Tam: 10.17]

  28. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 43, Tam Média: 19.82, DesvPad Tam: 2.09]

  29. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 21, Tam Máx: 39, Tam Média: 38.97, DesvPad Tam: 0.76]

  30. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **92** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 117.63, DesvPad Tam: 45.55]

  31. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 39.44, DesvPad Tam: 8.4]

  32. `descricaoTipo` ➔ Nulos: **0.01%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **91** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 117.63, DesvPad Tam: 45.55]

  33. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **52** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 37.44, DesvPad Tam: 8.62]

  34. `descricaoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **67** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 20.25, DesvPad Tam: 6.33]

  35. `documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.04%** (4 zeros) | Distintos: **3056** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  36. `tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 18, Tam Média: 16.24, DesvPad Tam: 1.31]

  37. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  38. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  39. `valorArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **77.4%** (7740 zeros) | Distintos: **1963** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -122363213.04, Máx: 122363213.04, Média: 84672.97, Mediana: 0.0, DesvPad: 3933083.44]

  40. `valorArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **96.27%** (9627 zeros) | Distintos: **353** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -45469071.49, Máx: 10070104.99, Média: -31476.94, Mediana: 0.0, DesvPad: 1096669.79]

  41. `valorArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **70.01%** (7001 zeros) | Distintos: **2543** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -42974894.88, Máx: 43300137.19, Média: 8012.9, Mediana: 0.0, DesvPad: 1244403.49]

  42. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  43. `valorPrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.99%** (9999 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 3783792.0, Média: 378.38, Mediana: 0.0, DesvPad: 37836.03]

  44. `valorPrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.95%** (9995 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: -11453638.0, Máx: 0.0, Média: -1806.61, Mediana: 0.0, DesvPad: 122011.49]

  45. `valorPrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  46. `valorRecolhida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  47. `valorRecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **56.38%** (5638 zeros) | Distintos: **3323** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -10872727.41, Máx: 10890244.39, Média: 16694.5, Mediana: 0.0, DesvPad: 529836.3]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `codigoNatureza`, `codigoTipo`

> - `valorArrecadada`, `valorPrevista`, `valorPrevistaLiquida`, `valorRecolhida`


---
### 🔹 Período: 2023
- **Quantidade Total de Colunas:** `56`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Receitas-2023.csv`** *(ID: `d59902ff-41e5-4b61-a50d-9cf0769c74af`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Alinea` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2023.0, Máx: 2023.0, Média: 2023.0, Mediana: 2023.0, DesvPad: 0.0]

  3. `ArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **81.69%** (8169 zeros) | Distintos: **1490** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -3736209.87, Máx: 13551083.08, Média: 20151.88, Mediana: 0.0, DesvPad: 342053.6]

  4. `ArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **96.33%** (9633 zeros) | Distintos: **362** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -5820.26, Máx: 5689.12, Média: -169.69, Mediana: 0.0, DesvPad: 906.04]

  5. `ArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **95.94%** (9594 zeros) | Distintos: **325** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -62634.24, Máx: 322866.05, Média: 161.44, Mediana: 0.0, DesvPad: 6662.47]

  6. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.52, DesvPad Tam: 3.09]

  7. `CodAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **44** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 761101.0, Média: 137335.35, Mediana: 111450.0, DesvPad: 100854.19]

  8. `CodCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.16, Mediana: 1.0, DesvPad: 0.98]

  9. `CodDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **21** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7611.0, Média: 1372.98, Mediana: 1114.0, DesvPad: 1008.61]

  10. `CodDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **44** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 761101.0, Média: 137335.35, Mediana: 111450.0, DesvPad: 100854.19]

  11. `CodDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **53** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 7611010.0, Média: 1373354.34, Mediana: 1114501.0, DesvPad: 1008541.96]

  12. `CodEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 761.0, Média: 136.95, Mediana: 111.0, DesvPad: 100.84]

  13. `CodNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 76110101.0, Média: 13733545.0, Mediana: 11145011.0, DesvPad: 10085419.44]

  14. `CodOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 76.0, Média: 13.57, Mediana: 11.0, DesvPad: 10.08]

  15. `CodRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **21** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7611.0, Média: 1372.98, Mediana: 1114.0, DesvPad: 1008.61]

  16. `CodSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 76110101.0, Média: 13733545.0, Mediana: 11145011.0, DesvPad: 10085419.44]

  17. `CodTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 76110101.0, Média: 13733545.0, Mediana: 11145011.0, DesvPad: 10085419.44]

  18. `CodUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 30901.0, Máx: 800102.0, Média: 696988.27, Mediana: 800102.0, DesvPad: 198271.13]

  19. `CodigoContaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621340000.0, Média: 407684400.22, Mediana: 621200000.0, DesvPad: 251646774.02]

  20. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **49.39%** (4939 zeros) | Distintos: **28** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 213100.0, Média: 13418.8, Mediana: 2.0, DesvPad: 33790.28]

  21. `CodigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.00011, Média: 569.19, Mediana: 500.000004, DesvPad: 121.44]

  22. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 569.18, Mediana: 500.0, DesvPad: 121.45]

  23. `CodigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 5.0, Máx: 8.0, Média: 5.61, Mediana: 5.0, DesvPad: 1.1]

  24. `CodigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.18%** (18 zeros) | Distintos: **2** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1.0, Média: 1.0, Mediana: 1.0, DesvPad: 0.04]

  25. `CodigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **42** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 664875.31, Mediana: 800102.0, DesvPad: 237371.17]

  26. `ContaContabil` ➔ Nulos: **41.86%** (4186 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 19.32, DesvPad Tam: 7.54]

  27. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  28. `DataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6662** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  29. `DataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **263** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  30. `Detalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 80, Tam Média: 54.53, DesvPad Tam: 17.97]

  31. `Detalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **43** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 144, Tam Média: 55.17, DesvPad Tam: 13.84]

  32. `Detalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **52** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 154, Tam Média: 104.26, DesvPad Tam: 54.45]

  33. `DetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 140, Tam Média: 46.5, DesvPad Tam: 17.19]

  34. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.03%** (3 zeros) | Distintos: **3615** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  35. `Especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 47, Tam Média: 12.86, DesvPad Tam: 10.94]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 140, Tam Média: 38.6, DesvPad Tam: 13.52]

  37. `GrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 50, Tam Máx: 50, Tam Média: 50.0, DesvPad Tam: 0.0]

  38. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 415731210.0, Máx: 415741209.0, Média: 415736209.5, Mediana: 415736209.5, DesvPad: 2886.75]

  39. `IdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 30, Tam Média: 29.97, DesvPad Tam: 0.76]

  40. `Mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 12.0, Média: 6.82, Mediana: 7.0, DesvPad: 3.34]

  41. `Natureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 109.81, DesvPad Tam: 47.28]

  42. `Origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 37.37, DesvPad Tam: 10.62]

  43. `PrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  44. `PrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  45. `PrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  46. `Previsto` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Realizado` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `RecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **26.04%** (2604 zeros) | Distintos: **5075** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -2105477.95, Máx: 5974037.02, Média: 20852.19, Mediana: 0.0, DesvPad: 239779.68]

  49. `Recolhido` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  50. `Rubrica` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Subalinea` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  52. `Tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 109.81, DesvPad Tam: 47.28]

  53. `TipoArquivo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 18, Tam Média: 15.41, DesvPad Tam: 0.84]

  54. `TipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  55. `UGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **42** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 18.64, DesvPad Tam: 7.57]

  56. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 87, Tam Média: 36.74, DesvPad Tam: 9.17]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `Alinea`, `Previsto`, `Realizado`, `Recolhido`, `Rubrica`, `Subalinea`

> - `CodAlinea`, `CodDetalhamento2`

> - `CodDetalhamento1`, `CodRubrica`

> - `CodNatureza`, `CodSubalinea`, `CodTipo`

> - `Natureza`, `Tipo`

> - `PrevistaBruta`, `PrevistaDeducao`, `PrevistaLiquida`


---
### 🔹 Período: 2024 até 2025
- **Quantidade Total de Colunas:** `47`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Receitas-2024.csv`** *(ID: `9ba06f4d-5c0e-4160-bad3-1a325e432496`)*
  - 📄 **`Receitas-2025.csv`** *(ID: `2dc2d874-0d72-4c01-b8a0-ecb6f392d6e4`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2024.0, Máx: 2025.0, Média: 2024.5, Mediana: 2024.5, DesvPad: 0.5]

  2. `codigoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.11, Mediana: 1.0, DesvPad: 0.79]

  3. `codigoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **72** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7923.0, Média: 1312.73, Mediana: 1114.0, DesvPad: 838.88]

  4. `codigoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **140** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 792399.0, Média: 131314.62, Mediana: 111450.0, DesvPad: 83881.98]

  5. `codigoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **165** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 7923990.0, Média: 1313146.96, Mediana: 1114501.0, DesvPad: 838819.74]

  6. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **45.11%** (9021 zeros) | Distintos: **109** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 900000.0, Média: 21727.19, Mediana: 2.0, DesvPad: 67676.98]

  7. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **204** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.000675, Média: 543.67, Mediana: 500.000003, DesvPad: 99.61]

  8. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **44** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 130.93, Mediana: 111.0, DesvPad: 83.88]

  9. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **68** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 543.64, Mediana: 500.0, DesvPad: 99.6]

  10. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 5.0, Máx: 8.0, Média: 5.37, Mediana: 5.0, DesvPad: 0.85]

  11. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 2.0, Média: 1.0, Mediana: 1.0, DesvPad: 0.01]

  12. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **204** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79239901.0, Média: 13131471.18, Mediana: 11145011.0, DesvPad: 8388197.27]

  13. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **28** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 12.97, Mediana: 11.0, DesvPad: 8.38]

  14. `codigoTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **204** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79239901.0, Média: 13131471.18, Mediana: 11145011.0, DesvPad: 8388197.27]

  15. `codigoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **114** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 727595.53, Mediana: 800102.0, DesvPad: 174302.19]

  16. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **146** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 720331.65, Mediana: 800102.0, DesvPad: 186034.9]

  17. `contaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621350000.0, Média: 456236197.12, Mediana: 621200000.0, DesvPad: 238475273.23]

  18. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13649** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  19. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **531** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.33, DesvPad Tam: 2.48]

  21. `descricaoContaContabil` ➔ Nulos: **32.31%** (6462 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 19.29, DesvPad Tam: 7.32]

  22. `descricaoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **36** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 142, Tam Média: 52.9, DesvPad Tam: 17.82]

  23. `descricaoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **80** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 145, Tam Média: 57.39, DesvPad Tam: 13.84]

  24. `descricaoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **94** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 154, Tam Média: 112.74, DesvPad Tam: 52.34]

  25. `descricaoDetalhamentoFonte` ➔ Nulos: **0.01%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **136** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 180, Tam Média: 54.23, DesvPad Tam: 24.44]

  26. `descricaoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **22** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 60, Tam Média: 12.44, DesvPad Tam: 11.17]

  27. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **41** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 141, Tam Média: 36.59, DesvPad Tam: 11.82]

  28. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 50, Tam Máx: 50, Tam Média: 50.0, DesvPad Tam: 0.0]

  29. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 30, Tam Máx: 33, Tam Média: 30.0, DesvPad Tam: 0.03]

  30. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **125** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 117.18, DesvPad Tam: 45.72]

  31. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 39.19, DesvPad Tam: 8.49]

  32. `descricaoTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **125** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 117.18, DesvPad Tam: 45.72]

  33. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **73** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 87, Tam Média: 37.31, DesvPad Tam: 8.37]

  34. `descricaoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 20.16, DesvPad Tam: 6.44]

  35. `documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.04%** (9 zeros) | Distintos: **6275** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  36. `tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 18, Tam Média: 15.99, DesvPad Tam: 1.26]

  37. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  38. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (20000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  39. `valorArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **79.69%** (15938 zeros) | Distintos: **3736** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -77685138.12, Máx: 109787939.65, Média: 72990.21, Mediana: 0.0, DesvPad: 2440013.23]

  40. `valorArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **96.07%** (19214 zeros) | Distintos: **771** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -18340732.88, Máx: 1152899.22, Média: -6877.39, Mediana: 0.0, DesvPad: 290607.33]

  41. `valorArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **77.6%** (15520 zeros) | Distintos: **4040** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -28232300.03, Máx: 357518954.24, Média: 189191.84, Mediana: 0.0, DesvPad: 6836353.22]

  42. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (20000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  43. `valorPrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.94%** (19989 zeros) | Distintos: **12** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 84878930.0, Média: 12236.75, Mediana: 0.0, DesvPad: 860193.27]

  44. `valorPrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (20000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  45. `valorPrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.89%** (19978 zeros) | Distintos: **20** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1983274603.0, Média: 213529.89, Mediana: 0.0, DesvPad: 17161038.98]

  46. `valorRecolhida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (20000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  47. `valorRecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **46.8%** (9361 zeros) | Distintos: **8915** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -85001407.33, Máx: 84544358.68, Média: 64392.83, Mediana: 0.0, DesvPad: 3123787.32]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `codigoNatureza`, `codigoTipo`

> - `descricaoNatureza`, `descricaoTipo`

> - `valorArrecadada`, `valorPrevista`, `valorPrevistaDeducao`, `valorRecolhida`


---
### 🔹 Período: 2026
- **Quantidade Total de Colunas:** `56`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Receitas-2026.csv`** *(ID: `dcefa0ca-7e31-4b53-b6bd-0e559ef42d43`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Alinea` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2026.0, Máx: 2026.0, Média: 2026.0, Mediana: 2026.0, DesvPad: 0.0]

  3. `ArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **68.08%** (6808 zeros) | Distintos: **2422** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -4868897.27, Máx: 7079939.24, Média: 31456.28, Mediana: 0.0, DesvPad: 437844.1]

  4. `ArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **97.29%** (9729 zeros) | Distintos: **272** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -133092.49, Máx: 0.0, Média: -1971.75, Mediana: 0.0, DesvPad: 14310.8]

  5. `ArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **83.08%** (8308 zeros) | Distintos: **1498** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -52929717.03, Máx: 138649.56, Média: -157611.18, Mediana: 0.0, DesvPad: 2000126.85]

  6. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 18, Tam Média: 18.0, DesvPad Tam: 0.0]

  7. `CodAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **34** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 199999.0, Média: 122778.17, Mediana: 111450.0, DesvPad: 26399.26]

  8. `CodCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 1.0, Média: 1.0, Mediana: 1.0, DesvPad: 0.0]

  9. `CodDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **20** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 1999.0, Média: 1227.37, Mediana: 1114.0, DesvPad: 264.1]

  10. `CodDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **34** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 199999.0, Média: 122778.17, Mediana: 111450.0, DesvPad: 26399.26]

  11. `CodDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **38** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 1999992.0, Média: 1227782.47, Mediana: 1114501.0, DesvPad: 263992.42]

  12. `CodEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 199.0, Média: 122.41, Mediana: 111.0, DesvPad: 26.44]

  13. `CodNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 19999923.0, Média: 12277826.22, Mediana: 11145011.0, DesvPad: 2639924.03]

  14. `CodOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 19.0, Média: 12.12, Mediana: 11.0, DesvPad: 2.6]

  15. `CodRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **20** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 1999.0, Média: 1227.37, Mediana: 1114.0, DesvPad: 264.1]

  16. `CodSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 19999923.0, Média: 12277826.22, Mediana: 11145011.0, DesvPad: 2639924.03]

  17. `CodTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 19999923.0, Média: 12277826.22, Mediana: 11145011.0, DesvPad: 2639924.03]

  18. `CodUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 310201.0, Máx: 800102.0, Média: 735549.84, Mediana: 800102.0, DesvPad: 142924.84]

  19. `CodigoContaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621350000.0, Média: 476138060.48, Mediana: 621200000.0, DesvPad: 230118913.17]

  20. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **50.22%** (5022 zeros) | Distintos: **36** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 312000.0, Média: 20274.49, Mediana: 0.0, DesvPad: 53464.55]

  21. `CodigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.000114, Média: 528.78, Mediana: 500.000002, DesvPad: 78.28]

  22. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **28** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 528.76, Mediana: 500.0, DesvPad: 78.28]

  23. `CodigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 5.0, Máx: 8.0, Média: 5.23, Mediana: 5.0, DesvPad: 0.63]

  24. `CodigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 1.0, Média: 1.0, Mediana: 1.0, DesvPad: 0.0]

  25. `CodigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 310201.0, Máx: 800102.0, Média: 735549.85, Mediana: 800102.0, DesvPad: 142924.83]

  26. `ContaContabil` ➔ Nulos: **28.44%** (2844 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 18.37, DesvPad Tam: 5.83]

  27. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  28. `DataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6062** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  29. `DataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **210** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  30. `Detalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **20** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 169, Tam Média: 51.42, DesvPad Tam: 19.57]

  31. `Detalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **34** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 144, Tam Média: 56.71, DesvPad Tam: 15.39]

  32. `Detalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **38** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 154, Tam Média: 114.0, DesvPad Tam: 52.88]

  33. `DetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **59** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 192, Tam Média: 52.02, DesvPad Tam: 23.03]

  34. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.02%** (2 zeros) | Distintos: **2706** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  35. `Especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 47, Tam Média: 13.09, DesvPad Tam: 11.94]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **28** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 140, Tam Média: 37.65, DesvPad Tam: 16.03]

  37. `GrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 50, Tam Máx: 50, Tam Média: 50.0, DesvPad Tam: 0.0]

  38. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 613895732.0, Máx: 613905731.0, Média: 613900731.5, Mediana: 613900731.5, DesvPad: 2886.75]

  39. `IdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 30, Tam Máx: 30, Tam Média: 30.0, DesvPad Tam: 0.0]

  40. `Mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 10.0, Média: 5.56, Mediana: 6.0, DesvPad: 2.72]

  41. `Natureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 27, Tam Máx: 195, Tam Média: 117.51, DesvPad Tam: 46.61]

  42. `Origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 43, Tam Média: 39.24, DesvPad Tam: 7.93]

  43. `PrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  44. `PrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  45. `PrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  46. `Previsto` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Realizado` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `RecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **51.55%** (5155 zeros) | Distintos: **3807** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -2876545.06, Máx: 2876545.06, Média: 2710.83, Mediana: 0.0, DesvPad: 409947.28]

  49. `Recolhido` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  50. `Rubrica` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Subalinea` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  52. `Tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 27, Tam Máx: 195, Tam Média: 117.51, DesvPad Tam: 46.61]

  53. `TipoArquivo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 18, Tam Média: 15.91, DesvPad Tam: 1.12]

  54. `TipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  55. `UGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 19.75, DesvPad Tam: 7.12]

  56. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 23, Tam Máx: 67, Tam Média: 36.1, DesvPad Tam: 4.98]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `Alinea`, `Previsto`, `Realizado`, `Recolhido`, `Rubrica`, `Subalinea`

> - `CodAlinea`, `CodDetalhamento2`

> - `CodCategoriaEconomica`, `CodigoIdUso`

> - `CodDetalhamento1`, `CodRubrica`

> - `CodNatureza`, `CodSubalinea`, `CodTipo`

> - `Natureza`, `Tipo`

> - `PrevistaBruta`, `PrevistaDeducao`, `PrevistaLiquida`


---

## 📂 Grupo Principal: `receitas`

### 🔹 Período: 2016 até 2017
- **Quantidade Total de Colunas:** `21`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`receitas2016.csv`** *(ID: `4e32b780-939e-4472-b166-00631f3b8244`)*
  - 📄 **`receitas2017.csv`** *(ID: `fb0e5556-7f1b-4f08-b62f-6a2080faf5b3`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `alinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **232** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 154, Tam Média: 47.33, DesvPad Tam: 30.01]

  2. `ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2016.0, Máx: 2017.0, Média: 2016.51, Mediana: 2017.0, DesvPad: 0.5]

  3. `categoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 19.04, DesvPad Tam: 4.04]

  4. `codAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **357** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111204.0, Máx: 952136.0, Média: 265454.47, Mediana: 172122.0, DesvPad: 264085.55]

  5. `codCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9.0, Média: 2.16, Mediana: 1.0, DesvPad: 2.67]

  6. `codEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **81** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 952.0, Média: 265.15, Mediana: 172.0, DesvPad: 264.1]

  7. `codOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **40** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 95.0, Média: 26.3, Mediana: 17.0, DesvPad: 26.44]

  8. `codRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **142** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 9521.0, Média: 2654.21, Mediana: 1721.0, DesvPad: 2640.9]

  9. `codSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **724** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120410.0, Máx: 95213600.0, Média: 26545469.2, Mediana: 17212211.0, DesvPad: 26408556.71]

  10. `codUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **143** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 60101.0, Máx: 800102.0, Média: 557922.51, Mediana: 600201.0, DesvPad: 222778.38]

  11. `codigoDetalhamentoFonteAux` ➔ Nulos: **100.0%** (9595 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  12. `data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  13. `especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **51** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 39, Tam Média: 21.79, DesvPad Tam: 9.02]

  14. `mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 12.0, Média: 6.52, Mediana: 7.0, DesvPad: 3.53]

  15. `origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 33, Tam Média: 21.18, DesvPad Tam: 4.11]

  16. `previsto` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **92.15%** (8842 zeros) | Distintos: **639** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -1816461336.0, Máx: 2046565000.0, Média: 3427642.77, Mediana: 0.0, DesvPad: 70498905.43]

  17. `realizado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **5.59%** (536 zeros) | Distintos: **8644** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -155382354.55, Máx: 229711330.42, Média: 3084662.27, Mediana: 25867.35, DesvPad: 19790630.62]

  18. `recolhido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (9595 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  19. `rubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **97** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 74, Tam Média: 28.63, DesvPad Tam: 10.95]

  20. `subalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **539** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 142, Tam Média: 41.8, DesvPad Tam: 19.75]

  21. `unidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **87** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 89, Tam Média: 41.03, DesvPad Tam: 15.02]

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