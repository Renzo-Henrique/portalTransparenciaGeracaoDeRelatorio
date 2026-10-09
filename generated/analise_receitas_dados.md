# Relatório de Análise Estrutural e Qualidade de Dados - CKAN

Este documento apresenta um resumo consolidado das bases de dados por período, evolução das colunas e métricas de qualidade consolidadas por período de tempo com marcação de alertas (Caso 1: Nulos/Zeros > 50 e Caso 2: Distintos > 50).

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
  1. `alinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **114** ⚠️ [Caso 2: >50 Distintos]

  2. `ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  3. `categoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  4. `codAlinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **123** ⚠️ [Caso 2: >50 Distintos]

  5. `codCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  6. `codEspecie` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **31**

  7. `codOrigem` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **16** 🟢 [Enum]

  8. `codRubrica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **57** ⚠️ [Caso 2: >50 Distintos]

  9. `codSubalinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **268** ⚠️ [Caso 2: >50 Distintos]

  10. `codUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **45** ⚠️ [Caso 2: >50 Distintos]

  11. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  12. `data` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  13. `especie` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **29**

  14. `mes` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  15. `origem` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **15** 🟢 [Enum]

  16. `previsto` ➔ Nulos: **0.0%** (0 nulos, 202 zeros) | Distintos: **244** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  17. `realizado` ➔ Nulos: **0.0%** (0 nulos, 132 zeros) | Distintos: **351** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  18. `recolhido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  19. `rubrica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **56** ⚠️ [Caso 2: >50 Distintos]

  20. `subalinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **265** ⚠️ [Caso 2: >50 Distintos]

  21. `unidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **43**

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
  1. `alinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **127** ⚠️ [Caso 2: >50 Distintos]

  2. `ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  3. `categoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  4. `codAlinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **141** ⚠️ [Caso 2: >50 Distintos]

  5. `codCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  6. `codEspecie` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **36** 🟢 [Enum]

  7. `codOrigem` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **19** 🟢 [Enum]

  8. `codRubrica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **61** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  9. `codSubalinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **295** ⚠️ [Caso 2: >50 Distintos]

  10. `codUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **52** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  11. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  12. `data` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11** 🟢 [Enum]

  13. `especie` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **28** 🟢 [Enum]

  14. `mes` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11** 🟢 [Enum]

  15. `origem` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **14** 🟢 [Enum]

  16. `previsto` ➔ Nulos: **0.0%** (0 nulos, 2959 zeros) | Distintos: **328** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  17. `realizado` ➔ Nulos: **0.0%** (0 nulos, 141 zeros) | Distintos: **3983** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  18. `recolhido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  19. `rubrica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  20. `subalinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **278** ⚠️ [Caso 2: >50 Distintos]

  21. `unidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **51** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

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
  1. `ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  2. `codigoAlinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **123** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  3. `codigoCategoria` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  4. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos, 16366 zeros) | Distintos: **35** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  5. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos, 6 zeros) | Distintos: **128** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  6. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **31** 🟢 [Enum]

  7. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos, 6 zeros) | Distintos: **48** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  8. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos, 6 zeros) | Distintos: **5** 🟢 [Enum]

  9. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **4** 🟢 [Enum]

  10. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **288** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  11. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **16** 🟢 [Enum]

  12. `codigoRubrica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **49** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  13. `codigoSubAlinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **288** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  14. `codigoUG` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **88** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  15. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **114** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  16. `contaContabil` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7** 🟢 [Enum]

  17. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **13227** ⚠️ [Caso 2: >50 Distintos]

  18. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **278** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  19. `descricaoAlinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **113** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  21. `descricaoContaContabil` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7** 🟢 [Enum]

  22. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **120** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  23. `descricaoEspecie` ➔ Nulos: **7.75%** (2325 nulos, 0 zeros) | Distintos: **23** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  24. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **47** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  25. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum]

  26. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **4** 🟢 [Enum]

  27. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **283** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  28. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **12** 🟢 [Enum]

  29. `descricaoRubrica` ➔ Nulos: **31.88%** (9565 nulos, 0 zeros) | Distintos: **34** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  30. `descricaoSubAlinea` ➔ Nulos: **13.97%** (4191 nulos, 0 zeros) | Distintos: **220** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  31. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **87** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  32. `descricaoUGEmitente` ➔ Nulos: **0.61%** (185 nulos, 0 zeros) | Distintos: **111** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  33. `documento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7409** ⚠️ [Caso 2: >50 Distintos]

  34. `tipo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  35. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  36. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **23636** ⚠️ [Caso 2: >50 Distintos]

  37. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos, 29446 zeros) | Distintos: **510** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

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
  1. `ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  2. `codigoCategoria` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  3. `codigoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **43** 🟢 [Enum]

  4. `codigoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **85** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  5. `codigoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **101** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  6. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos, 9148 zeros) | Distintos: **62** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  7. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **133** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  8. `codigoEspecie` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **27** 🟢 [Enum]

  9. `codigoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **43** 🟢 [Enum]

  10. `codigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  11. `codigoIdUso` ➔ Nulos: **0.0%** (0 nulos, 8 zeros) | Distintos: **1** 🟢 [Enum]

  12. `codigoNatureza` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **125** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  13. `codigoOrigem` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **14** 🟢 [Enum]

  14. `codigoTipo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **125** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  15. `codigoUG` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **77** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  16. `codigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **93** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  17. `contaContabil` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7** 🟢 [Enum]

  18. `dataContabilizacao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11598** ⚠️ [Caso 2: >50 Distintos]

  19. `dataEmissao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **240** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  20. `descricaoCategoria` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  21. `descricaoContaContabil` ➔ Nulos: **30.57%** (9171 nulos, 0 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  22. `descricaoDetalhamento1` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **37** 🟢 [Enum]

  23. `descricaoDetalhamento2` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **78** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  24. `descricaoDetalhamento3` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **92** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  25. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **127** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  26. `descricaoEspecie` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **23** 🟢 [Enum]

  27. `descricaoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **43** 🟢 [Enum]

  28. `descricaoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  29. `descricaoIdUso` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  30. `descricaoNatureza` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **122** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  31. `descricaoOrigem` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11** 🟢 [Enum]

  32. `descricaoTipo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **122** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  33. `descricaoUG` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **77** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  34. `descricaoUGEmitente` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **92** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  35. `documento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5099** ⚠️ [Caso 2: >50 Distintos]

  36. `tipo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6** 🟢 [Enum]

  37. `tipoLancamento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  38. `valorArrecadada` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  39. `valorArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos, 9534 zeros) | Distintos: **4263** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  40. `valorArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos, 11505 zeros) | Distintos: **899** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  41. `valorArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos, 9302 zeros) | Distintos: **4945** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  42. `valorPrevista` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  43. `valorPrevistaBruta` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **16** 🟢 [Enum]

  44. `valorPrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum]

  45. `valorPrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **50** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  46. `valorRecolhida` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  47. `valorRecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos, 5665 zeros) | Distintos: **10240** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

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
  1. `Alinea` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  3. `ArrecadadaBruta` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **4690** ⚠️ [Caso 2: >50 Distintos]

  4. `ArrecadadaDeducao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1161** ⚠️ [Caso 2: >50 Distintos]

  5. `ArrecadadaLiquida` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6045** ⚠️ [Caso 2: >50 Distintos]

  6. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  7. `CodAlinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **66** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  8. `CodCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  9. `CodDetalhamento1` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **32** 🟢 [Enum]

  10. `CodDetalhamento2` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **66** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  11. `CodDetalhamento3` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **78** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  12. `CodEspecie` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **21** 🟢 [Enum]

  13. `CodNatureza` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **100** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  14. `CodOrigem` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11** 🟢 [Enum]

  15. `CodRubrica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **32** 🟢 [Enum]

  16. `CodSubalinea` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **100** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  17. `CodTipo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **100** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  18. `CodUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **35** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  19. `CodigoContaContabil` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum]

  20. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **50** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  21. `CodigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **99** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  22. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **35** 🟢 [Enum]

  23. `CodigoGrupoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  24. `CodigoIdUso` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  25. `CodigoUGEmitente` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **53** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  26. `ContaContabil` ➔ Nulos: **38.15%** (11444 nulos, 0 zeros) | Distintos: **4** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  27. `Data` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11** 🟢 [Enum]

  28. `DataContabilizacao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **13284** ⚠️ [Caso 2: >50 Distintos]

  29. `DataEmissao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **249** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  30. `Detalhamento1` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **29** 🟢 [Enum]

  31. `Detalhamento2` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **62** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  32. `Detalhamento3` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **74** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  33. `DetalhamentoFonte` ➔ Nulos: **0.01%** (1 nulos, 0 zeros) | Distintos: **96** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  34. `Documento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5465** ⚠️ [Caso 2: >50 Distintos]

  35. `Especie` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **17** 🟢 [Enum]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **35** 🟢 [Enum]

  37. `GrupoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  38. `Id` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **30000** ⚠️ [Caso 2: >50 Distintos]

  39. `IdUso` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  40. `Mes` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11** 🟢 [Enum]

  41. `Natureza` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **99** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  42. `Origem` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **8** 🟢 [Enum]

  43. `PrevistaBruta` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **33** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  44. `PrevistaDeducao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **12** 🟢 [Enum]

  45. `PrevistaLiquida` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **33** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  46. `Previsto` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Realizado` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `RecolhidaBruta` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11548** ⚠️ [Caso 2: >50 Distintos]

  49. `Recolhido` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  50. `Rubrica` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Subalinea` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  52. `Tipo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **99** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  53. `TipoArquivo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **4** 🟢 [Enum]

  54. `TipoLancamento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  55. `UGEmitente` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **53** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  56. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **35** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

---

## 📂 Grupo Principal: `DividaAtiva`

### 🔹 Período: None
- **Quantidade Total de Colunas:** `9`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`DividaAtiva.csv`** *(ID: `016bbc36-15fb-476b-b249-d9726426c82c`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**
  1. `Ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  2. `CpfCnpj` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **678** ⚠️ [Caso 2: >50 Distintos]

  3. `DataInscricao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **223** ⚠️ [Caso 2: >50 Distintos]

  4. `Id` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2507** ⚠️ [Caso 2: >50 Distintos]

  5. `NomeDevedor` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **576** ⚠️ [Caso 2: >50 Distintos]

  6. `NumeroCDA` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2507** ⚠️ [Caso 2: >50 Distintos]

  7. `NumeroProcesso` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2507** ⚠️ [Caso 2: >50 Distintos]

  8. `ValorReal` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2404** ⚠️ [Caso 2: >50 Distintos]

  9. `ValorVRTE` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

---