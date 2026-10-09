# Relatório de Análise Estrutural e Qualidade de Dados - CKAN

Este documento apresenta um resumo consolidado das bases de dados por período, evolução das colunas e métricas de qualidade consolidadas por período de tempo com marcação de alertas (Caso 1: Nulos/Zeros > 50 e Caso 2: Distintos > 50).

---

## 📂 Grupo Principal: `Despesas-`

### 🔹 Período: 2004 até 2013
- **Quantidade Total de Colunas:** `71`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Despesas-2004.csv`** *(ID: `8ffd4e6c-6e30-419d-9baa-921045caa22e`)*
  - 📄 **`Despesas-2005.csv`** *(ID: `cebd540a-95da-4774-a183-068a9397b944`)*
  - 📄 **`Despesas-2006.csv`** *(ID: `f931a6bc-a8da-49fd-adb6-291cc2c47b03`)*
  - 📄 **`Despesas-2007.csv`** *(ID: `294656bd-d840-4efd-afc7-3172c75892d9`)*
  - 📄 **`Despesas-2008.csv`** *(ID: `9c3ca5da-b821-43c9-ad4d-bf992935382c`)*
  - 📄 **`Despesas-2009.csv`** *(ID: `cf68f140-d077-4fe4-98fe-45232dc584a9`)*
  - 📄 **`Despesas-2010.csv`** *(ID: `55d2ab05-f8a7-41d2-9bb3-23a6b919e0b7`)*
  - 📄 **`Despesas-2011.csv`** *(ID: `732be7ee-8e04-4568-901d-800ec515f6ca`)*
  - 📄 **`Despesas-2012.csv`** *(ID: `152335dc-473d-481b-a61d-77cc4300ef5d`)*
  - 📄 **`Despesas-2013.csv`** *(ID: `a42b22d5-96bd-4778-8279-d1077cffb2a4`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**
  1. `Acao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **108** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  2. `AgenciaOrigem` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  3. `Ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  4. `AnoLicitacao` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  5. `BancoOrigem` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  6. `CargoFuncao` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  7. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  8. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **168** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  9. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  10. `CodigoConvenioConcedido` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  11. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  12. `CodigoDetalhamentoFonte` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  13. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **52** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  14. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **9** 🟢 [Enum]

  15. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **9** 🟢 [Enum]

  16. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **41** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  17. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11** 🟢 [Enum]

  18. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum]

  19. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **10** 🟢 [Enum]

  20. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **15** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  21. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  22. `CodigoProcesso` ➔ Nulos: **10.69%** (3208 nulos, 0 zeros) | Distintos: **3875** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  23. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **35** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  24. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **23** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  25. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **164** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  26. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  27. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **68** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  28. `Contrato` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  29. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2391** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  30. `CredorRetencao` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  31. `Data` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **125** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  32. `DescricaoElementoDespesa` ➔ Nulos: **50.0%** (15000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  33. `DescricaoEsfera` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  34. `DescricaoIdUso` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  35. `DetalhamentoFonte` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  36. `Documento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6532** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  37. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2909** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  38. `DomicilioBancarioOrigem` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  39. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **42** 🟢 [Enum]

  40. `Embasamento` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  41. `Emenda` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  42. `Esfera` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  43. `Favorecido` ➔ Nulos: **10.0%** (3000 nulos, 0 zeros) | Distintos: **1765** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  44. `Fonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **9** 🟢 [Enum]

  45. `Funcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **9** 🟢 [Enum]

  46. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum]

  47. `HistoricoDocumento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **10205** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  48. `Id` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **15582** ⚠️ [Caso 2: >50 Distintos]

  49. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2408** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  50. `IdUso` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Modalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **8** 🟢 [Enum]

  52. `NomeCredorRetencao` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  53. `NomeTipoRetencao` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  54. `NumeroLicitacao` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  55. `NumeroProcesso` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  56. `Orgao` ➔ Nulos: **50.0%** (15000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  57. `PlanoOrcamentario` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  58. `Processo` ➔ Nulos: **14.51%** (4351 nulos, 0 zeros) | Distintos: **2941** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  59. `ProcessoAssunto` ➔ Nulos: **64.51%** (4934 nulos, 0 zeros) | Distintos: **92** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  60. `Programa` ➔ Nulos: **1.99%** (597 nulos, 0 zeros) | Distintos: **30** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  61. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **23** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  62. `SubelementoDespesa` ➔ Nulos: **3.32%** (995 nulos, 0 zeros) | Distintos: **129** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  63. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  64. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  65. `TipoLicitacao` ➔ Nulos: **50.0%** (582 nulos, 0 zeros) | Distintos: **4** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  66. `TipoRetencao` ➔ Nulos: **100.0%** (15582 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  67. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **67** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  68. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1177** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  69. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1968** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  70. `ValorPago` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6470** ⚠️ [Caso 2: >50 Distintos]

  71. `ValorRap` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **42** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

---
### 🔹 Período: 2013
- **Quantidade Total de Colunas:** `53`
  - *Colunas removidas/alteradas:* `AgenciaOrigem`, `AnoLicitacao`, `BancoOrigem`, `CodigoDetalhamentoFonte`, `Contrato`, `CredorRetencao`, `DescricaoEsfera`, `DescricaoIdUso`, `DetalhamentoFonte`, `DomicilioBancarioOrigem`, `Embasamento`, `Emenda`, `Esfera`, `IdUso`, `NomeCredorRetencao`, `NomeTipoRetencao`, `NumeroLicitacao`, `TipoRetencao`

**Arquivos Vinculados ao Período:**
  - 📄 **`Despesas-2013.csv`** *(ID: `a0401328-dc70-4b6b-9972-03ee47f37574`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**
  1. `Acao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **400** ⚠️ [Caso 2: >50 Distintos]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  3. `CargoFuncao` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  4. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  5. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **649** ⚠️ [Caso 2: >50 Distintos]

  6. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  7. `CodigoConvenioConcedido` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  8. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  9. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **45** 🟢 [Enum]

  10. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **23** 🟢 [Enum]

  11. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **24** 🟢 [Enum]

  12. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  13. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **36** 🟢 [Enum]

  14. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6** 🟢 [Enum]

  15. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7** 🟢 [Enum]

  16. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  17. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  18. `CodigoProcesso` ➔ Nulos: **13.06%** (3917 nulos, 0 zeros) | Distintos: **11386** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  19. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **92** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  20. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  21. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **422** ⚠️ [Caso 2: >50 Distintos]

  22. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  23. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  24. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7866** ⚠️ [Caso 2: >50 Distintos]

  25. `Data` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **253** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  26. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  27. `Documento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **14324** ⚠️ [Caso 2: >50 Distintos]

  28. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6393** ⚠️ [Caso 2: >50 Distintos]

  29. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **45** 🟢 [Enum]

  30. `Favorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7964** ⚠️ [Caso 2: >50 Distintos]

  31. `Fonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **23** 🟢 [Enum]

  32. `Funcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **24** 🟢 [Enum]

  33. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6** 🟢 [Enum]

  34. `HistoricoDocumento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **23149** ⚠️ [Caso 2: >50 Distintos]

  35. `Id` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **30000** ⚠️ [Caso 2: >50 Distintos]

  36. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7984** ⚠️ [Caso 2: >50 Distintos]

  37. `Modalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7** 🟢 [Enum]

  38. `NumeroProcesso` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  39. `Orgao` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  40. `PlanoOrcamentario` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  41. `Processo` ➔ Nulos: **14.96%** (4487 nulos, 0 zeros) | Distintos: **9783** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  42. `ProcessoAssunto` ➔ Nulos: **14.96%** (4487 nulos, 0 zeros) | Distintos: **274** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  43. `Programa` ➔ Nulos: **0.1%** (30 nulos, 0 zeros) | Distintos: **87** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  44. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  45. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **373** ⚠️ [Caso 2: >50 Distintos]

  46. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  47. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **4** 🟢 [Enum]

  48. `TipoLicitacao` ➔ Nulos: **0.01%** (4 nulos, 0 zeros) | Distintos: **9** 🟢 [Enum]

  49. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  50. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1780** ⚠️ [Caso 2: >50 Distintos]

  51. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6377** ⚠️ [Caso 2: >50 Distintos]

  52. `ValorPago` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7766** ⚠️ [Caso 2: >50 Distintos]

  53. `ValorRap` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **770** ⚠️ [Caso 2: >50 Distintos]

---
### 🔹 Período: 2014 até 2026
- **Quantidade Total de Colunas:** `71`
  - *Colunas removidas/alteradas:* `AgenciaOrigem`, `AnoLicitacao`, `BancoOrigem`, `CodigoDetalhamentoFonte`, `Contrato`, `CredorRetencao`, `DescricaoEsfera`, `DescricaoIdUso`, `DetalhamentoFonte`, `DomicilioBancarioOrigem`, `Embasamento`, `Emenda`, `Esfera`, `IdUso`, `NomeCredorRetencao`, `NomeTipoRetencao`, `NumeroLicitacao`, `TipoRetencao`

**Arquivos Vinculados ao Período:**
  - 📄 **`Despesas-2014.csv`** *(ID: `5ddb74e2-73a7-40e4-bad0-6632bdbfc982`)*
  - 📄 **`Despesas-2015.csv`** *(ID: `3739e443-e01e-4eca-bd89-87e42aa50a9d`)*
  - 📄 **`Despesas-2016.csv`** *(ID: `f10178de-008f-4942-a249-89cdc172dd03`)*
  - 📄 **`Despesas-2017.csv`** *(ID: `22476243-8565-4649-bd4f-abd2cafbd144`)*
  - 📄 **`Despesas-2018.csv`** *(ID: `2c26fe9a-7d90-4c44-a3fb-68fcd5790800`)*
  - 📄 **`Despesas-2019.csv`** *(ID: `8f3e2097-d89e-4ac7-8f20-660ca9dbd75d`)*
  - 📄 **`Despesas-2020.csv`** *(ID: `19c1fe94-56e7-41e3-957f-46c3de28a2ab`)*
  - 📄 **`Despesas-2021.csv`** *(ID: `3f0d341b-7c09-4b4a-83b1-bdf5ae26ec13`)*
  - 📄 **`Despesas-2022.csv`** *(ID: `2dddb456-5481-43f7-ab09-5b0a0faa784f`)*
  - 📄 **`Despesas-2023.csv`** *(ID: `2c3328bd-329e-4db6-b742-630619b0dd65`)*
  - 📄 **`Despesas-2024.csv`** *(ID: `b34ae52a-a739-412a-9bab-80f53ba72f4f`)*
  - 📄 **`Despesas-2025.csv`** *(ID: `b9c229f8-884c-4fa6-85a9-15469172d6a8`)*
  - 📄 **`Despesas-2026.csv`** *(ID: `1d4a0ae2-5e0c-41d2-8e36-45e092afe109`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**
  1. `Acao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **273** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  2. `AgenciaOrigem` ➔ Nulos: **85.2%** (25559 nulos, 0 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  3. `Ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  4. `AnoLicitacao` ➔ Nulos: **53.85%** (16153 nulos, 0 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  5. `BancoOrigem` ➔ Nulos: **85.2%** (25559 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  6. `CargoFuncao` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  7. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  8. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **321** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  9. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  10. `CodigoConvenioConcedido` ➔ Nulos: **53.47%** (16040 nulos, 0 zeros) | Distintos: **70** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  11. `CodigoConvenioRecebido` ➔ Nulos: **99.62%** (29886 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  12. `CodigoDetalhamentoFonte` ➔ Nulos: **53.85%** (16153 nulos, 0 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  13. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **47** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  14. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **41** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  15. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **23** 🟢 [Enum]

  16. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  17. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **47** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  18. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum]

  19. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **9** 🟢 [Enum]

  20. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **27** 🟢 [Enum]

  21. `CodigoPlanoOrcamentario` ➔ Nulos: **99.62%** (29886 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  22. `CodigoProcesso` ➔ Nulos: **0.06%** (16 nulos, 17 zeros) | Distintos: **11985** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  23. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **64** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  24. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **63** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  25. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 57 zeros) | Distintos: **575** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  26. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos, 8583 zeros) | Distintos: **10** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  27. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **102** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  28. `Contrato` ➔ Nulos: **53.85%** (16153 nulos, 0 zeros) | Distintos: **1465** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  29. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6476** ⚠️ [Caso 2: >50 Distintos]

  30. `CredorRetencao` ➔ Nulos: **94.03%** (28209 nulos, 0 zeros) | Distintos: **177** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  31. `Data` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **274** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  32. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  33. `DescricaoEsfera` ➔ Nulos: **92.31%** (27692 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  34. `DescricaoIdUso` ➔ Nulos: **53.85%** (16153 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  35. `DetalhamentoFonte` ➔ Nulos: **53.85%** (16153 nulos, 0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  36. `Documento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **15076** ⚠️ [Caso 2: >50 Distintos]

  37. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5137** ⚠️ [Caso 2: >50 Distintos]

  38. `DomicilioBancarioOrigem` ➔ Nulos: **85.2%** (25559 nulos, 0 zeros) | Distintos: **52** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  39. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **47** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  40. `Embasamento` ➔ Nulos: **53.85%** (16153 nulos, 0 zeros) | Distintos: **945** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  41. `Emenda` ➔ Nulos: **99.87%** (29961 nulos, 0 zeros) | Distintos: **36** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  42. `Esfera` ➔ Nulos: **53.85%** (16153 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  43. `Favorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6535** ⚠️ [Caso 2: >50 Distintos]

  44. `Fonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **41** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  45. `Funcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **23** 🟢 [Enum]

  46. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum]

  47. `HistoricoDocumento` ➔ Nulos: **12.81%** (3842 nulos, 0 zeros) | Distintos: **21535** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  48. `Id` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **30000** ⚠️ [Caso 2: >50 Distintos]

  49. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6554** ⚠️ [Caso 2: >50 Distintos]

  50. `IdUso` ➔ Nulos: **53.85%** (16153 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Modalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **9** 🟢 [Enum]

  52. `NomeCredorRetencao` ➔ Nulos: **94.03%** (28209 nulos, 0 zeros) | Distintos: **176** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  53. `NomeTipoRetencao` ➔ Nulos: **94.03%** (28209 nulos, 0 zeros) | Distintos: **29** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  54. `NumeroLicitacao` ➔ Nulos: **53.85%** (16153 nulos, 0 zeros) | Distintos: **338** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  55. `NumeroProcesso` ➔ Nulos: **99.62%** (29886 nulos, 0 zeros) | Distintos: **19** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  56. `Orgao` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  57. `PlanoOrcamentario` ➔ Nulos: **99.62%** (29886 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  58. `Processo` ➔ Nulos: **65.89%** (19765 nulos, 0 zeros) | Distintos: **3431** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  59. `ProcessoAssunto` ➔ Nulos: **65.88%** (19763 nulos, 0 zeros) | Distintos: **129** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  60. `Programa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **64** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  61. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **63** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  62. `SubelementoDespesa` ➔ Nulos: **0.19%** (57 nulos, 0 zeros) | Distintos: **561** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  63. `Subtitulo` ➔ Nulos: **15.38%** (4615 nulos, 0 zeros) | Distintos: **9** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  64. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **4** 🟢 [Enum]

  65. `TipoLicitacao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **12** 🟢 [Enum]

  66. `TipoRetencao` ➔ Nulos: **94.03%** (28209 nulos, 0 zeros) | Distintos: **29** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  67. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **102** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  68. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3401** ⚠️ [Caso 2: >50 Distintos]

  69. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7697** ⚠️ [Caso 2: >50 Distintos]

  70. `ValorPago` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7612** ⚠️ [Caso 2: >50 Distintos]

  71. `ValorRap` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **484** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

---

## 📂 Grupo Principal: `Despesas-_Semestre`

### 🔹 Período: 2024
- **Quantidade Total de Colunas:** `62`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Despesas-2024_1Semestre.csv`** *(ID: `99de03cc-6bf8-489d-81a4-4bd5e7351975`)*
  - 📄 **`Despesas-2024_2Semestre.csv`** *(ID: `5d2b16c5-fb9e-48da-b9f4-76de88951227`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**
  1. `Acao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **268** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  3. `AnoLicitacao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **21** 🟢 [Enum]

  4. `CargoFuncao` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  5. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  6. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **275** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  7. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  8. `CodigoConvenioConcedido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **64** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  9. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  10. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **127** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  11. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **51** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  12. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **41** 🟢 [Enum]

  13. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **24** 🟢 [Enum]

  14. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  15. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **52** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  16. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6** 🟢 [Enum]

  17. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **9** 🟢 [Enum]

  18. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **29** 🟢 [Enum]

  19. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  20. `CodigoProcesso` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **14875** ⚠️ [Caso 2: >50 Distintos]

  21. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **53** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  22. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **68** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  23. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **651** ⚠️ [Caso 2: >50 Distintos]

  24. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11** 🟢 [Enum]

  25. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **110** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  26. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7698** ⚠️ [Caso 2: >50 Distintos]

  27. `CredorRetencao` ➔ Nulos: **88.17%** (26452 nulos, 0 zeros) | Distintos: **393** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  28. `Data` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **154** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  29. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  30. `DetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  31. `Documento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **17450** ⚠️ [Caso 2: >50 Distintos]

  32. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6205** ⚠️ [Caso 2: >50 Distintos]

  33. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **51** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  34. `Embasamento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1761** ⚠️ [Caso 2: >50 Distintos]

  35. `Favorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7774** ⚠️ [Caso 2: >50 Distintos]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **41** 🟢 [Enum]

  37. `Funcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **24** 🟢 [Enum]

  38. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **6** 🟢 [Enum]

  39. `HistoricoDocumento` ➔ Nulos: **16.25%** (4876 nulos, 0 zeros) | Distintos: **21569** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  40. `Id` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **30000** ⚠️ [Caso 2: >50 Distintos]

  41. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7801** ⚠️ [Caso 2: >50 Distintos]

  42. `Modalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **9** 🟢 [Enum]

  43. `NomeCredorRetencao` ➔ Nulos: **88.17%** (26452 nulos, 0 zeros) | Distintos: **392** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  44. `NomeTipoRetencao` ➔ Nulos: **88.17%** (26452 nulos, 0 zeros) | Distintos: **70** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  45. `NumeroLicitacao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1061** ⚠️ [Caso 2: >50 Distintos]

  46. `NumeroProcesso` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Orgao` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `PlanoOrcamentario` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  49. `Processo` ➔ Nulos: **99.03%** (29707 nulos, 0 zeros) | Distintos: **49** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  50. `ProcessoAssunto` ➔ Nulos: **99.02%** (29706 nulos, 0 zeros) | Distintos: **33** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Programa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **53** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  52. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **68** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  53. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **735** ⚠️ [Caso 2: >50 Distintos]

  54. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11** 🟢 [Enum]

  55. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **4** 🟢 [Enum]

  56. `TipoLicitacao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **15** 🟢 [Enum]

  57. `TipoRetencao` ➔ Nulos: **88.17%** (26452 nulos, 0 zeros) | Distintos: **70** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  58. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **109** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  59. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2510** ⚠️ [Caso 2: >50 Distintos]

  60. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **8397** ⚠️ [Caso 2: >50 Distintos]

  61. `ValorPago` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7710** ⚠️ [Caso 2: >50 Distintos]

  62. `ValorRap` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **694** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

---

## 📂 Grupo Principal: `RestosAPagar-`

### 🔹 Período: 2008 até 2024
- **Quantidade Total de Colunas:** `13`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`RestosAPagar-2008.csv`** *(ID: `21d56e8a-f3ff-4bc1-a05c-9775acf9688f`)*
  - 📄 **`RestosAPagar-2009.csv`** *(ID: `cf4c30ed-ad41-4d5e-8524-15697155b553`)*
  - 📄 **`RestosAPagar-2010.csv`** *(ID: `8397b492-ca60-4758-ae36-2375c4127642`)*
  - 📄 **`RestosAPagar-2011.csv`** *(ID: `f03c88c0-12fc-4cc1-8867-adc3b47f4bf1`)*
  - 📄 **`RestosAPagar-2012.csv`** *(ID: `2dd67530-0f73-4301-989a-e179e43bfba7`)*
  - 📄 **`RestosAPagar-2013.csv`** *(ID: `b6e0349d-cc05-4272-b94d-9de9b5434ef7`)*
  - 📄 **`RestosAPagar-2014.csv`** *(ID: `9b9961dc-4525-49f0-a7e3-977dee918860`)*
  - 📄 **`RestosAPagar-2015.csv`** *(ID: `08035275-3535-486b-a2d9-1804bf1c7698`)*
  - 📄 **`RestosAPagar-2016.csv`** *(ID: `f852ff54-05c8-4c3e-965e-67f4c09b94a5`)*
  - 📄 **`RestosAPagar-2017.csv`** *(ID: `aa434227-51a9-4601-ae06-b742754048de`)*
  - 📄 **`RestosAPagar-2018.csv`** *(ID: `f8692eaa-b24e-470b-a764-9b521c733724`)*
  - 📄 **`RestosAPagar-2019.csv`** *(ID: `342e19e8-9886-4e80-ab48-8165a9661366`)*
  - 📄 **`RestosAPagar-2020.csv`** *(ID: `d27c5214-55f3-49ca-97d9-e5a2635c226c`)*
  - 📄 **`RestosAPagar-2021.csv`** *(ID: `6158cc6d-60c0-48a4-ada4-475a447b45ff`)*
  - 📄 **`RestosAPagar-2022.csv`** *(ID: `b8c0555f-568c-405e-b709-4f8a535229f6`)*
  - 📄 **`RestosAPagar-2023.csv`** *(ID: `1a8cb467-c6d9-4ce2-8204-47735a96aa46`)*
  - 📄 **`RestosAPagar-2024.csv`** *(ID: `7a9d2ca0-73ff-49da-9429-11548b6d8e0c`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**
  1. `Ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  2. `CodigoElemento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **15** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  3. `CodigoPoder` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  4. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **19** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  5. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **333** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  6. `Elemento` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **11** 🟢 [Enum]

  7. `Favorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **331** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  8. `Id` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **579** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  9. `Poder` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  10. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **19** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  11. `ValorNaoProcessado` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **45** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  12. `ValorNaoProcessadoLiquidado` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **13** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  13. `ValorProcessado` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **54** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

---

## 📂 Grupo Principal: `OrcamentosDespesa-`

### 🔹 Período: 2014 até 2026
- **Quantidade Total de Colunas:** `42`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`OrcamentosDespesa-2014.csv`** *(ID: `52ac8415-4f9e-4eeb-98ca-3f7d3a82c61e`)*
  - 📄 **`OrcamentosDespesa-2015.csv`** *(ID: `eee1f2dd-bb89-4cd7-8381-3ccd2ed07a2f`)*
  - 📄 **`OrcamentosDespesa-2016.csv`** *(ID: `3878500a-9e36-4ce0-8885-4217e8a06bdf`)*
  - 📄 **`OrcamentosDespesa-2017.csv`** *(ID: `83728f6a-e5f0-4488-b7df-005be8c54678`)*
  - 📄 **`OrcamentosDespesa-2018.csv`** *(ID: `793641e2-0ae2-4aeb-8d45-59ca5624c10d`)*
  - 📄 **`OrcamentosDespesa-2019.csv`** *(ID: `38f8354b-55f6-4a30-9e6c-8c042cda8806`)*
  - 📄 **`OrcamentosDespesa-2020.csv`** *(ID: `f0795748-a647-4cae-a115-fa7bf8975de6`)*
  - 📄 **`OrcamentosDespesa-2021.csv`** *(ID: `e2c414b5-c8ca-424e-b8c6-84d6a4a9e587`)*
  - 📄 **`OrcamentosDespesa-2022.csv`** *(ID: `6f0cd160-1ed6-4a81-96b2-772f3dac8178`)*
  - 📄 **`OrcamentosDespesa-2023.csv`** *(ID: `f2130f41-c197-4686-a879-3d0f9f86df5c`)*
  - 📄 **`OrcamentosDespesa-2024.csv`** *(ID: `8aaabf6a-db45-4c9f-bd5d-9e4cb8a29b93`)*
  - 📄 **`OrcamentosDespesa-2025.csv`** *(ID: `c98132b7-a2ce-431f-be7b-1ba5998a62b9`)*
  - 📄 **`OrcamentosDespesa-2026.csv`** *(ID: `914959c5-867b-4800-bbfb-859a37bbb276`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**
  1. `Acao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **273** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  3. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  4. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **299** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  5. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **2** 🟢 [Enum]

  6. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **45** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  7. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **42** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  8. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **20** 🟢 [Enum]

  9. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum]

  10. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **10** 🟢 [Enum]

  11. `CodigoPlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **466** ⚠️ [Caso 2: >50 Distintos]

  12. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  13. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **58** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  14. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 3284 zeros) | Distintos: **527** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  15. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **68** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  16. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos, 3115 zeros) | Distintos: **7122** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  17. `DespesaEmpenhada` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **8539** ⚠️ [Caso 2: >50 Distintos]

  18. `DespesaLiquidada` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **8277** ⚠️ [Caso 2: >50 Distintos]

  19. `DespesaPaga` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **9494** ⚠️ [Caso 2: >50 Distintos]

  20. `DotacaoAtualizada` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **9917** ⚠️ [Caso 2: >50 Distintos]

  21. `DotacaoInicial` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **802** ⚠️ [Caso 2: >50 Distintos]

  22. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **45** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  23. `Emenda` ➔ Nulos: **98.11%** (20953 nulos, 0 zeros) | Distintos: **341** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  24. `Esfera` ➔ Nulos: **53.85%** (7673 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  25. `Favorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **7102** ⚠️ [Caso 2: >50 Distintos]

  26. `Fonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **42** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  27. `Funcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **20** 🟢 [Enum]

  28. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum]

  29. `Id` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **21519** ⚠️ [Caso 2: >50 Distintos]

  30. `Microregiao` ➔ Nulos: **53.85%** (7673 nulos, 5269 zeros) | Distintos: **5** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  31. `Modalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **10** 🟢 [Enum]

  32. `Municipio` ➔ Nulos: **53.85%** (7673 nulos, 0 zeros) | Distintos: **36** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  33. `NomeEsfera` ➔ Nulos: **53.85%** (7673 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  34. `NomeMicroregiao` ➔ Nulos: **53.85%** (7673 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  35. `NomeMunicipio` ➔ Nulos: **53.85%** (7673 nulos, 0 zeros) | Distintos: **36** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  36. `NomeUnidadeOrcamentaria` ➔ Nulos: **53.85%** (7673 nulos, 0 zeros) | Distintos: **36** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

  37. `PlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **463** ⚠️ [Caso 2: >50 Distintos]

  38. `Programa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  39. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **58** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  40. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **508** ⚠️ [Caso 2: >50 Distintos]

  41. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **67** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  42. `UnidadeOrcamentaria` ➔ Nulos: **53.85%** (7673 nulos, 0 zeros) | Distintos: **36** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos]

---

## 📂 Grupo Principal: `OrcamentosExecucoes-`

### 🔹 Período: 2009 até 2026
- **Quantidade Total de Colunas:** `11`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`OrcamentosExecucoes-2009.csv`** *(ID: `04435ede-cb77-49e4-9d8e-5a1a2963e50d`)*
  - 📄 **`OrcamentosExecucoes-2010.csv`** *(ID: `8708a152-7979-48d0-ac81-1ad16577e600`)*
  - 📄 **`OrcamentosExecucoes-2011.csv`** *(ID: `71c38c9a-2c7d-46cf-8787-1475f78cd41b`)*
  - 📄 **`OrcamentosExecucoes-2012.csv`** *(ID: `aa4a9bcc-cab8-4ce2-bb1b-f22c452c0d8b`)*
  - 📄 **`OrcamentosExecucoes-2013.csv`** *(ID: `30e5574c-29ce-439a-ae83-8e7f43488739`)*
  - 📄 **`OrcamentosExecucoes-2014.csv`** *(ID: `97ded727-29c6-499f-8da7-4f458ff64fd5`)*
  - 📄 **`OrcamentosExecucoes-2015.csv`** *(ID: `0f6249df-6df3-4c48-9546-edcf52495812`)*
  - 📄 **`OrcamentosExecucoes-2016.csv`** *(ID: `2f8e7519-e744-49b8-811f-91a8eb56017d`)*
  - 📄 **`OrcamentosExecucoes-2017.csv`** *(ID: `1d8ef0c7-0d86-4724-a435-317f2f97e290`)*
  - 📄 **`OrcamentosExecucoes-2018.csv`** *(ID: `508996c9-d7c7-4e3b-b1d6-57fe4cd5a27a`)*
  - 📄 **`OrcamentosExecucoes-2019.csv`** *(ID: `e56255b8-0a0f-4fa5-933b-0a20f3620572`)*
  - 📄 **`OrcamentosExecucoes-2020.csv`** *(ID: `f1928bac-a0b3-45ca-9fcc-65cb47f01577`)*
  - 📄 **`OrcamentosExecucoes-2021.csv`** *(ID: `6c0f83eb-da23-498c-9b51-ced911093159`)*
  - 📄 **`OrcamentosExecucoes-2022.csv`** *(ID: `9bd7cd97-e1dc-4a88-bf75-b7d751b8f9a4`)*
  - 📄 **`OrcamentosExecucoes-2023.csv`** *(ID: `00827698-d8da-40eb-8798-5fb3916e0f28`)*
  - 📄 **`OrcamentosExecucoes-2024.csv`** *(ID: `3b39753a-1b99-459b-9955-56b7449f810b`)*
  - 📄 **`OrcamentosExecucoes-2025.csv`** *(ID: `538b6477-dbc6-4183-9b73-adcc18867369`)*
  - 📄 **`OrcamentosExecucoes-2026.csv`** *(ID: `240f70ca-c810-442b-bade-bb0ea3280880`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**
  1. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **114** ⚠️ [Caso 2: >50 Distintos]

  2. `Data` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  3. `Id` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **114** ⚠️ [Caso 2: >50 Distintos]

  4. `SiglaUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **114** ⚠️ [Caso 2: >50 Distintos]

  5. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **114** ⚠️ [Caso 2: >50 Distintos]

  6. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **101** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  7. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **105** ⚠️ [Caso 2: >50 Distintos]

  8. `ValorOrcado` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **112** ⚠️ [Caso 2: >50 Distintos]

  9. `ValorOrcadoInicial` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **110** ⚠️ [Caso 2: >50 Distintos]

  10. `ValorPago` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **105** ⚠️ [Caso 2: >50 Distintos]

  11. `ValorRap` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **78** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

---

## 📂 Grupo Principal: `OrcamentosDespesaAssembleia-`

### 🔹 Período: 2021
- **Quantidade Total de Colunas:** `41`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`OrcamentosDespesaAssembleia-2021.csv`** *(ID: `dfe19849-50b5-482a-b766-2b1f0cb06a91`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**
  1. `Acao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **315** ⚠️ [Caso 2: >50 Distintos]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1** 🟢 [Enum]

  3. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  4. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **312** ⚠️ [Caso 2: >50 Distintos]

  5. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **3** 🟢 [Enum]

  6. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **49** 🟢 [Enum]

  7. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **71** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  8. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **23** 🟢 [Enum]

  9. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum]

  10. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **14** 🟢 [Enum]

  11. `CodigoPlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **615** ⚠️ [Caso 2: >50 Distintos]

  12. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  13. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  14. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **640** ⚠️ [Caso 2: >50 Distintos]

  15. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **79** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  16. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **8692** ⚠️ [Caso 2: >50 Distintos]

  17. `DespesaEmpenhada` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **14266** ⚠️ [Caso 2: >50 Distintos]

  18. `DespesaLiquidada` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **13729** ⚠️ [Caso 2: >50 Distintos]

  19. `DespesaPaga` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **14606** ⚠️ [Caso 2: >50 Distintos]

  20. `DotacaoAtualizada` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **16702** ⚠️ [Caso 2: >50 Distintos]

  21. `DotacaoInicial` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **1120** ⚠️ [Caso 2: >50 Distintos]

  22. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **49** 🟢 [Enum]

  23. `Esfera` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  24. `Favorecido` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **8649** ⚠️ [Caso 2: >50 Distintos]

  25. `Fonte` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **70** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  26. `Funcao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **23** 🟢 [Enum]

  27. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **5** 🟢 [Enum]

  28. `Id` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **30000** ⚠️ [Caso 2: >50 Distintos]

  29. `Microregiao` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  30. `Modalidade` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **14** 🟢 [Enum]

  31. `Municipio` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  32. `NomeEsfera` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  33. `NomeMicroregiao` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  34. `NomeMunicipio` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  35. `NomeUnidadeOrcamentaria` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  36. `PlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **614** ⚠️ [Caso 2: >50 Distintos]

  37. `Programa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  38. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  39. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **614** ⚠️ [Caso 2: >50 Distintos]

  40. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos, 0 zeros) | Distintos: **76** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos]

  41. `UnidadeOrcamentaria` ➔ Nulos: **100.0%** (30000 nulos, 0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

---