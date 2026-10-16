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

  2. `codigoAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **157** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111204.0, Máx: 792299.0, Média: 176106.6, Mediana: 121029.0, DesvPad: 146421.81]

  3. `codigoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.37, Mediana: 1.0, DesvPad: 1.43]

  4. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **58.1%** (92956 zeros) | Distintos: **38** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 922.0, Média: 3.7, Mediana: 0.0, DesvPad: 27.7]

  5. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.02%** (26 zeros) | Distintos: **187** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 675.000002, Média: 175.88, Mediana: 136.000003, DesvPad: 77.86]

  6. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 175.86, Mediana: 121.0, DesvPad: 146.47]

  7. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.02%** (26 zeros) | Distintos: **66** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 675.0, Média: 175.88, Mediana: 136.0, DesvPad: 77.86]

  8. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.02%** (26 zeros) | Distintos: **5** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 6.0, Média: 1.39, Mediana: 1.0, DesvPad: 0.49]

  9. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.19%** (158711 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5.0, Média: 0.03, Mediana: 0.0, DesvPad: 0.35]

  10. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **379** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120410.0, Máx: 79229900.0, Média: 17610678.88, Mediana: 12102908.0, DesvPad: 14642176.83]

  11. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 17.42, Mediana: 12.0, DesvPad: 14.64]

  12. `codigoRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **54** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7922.0, Média: 1760.8, Mediana: 1210.0, DesvPad: 1464.19]

  13. `codigoSubAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **379** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120410.0, Máx: 79229900.0, Média: 17610678.88, Mediana: 12102908.0, DesvPad: 14642176.83]

  14. `codigoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 20101.0, Máx: 800102.0, Média: 602750.62, Mediana: 600211.0, DesvPad: 232135.72]

  15. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **123** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 580400.34, Mediana: 600211.0, DesvPad: 247641.32]

  16. `contaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 521110000.0, Máx: 621390000.0, Média: 619818520.81, Mediana: 621200000.0, DesvPad: 11688956.3]

  17. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **56466** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  18. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1119** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  19. `descricaoAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **146** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 154, Tam Média: 81.45, DesvPad Tam: 49.96]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 19.15, DesvPad Tam: 4.53]

  21. `descricaoContaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 43, Tam Média: 17.67, DesvPad Tam: 3.69]

  22. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **208** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 174, Tam Média: 22.0, DesvPad Tam: 13.97]

  23. `descricaoEspecie` ➔ Nulos: **6.04%** (9669 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 39, Tam Média: 16.56, DesvPad Tam: 9.33]

  24. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **77** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 111, Tam Média: 25.36, DesvPad Tam: 10.11]

  25. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 49, Tam Média: 21.34, DesvPad Tam: 2.97]

  26. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 21, Tam Máx: 96, Tam Média: 38.86, DesvPad Tam: 1.62]

  27. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **385** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 152, Tam Média: 46.19, DesvPad Tam: 23.22]

  28. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 26, Tam Média: 20.78, DesvPad Tam: 3.15]

  29. `descricaoRubrica` ➔ Nulos: **25.13%** (40203 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **38** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 80, Tam Média: 34.55, DesvPad Tam: 8.48]

  30. `descricaoSubAlinea` ➔ Nulos: **12.38%** (19805 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **299** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 152, Tam Média: 44.28, DesvPad Tam: 21.16]

  31. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **194** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 87, Tam Média: 26.77, DesvPad Tam: 16.23]

  32. `descricaoUGEmitente` ➔ Nulos: **0.48%** (774 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **228** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 87, Tam Média: 27.58, DesvPad Tam: 17.41]

  33. `documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **31645** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  34. `tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 10, Tam Média: 9.97, DesvPad Tam: 0.23]

  35. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  36. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **1.39%** (2220 zeros) | Distintos: **119569** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -51107989.0, Máx: 355401146.7, Média: 123278.97, Mediana: 567.52, DesvPad: 2548775.09]

  37. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **98.62%** (157787 zeros) | Distintos: **1942** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -335784072.0, Máx: 2413081000.0, Média: 249088.24, Mediana: 0.0, DesvPad: 11949094.55]


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

  3. `codigoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **101** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7923.0, Média: 1290.19, Mediana: 1114.0, DesvPad: 791.26]

  4. `codigoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **218** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111205.0, Máx: 792399.0, Média: 129061.06, Mediana: 111450.0, DesvPad: 79120.29]

  5. `codigoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **263** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112050.0, Máx: 7923990.0, Média: 1290611.38, Mediana: 1114501.0, DesvPad: 791202.89]

  6. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **48.93%** (97857 zeros) | Distintos: **196** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 901001.0, Média: 15724.71, Mediana: 1.0, DesvPad: 53223.44]

  7. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **499** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.000675, Média: 459.33, Mediana: 500.0, DesvPad: 186.61]

  8. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 128.68, Mediana: 111.0, DesvPad: 79.13]

  9. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **146** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.0, Média: 459.31, Mediana: 500.0, DesvPad: 186.6]

  10. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 8.0, Média: 4.5, Mediana: 5.0, DesvPad: 1.85]

  11. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **19.99%** (39971 zeros) | Distintos: **7** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4.0, Média: 0.8, Mediana: 1.0, DesvPad: 0.41]

  12. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **336** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120501.0, Máx: 79239901.0, Média: 12906115.4, Mediana: 11145011.0, DesvPad: 7912028.79]

  13. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 12.74, Mediana: 11.0, DesvPad: 7.9]

  14. `codigoTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **336** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11120501.0, Máx: 79239901.0, Média: 12906115.4, Mediana: 11145011.0, DesvPad: 7912028.79]

  15. `codigoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **211** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 731485.16, Mediana: 800102.0, DesvPad: 169072.59]

  16. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **227** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 723631.72, Mediana: 800102.0, DesvPad: 181630.53]

  17. `contaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621390000.0, Média: 468027427.59, Mediana: 621200000.0, DesvPad: 233680045.63]

  18. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **72085** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  19. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1308** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.29, DesvPad Tam: 2.33]

  21. `descricaoContaContabil` ➔ Nulos: **30.0%** (59996 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 19.22, DesvPad Tam: 7.18]

  22. `descricaoDetalhamento1` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **48** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 142, Tam Média: 53.28, DesvPad Tam: 17.47]

  23. `descricaoDetalhamento2` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 147, Tam Média: 57.32, DesvPad Tam: 13.79]

  24. `descricaoDetalhamento3` ➔ Nulos: **0.0%** (2 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **143** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 154, Tam Média: 113.69, DesvPad Tam: 51.98]

  25. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** (6 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **349** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 185, Tam Média: 47.46, DesvPad Tam: 23.95]

  26. `descricaoEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **29** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 84, Tam Média: 11.98, DesvPad Tam: 10.61]

  27. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **96** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 141, Tam Média: 34.59, DesvPad Tam: 12.72]

  28. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 50, Tam Média: 43.95, DesvPad Tam: 12.14]

  29. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 39, Tam Média: 31.79, DesvPad Tam: 3.62]

  30. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **202** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 195, Tam Média: 117.89, DesvPad Tam: 45.39]

  31. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 39.38, DesvPad Tam: 8.39]

  32. `descricaoTipo` ➔ Nulos: **0.0%** (7 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **199** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 117.89, DesvPad Tam: 45.39]

  33. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **114** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 37.24, DesvPad Tam: 8.13]

  34. `descricaoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **120** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 20.25, DesvPad Tam: 6.37]

  35. `documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.03%** (68 zeros) | Distintos: **30707** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  36. `tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 18, Tam Média: 16.06, DesvPad Tam: 1.28]

  37. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  38. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (200000 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  39. `valorArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **79.09%** (158172 zeros) | Distintos: **36474** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -178325000.0, Máx: 333510093.66, Média: 67085.07, Mediana: 0.0, DesvPad: 3420740.43]

  40. `valorArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **96.16%** (192325 zeros) | Distintos: **7205** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -48583192.37, Máx: 10070104.99, Média: -12639.71, Mediana: 0.0, DesvPad: 474876.16]

  41. `valorArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **75.56%** (151121 zeros) | Distintos: **41953** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -180000000.0, Máx: 917386363.63, Média: 57955.71, Mediana: 0.0, DesvPad: 4327249.24]

  42. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (200000 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  43. `valorPrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.92%** (199839 zeros) | Distintos: **143** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 921949494.0, Média: 11836.59, Mediana: 0.0, DesvPad: 2251383.8]

  44. `valorPrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (199995 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: -11453638.0, Máx: 0.0, Média: -90.33, Mediana: 0.0, DesvPad: 27285.44]

  45. `valorPrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.92%** (199831 zeros) | Distintos: **146** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -172865464.0, Máx: 3305457676.0, Média: 49131.61, Mediana: 0.0, DesvPad: 9560813.52]

  46. `valorRecolhida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (200000 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  47. `valorRecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **49.36%** (98717 zeros) | Distintos: **78787** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -152772727.14, Máx: 1059074681.87, Média: 34697.02, Mediana: 0.0, DesvPad: 3344904.39]


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

  1. `Alinea` ➔ Nulos: **100.0%** (160000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2023.0, Máx: 2026.0, Média: 2024.5, Mediana: 2024.5, DesvPad: 1.12]

  3. `ArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **79.64%** (127429 zeros) | Distintos: **27873** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -37382426.79, Máx: 57275014.4, Média: 30321.21, Mediana: 0.0, DesvPad: 952441.77]

  4. `ArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **94.86%** (151782 zeros) | Distintos: **8047** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -915245.84, Máx: 882175.14, Média: -1675.04, Mediana: 0.0, DesvPad: 24172.87]

  5. `ArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **77.67%** (124265 zeros) | Distintos: **30233** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -68735853.76, Máx: 72876466.2, Média: 26017.23, Mediana: 0.0, DesvPad: 1570948.13]

  6. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 37, Tam Média: 18.26, DesvPad Tam: 2.18]

  7. `CodAlinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **117** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 792299.0, Média: 128577.06, Mediana: 111450.0, DesvPad: 75335.0]

  8. `CodCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 7.0, Média: 1.08, Mediana: 1.0, DesvPad: 0.69]

  9. `CodDetalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **52** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7922.0, Média: 1285.36, Mediana: 1114.0, DesvPad: 753.41]

  10. `CodDetalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **117** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 111251.0, Máx: 792299.0, Média: 128577.06, Mediana: 111450.0, DesvPad: 75335.0]

  11. `CodDetalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **138** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112510.0, Máx: 7922990.0, Média: 1285771.42, Mediana: 1114501.0, DesvPad: 753349.9]

  12. `CodEspecie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111.0, Máx: 792.0, Média: 128.2, Mediana: 111.0, DesvPad: 75.35]

  13. `CodNatureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **172** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79229901.0, Média: 12857715.71, Mediana: 11145011.0, DesvPad: 7533498.93]

  14. `CodOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 11.0, Máx: 79.0, Média: 12.7, Mediana: 11.0, DesvPad: 7.52]

  15. `CodRubrica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **52** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1112.0, Máx: 7922.0, Média: 1285.36, Mediana: 1114.0, DesvPad: 753.41]

  16. `CodSubalinea` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **172** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79229901.0, Média: 12857715.71, Mediana: 11145011.0, DesvPad: 7533498.93]

  17. `CodTipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **172** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11125101.0, Máx: 79229901.0, Média: 12857715.71, Mediana: 11145011.0, DesvPad: 7533498.93]

  18. `CodUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **87** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 723786.13, Mediana: 800102.0, DesvPad: 174552.84]

  19. `CodigoContaContabil` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 111113001.0, Máx: 621350000.0, Média: 436155241.78, Mediana: 621200000.0, DesvPad: 245080585.52]

  20. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **44.44%** (71107 zeros) | Distintos: **91** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 901001.0, Média: 20948.99, Mediana: 2.0, DesvPad: 67432.58]

  21. `CodigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **212** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.000675, Média: 538.72, Mediana: 500.000003, DesvPad: 94.29]

  22. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 538.7, Mediana: 500.0, DesvPad: 94.29]

  23. `CodigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 5.0, Máx: 8.0, Média: 5.32, Mediana: 5.0, DesvPad: 0.8]

  24. `CodigoIdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.03%** (53 zeros) | Distintos: **3** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2.0, Média: 1.0, Mediana: 1.0, DesvPad: 0.02]

  25. `CodigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **109** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 715195.21, Mediana: 800102.0, DesvPad: 184232.1]

  26. `ContaContabil` ➔ Nulos: **36.24%** (57979 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 45, Tam Média: 20.25, DesvPad Tam: 8.69]

  27. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **46** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  28. `DataContabilizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **61793** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  29. `DataEmissao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1013** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  30. `Detalhamento1` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **44** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 169, Tam Média: 52.8, DesvPad Tam: 17.82]

  31. `Detalhamento2` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **109** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 145, Tam Média: 57.09, DesvPad Tam: 14.43]

  32. `Detalhamento3` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **127** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 154, Tam Média: 112.84, DesvPad Tam: 52.32]

  33. `DetalhamentoFonte` ➔ Nulos: **0.0%** (6 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **237** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 219, Tam Média: 52.91, DesvPad Tam: 21.97]

  34. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.05%** (73 zeros) | Distintos: **24851** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  35. `Especie` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **27** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 84, Tam Média: 12.33, DesvPad Tam: 11.0]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 141, Tam Média: 36.99, DesvPad Tam: 14.03]

  37. `GrupoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 50, Tam Máx: 50, Tam Média: 50.0, DesvPad Tam: 0.0]

  38. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **160000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 403491956.0, Máx: 608101310.0, Média: 485892503.75, Mediana: 465988374.5, DesvPad: 83000834.3]

  39. `IdUso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 33, Tam Média: 29.99, DesvPad Tam: 0.33]

  40. `Mes` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 12.0, Média: 6.28, Mediana: 6.0, DesvPad: 3.31]

  41. `Natureza` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **168** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 116.81, DesvPad Tam: 45.75]

  42. `Origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 43, Tam Média: 39.12, DesvPad Tam: 8.58]

  43. `PrevistaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.9%** (159839 zeros) | Distintos: **132** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -42898828.27, Máx: 996943000.0, Média: 17901.83, Mediana: 0.0, DesvPad: 2707443.69]

  44. `PrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.97%** (159952 zeros) | Distintos: **46** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: -3076762984.0, Máx: 0.0, Média: -49178.6, Mediana: 0.0, DesvPad: 9972314.01]

  45. `PrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.91%** (159861 zeros) | Distintos: **130** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -323381050.0, Máx: 612000000.0, Média: 11294.47, Mediana: 0.0, DesvPad: 2263711.74]

  46. `Previsto` ➔ Nulos: **100.0%** (160000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Realizado` ➔ Nulos: **100.0%** (160000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `RecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **48.05%** (76872 zeros) | Distintos: **58066** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -97180632.31, Máx: 371610825.88, Média: 37689.52, Mediana: 0.0, DesvPad: 2708068.73]

  49. `Recolhido` ➔ Nulos: **100.0%** (160000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  50. `Rubrica` ➔ Nulos: **100.0%** (160000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Subalinea` ➔ Nulos: **100.0%** (160000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  52. `Tipo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **168** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 195, Tam Média: 116.81, DesvPad Tam: 45.75]

  53. `TipoArquivo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 18, Tam Média: 16.03, DesvPad Tam: 1.27]

  54. `TipoLancamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  55. `UGEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **108** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 19.76, DesvPad Tam: 6.86]

  56. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **87** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 37.48, DesvPad Tam: 8.36]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `Alinea`, `Previsto`, `Realizado`, `Recolhido`, `Rubrica`, `Subalinea`

> - `CodAlinea`, `CodDetalhamento2`

> - `CodDetalhamento1`, `CodRubrica`

> - `CodNatureza`, `CodSubalinea`, `CodTipo`

> - `Natureza`, `Tipo`


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