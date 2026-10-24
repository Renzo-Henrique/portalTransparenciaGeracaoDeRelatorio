# Relatório de Análise Estrutural e Qualidade de Dados - CKAN

Este documento apresenta um resumo consolidado das bases de dados por período, evolução das colunas, métricas de qualidade e estatísticas numéricas consolidadas com marcação de alertas (Caso 1: Nulos/Zeros > 50 e Caso 2: Distintos > 50). Foram utilizados apenas `50000 registros por recurso`

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

  2. `codigoAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **158** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111204.0, Máx: 792299.0, Média: 168110.55, Mediana: 121029.0, DesvPad: 133478.95]

  3. `codigoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.29, Mediana: 1.0, DesvPad: 1.29]

  4. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **60.39%** (120771 zeros) | Distintos: **38** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 922.0, Média: 3.17, Mediana: 0.0, DesvPad: 24.88]

  5. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.01%** (29 zeros) | Distintos: **188** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 675.000002, Média: 162.83, Mediana: 133.0, DesvPad: 74.84]

  6. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 167.86, Mediana: 121.0, DesvPad: 133.53]

  7. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.01%** (29 zeros) | Distintos: **66** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 675.0, Média: 162.83, Mediana: 133.0, DesvPad: 74.84]

  8. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.01%** (29 zeros) | Distintos: **5** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 6.0, Média: 1.31, Mediana: 1.0, DesvPad: 0.47]

  9. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.31%** (198613 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5.0, Média: 0.03, Mediana: 0.0, DesvPad: 0.33]

  10. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **382** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120410.0, Máx: 79229900.0, Média: 16811073.3, Mediana: 12102901.0, DesvPad: 13347891.31]

  11. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 16.63, Mediana: 12.0, DesvPad: 13.34]

  12. `codigoRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7922.0, Média: 1680.87, Mediana: 1210.0, DesvPad: 1334.75]

  13. `codigoSubAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **382** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120410.0, Máx: 79229900.0, Média: 16811073.3, Mediana: 12102901.0, DesvPad: 13347891.31]

  14. `codigoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 20101.0, Máx: 800102.0, Média: 642220.9, Mediana: 800102.0, DesvPad: 222128.8]

  15. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **123** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 619843.72, Mediana: 800102.0, DesvPad: 239635.12]

  16. `contaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 521110000.0, Máx: 621390000.0, Média: 620094816.65, Mediana: 621200000.0, DesvPad: 10469513.7]

  17. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **59883** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  18. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1121** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  19. `descricaoAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **147** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 154, Tam Média: 88.17, DesvPad Tam: 51.16]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.93, DesvPad Tam: 4.09]

  21. `descricaoContaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 43, Tam Média: 17.54, DesvPad Tam: 3.31]

  22. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **208** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 174, Tam Média: 22.12, DesvPad Tam: 14.19]

  23. `descricaoEspecie` ➔ Nulos: **5.02%** (10046 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 39, Tam Média: 15.68, DesvPad Tam: 9.07]

  24. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **77** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 111, Tam Média: 25.4, DesvPad Tam: 10.07]

  25. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 49, Tam Média: 20.88, DesvPad Tam: 2.82]

  26. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 21, Tam Máx: 96, Tam Média: 38.88, DesvPad Tam: 1.5]

  27. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **388** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 152, Tam Média: 45.11, DesvPad Tam: 23.13]

  28. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 26, Tam Média: 20.62, DesvPad Tam: 3.16]

  29. `descricaoRubrica` ➔ Nulos: **21.1%** (42204 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **39** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 80, Tam Média: 35.21, DesvPad Tam: 7.83]

  30. `descricaoSubAlinea` ➔ Nulos: **11.36%** (22714 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **301** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 152, Tam Média: 42.73, DesvPad Tam: 20.53]

  31. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **194** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 87, Tam Média: 27.32, DesvPad Tam: 14.84]

  32. `descricaoUGEmitente` ➔ Nulos: **0.4%** (807 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **229** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 90, Tam Média: 28.02, DesvPad Tam: 16.08]

  33. `documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **34238** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  34. `tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 10, Tam Média: 9.98, DesvPad Tam: 0.21]

  35. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  36. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **1.11%** (2222 zeros) | Distintos: **150254** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -156746328.4, Máx: 810519891.63, Média: 128263.96, Mediana: 511.345, DesvPad: 3348462.68]

  37. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **98.89%** (197787 zeros) | Distintos: **1942** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -335784072.0, Máx: 2413081000.0, Média: 199270.59, Mediana: 0.0, DesvPad: 10688059.49]


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

  2. `codigoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.11, Mediana: 1.0, DesvPad: 0.82]

  3. `codigoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7923.0, Média: 1305.11, Mediana: 1114.0, DesvPad: 871.44]

  4. `codigoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **94** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111205.0, Máx: 792399.0, Média: 130552.24, Mediana: 111450.0, DesvPad: 87137.87]

  5. `codigoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112050.0, Máx: 7923990.0, Média: 1305523.17, Mediana: 1114501.0, DesvPad: 871378.66]

  6. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **59.93%** (29967 zeros) | Distintos: **48** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 312700.0, Média: 332.0, Mediana: 0.0, DesvPad: 9371.54]

  7. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **130** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 301.0, Média: 132.05, Mediana: 101.000002, DesvPad: 54.56]

  8. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 130.17, Mediana: 111.0, DesvPad: 87.15]

  9. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **43** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 301.0, Média: 132.05, Mediana: 101.0, DesvPad: 54.56]

  10. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 3.0, Média: 1.12, Mediana: 1.0, DesvPad: 0.33]

  11. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.74%** (49871 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4.0, Média: 0.01, Mediana: 0.0, DesvPad: 0.2]

  12. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **145** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120501.0, Máx: 79239901.0, Média: 13055233.34, Mediana: 11145011.0, DesvPad: 8713786.48]

  13. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 12.9, Mediana: 11.0, DesvPad: 8.71]

  14. `codigoTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **145** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120501.0, Máx: 79239901.0, Média: 13055233.34, Mediana: 11145011.0, DesvPad: 8713786.48]

  15. `codigoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **93** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 731814.31, Mediana: 800102.0, DesvPad: 166810.05]

  16. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **104** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 724707.39, Mediana: 800102.0, DesvPad: 178737.44]

  17. `contaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621350000.0, Média: 507839010.08, Mediana: 621200000.0, DesvPad: 211964181.89]

  18. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11515** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  19. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **277** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.36, DesvPad Tam: 2.58]

  21. `descricaoContaContabil` ➔ Nulos: **22.2%** (11101 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 19.28, DesvPad Tam: 7.29]

  22. `descricaoDetalhamento1` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **38** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 142, Tam Média: 53.72, DesvPad Tam: 17.18]

  23. `descricaoDetalhamento2` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **84** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 162, Tam Média: 57.09, DesvPad Tam: 13.42]

  24. `descricaoDetalhamento3` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **105** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 162, Tam Média: 114.29, DesvPad Tam: 51.8]

  25. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **123** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 138, Tam Média: 27.17, DesvPad Tam: 18.83]

  26. `descricaoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **21** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 59, Tam Média: 11.76, DesvPad Tam: 10.34]

  27. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **43** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 109, Tam Média: 26.17, DesvPad Tam: 10.36]

  28. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 43, Tam Média: 19.73, DesvPad Tam: 1.97]

  29. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 21, Tam Máx: 39, Tam Média: 38.95, DesvPad Tam: 0.91]

  30. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **144** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 195, Tam Média: 118.51, DesvPad Tam: 45.14]

  31. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 39.4, DesvPad Tam: 8.5]

  32. `descricaoTipo` ➔ Nulos: **0.02%** (9 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **140** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 118.51, DesvPad Tam: 45.14]

  33. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **93** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 37.31, DesvPad Tam: 8.55]

  34. `descricaoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **104** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 20.28, DesvPad Tam: 6.31]

  35. `documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.03%** (17 zeros) | Distintos: **6932** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  36. `tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 18, Tam Média: 16.21, DesvPad Tam: 1.31]

  37. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  38. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  39. `valorArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **77.73%** (38864 zeros) | Distintos: **9249** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -122363213.04, Máx: 132211975.85, Média: 59641.21, Mediana: 0.0, DesvPad: 2536117.49]

  40. `valorArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **95.43%** (47717 zeros) | Distintos: **2111** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -45469071.49, Máx: 10070104.99, Média: -10866.07, Mediana: 0.0, DesvPad: 507944.72]

  41. `valorArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **71.64%** (35820 zeros) | Distintos: **11719** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -43719523.66, Máx: 43767507.35, Média: 10429.7, Mediana: 0.0, DesvPad: 1136763.4]

  42. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  43. `valorPrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.93%** (49964 zeros) | Distintos: **33** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 135000000.0, Média: 6747.4, Mediana: 0.0, DesvPad: 766421.26]

  44. `valorPrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.99%** (49995 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: -11453638.0, Máx: 0.0, Média: -361.32, Mediana: 0.0, DesvPad: 54569.98]

  45. `valorPrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.96%** (49979 zeros) | Distintos: **22** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: -5004787.0, Máx: 26964514.0, Média: 898.64, Mediana: 0.0, DesvPad: 140040.63]

  46. `valorRecolhida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  47. `valorRecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **55.32%** (27661 zeros) | Distintos: **16285** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -138159420.91, Máx: 145141548.7, Média: 33128.82, Mediana: 0.0, DesvPad: 2330452.06]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `codigoNatureza`, `codigoTipo`

> - `valorArrecadada`, `valorPrevista`, `valorRecolhida`


---
### 🔹 Período: 2023
- **Quantidade Total de Colunas:** `56`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Receitas-2023.csv`** *(ID: `d59902ff-41e5-4b61-a50d-9cf0769c74af`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Alinea` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2023.0, Máx: 2023.0, Média: 2023.0, Mediana: 2023.0, DesvPad: 0.0]

  3. `ArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **73.5%** (36752 zeros) | Distintos: **11264** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -4895367.95, Máx: 51402350.37, Média: 21944.09, Mediana: 0.0, DesvPad: 450067.97]

  4. `ArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **98.0%** (49002 zeros) | Distintos: **981** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -39009.02, Máx: 28339.78, Média: -110.3, Mediana: 0.0, DesvPad: 1282.31]

  5. `ArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **80.2%** (40100 zeros) | Distintos: **7634** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -26410906.74, Máx: 51402350.37, Média: 28739.0, Mediana: 0.0, DesvPad: 1253683.54]

  6. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.54, DesvPad Tam: 3.15]

  7. `CodAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **99** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 792299.0, Média: 138048.22, Mediana: 111450.0, DesvPad: 106870.29]

  8. `CodCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.18, Mediana: 1.0, DesvPad: 1.0]

  9. `CodDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7922.0, Média: 1380.09, Mediana: 1114.0, DesvPad: 1068.77]

  10. `CodDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **99** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 792299.0, Média: 138048.22, Mediana: 111450.0, DesvPad: 106870.29]

  11. `CodDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **115** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 7922990.0, Média: 1380483.03, Mediana: 1114501.0, DesvPad: 1068702.88]

  12. `CodEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **28** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 137.68, Mediana: 111.0, DesvPad: 106.9]

  13. `CodNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **138** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79229901.0, Média: 13804831.86, Mediana: 11145011.0, DesvPad: 10687028.63]

  14. `CodOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 13.65, Mediana: 11.0, DesvPad: 10.68]

  15. `CodRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7922.0, Média: 1380.09, Mediana: 1114.0, DesvPad: 1068.77]

  16. `CodSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **138** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79229901.0, Média: 13804831.86, Mediana: 11145011.0, DesvPad: 10687028.63]

  17. `CodTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **138** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79229901.0, Média: 13804831.86, Mediana: 11145011.0, DesvPad: 10687028.63]

  18. `CodUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **75** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 709598.97, Mediana: 800102.0, DesvPad: 193204.36]

  19. `CodigoContaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621350000.0, Média: 472542125.14, Mediana: 621200000.0, DesvPad: 231184115.23]

  20. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **49.14%** (24569 zeros) | Distintos: **67** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 900010.0, Média: 15745.5, Mediana: 1.0, DesvPad: 42894.6]

  21. `CodigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **150** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.000675, Média: 551.8, Mediana: 500.000003, DesvPad: 107.05]

  22. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **46** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 551.79, Mediana: 500.0, DesvPad: 107.05]

  23. `CodigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 5.0, Máx: 8.0, Média: 5.44, Mediana: 5.0, DesvPad: 0.92]

  24. `CodigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.12%** (61 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1.0, Média: 1.0, Mediana: 1.0, DesvPad: 0.03]

  25. `CodigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **94** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 694642.74, Mediana: 800102.0, DesvPad: 209441.81]

  26. `ContaContabil` ➔ Nulos: **29.01%** (14504 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 18.33, DesvPad Tam: 5.68]

  27. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  28. `DataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **17969** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  29. `DataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **272** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  30. `Detalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **38** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 82, Tam Média: 52.54, DesvPad Tam: 17.48]

  31. `Detalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **91** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 144, Tam Média: 56.1, DesvPad Tam: 14.25]

  32. `Detalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **106** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 154, Tam Média: 107.65, DesvPad Tam: 53.29]

  33. `DetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **144** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 142, Tam Média: 47.87, DesvPad Tam: 16.63]

  34. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.02%** (12 zeros) | Distintos: **7610** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  35. `Especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 84, Tam Média: 12.76, DesvPad Tam: 11.39]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **46** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 141, Tam Média: 36.67, DesvPad Tam: 11.32]

  37. `GrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 50, Tam Máx: 50, Tam Média: 50.0, DesvPad Tam: 0.0]

  38. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **50000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 415731210.0, Máx: 415781209.0, Média: 415756209.5, Mediana: 415756209.5, DesvPad: 14433.76]

  39. `IdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 30, Tam Média: 29.98, DesvPad Tam: 0.63]

  40. `Mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 12.0, Média: 6.67, Mediana: 7.0, DesvPad: 3.41]

  41. `Natureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **135** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 112.65, DesvPad Tam: 46.54]

  42. `Origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 38.45, DesvPad Tam: 9.37]

  43. `PrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.68%** (49839 zeros) | Distintos: **132** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -42898828.27, Máx: 996943000.0, Média: 57285.86, Mediana: 0.0, DesvPad: 4842989.58]

  44. `PrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.9%** (49952 zeros) | Distintos: **46** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: -3076762984.0, Máx: 0.0, Média: -157371.52, Mediana: 0.0, DesvPad: 17838540.39]

  45. `PrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.72%** (49861 zeros) | Distintos: **130** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -323381050.0, Máx: 612000000.0, Média: 36142.31, Mediana: 0.0, DesvPad: 4049339.78]

  46. `Previsto` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Realizado` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `RecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **48.99%** (24494 zeros) | Distintos: **18557** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -97180632.31, Máx: 371610825.88, Média: 106340.28, Mediana: 0.0, DesvPad: 4817175.14]

  49. `Recolhido` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  50. `Rubrica` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Subalinea` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  52. `Tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **135** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 112.65, DesvPad Tam: 46.54]

  53. `TipoArquivo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 18, Tam Média: 15.92, DesvPad Tam: 1.18]

  54. `TipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  55. `UGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **94** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 19.38, DesvPad Tam: 7.03]

  56. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **75** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 38.07, DesvPad Tam: 9.89]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `Alinea`, `Previsto`, `Realizado`, `Recolhido`, `Rubrica`, `Subalinea`

> - `CodAlinea`, `CodDetalhamento2`

> - `CodDetalhamento1`, `CodRubrica`

> - `CodNatureza`, `CodSubalinea`, `CodTipo`

> - `Natureza`, `Tipo`


---
### 🔹 Período: 2024 até 2025
- **Quantidade Total de Colunas:** `47`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Receitas-2024.csv`** *(ID: `9ba06f4d-5c0e-4160-bad3-1a325e432496`)*
  - 📄 **`Receitas-2025.csv`** *(ID: `2dc2d874-0d72-4c01-b8a0-ecb6f392d6e4`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2024.0, Máx: 2025.0, Média: 2024.5, Mediana: 2024.5, DesvPad: 0.5]

  2. `codigoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.1, Mediana: 1.0, DesvPad: 0.75]

  3. `codigoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **96** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7923.0, Média: 1296.38, Mediana: 1114.0, DesvPad: 800.63]

  4. `codigoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **190** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 792399.0, Média: 129680.0, Mediana: 111450.0, DesvPad: 80057.38]

  5. `codigoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **222** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 7923990.0, Média: 1296800.76, Mediana: 1114501.0, DesvPad: 800573.79]

  6. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **45.71%** (45711 zeros) | Distintos: **157** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 900010.0, Média: 20907.77, Mediana: 2.0, DesvPad: 62858.38]

  7. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **334** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.000675, Média: 541.56, Mediana: 500.000003, DesvPad: 97.24]

  8. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **58** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 129.3, Mediana: 111.0, DesvPad: 80.06]

  9. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **99** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 541.54, Mediana: 500.0, DesvPad: 97.24]

  10. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 5.0, Máx: 8.0, Média: 5.35, Mediana: 5.0, DesvPad: 0.83]

  11. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 2.0, Média: 1.0, Mediana: 1.0, DesvPad: 0.01]

  12. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **273** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79239901.0, Média: 12968009.12, Mediana: 11145011.0, DesvPad: 8005737.75]

  13. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 12.81, Mediana: 11.0, DesvPad: 7.99]

  14. `codigoTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **273** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79239901.0, Média: 12968009.12, Mediana: 11145011.0, DesvPad: 8005737.75]

  15. `codigoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **177** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 730985.99, Mediana: 800102.0, DesvPad: 170483.91]

  16. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **203** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 724020.29, Mediana: 800102.0, DesvPad: 182067.36]

  17. `contaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621350000.0, Média: 457512817.73, Mediana: 621200000.0, DesvPad: 238021123.22]

  18. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **35954** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  19. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **555** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.3, DesvPad Tam: 2.37]

  21. `descricaoContaContabil` ➔ Nulos: **32.07%** (32067 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 19.25, DesvPad Tam: 7.24]

  22. `descricaoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 169, Tam Média: 53.15, DesvPad Tam: 17.65]

  23. `descricaoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **102** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 145, Tam Média: 57.59, DesvPad Tam: 13.74]

  24. `descricaoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **118** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 154, Tam Média: 113.66, DesvPad Tam: 51.97]

  25. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** (4 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **213** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 185, Tam Média: 54.19, DesvPad Tam: 24.18]

  26. `descricaoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **28** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 60, Tam Média: 12.12, DesvPad Tam: 10.78]

  27. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **54** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 141, Tam Média: 36.63, DesvPad Tam: 12.04]

  28. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 50, Tam Máx: 50, Tam Média: 50.0, DesvPad Tam: 0.0]

  29. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 30, Tam Máx: 33, Tam Média: 30.0, DesvPad Tam: 0.02]

  30. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **154** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 117.88, DesvPad Tam: 45.38]

  31. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 39.34, DesvPad Tam: 8.39]

  32. `descricaoTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **154** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 117.88, DesvPad Tam: 45.38]

  33. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **103** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 37.22, DesvPad Tam: 8.01]

  34. `descricaoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **112** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 20.28, DesvPad Tam: 6.33]

  35. `documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.04%** (43 zeros) | Distintos: **13979** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  36. `tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 18, Tam Média: 16.01, DesvPad Tam: 1.27]

  37. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  38. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (100000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  39. `valorArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **79.77%** (79769 zeros) | Distintos: **18055** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -99674484.24, Máx: 241090553.6, Média: 60623.59, Mediana: 0.0, DesvPad: 2573603.28]

  40. `valorArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **96.28%** (96275 zeros) | Distintos: **3543** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -40406855.63, Máx: 1152899.22, Média: -11195.85, Mediana: 0.0, DesvPad: 418934.56]

  41. `valorArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **76.68%** (76682 zeros) | Distintos: **20478** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -117674962.62, Máx: 917386363.63, Média: 95751.67, Mediana: 0.0, DesvPad: 5658728.79]

  42. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (100000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  43. `valorPrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.95%** (99949 zeros) | Distintos: **51** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 250000000.0, Média: 7777.16, Mediana: 0.0, DesvPad: 1075928.19]

  44. `valorPrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.99%** (99992 zeros) | Distintos: **8** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: -471347423.0, Máx: 0.0, Média: -7138.92, Mediana: 0.0, DesvPad: 1581834.86]

  45. `valorPrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.93%** (99931 zeros) | Distintos: **63** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 3305457676.0, Média: 78190.24, Mediana: 0.0, DesvPad: 12972075.1]

  46. `valorRecolhida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (100000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  47. `valorRecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **47.4%** (47402 zeros) | Distintos: **41689** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -85001407.33, Máx: 1059074681.87, Média: 44891.6, Mediana: 0.0, DesvPad: 3962775.48]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `codigoNatureza`, `codigoTipo`

> - `descricaoNatureza`, `descricaoTipo`

> - `valorArrecadada`, `valorPrevista`, `valorRecolhida`


---
### 🔹 Período: 2026
- **Quantidade Total de Colunas:** `56`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Receitas-2026.csv`** *(ID: `dcefa0ca-7e31-4b53-b6bd-0e559ef42d43`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Alinea` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2026.0, Máx: 2026.0, Média: 2026.0, Mediana: 2026.0, DesvPad: 0.0]

  3. `ArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **83.41%** (41706 zeros) | Distintos: **7026** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -11761860.14, Máx: 11914769.99, Média: 17428.75, Mediana: 0.0, DesvPad: 483087.83]

  4. `ArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **96.6%** (48301 zeros) | Distintos: **1688** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -52929717.03, Máx: 2147527.56, Média: -52197.16, Mediana: 0.0, DesvPad: 961692.8]

  5. `ArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **74.28%** (37142 zeros) | Distintos: **10881** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -77886262.31, Máx: 77886262.31, Média: 33247.17, Mediana: 0.0, DesvPad: 2584782.22]

  6. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.08, DesvPad Tam: 1.18]

  7. `CodAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **73** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 792206.0, Média: 121799.78, Mediana: 111450.0, DesvPad: 43877.99]

  8. `CodCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.03, Mediana: 1.0, DesvPad: 0.37]

  9. `CodDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **34** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7922.0, Média: 1217.57, Mediana: 1114.0, DesvPad: 438.83]

  10. `CodDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **73** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 792206.0, Média: 121799.78, Mediana: 111450.0, DesvPad: 43877.99]

  11. `CodDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **86** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 7922063.0, Média: 1217998.62, Mediana: 1114501.0, DesvPad: 438779.91]

  12. `CodEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **22** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 121.41, Mediana: 111.0, DesvPad: 43.88]

  13. `CodNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **115** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79220631.0, Média: 12179987.72, Mediana: 11145011.0, DesvPad: 4387798.98]

  14. `CodOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **15** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 12.02, Mediana: 11.0, DesvPad: 4.36]

  15. `CodRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **34** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7922.0, Média: 1217.57, Mediana: 1114.0, DesvPad: 438.83]

  16. `CodSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **115** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79220631.0, Média: 12179987.72, Mediana: 11145011.0, DesvPad: 4387798.98]

  17. `CodTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **115** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79220631.0, Média: 12179987.72, Mediana: 11145011.0, DesvPad: 4387798.98]

  18. `CodUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 30901.0, Máx: 800102.0, Média: 743227.5, Mediana: 800102.0, DesvPad: 150878.75]

  19. `CodigoContaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621350000.0, Média: 453180159.09, Mediana: 621200000.0, DesvPad: 239620703.35]

  20. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **43.19%** (21595 zeros) | Distintos: **71** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 900010.0, Média: 22526.05, Mediana: 2.0, DesvPad: 69046.05]

  21. `CodigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **118** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.00011, Média: 537.07, Mediana: 500.000003, DesvPad: 94.29]

  22. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **37** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 537.05, Mediana: 500.0, DesvPad: 94.28]

  23. `CodigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 5.0, Máx: 8.0, Média: 5.32, Mediana: 5.0, DesvPad: 0.81]

  24. `CodigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 1.0, Média: 1.0, Mediana: 1.0, DesvPad: 0.0]

  25. `CodigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **64** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 733886.96, Mediana: 800102.0, DesvPad: 166775.09]

  26. `ContaContabil` ➔ Nulos: **32.91%** (16456 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 19.77, DesvPad Tam: 7.83]

  27. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  28. `DataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **15129** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  29. `DataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **214** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  30. `Detalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **29** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 80, Tam Média: 53.33, DesvPad Tam: 17.47]

  31. `Detalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 144, Tam Média: 57.81, DesvPad Tam: 12.82]

  32. `Detalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **81** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 154, Tam Média: 116.41, DesvPad Tam: 50.82]

  33. `DetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **115** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 247, Tam Média: 54.54, DesvPad Tam: 23.55]

  34. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.05%** (26 zeros) | Distintos: **6067** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  35. `Especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **18** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 47, Tam Média: 11.61, DesvPad Tam: 10.23]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **37** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 141, Tam Média: 36.44, DesvPad Tam: 11.39]

  37. `GrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 50, Tam Máx: 50, Tam Média: 50.0, DesvPad Tam: 0.0]

  38. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **50000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 613065824.0, Máx: 613115823.0, Média: 613090823.5, Mediana: 613090823.5, DesvPad: 14433.76]

  39. `IdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 30, Tam Máx: 30, Tam Média: 30.0, DesvPad Tam: 0.0]

  40. `Mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 10.0, Média: 5.46, Mediana: 6.0, DesvPad: 2.76]

  41. `Natureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **113** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 27, Tam Máx: 195, Tam Média: 120.13, DesvPad Tam: 44.59]

  42. `Origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 39.92, DesvPad Tam: 7.72]

  43. `PrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.85%** (49923 zeros) | Distintos: **68** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 124999407.0, Média: 11398.57, Mediana: 0.0, DesvPad: 862523.17]

  44. `PrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  45. `PrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  46. `Previsto` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Realizado` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `RecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **45.86%** (22928 zeros) | Distintos: **20278** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -161862806.14, Máx: 293498162.54, Média: 140352.2, Mediana: 0.0, DesvPad: 5503828.65]

  49. `Recolhido` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  50. `Rubrica` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Subalinea` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  52. `Tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **113** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 27, Tam Máx: 195, Tam Média: 120.13, DesvPad Tam: 44.59]

  53. `TipoArquivo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 18, Tam Média: 16.04, DesvPad Tam: 1.31]

  54. `TipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  55. `UGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **64** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 20.61, DesvPad Tam: 5.93]

  56. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 87, Tam Média: 36.89, DesvPad Tam: 7.34]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `Alinea`, `Previsto`, `Realizado`, `Recolhido`, `Rubrica`, `Subalinea`

> - `CodAlinea`, `CodDetalhamento2`

> - `CodDetalhamento1`, `CodRubrica`

> - `CodNatureza`, `CodSubalinea`, `CodTipo`

> - `Natureza`, `Tipo`

> - `PrevistaDeducao`, `PrevistaLiquida`


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