# Relatório de Análise Estrutural e Qualidade de Dados - CKAN

Este documento apresenta um resumo consolidado das bases de dados por período, evolução das colunas, métricas de qualidade e estatísticas numéricas consolidadas com marcação de alertas (Caso 1: Nulos/Zeros > 50 e Caso 2: Distintos > 50). Foram utilizados apenas `50000 registros por recurso`

---

## 📂 Grupo Principal: `Contratos-`

### 🔹 Período: None
- **Quantidade Total de Colunas:** `27`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Contratos-1753.csv`** *(ID: `a1f38833-1e18-4b6b-875e-df8a67d8909c`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `CnpjFormatado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **72** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 18, Tam Média: 18.0, DesvPad Tam: 0.0]

  2. `CnpjFornecedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **72** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 7950754729.0, Máx: 92264472000170.0, Média: 21096004552040.92, Mediana: 18269239000127.0, DesvPad: 12848830588141.9]

  3. `DataCelebracao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  4. `DataFimVigencia` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **50** | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  5. `DataInicioVigencia` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **48** | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  6. `Fornecedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **72** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 70, Tam Média: 45.82, DesvPad Tam: 12.02]

  7. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **180** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 68.0, Máx: 39872.0, Média: 23423.44, Mediana: 26472.0, DesvPad: 9012.66]

  8. `IdOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 25.0, Máx: 187.0, Média: 134.86, Mediana: 162.0, DesvPad: 45.42]

  9. `ModalidadeProcesso` ➔ Nulos: **11.11%** (20 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 21, Tam Média: 17.1, DesvPad Tam: 0.73]

  10. `NomeOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 27, Tam Máx: 71, Tam Média: 39.16, DesvPad Tam: 12.32]

  11. `NumeroDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **180** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 23, Tam Máx: 39, Tam Média: 34.2, DesvPad Tam: 3.55]

  12. `NumeroEdital` ➔ Nulos: **87.78%** (158 nulos) | Zeros: **0.56%** (1 zeros) | Distintos: **21** ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 15, Tam Média: 8.91, DesvPad Tam: 2.27]

  13. `NumeroProcesso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **80** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 10, Tam Média: 9.32, DesvPad Tam: 0.95]

  14. `Objeto` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **124** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 977, Tam Média: 76.46, DesvPad Tam: 88.42]

  15. `Situacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 9, Tam Média: 9.0, DesvPad Tam: 0.0]

  16. `TipoAquisicao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 56, Tam Média: 16.87, DesvPad Tam: 5.12]

  17. `TipoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 28, Tam Média: 23.59, DesvPad Tam: 6.38]

  18. `ValorFinal` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **99** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 54.0, Máx: 14751756.36, Média: 100510.41, Mediana: 518.635, DesvPad: 1097261.56]

  19. `ValorInicial` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **99** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 54.0, Máx: 14751756.36, Média: 100510.41, Mediana: 518.635, DesvPad: 1097261.56]

  20. `eRegistroPreco` ➔ Nulos: **16.67%** (30 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  21. `idOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **180** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 6993.0, Máx: 181603.0, Média: 123801.14, Mediana: 137574.5, DesvPad: 32212.05]

  22. `justificativaProcForaSiga` ➔ Nulos: **97.78%** (176 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 2, Tam Máx: 140, Tam Média: 76.5, DesvPad Tam: 50.23]

  23. `numProcUtilizacao` ➔ Nulos: **20.56%** (37 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **138** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 10, Tam Média: 9.66, DesvPad Tam: 0.75]

  24. `orgaoOrigemProcesso` ➔ Nulos: **98.33%** (177 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 8, Tam Média: 6.67, DesvPad Tam: 0.94]

  25. `origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 1.0, Média: 1.0, Mediana: 1.0, DesvPad: 0.0]

  26. `origemContrato` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (180 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  27. `procRealizadoSiga` ➔ Nulos: **16.67%** (30 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `ValorFinal`, `ValorInicial`

> - `eRegistroPreco`, `procRealizadoSiga`


---
### 🔹 Período: None
- **Quantidade Total de Colunas:** `26`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Contratos-2224.csv`** *(ID: `db608579-ff45-41ad-b65b-8913e981d94f`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `CnpjFormatado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 18, Tam Média: 18.0, DesvPad Tam: 0.0]

  2. `CnpjFornecedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 34617980000198.0, Máx: 34617980000198.0, Média: 34617980000198.0, Mediana: 34617980000198.0, DesvPad: 0.0]

  3. `DataCelebracao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  4. `DataFimVigencia` ➔ Nulos: **100.0%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  5. `DataInicioVigencia` ➔ Nulos: **100.0%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  6. `Fornecedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 33, Tam Máx: 33, Tam Média: 33.0, DesvPad Tam: 0.0]

  7. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 43568.0, Máx: 43568.0, Média: 43568.0, Mediana: 43568.0, DesvPad: 0.0]

  8. `IdOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 159.0, Máx: 159.0, Média: 159.0, Mediana: 159.0, DesvPad: 0.0]

  9. `ModalidadeProcesso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 21, Tam Máx: 21, Tam Média: 21.0, DesvPad Tam: 0.0]

  10. `NomeOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 60, Tam Máx: 60, Tam Média: 60.0, DesvPad Tam: 0.0]

  11. `NumeroDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  12. `NumeroEdital` ➔ Nulos: **100.0%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  13. `NumeroProcesso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 10, Tam Média: 10.0, DesvPad Tam: 0.0]

  14. `Objeto` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 38, Tam Máx: 38, Tam Média: 38.0, DesvPad Tam: 0.0]

  15. `Situacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 134, Tam Máx: 134, Tam Média: 134.0, DesvPad Tam: 0.0]

  16. `TipoAquisicao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 7, Tam Média: 7.0, DesvPad Tam: 0.0]

  17. `TipoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 7, Tam Média: 7.0, DesvPad Tam: 0.0]

  18. `ValorFinal` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 692.0, Máx: 692.0, Média: 692.0, Mediana: 692.0, DesvPad: 0.0]

  19. `ValorInicial` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 692.0, Máx: 692.0, Média: 692.0, Mediana: 692.0, DesvPad: 0.0]

  20. `eRegistroPreco` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  21. `idOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 18487.0, Máx: 18487.0, Média: 18487.0, Mediana: 18487.0, DesvPad: 0.0]

  22. `justificativaProcForaSiga` ➔ Nulos: **100.0%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  23. `numProcUtilizacao` ➔ Nulos: **100.0%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  24. `orgaoOrigemProcesso` ➔ Nulos: **100.0%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  25. `origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 2.0, Média: 2.0, Mediana: 2.0, DesvPad: 0.0]

  26. `procRealizadoSiga` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `DataCelebracao`, `NumeroDocumento`

> - `DataFimVigencia`, `DataInicioVigencia`, `NumeroEdital`, `justificativaProcForaSiga`, `numProcUtilizacao`, `orgaoOrigemProcesso`

> - `TipoAquisicao`, `TipoDocumento`

> - `ValorFinal`, `ValorInicial`

> - `eRegistroPreco`, `procRealizadoSiga`


---
### 🔹 Período: None até 2032
- **Quantidade Total de Colunas:** `27`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Contratos-3024.csv`** *(ID: `1b620ab8-bdba-40d5-9af7-95e78787def3`)*
  - 📄 **`Contratos-5024.csv`** *(ID: `c0533a5f-3ef2-403d-9c31-dfeef4da40f5`)*
  - 📄 **`Contratos-1991.csv`** *(ID: `1fabe5d9-8252-432e-9506-b3d6697651f6`)*
  - 📄 **`Contratos-2001.csv`** *(ID: `dc58e360-eeda-4dba-aaeb-23d436a89833`)*
  - 📄 **`Contratos-2006.csv`** *(ID: `8521e2c6-ceeb-4b53-8cec-99ce87caa4cc`)*
  - 📄 **`Contratos-2008.csv`** *(ID: `8415fca5-e522-499c-89e4-a4272146f7a3`)*
  - 📄 **`Contratos-2009.csv`** *(ID: `ca351857-d948-429c-9951-3d7a1bca81a9`)*
  - 📄 **`Contratos-2010.csv`** *(ID: `f8c665bb-9539-4ee3-9007-6c83b1facaaf`)*
  - 📄 **`Contratos-2011.csv`** *(ID: `e5b0e1da-1ad8-47db-9b54-91c25d0cb2eb`)*
  - 📄 **`Contratos-2012.csv`** *(ID: `61c2911c-97cc-4c24-9cf8-f0325f5caab6`)*
  - 📄 **`Contratos-2013.csv`** *(ID: `87afa923-9767-4244-b973-528e1ae9ebf8`)*
  - 📄 **`Contratos-2014.csv`** *(ID: `2951b922-fd9e-4c9a-85a1-423969127cc8`)*
  - 📄 **`Contratos-2015.csv`** *(ID: `cdc1e21c-2aca-448b-b4e4-34a0a1aa7f5d`)*
  - 📄 **`Contratos-2016.csv`** *(ID: `52367d44-2ead-49c7-bde7-58ed3a94e80b`)*
  - 📄 **`Contratos-2017.csv`** *(ID: `f7a2ef64-2e8a-43cb-9e8d-b8c18dbfeaae`)*
  - 📄 **`Contratos-2018.csv`** *(ID: `479a6c98-041c-485f-8029-845672218806`)*
  - 📄 **`Contratos-2019.csv`** *(ID: `31e6f40e-d1a8-4e1f-b9e0-6e08a0366b94`)*
  - 📄 **`Contratos-2020.csv`** *(ID: `8f8c75b7-d22c-4110-b200-d2fbeb9dedbf`)*
  - 📄 **`Contratos-2021.csv`** *(ID: `01eab5a5-9c8f-4dd4-bf31-dcdbae5f2b5a`)*
  - 📄 **`Contratos-2022.csv`** *(ID: `f9b04d92-9b41-4379-847b-221cd03f20af`)*
  - 📄 **`Contratos-2023.csv`** *(ID: `e54cca38-8bda-45ac-b342-f25c77ee0a7f`)*
  - 📄 **`Contratos-2024.csv`** *(ID: `85e4d84d-3738-4067-b2e1-a2bb8c80f84b`)*
  - 📄 **`Contratos-2025.csv`** *(ID: `54a632a4-cb07-4e85-98f9-5f47f1e024b7`)*
  - 📄 **`Contratos-2026.csv`** *(ID: `7b39e272-5914-4a8a-a7d6-30b174fce210`)*
  - 📄 **`Contratos-2027.csv`** *(ID: `d71c0ab8-8ef4-4fe5-bdaf-9dfcd44c0e86`)*
  - 📄 **`Contratos-2028.csv`** *(ID: `ff1b6e80-9feb-4623-a7e3-758174ecb988`)*
  - 📄 **`Contratos-2032.csv`** *(ID: `6fe0aaeb-424d-4f23-bb63-77459f2f030d`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `CnpjFormatado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7737** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 18, Tam Média: 18.0, DesvPad Tam: 0.01]

  2. `CnpjFornecedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9669** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 14, Tam Média: 13.74, DesvPad Tam: 0.69]

  3. `DataCelebracao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3526** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  4. `DataFimVigencia` ➔ Nulos: **38.46%** (28997 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5760** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  5. `DataInicioVigencia` ➔ Nulos: **38.23%** (28822 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4032** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  6. `Fornecedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7948** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 142, Tam Média: 38.69, DesvPad Tam: 13.89]

  7. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **75391** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 79871.0, Média: 41847.45, Mediana: 42176.5, DesvPad: 22242.67]

  8. `IdOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **197** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 1413.0, Média: 107.27, Mediana: 67.0, DesvPad: 135.04]

  9. `ModalidadeProcesso` ➔ Nulos: **7.49%** (5644 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 39, Tam Média: 18.12, DesvPad Tam: 2.95]

  10. `NomeOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **103** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 98, Tam Média: 40.15, DesvPad Tam: 15.15]

  11. `NumeroDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **71238** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 69, Tam Média: 41.97, DesvPad Tam: 17.66]

  12. `NumeroEdital` ➔ Nulos: **51.73%** (39000 nulos) | Zeros: **0.01%** (11 zeros) | Distintos: **6448** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 30, Tam Média: 8.65, DesvPad Tam: 1.6]

  13. `NumeroProcesso` ➔ Nulos: **0.86%** (650 nulos) | Zeros: **0.0%** (2 zeros) | Distintos: **28533** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 31, Tam Média: 9.6, DesvPad Tam: 1.41]

  14. `Objeto` ➔ Nulos: **0.21%** (161 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **40015** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 4139, Tam Média: 107.65, DesvPad Tam: 137.32]

  15. `Situacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 44, Tam Média: 21.69, DesvPad Tam: 11.98]

  16. `TipoAquisicao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 82, Tam Média: 13.53, DesvPad Tam: 8.86]

  17. `TipoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 43, Tam Média: 25.05, DesvPad Tam: 13.87]

  18. `ValorFinal` ➔ Nulos: **0.05%** (38 nulos) | Zeros: **0.03%** (21 zeros) | Distintos: **43533** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2015602082.88, Média: 462290.75, Mediana: 5831.0, DesvPad: 9918683.62]

  19. `ValorInicial` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.08%** (59 zeros) | Distintos: **43355** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2472718950.16, Média: 415556.72, Mediana: 5805.75, DesvPad: 10736413.98]

  20. `eRegistroPreco` ➔ Nulos: **12.14%** (9150 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

  21. `idOrigem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **74467** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 182403.0, Média: 68173.33, Mediana: 40356.5, DesvPad: 54532.74]

  22. `justificativaProcForaSiga` ➔ Nulos: **96.79%** (72974 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **864** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 249, Tam Média: 77.01, DesvPad Tam: 62.52]

  23. `numProcUtilizacao` ➔ Nulos: **37.82%** (28514 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14049** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 31, Tam Média: 9.7, DesvPad Tam: 0.76]

  24. `orgaoOrigemProcesso` ➔ Nulos: **65.02%** (49023 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **614** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 2, Tam Máx: 156, Tam Média: 13.47, DesvPad Tam: 19.25]

  25. `origem` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 2.0, Média: 1.53, Mediana: 2.0, DesvPad: 0.5]

  26. `origemContrato` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **46.99%** (35423 zeros) | Distintos: **12** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5.0, Média: 1.37, Mediana: 1.0, DesvPad: 1.4]

  27. `procRealizadoSiga` ➔ Nulos: **18.44%** (13904 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1, Tam Média: 1.0, DesvPad Tam: 0.0]

---

## 📂 Grupo Principal: `Empenhos-`

### 🔹 Período: None
- **Quantidade Total de Colunas:** `14`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Empenhos-1753.csv`** *(ID: `fdc3f16d-c46b-440c-9859-10435aed5894`)*
  - 📄 **`Empenhos-2224.csv`** *(ID: `2f63817b-3602-495e-b074-abb614c72336`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **194** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 352.0, Máx: 45715.0, Média: 27556.82, Mediana: 32092.5, DesvPad: 10360.91]

  2. `NumeroDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **181** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 39, Tam Média: 33.62, DesvPad Tam: 4.24]

  3. `NumeroEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **191** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 11, Tam Média: 9.64, DesvPad Tam: 2.51]

  4. `NumeroProcesso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **81** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 10, Tam Média: 9.3, DesvPad Tam: 0.95]

  5. `TipoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 28, Tam Média: 22.77, DesvPad Tam: 7.16]

  6. `TipoEmpenho` ➔ Nulos: **0.52%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 10, Tam Média: 8.88, DesvPad Tam: 0.92]

  7. `cnpjFornecedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **73** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 7950754729.0, Máx: 92264472000170.0, Média: 20434460126627.52, Mediana: 18269239000127.0, DesvPad: 12858719944183.33]

  8. `fonteRecurso` ➔ Nulos: **76.29%** (148 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 23, Tam Máx: 112, Tam Média: 52.91, DesvPad Tam: 17.58]

  9. `naturezaDespesa` ➔ Nulos: **76.8%** (149 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 30, Tam Máx: 73, Tam Média: 43.91, DesvPad Tam: 12.78]

  10. `nomeFornecedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **72** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 70, Tam Média: 45.71, DesvPad Tam: 11.76]

  11. `programaTrabalho` ➔ Nulos: **77.32%** (150 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 46, Tam Máx: 114, Tam Média: 69.32, DesvPad Tam: 21.36]

  12. `saldo` ➔ Nulos: **0.52%** (1 nulos) | Zeros: **42.78%** (83 zeros) | Distintos: **84** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 505000.0, Média: 9801.98, Mediana: 201.46, DesvPad: 45549.42]

  13. `situacao` ➔ Nulos: **0.52%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 5, Tam Média: 5.0, DesvPad Tam: 0.0]

  14. `valorGlobal` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.52%** (1 zeros) | Distintos: **109** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 505000.0, Média: 11675.28, Mediana: 530.0, DesvPad: 47675.6]

---
### 🔹 Período: None até 1991
- **Quantidade Total de Colunas:** `0`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Empenhos-3024.csv`** *(ID: `81ecafd8-68dd-4200-ba61-6b111a3699a9`)*
  - 📄 **`Empenhos-5024.csv`** *(ID: `7cf61401-2a8f-442a-9325-caceb7604a0a`)*
  - 📄 **`Empenhos-1991.csv`** *(ID: `24e3a501-e87e-4773-8d65-222024e588f6`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  - *Nenhuma métrica obtida para este período.*
---
### 🔹 Período: 2001 até 2026
- **Quantidade Total de Colunas:** `14`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Empenhos-2001.csv`** *(ID: `f5291377-c675-4a98-8982-daeb1b93ca56`)*
  - 📄 **`Empenhos-2006.csv`** *(ID: `b423d494-3c3a-42c0-8d46-03b82729e12f`)*
  - 📄 **`Empenhos-2008.csv`** *(ID: `70be15fd-682b-4e77-9ed5-a9933512870b`)*
  - 📄 **`Empenhos-2009.csv`** *(ID: `68e97349-c39e-452d-acc8-6ff8b9c67bf8`)*
  - 📄 **`Empenhos-2010.csv`** *(ID: `c2947dcf-b520-406b-ae1c-a50bc53072e0`)*
  - 📄 **`Empenhos-2011.csv`** *(ID: `19f3c11d-5571-4d78-980d-9606198daae3`)*
  - 📄 **`Empenhos-2012.csv`** *(ID: `7d8a1e2e-ca97-4c6b-b773-d946d27f4167`)*
  - 📄 **`Empenhos-2013.csv`** *(ID: `e9a732c6-fd69-4323-a00d-c78d31541c2d`)*
  - 📄 **`Empenhos-2014.csv`** *(ID: `021fec2d-0ef3-479b-981e-ca3d5385d3a0`)*
  - 📄 **`Empenhos-2015.csv`** *(ID: `0205d350-0004-4c48-9e9b-a5394ab3c64f`)*
  - 📄 **`Empenhos-2016.csv`** *(ID: `32cbbdd2-1d4a-4c14-b3af-bfb863dec69e`)*
  - 📄 **`Empenhos-2017.csv`** *(ID: `02c3550d-d813-4e22-8cce-eb13a1fc41d8`)*
  - 📄 **`Empenhos-2018.csv`** *(ID: `ebacf738-848f-4de5-9d58-4362a1aa39c8`)*
  - 📄 **`Empenhos-2019.csv`** *(ID: `cfa9f537-0545-4ee7-8a9e-f05fa902554e`)*
  - 📄 **`Empenhos-2020.csv`** *(ID: `c77e25e0-5f94-4d5c-bf42-314415a950cc`)*
  - 📄 **`Empenhos-2021.csv`** *(ID: `d4c95c4e-9dea-4d87-b8bf-9c9dacbd50ca`)*
  - 📄 **`Empenhos-2022.csv`** *(ID: `a5f1c107-21b4-40df-b41f-576d3e566d35`)*
  - 📄 **`Empenhos-2023.csv`** *(ID: `330bb165-b390-4f40-896d-203ad7be50ef`)*
  - 📄 **`Empenhos-2024.csv`** *(ID: `5cfe1779-1468-4a7a-9f67-cbd006ed3475`)*
  - 📄 **`Empenhos-2025.csv`** *(ID: `d8d5b375-1b69-44ff-aadd-d5a467323918`)*
  - 📄 **`Empenhos-2026.csv`** *(ID: `ffd20ce7-7f30-404b-a3be-a838e6706336`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **187565** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 187761.0, Média: 93949.21, Mediana: 93978.0, DesvPad: 54187.27]

  2. `NumeroDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **65472** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 69, Tam Média: 35.38, DesvPad Tam: 17.97]

  3. `NumeroEmpenho` ➔ Nulos: **0.0%** (1 nulos) | Zeros: **0.01%** (14 zeros) | Distintos: **54860** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 50, Tam Média: 10.76, DesvPad Tam: 1.69]

  4. `NumeroProcesso` ➔ Nulos: **0.41%** (771 nulos) | Zeros: **0.0%** (2 zeros) | Distintos: **26399** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 31, Tam Média: 9.92, DesvPad Tam: 1.86]

  5. `TipoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 43, Tam Média: 19.02, DesvPad Tam: 14.48]

  6. `TipoEmpenho` ➔ Nulos: **75.58%** (141770 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 10, Tam Média: 8.87, DesvPad Tam: 1.41]

  7. `cnpjFornecedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6795** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 14, Tam Média: 13.94, DesvPad Tam: 0.42]

  8. `fonteRecurso` ➔ Nulos: **89.53%** (167931 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **164** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 20, Tam Máx: 112, Tam Média: 56.75, DesvPad Tam: 20.67]

  9. `naturezaDespesa` ➔ Nulos: **89.87%** (168557 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **343** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 17, Tam Máx: 109, Tam Média: 42.77, DesvPad Tam: 12.85]

  10. `nomeFornecedor` ➔ Nulos: **0.0%** (1 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7915** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 142, Tam Média: 38.58, DesvPad Tam: 14.36]

  11. `programaTrabalho` ➔ Nulos: **90.41%** (169572 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **790** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 40, Tam Máx: 159, Tam Média: 66.81, DesvPad Tam: 20.05]

  12. `saldo` ➔ Nulos: **75.58%** (141770 nulos) | Zeros: **5.2%** (9746 zeros) | Distintos: **23495** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -3846.68, Máx: 270507415.51, Média: 82923.07, Mediana: 2013.36, DesvPad: 1645859.53]

  13. `situacao` ➔ Nulos: **75.58%** (141770 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 5, Tam Média: 5.0, DesvPad Tam: 0.0]

  14. `valorGlobal` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.34%** (640 zeros) | Distintos: **102631** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 271089287.0, Média: 88652.22, Mediana: 3510.0, DesvPad: 1255078.61]

---
### 🔹 Período: 2027
- **Quantidade Total de Colunas:** `0`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Empenhos-2027.csv`** *(ID: `c062f0c1-8668-4c4b-8623-9d8b07bfd514`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  - *Nenhuma métrica obtida para este período.*
---
### 🔹 Período: 2032
- **Quantidade Total de Colunas:** `14`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Empenhos-2032.csv`** *(ID: `5278768f-1dc9-4153-b674-31866522b598`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 85221.0, Máx: 131828.0, Média: 100757.0, Mediana: 85222.0, DesvPad: 21970.51]

  2. `NumeroDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 53, Tam Máx: 53, Tam Média: 53.0, DesvPad Tam: 0.0]

  3. `NumeroEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  4. `NumeroProcesso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 10, Tam Máx: 10, Tam Média: 10.0, DesvPad Tam: 0.0]

  5. `TipoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 43, Tam Máx: 43, Tam Média: 43.0, DesvPad Tam: 0.0]

  6. `TipoEmpenho` ➔ Nulos: **100.0%** (3 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  7. `cnpjFornecedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 10586940000168.0, Máx: 10586940000168.0, Média: 10586940000168.0, Mediana: 10586940000168.0, DesvPad: 0.0]

  8. `fonteRecurso` ➔ Nulos: **100.0%** (3 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  9. `naturezaDespesa` ➔ Nulos: **100.0%** (3 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  10. `nomeFornecedor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 42, Tam Máx: 42, Tam Média: 42.0, DesvPad Tam: 0.0]

  11. `programaTrabalho` ➔ Nulos: **100.0%** (3 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  12. `saldo` ➔ Nulos: **100.0%** (3 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  13. `situacao` ➔ Nulos: **100.0%** (3 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum]

  14. `valorGlobal` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 55.02, Máx: 4930.2, Média: 3171.76, Mediana: 4530.07, DesvPad: 2209.92]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `TipoEmpenho`, `fonteRecurso`, `naturezaDespesa`, `programaTrabalho`, `saldo`, `situacao`


---

## 📂 Grupo Principal: `AlteracoesContratuais-`

### 🔹 Período: None até 2009
- **Quantidade Total de Colunas:** `0`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`AlteracoesContratuais-1753.csv`** *(ID: `5bcc2b46-7d94-4d4a-aaae-7495b2c21272`)*
  - 📄 **`AlteracoesContratuais-2224.csv`** *(ID: `2f9849af-afb1-4a51-8659-97991705af9c`)*
  - 📄 **`AlteracoesContratuais-3024.csv`** *(ID: `31ceeba6-7138-4ee5-8b8c-149e237a4269`)*
  - 📄 **`AlteracoesContratuais-5024.csv`** *(ID: `426359c7-c7a6-4cab-bb77-7608261c4a87`)*
  - 📄 **`AlteracoesContratuais-1991.csv`** *(ID: `75b13225-35ec-4a84-a722-12a5c4895627`)*
  - 📄 **`AlteracoesContratuais-2001.csv`** *(ID: `8143a07a-d141-472b-a9c0-531f4dc26d5c`)*
  - 📄 **`AlteracoesContratuais-2006.csv`** *(ID: `4952d33b-3813-4b0e-b33e-7e34cec0ad99`)*
  - 📄 **`AlteracoesContratuais-2008.csv`** *(ID: `0ce629ce-8b6c-40eb-bca5-590133c035a9`)*
  - 📄 **`AlteracoesContratuais-2009.csv`** *(ID: `33ebb82b-7a58-430a-9037-55b4431fb653`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  - *Nenhuma métrica obtida para este período.*
---
### 🔹 Período: 2010 até 2026
- **Quantidade Total de Colunas:** `9`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`AlteracoesContratuais-2010.csv`** *(ID: `2bfc9572-b695-43e6-b442-358adf62f160`)*
  - 📄 **`AlteracoesContratuais-2011.csv`** *(ID: `98d16b88-2558-4203-a4cb-430e964dd9fb`)*
  - 📄 **`AlteracoesContratuais-2012.csv`** *(ID: `21391d94-29d8-491d-bf6f-e0b5a529557c`)*
  - 📄 **`AlteracoesContratuais-2013.csv`** *(ID: `5711c158-463f-4a01-9a9e-7e394aa263ed`)*
  - 📄 **`AlteracoesContratuais-2014.csv`** *(ID: `654425b1-283a-4773-b3b0-16b525ade118`)*
  - 📄 **`AlteracoesContratuais-2015.csv`** *(ID: `eca8003b-4fb2-42b0-9ae2-e823fb1b64c5`)*
  - 📄 **`AlteracoesContratuais-2016.csv`** *(ID: `8119beab-e65a-4eb6-a752-cd4fcdae1bd2`)*
  - 📄 **`AlteracoesContratuais-2017.csv`** *(ID: `06bef32f-ae82-4c18-9c46-736d8c688f6c`)*
  - 📄 **`AlteracoesContratuais-2018.csv`** *(ID: `086e01a9-ab6b-4df9-ad43-7a35433130ac`)*
  - 📄 **`AlteracoesContratuais-2019.csv`** *(ID: `6ce5abc5-feca-4205-a682-90024a0961af`)*
  - 📄 **`AlteracoesContratuais-2020.csv`** *(ID: `3bd637c7-42c5-4096-800d-90642f4286d8`)*
  - 📄 **`AlteracoesContratuais-2021.csv`** *(ID: `660503c5-8879-4f93-b44c-b8edb1f92b17`)*
  - 📄 **`AlteracoesContratuais-2022.csv`** *(ID: `ac3e6d8b-98c8-4249-acd0-b2cdea095878`)*
  - 📄 **`AlteracoesContratuais-2023.csv`** *(ID: `edf68ba8-a232-4d1e-87b0-8b7544343b75`)*
  - 📄 **`AlteracoesContratuais-2024.csv`** *(ID: `5df70394-0990-484a-a006-9e2f8e95bfd7`)*
  - 📄 **`AlteracoesContratuais-2025.csv`** *(ID: `7d75a274-224b-4321-a8fe-2d47066a9381`)*
  - 📄 **`AlteracoesContratuais-2026.csv`** *(ID: `780d3991-818f-4dd3-a753-3cbe7ae72cd0`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `DataAlteracao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1913** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  2. `DataFimVigencia` ➔ Nulos: **10.46%** (442 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1493** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  3. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4226** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 4226.0, Média: 2113.5, Mediana: 2113.5, DesvPad: 1219.94]

  4. `NumeroDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1736** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 69, Tam Média: 24.91, DesvPad Tam: 9.86]

  5. `NumeroProcesso` ➔ Nulos: **0.12%** (5 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1546** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 31, Tam Média: 9.92, DesvPad Tam: 2.17]

  6. `TipoAlteracao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **87** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 123, Tam Média: 27.6, DesvPad Tam: 19.79]

  7. `TipoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 43, Tam Média: 9.25, DesvPad Tam: 6.39]

  8. `TipoFormalizacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 19, Tam Média: 14.09, DesvPad Tam: 2.91]

  9. `ValorAlteracao` ➔ Nulos: **33.96%** (1435 nulos) | Zeros: **13.87%** (586 zeros) | Distintos: **1979** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 320345267.0, Média: 3000345.02, Mediana: 34200.0, DesvPad: 16737741.98]

---
### 🔹 Período: 2027 até 2032
- **Quantidade Total de Colunas:** `0`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`AlteracoesContratuais-2027.csv`** *(ID: `b485281e-da1d-4d8d-a877-4d9d0feb4dbd`)*
  - 📄 **`AlteracoesContratuais-2032.csv`** *(ID: `caee0c6f-6a11-4c38-ab4c-ddcbcf93f9c9`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  - *Nenhuma métrica obtida para este período.*
---

## 📂 Grupo Principal: `Comissoes-`

### 🔹 Período: None até 2026
- **Quantidade Total de Colunas:** `8`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Comissoes-1753.csv`** *(ID: `b7a159e3-5d31-4dae-b784-399b80af3853`)*
  - 📄 **`Comissoes-2001.csv`** *(ID: `a96682ec-60f9-4f23-9072-56bb00033fb2`)*
  - 📄 **`Comissoes-2006.csv`** *(ID: `30e27d07-901f-4295-ae6a-5ef1af8a7808`)*
  - 📄 **`Comissoes-2008.csv`** *(ID: `09bc6d30-7469-4f0d-b1b8-8fd747d91a30`)*
  - 📄 **`Comissoes-2009.csv`** *(ID: `0e6d7a1e-cac7-497c-a451-133b78076126`)*
  - 📄 **`Comissoes-2010.csv`** *(ID: `a15975e4-ebbd-4d8c-98e0-aed4aac8e8fa`)*
  - 📄 **`Comissoes-2011.csv`** *(ID: `5d1070ca-30eb-40e9-9110-34e14bdc0562`)*
  - 📄 **`Comissoes-2012.csv`** *(ID: `16294819-6e4f-467f-a87e-d8aac7fe2a00`)*
  - 📄 **`Comissoes-2013.csv`** *(ID: `ca7a4ff5-7a4d-4bf1-99f2-4843d6d637be`)*
  - 📄 **`Comissoes-2014.csv`** *(ID: `375e9b0d-5952-4ca9-b1fd-05a2164c65e8`)*
  - 📄 **`Comissoes-2015.csv`** *(ID: `89096f83-d0e6-4682-8c83-65529eb8854a`)*
  - 📄 **`Comissoes-2016.csv`** *(ID: `b9e60b25-559d-484b-82d5-854f0275aae4`)*
  - 📄 **`Comissoes-2017.csv`** *(ID: `01d61061-0d5c-43af-b6a3-6eb2cfe909a7`)*
  - 📄 **`Comissoes-2018.csv`** *(ID: `87eb4bd0-cb01-411e-acc1-29708e42a8df`)*
  - 📄 **`Comissoes-2019.csv`** *(ID: `6c4c3d1a-d2fa-4999-9bba-5b51de43cb2e`)*
  - 📄 **`Comissoes-2020.csv`** *(ID: `588c43bf-23bc-463c-9be6-794cdcf57cfd`)*
  - 📄 **`Comissoes-2021.csv`** *(ID: `70a90009-81f6-4bf3-b665-840a35140831`)*
  - 📄 **`Comissoes-2022.csv`** *(ID: `8918a8a2-9a6b-4e5b-8800-c5c4d6b2ef84`)*
  - 📄 **`Comissoes-2023.csv`** *(ID: `2ad8ecc6-a6b5-48c2-b6dd-014494e39d27`)*
  - 📄 **`Comissoes-2024.csv`** *(ID: `9065970b-608a-4874-bc35-bdf6516d9f3e`)*
  - 📄 **`Comissoes-2025.csv`** *(ID: `89ae9787-e943-4795-99e3-cc658e9aa9a5`)*
  - 📄 **`Comissoes-2026.csv`** *(ID: `e5a22c7e-6db9-42ba-bc65-903b0c96d9c3`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `DataFim` ➔ Nulos: **6.71%** (1106 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3170** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  2. `DataInicio` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3221** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  3. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 21, Tam Média: 7.91, DesvPad Tam: 3.68]

  4. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16481** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 63930.0, Média: 42874.9, Mediana: 43837.0, DesvPad: 14627.44]

  5. `Nome` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2188** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 63, Tam Média: 24.24, DesvPad Tam: 5.99]

  6. `Setor` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1021** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 127, Tam Média: 28.91, DesvPad Tam: 13.34]

  7. `Situacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 7, Tam Média: 5.41, DesvPad Tam: 0.81]

  8. `idContrato` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11747** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 79483.0, Média: 16125.49, Mediana: 11215.0, DesvPad: 15087.63]

---