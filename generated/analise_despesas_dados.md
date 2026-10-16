# Relatório de Análise Estrutural e Qualidade de Dados - CKAN

Este documento apresenta um resumo consolidado das bases de dados por período, evolução das colunas, métricas de qualidade e estatísticas numéricas consolidadas com marcação de alertas (Caso 1: Nulos/Zeros > 50 e Caso 2: Distintos > 50).

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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **428** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 121, Tam Média: 31.44, DesvPad Tam: 9.05]

  2. `AgenciaOrigem` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  3. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2004.0, Máx: 2013.0, Média: 2010.5, Mediana: 2011.0, DesvPad: 2.04]

  4. `AnoLicitacao` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  5. `BancoOrigem` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  6. `CargoFuncao` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  7. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.06, DesvPad Tam: 0.23]

  8. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **10.44%** (5829 zeros) | Distintos: **704** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 8684.0, Média: 2329.41, Mediana: 2530.0, DesvPad: 1696.65]

  9. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.06, Mediana: 3.0, DesvPad: 0.23]

  10. `CodigoConvenioConcedido` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  11. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  12. `CodigoDetalhamentoFonte` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  13. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **169** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 469092.0, Média: 36430.79, Mediana: 39.0, DesvPad: 107393.29]

  14. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **10.44%** (5829 zeros) | Distintos: **32** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 274.0, Média: 116.39, Mediana: 102.0, DesvPad: 63.61]

  15. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **10.44%** (5829 zeros) | Distintos: **39** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 28.0, Média: 13.5, Mediana: 12.0, DesvPad: 9.0]

  16. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **82.09%** (45829 zeros) | Distintos: **115** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2544.0, Média: 289.27, Mediana: 0.0, DesvPad: 620.86]

  17. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **10.44%** (5829 zeros) | Distintos: **42** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 60201.0, Média: 13309.61, Mediana: 1.0, DesvPad: 20797.42]

  18. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **18** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 46.0, Média: 6.13, Mediana: 3.0, DesvPad: 9.62]

  19. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **32** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 30.0, Máx: 4690.0, Média: 432.81, Mediana: 90.0, DesvPad: 1050.77]

  20. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **10.44%** (5829 zeros) | Distintos: **61** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 80000.0, Média: 44468.05, Mediana: 42000.0, DesvPad: 22305.67]

  21. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  22. `CodigoProcesso` ➔ Nulos: **6.66%** (3721 nulos) | Zeros: **10.44%** (5829 zeros) | Distintos: **12432** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 16, Tam Média: 8.36, DesvPad Tam: 2.8]

  23. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **10.44%** (5829 zeros) | Distintos: **153** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 905.0, Média: 600.33, Mediana: 800.0, DesvPad: 319.23]

  24. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **10.44%** (5829 zeros) | Distintos: **93** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 846.0, Média: 302.22, Mediana: 122.0, DesvPad: 283.65]

  25. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **10.44%** (5829 zeros) | Distintos: **654** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 46907126.0, Média: 30582041.33, Mediana: 33901414.0, DesvPad: 10703202.09]

  26. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.96%** (55804 zeros) | Distintos: **7** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 12.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.15]

  27. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **176** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 100101.0, Máx: 800103.0, Média: 480750.85, Mediana: 420101.0, DesvPad: 174382.64]

  28. `Contrato` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  29. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **10.44%** (5829 zeros) | Distintos: **8447** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 14, Tam Média: 12.27, DesvPad Tam: 3.97]

  30. `CredorRetencao` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  31. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1123** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  32. `DescricaoElementoDespesa` ➔ Nulos: **89.56%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 26, Tam Média: 26.0, DesvPad Tam: 0.0]

  33. `DescricaoEsfera` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  34. `DescricaoIdUso` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  35. `DetalhamentoFonte` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  36. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **28559** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  37. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19206** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  38. `DomicilioBancarioOrigem` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  39. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **86** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 49, Tam Média: 26.0, DesvPad Tam: 11.77]

  40. `Embasamento` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  41. `Emenda` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  42. `Esfera` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  43. `Favorecido` ➔ Nulos: **17.91%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7988** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 45, Tam Média: 28.91, DesvPad Tam: 8.43]

  44. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **21** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 48, Tam Média: 29.08, DesvPad Tam: 10.14]

  45. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 26, Tam Média: 14.3, DesvPad Tam: 6.26]

  46. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.42, DesvPad Tam: 2.8]

  47. `HistoricoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **25753** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 231, Tam Média: 114.82, DesvPad Tam: 57.7]

  48. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55829** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 196144748.0, Máx: 198860830.0, Média: 197394374.55, Mediana: 197561305.0, DesvPad: 1007512.23]

  49. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9603** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314692.0, Máx: 8390834.0, Média: 8332664.09, Mediana: 8332403.0, DesvPad: 13537.96]

  50. `IdUso` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **21** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 129, Tam Média: 23.13, DesvPad Tam: 14.31]

  52. `NomeCredorRetencao` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  53. `NomeTipoRetencao` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  54. `NumeroLicitacao` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  55. `NumeroProcesso` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  56. `Orgao` ➔ Nulos: **89.56%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 26, Tam Média: 26.0, DesvPad Tam: 0.0]

  57. `PlanoOrcamentario` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  58. `Processo` ➔ Nulos: **11.52%** (6431 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9624** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 293, Tam Média: 86.24, DesvPad Tam: 43.29]

  59. `ProcessoAssunto` ➔ Nulos: **21.96%** (12260 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **255** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 41, Tam Média: 10.15, DesvPad Tam: 5.03]

  60. `Programa` ➔ Nulos: **17.35%** (9688 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **130** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 14, Tam Máx: 121, Tam Média: 32.16, DesvPad Tam: 19.12]

  61. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **64** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 56, Tam Média: 22.42, DesvPad Tam: 5.8]

  62. `SubelementoDespesa` ➔ Nulos: **6.04%** (3370 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **369** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 45, Tam Média: 31.04, DesvPad Tam: 8.12]

  63. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 26, Tam Média: 8.09, DesvPad Tam: 6.12]

  64. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **10.44%** (5829 zeros) | Distintos: **8** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4.0, Média: 1.63, Mediana: 2.0, DesvPad: 0.83]

  65. `TipoLicitacao` ➔ Nulos: **10.44%** (5829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 52, Tam Média: 20.42, DesvPad Tam: 9.0]

  66. `TipoRetencao` ➔ Nulos: **100.0%** (55829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  67. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **170** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 2, Tam Máx: 81, Tam Média: 35.82, DesvPad Tam: 16.69]

  68. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **75.36%** (42071 zeros) | Distintos: **8919** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1959182420.08, Média: 656336.92, Mediana: 0.0, DesvPad: 19474022.16]

  69. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **48.88%** (27292 zeros) | Distintos: **17420** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -636274.17, Máx: 1959182420.08, Média: 641105.83, Mediana: 0.0, DesvPad: 19383870.86]

  70. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **57.93%** (32339 zeros) | Distintos: **17513** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -35000000.0, Máx: 1945104598.71, Média: 619057.61, Mediana: 0.0, DesvPad: 19072021.75]

  71. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **97.81%** (54609 zeros) | Distintos: **1083** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -14450.0, Máx: 528590.0, Média: 268.6, Mediana: 0.0, DesvPad: 6795.14]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `AgenciaOrigem`, `AnoLicitacao`, `BancoOrigem`, `CargoFuncao`, `CodigoConvenioConcedido`, `CodigoConvenioRecebido`, `CodigoDetalhamentoFonte`, `CodigoPlanoOrcamentario`, `Contrato`, `CredorRetencao`, `DescricaoEsfera`, `DescricaoIdUso`, `DetalhamentoFonte`, `DomicilioBancarioOrigem`, `Embasamento`, `Emenda`, `Esfera`, `IdUso`, `NomeCredorRetencao`, `NomeTipoRetencao`, `NumeroLicitacao`, `NumeroProcesso`, `PlanoOrcamentario`, `TipoRetencao`

> - `DescricaoElementoDespesa`, `Orgao`


---
### 🔹 Período: 2013
- **Quantidade Total de Colunas:** `53`
  - *Colunas removidas/alteradas:* `AgenciaOrigem`, `AnoLicitacao`, `BancoOrigem`, `CodigoDetalhamentoFonte`, `Contrato`, `CredorRetencao`, `DescricaoEsfera`, `DescricaoIdUso`, `DetalhamentoFonte`, `DomicilioBancarioOrigem`, `Embasamento`, `Emenda`, `Esfera`, `IdUso`, `NomeCredorRetencao`, `NomeTipoRetencao`, `NumeroLicitacao`, `TipoRetencao`

**Arquivos Vinculados ao Período:**
  - 📄 **`Despesas-2013.csv`** *(ID: `a0401328-dc70-4b6b-9972-03ee47f37574`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **314** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 97, Tam Média: 33.84, DesvPad Tam: 9.75]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2013.0, Máx: 2013.0, Média: 2013.0, Mediana: 2013.0, DesvPad: 0.0]

  3. `CargoFuncao` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  4. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.04, DesvPad Tam: 0.2]

  5. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **504** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 9.0, Máx: 8684.0, Média: 3276.99, Mediana: 2718.0, DesvPad: 1560.35]

  6. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.04, Mediana: 3.0, DesvPad: 0.2]

  7. `CodigoConvenioConcedido` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  8. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  9. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **43** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 96.0, Média: 28.13, Mediana: 30.0, DesvPad: 17.83]

  10. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 273.0, Média: 133.7, Mediana: 102.0, DesvPad: 61.39]

  11. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 28.0, Média: 12.8, Mediana: 10.0, DesvPad: 6.87]

  12. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  13. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 60201.0, Média: 22896.29, Mediana: 31201.0, DesvPad: 20908.86]

  14. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 6.0, Média: 2.77, Mediana: 3.0, DesvPad: 0.73]

  15. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 40.0, Máx: 91.0, Média: 88.41, Mediana: 90.0, DesvPad: 8.06]

  16. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **53** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10000.0, Máx: 80000.0, Média: 38716.76, Mediana: 42000.0, DesvPad: 10728.31]

  17. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  18. `CodigoProcesso` ➔ Nulos: **12.79%** (1279 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4722** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 6060388102.0, Média: 62101632.97, Mediana: 60902108.0, DesvPad: 72479230.65]

  19. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **88** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 905.0, Média: 617.28, Mediana: 800.0, DesvPad: 263.36]

  20. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 61.0, Máx: 846.0, Média: 228.17, Mediana: 122.0, DesvPad: 153.79]

  21. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **344** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31900101.0, Máx: 46907122.0, Média: 34059147.88, Mediana: 33903005.0, DesvPad: 2301401.2]

  22. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (10000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  23. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **86** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 100101.0, Máx: 800103.0, Média: 384405.09, Mediana: 420101.0, DesvPad: 106483.29]

  24. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4102** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 14, Tam Média: 13.6, DesvPad Tam: 1.02]

  25. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **247** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  26. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  27. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6686** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  28. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3742** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  29. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **43** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 45, Tam Média: 28.55, DesvPad Tam: 13.44]

  30. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4129** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 45, Tam Média: 29.58, DesvPad Tam: 9.5]

  31. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 109, Tam Média: 25.4, DesvPad Tam: 15.84]

  32. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 21, Tam Média: 10.94, DesvPad Tam: 5.17]

  33. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.66, DesvPad Tam: 2.39]

  34. `HistoricoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7604** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 231, Tam Média: 113.43, DesvPad Tam: 47.86]

  35. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 339897548.0, Máx: 339907547.0, Média: 339902547.5, Mediana: 339902547.5, DesvPad: 2886.75]

  36. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4136** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314696.0, Máx: 8390839.0, Média: 8338988.98, Mediana: 8337865.5, DesvPad: 15660.01]

  37. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 129, Tam Média: 21.3, DesvPad Tam: 15.94]

  38. `NumeroProcesso` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  39. `Orgao` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  40. `PlanoOrcamentario` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  41. `Processo` ➔ Nulos: **14.64%** (1464 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4154** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 326, Tam Média: 88.54, DesvPad Tam: 43.16]

  42. `ProcessoAssunto` ➔ Nulos: **14.64%** (1464 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **189** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 42, Tam Média: 11.83, DesvPad Tam: 6.25]

  43. `Programa` ➔ Nulos: **0.1%** (10 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **84** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 149, Tam Média: 35.04, DesvPad Tam: 18.58]

  44. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 56, Tam Média: 23.69, DesvPad Tam: 8.24]

  45. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **310** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 45, Tam Média: 31.03, DesvPad Tam: 9.11]

  46. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 6, Tam Média: 6.0, DesvPad Tam: 0.0]

  47. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 4.0, Média: 1.71, Mediana: 2.0, DesvPad: 0.69]

  48. `TipoLicitacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 52, Tam Média: 21.53, DesvPad Tam: 9.22]

  49. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **86** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 89, Tam Média: 40.57, DesvPad Tam: 16.37]

  50. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **85.33%** (8533 zeros) | Distintos: **778** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 31928740.13, Média: 13945.84, Mediana: 0.0, DesvPad: 370470.14]

  51. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **52.03%** (5203 zeros) | Distintos: **2841** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -18667205.82, Máx: 27291231.23, Média: 22826.64, Mediana: 0.0, DesvPad: 496073.15]

  52. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **66.73%** (6673 zeros) | Distintos: **2128** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -614534.48, Máx: 19658992.03, Média: 15264.41, Mediana: 0.0, DesvPad: 283680.82]

  53. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **95.91%** (9591 zeros) | Distintos: **370** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2102306.91, Média: 1349.28, Mediana: 0.0, DesvPad: 28487.2]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `CargoFuncao`, `CodigoConvenioConcedido`, `CodigoConvenioRecebido`, `CodigoPlanoOrcamentario`, `DescricaoElementoDespesa`, `NumeroProcesso`, `Orgao`, `PlanoOrcamentario`

> - `CodigoFuncionalProgramatica`, `CodigoSubtitulo`


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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1149** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 178, Tam Média: 48.31, DesvPad Tam: 20.26]

  2. `AgenciaOrigem` ➔ Nulos: **82.08%** (106698 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 51.0, Máx: 3665.0, Média: 876.68, Mediana: 675.0, DesvPad: 872.34]

  3. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2014.0, Máx: 2026.0, Média: 2020.0, Mediana: 2020.0, DesvPad: 3.74]

  4. `AnoLicitacao` ➔ Nulos: **53.85%** (70000 nulos) | Zeros: **37.7%** (49010 zeros) | Distintos: **26** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2026.0, Média: 370.43, Mediana: 0.0, DesvPad: 782.39]

  5. `BancoOrigem` ➔ Nulos: **82.08%** (106698 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 104.0, Média: 19.45, Mediana: 21.0, DesvPad: 6.83]

  6. `CargoFuncao` ➔ Nulos: **100.0%** (130000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  7. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.04, DesvPad Tam: 0.18]

  8. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1261** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 8684.0, Média: 2471.77, Mediana: 2128.0, DesvPad: 1311.53]

  9. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.04, Mediana: 3.0, DesvPad: 0.18]

  10. `CodigoConvenioConcedido` ➔ Nulos: **53.52%** (69581 nulos) | Zeros: **46.05%** (59862 zeros) | Distintos: **327** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 260760.0, Média: 2020.49, Mediana: 0.0, DesvPad: 21202.55]

  11. `CodigoConvenioRecebido` ➔ Nulos: **99.68%** (129581 nulos) | Zeros: **0.32%** (419 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  12. `CodigoDetalhamentoFonte` ➔ Nulos: **53.85%** (70000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **317** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.000113, Média: 409.97, Mediana: 500.0, DesvPad: 203.59]

  13. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **102** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 96.0, Média: 33.21, Mediana: 33.0, DesvPad: 22.82]

  14. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **170** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.0, Média: 273.25, Mediana: 142.0, DesvPad: 200.7]

  15. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 28.0, Média: 10.82, Mediana: 10.0, DesvPad: 6.43]

  16. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (130000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  17. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **128** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 60201.0, Média: 23609.9, Mediana: 28203.0, DesvPad: 21850.26]

  18. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 6.0, Média: 2.6, Mediana: 3.0, DesvPad: 0.87]

  19. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 20.0, Máx: 95.0, Média: 88.71, Mediana: 90.0, DesvPad: 7.47]

  20. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **58** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 80.0, Média: 36.78, Mediana: 44.0, DesvPad: 14.94]

  21. `CodigoPlanoOrcamentario` ➔ Nulos: **99.68%** (129581 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 1821.0, Máx: 1821.0, Média: 1821.0, Mediana: 1821.0, DesvPad: 0.0]

  22. `CodigoProcesso` ➔ Nulos: **0.07%** (94 nulos) | Zeros: **0.06%** (78 zeros) | Distintos: **61498** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 16, Tam Média: 10.16, DesvPad Tam: 2.19]

  23. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **229** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9999.0, Média: 269.79, Mediana: 53.0, DesvPad: 357.71]

  24. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **152** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31.0, Máx: 846.0, Média: 232.98, Mediana: 126.0, DesvPad: 159.8]

  25. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.04%** (55 zeros) | Distintos: **1592** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5897.0, Média: 3044.87, Mediana: 2742.0, DesvPad: 949.58]

  26. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **76.7%** (99705 zeros) | Distintos: **22** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 59.0, Média: 12.32, Mediana: 0.0, DesvPad: 22.42]

  27. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **249** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 366894.28, Mediana: 440901.0, DesvPad: 149419.08]

  28. `Contrato` ➔ Nulos: **53.85%** (70000 nulos) | Zeros: **33.46%** (43501 zeros) | Distintos: **6679** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 26004520.0, Média: 5915726.51, Mediana: 0.0, DesvPad: 9702021.01]

  29. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **21089** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 14, Tam Média: 12.17, DesvPad Tam: 3.36]

  30. `CredorRetencao` ➔ Nulos: **95.55%** (124210 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **515** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 191.0, Máx: 92872100000126.0, Média: 15799830507556.4, Mediana: 6641196000128.0, DesvPad: 17628806409524.21]

  31. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3364** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  32. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (130000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  33. `DescricaoEsfera` ➔ Nulos: **92.31%** (120000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 30, Tam Média: 20.08, DesvPad Tam: 6.36]

  34. `DescricaoIdUso` ➔ Nulos: **53.85%** (70000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 21, Tam Máx: 95, Tam Média: 33.14, DesvPad Tam: 4.2]

  35. `DetalhamentoFonte` ➔ Nulos: **53.85%** (70000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **282** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 197, Tam Média: 44.95, DesvPad Tam: 28.82]

  36. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **92955** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  37. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **35599** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  38. `DomicilioBancarioOrigem` ➔ Nulos: **82.08%** (106698 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **251** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 10, Tam Média: 8.3, DesvPad Tam: 1.44]

  39. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **99** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 120, Tam Média: 32.35, DesvPad Tam: 14.25]

  40. `Embasamento` ➔ Nulos: **53.85%** (70000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4971** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 243, Tam Média: 50.99, DesvPad Tam: 19.37]

  41. `Emenda` ➔ Nulos: **99.86%** (129813 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **179** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 12, Tam Média: 12.0, DesvPad Tam: 0.0]

  42. `Esfera` ➔ Nulos: **53.85%** (70000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 20.0, Média: 13.15, Mediana: 10.0, DesvPad: 4.65]

  43. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **22854** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 104, Tam Média: 33.82, DesvPad Tam: 13.78]

  44. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **174** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 150, Tam Média: 42.99, DesvPad Tam: 29.1]

  45. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **25** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 21, Tam Média: 12.07, DesvPad Tam: 5.56]

  46. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.8, DesvPad Tam: 2.27]

  47. `HistoricoDocumento` ➔ Nulos: **10.26%** (13343 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **101139** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 1024, Tam Média: 178.18, DesvPad Tam: 122.07]

  48. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **130000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 199445987.0, Máx: 218210599.0, Média: 204609728.88, Mediana: 203401004.5, DesvPad: 4804154.12]

  49. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26215** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314695.0, Máx: 8431649.0, Média: 8362421.63, Mediana: 8369959.0, DesvPad: 27904.04]

  50. `IdUso` ➔ Nulos: **53.85%** (70000 nulos) | Zeros: **15.36%** (19968 zeros) | Distintos: **5** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 6.0, Média: 0.72, Mediana: 1.0, DesvPad: 0.56]

  51. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 129, Tam Média: 21.92, DesvPad Tam: 18.43]

  52. `NomeCredorRetencao` ➔ Nulos: **95.55%** (124210 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **533** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 97, Tam Média: 31.06, DesvPad Tam: 13.92]

  53. `NomeTipoRetencao` ➔ Nulos: **95.55%** (124210 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **98** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 100, Tam Média: 36.53, DesvPad Tam: 17.56]

  54. `NumeroLicitacao` ➔ Nulos: **53.86%** (70018 nulos) | Zeros: **39.37%** (51186 zeros) | Distintos: **1656** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 15, Tam Média: 4.11, DesvPad Tam: 2.0]

  55. `NumeroProcesso` ➔ Nulos: **99.68%** (129581 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 58329617.0, Máx: 2020024240778.0, Média: 1764989131689.9, Mediana: 2020015997619.0, DesvPad: 670233541401.92]

  56. `Orgao` ➔ Nulos: **100.0%** (130000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  57. `PlanoOrcamentario` ➔ Nulos: **99.68%** (129581 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 22, Tam Média: 22.0, DesvPad Tam: 0.0]

  58. `Processo` ➔ Nulos: **63.56%** (82631 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **17169** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 473, Tam Média: 99.79, DesvPad Tam: 52.44]

  59. `ProcessoAssunto` ➔ Nulos: **63.55%** (82621 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **375** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 100, Tam Média: 12.59, DesvPad Tam: 5.91]

  60. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **185** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 149, Tam Média: 34.36, DesvPad Tam: 20.81]

  61. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **81** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 51, Tam Média: 23.93, DesvPad Tam: 8.37]

  62. `SubelementoDespesa` ➔ Nulos: **0.04%** (53 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1183** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 200, Tam Média: 42.42, DesvPad Tam: 21.34]

  63. `Subtitulo` ➔ Nulos: **15.38%** (20000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 16, Tam Média: 7.33, DesvPad Tam: 2.6]

  64. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 4.0, Média: 1.93, Mediana: 2.0, DesvPad: 0.72]

  65. `TipoLicitacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **29** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 70, Tam Média: 20.04, DesvPad Tam: 9.46]

  66. `TipoRetencao` ➔ Nulos: **95.55%** (124210 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **88** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 387.0, Média: 77.44, Mediana: 61.0, DesvPad: 84.73]

  67. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **153** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 42.63, DesvPad Tam: 15.82]

  68. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **83.3%** (108287 zeros) | Distintos: **10390** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -1909489066.2, Máx: 273806631.0, Média: 10987.57, Mediana: 0.0, DesvPad: 5541550.59]

  69. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **58.48%** (76019 zeros) | Distintos: **33937** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -103912215.18, Máx: 83011565.75, Média: 18174.25, Mediana: 0.0, DesvPad: 683627.89]

  70. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **59.73%** (77645 zeros) | Distintos: **33573** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -3275961.26, Máx: 53000000.0, Média: 22651.35, Mediana: 0.0, DesvPad: 421071.45]

  71. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **98.5%** (128049 zeros) | Distintos: **1747** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -424702.95, Máx: 17049985.54, Média: 853.57, Mediana: 0.0, DesvPad: 65897.13]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `CargoFuncao`, `DescricaoElementoDespesa`, `Orgao`


---

## 📂 Grupo Principal: `Despesas-_Semestre`

### 🔹 Período: 2024
- **Quantidade Total de Colunas:** `62`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Despesas-2024_1Semestre.csv`** *(ID: `99de03cc-6bf8-489d-81a4-4bd5e7351975`)*
  - 📄 **`Despesas-2024_2Semestre.csv`** *(ID: `5d2b16c5-fb9e-48da-b9f4-76de88951227`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **267** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 159, Tam Média: 44.48, DesvPad Tam: 18.46]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2024.0, Máx: 2024.0, Média: 2024.0, Mediana: 2024.0, DesvPad: 0.0]

  3. `AnoLicitacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **71.34%** (14269 zeros) | Distintos: **21** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2323.0, Média: 579.37, Mediana: 0.0, DesvPad: 914.41]

  4. `CargoFuncao` ➔ Nulos: **100.0%** (20000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  5. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.04, DesvPad Tam: 0.19]

  6. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **274** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 8683.0, Média: 2301.0, Mediana: 2136.0, DesvPad: 1016.47]

  7. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.04, Mediana: 3.0, DesvPad: 0.19]

  8. `CodigoConvenioConcedido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.76%** (19952 zeros) | Distintos: **36** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 240748.0, Média: 512.21, Mediana: 0.0, DesvPad: 10785.58]

  9. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (20000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  10. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **121** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.00011, Média: 534.64, Mediana: 500.1001, DesvPad: 80.87]

  11. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **51** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 96.0, Média: 34.84, Mediana: 36.0, DesvPad: 22.72]

  12. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **41** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 534.6, Mediana: 500.0, DesvPad: 80.87]

  13. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 28.0, Média: 10.64, Mediana: 10.0, DesvPad: 6.32]

  14. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (20000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  15. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **53** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 60201.0, Média: 22004.28, Mediana: 22901.0, DesvPad: 21946.83]

  16. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 6.0, Média: 2.75, Mediana: 3.0, DesvPad: 0.75]

  17. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 40.0, Máx: 92.0, Média: 88.64, Mediana: 90.0, DesvPad: 7.69]

  18. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **29** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 80.0, Média: 36.82, Mediana: 44.0, DesvPad: 15.15]

  19. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (20000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  20. `CodigoProcesso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.01%** (1 zeros) | Distintos: **11504** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 2, Tam Máx: 15, Tam Média: 10.66, DesvPad Tam: 1.78]

  21. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **53** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 1000.0, Média: 142.62, Mediana: 53.0, DesvPad: 233.2]

  22. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31.0, Máx: 846.0, Média: 252.84, Mediana: 181.0, DesvPad: 173.42]

  23. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **618** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1721.0, Máx: 5820.0, Média: 3174.71, Mediana: 2770.0, DesvPad: 1050.42]

  24. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **79.12%** (15825 zeros) | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 59.0, Média: 11.06, Mediana: 0.0, DesvPad: 21.59]

  25. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **111** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 366842.16, Mediana: 440901.0, DesvPad: 151643.48]

  26. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6370** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 14, Tam Média: 12.74, DesvPad Tam: 2.91]

  27. `CredorRetencao` ➔ Nulos: **87.43%** (17486 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **342** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 30901.0, Máx: 92872100000126.0, Média: 12576233328147.48, Mediana: 800102.0, DesvPad: 17220868399048.52]

  28. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **288** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  29. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (20000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  30. `DetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **109** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 185, Tam Média: 56.0, DesvPad Tam: 28.93]

  31. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13604** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  32. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5189** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  33. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **51** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 120, Tam Média: 29.78, DesvPad Tam: 12.74]

  34. `Embasamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1451** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 248, Tam Média: 47.78, DesvPad Tam: 20.99]

  35. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6419** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 100, Tam Média: 33.4, DesvPad Tam: 12.99]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **41** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 141, Tam Média: 42.41, DesvPad Tam: 26.2]

  37. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 21, Tam Média: 11.89, DesvPad Tam: 5.62]

  38. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.68, DesvPad Tam: 2.37]

  39. `HistoricoDocumento` ➔ Nulos: **17.09%** (3419 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **15028** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 1146, Tam Média: 216.86, DesvPad Tam: 138.98]

  40. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **20000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1906764725.0, Máx: 1906785089.0, Média: 1906774726.75, Mediana: 1906774724.5, DesvPad: 5777.41]

  41. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6442** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314695.0, Máx: 8424969.0, Média: 8370452.17, Mediana: 8371818.0, DesvPad: 31112.12]

  42. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 129, Tam Média: 21.4, DesvPad Tam: 16.79]

  43. `NomeCredorRetencao` ➔ Nulos: **87.43%** (17486 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **341** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 97, Tam Média: 29.7, DesvPad Tam: 12.72]

  44. `NomeTipoRetencao` ➔ Nulos: **87.43%** (17486 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **57** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 94, Tam Média: 36.62, DesvPad Tam: 17.18]

  45. `NumeroLicitacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **77.58%** (15516 zeros) | Distintos: **942** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 15, Tam Média: 4.35, DesvPad Tam: 2.9]

  46. `NumeroProcesso` ➔ Nulos: **100.0%** (20000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Orgao` ➔ Nulos: **100.0%** (20000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `PlanoOrcamentario` ➔ Nulos: **100.0%** (20000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  49. `Processo` ➔ Nulos: **98.89%** (19778 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **48** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 238, Tam Média: 128.37, DesvPad Tam: 55.97]

  50. `ProcessoAssunto` ➔ Nulos: **98.89%** (19778 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 36, Tam Média: 18.01, DesvPad Tam: 5.74]

  51. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **53** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 111, Tam Média: 31.62, DesvPad Tam: 22.13]

  52. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 48, Tam Média: 23.95, DesvPad Tam: 8.75]

  53. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **673** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 184, Tam Média: 43.9, DesvPad Tam: 21.1]

  54. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 16, Tam Média: 7.13, DesvPad Tam: 2.43]

  55. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 4.0, Média: 1.83, Mediana: 2.0, DesvPad: 0.68]

  56. `TipoLicitacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 70, Tam Média: 21.6, DesvPad Tam: 9.1]

  57. `TipoRetencao` ➔ Nulos: **87.43%** (17486 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **57** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 380.0, Média: 83.15, Mediana: 79.0, DesvPad: 81.68]

  58. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **110** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 40.99, DesvPad Tam: 15.02]

  59. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **84.47%** (16893 zeros) | Distintos: **1638** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -28532613.28, Máx: 126639121.0, Média: 34025.21, Mediana: 0.0, DesvPad: 1225401.9]

  60. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **53.08%** (10615 zeros) | Distintos: **6094** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -75276486.29, Máx: 95113946.02, Média: 7546.63, Mediana: 0.0, DesvPad: 934193.61]

  61. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **65.12%** (13024 zeros) | Distintos: **5272** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -6820523.21, Máx: 40955665.57, Média: 15421.0, Mediana: 0.0, DesvPad: 368196.31]

  62. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **97.34%** (19468 zeros) | Distintos: **506** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -304482.2, Máx: 2724286.5, Média: 1140.3, Mediana: 0.0, DesvPad: 28521.73]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `CargoFuncao`, `CodigoConvenioRecebido`, `CodigoPlanoOrcamentario`, `DescricaoElementoDespesa`, `NumeroProcesso`, `Orgao`, `PlanoOrcamentario`


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

  1. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **17** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2008.0, Máx: 2024.0, Média: 2023.71, Mediana: 2024.0, DesvPad: 1.07]

  2. `CodigoElemento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **82** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 319001.0, Máx: 459065.0, Média: 357532.22, Mediana: 339039.0, DesvPad: 42690.08]

  3. `CodigoPoder` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 6.0, Média: 4.8, Mediana: 5.0, DesvPad: 0.82]

  4. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **109** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 367064.84, Mediana: 420101.0, DesvPad: 130599.32]

  5. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5221** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 14, Tam Média: 13.16, DesvPad Tam: 1.77]

  6. `Elemento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **47** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 120, Tam Média: 33.86, DesvPad Tam: 15.52]

  7. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5185** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 100, Tam Média: 33.71, DesvPad Tam: 12.6]

  8. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9857** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9857.0, Média: 4929.17, Mediana: 4929.5, DesvPad: 2845.37]

  9. `Poder` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 18, Tam Média: 15.11, DesvPad Tam: 0.44]

  10. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **108** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 23, Tam Média: 5.37, DesvPad Tam: 2.65]

  11. `ValorNaoProcessado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **91.99%** (9068 zeros) | Distintos: **745** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 13436140.61, Média: 23437.07, Mediana: 0.0, DesvPad: 310201.92]

  12. `ValorNaoProcessadoLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **97.83%** (9644 zeros) | Distintos: **206** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 14171155.0, Média: 4933.26, Mediana: 0.0, DesvPad: 156022.82]

  13. `ValorProcessado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **90.19%** (8891 zeros) | Distintos: **865** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 21300000.0, Média: 9973.25, Mediana: 0.0, DesvPad: 240928.98]

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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **864** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 178, Tam Média: 51.09, DesvPad Tam: 27.18]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2014.0, Máx: 2026.0, Média: 2020.94, Mediana: 2021.0, DesvPad: 3.51]

  3. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 23, Tam Média: 18.13, DesvPad Tam: 0.34]

  4. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1146** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9999.0, Média: 2365.69, Mediana: 2114.0, DesvPad: 1289.8]

  5. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 9.0, Média: 3.13, Mediana: 3.0, DesvPad: 0.34]

  6. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **108** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 99.0, Média: 37.14, Mediana: 36.0, DesvPad: 22.99]

  7. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (1 zeros) | Distintos: **150** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 899.0, Média: 319.16, Mediana: 271.0, DesvPad: 220.33]

  8. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **51** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 99.0, Média: 10.8, Mediana: 10.0, DesvPad: 7.28]

  9. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9.0, Média: 2.89, Mediana: 3.0, DesvPad: 0.79]

  10. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **28** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 20.0, Máx: 99.0, Média: 86.85, Mediana: 90.0, DesvPad: 11.5]

  11. `CodigoPlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1529** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 3546.0, Média: 493.01, Mediana: 1.0, DesvPad: 818.65]

  12. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **201** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9999.0, Média: 218.71, Mediana: 47.0, DesvPad: 453.3]

  13. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **152** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31.0, Máx: 999.0, Média: 257.12, Mediana: 128.0, DesvPad: 199.44]

  14. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **15.54%** (16202 zeros) | Distintos: **1549** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5896.0, Média: 2591.59, Mediana: 2552.0, DesvPad: 1420.05]

  15. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **249** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 990101.0, Média: 322271.09, Mediana: 350201.0, DesvPad: 174457.22]

  16. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **17.06%** (17789 zeros) | Distintos: **28079** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 14, Tam Média: 9.8, DesvPad Tam: 4.65]

  17. `DespesaEmpenhada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **30.62%** (31918 zeros) | Distintos: **37377** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1535385174.9, Média: 342857.23, Mediana: 806.97, DesvPad: 8677688.61]

  18. `DespesaLiquidada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **35.59%** (37106 zeros) | Distintos: **36654** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1535385174.9, Média: 322967.96, Mediana: 448.0, DesvPad: 8658099.78]

  19. `DespesaPaga` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **27.85%** (29031 zeros) | Distintos: **42166** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1535319679.62, Média: 332421.71, Mediana: 900.0, DesvPad: 8636134.98]

  20. `DotacaoAtualizada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **21.21%** (22108 zeros) | Distintos: **43786** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1535385174.9, Média: 426146.8, Mediana: 1710.85, DesvPad: 9455835.25]

  21. `DotacaoInicial` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **89.77%** (93588 zeros) | Distintos: **3444** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1689500621.0, Média: 366805.38, Mediana: 0.0, DesvPad: 10580773.89]

  22. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **59** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 120, Tam Média: 30.78, DesvPad Tam: 15.09]

  23. `Emenda` ➔ Nulos: **96.91%** (101028 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2031** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 12, Tam Média: 12.0, DesvPad Tam: 0.0]

  24. `Esfera` ➔ Nulos: **42.45%** (44250 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 20.0, Média: 11.34, Mediana: 10.0, DesvPad: 3.41]

  25. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (1 zeros) | Distintos: **25727** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 100, Tam Média: 27.1, DesvPad Tam: 15.66]

  26. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **123** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 140, Tam Média: 32.09, DesvPad Tam: 17.4]

  27. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 23, Tam Média: 13.96, DesvPad Tam: 5.17]

  28. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 23.53, DesvPad Tam: 4.13]

  29. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **104250** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 327967.0, Máx: 66999671.0, Média: 38118235.88, Mediana: 65199808.5, DesvPad: 32233920.84]

  30. `Microregiao` ➔ Nulos: **42.45%** (44250 nulos) | Zeros: **46.17%** (48129 zeros) | Distintos: **22** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 59.0, Média: 10.41, Mediana: 0.0, DesvPad: 21.01]

  31. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **17** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 129, Tam Média: 23.48, DesvPad Tam: 19.9]

  32. `Municipio` ➔ Nulos: **42.45%** (44250 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **79** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 320010.0, Máx: 999999.0, Média: 918074.17, Mediana: 999999.0, DesvPad: 221295.03]

  33. `NomeEsfera` ➔ Nulos: **42.45%** (44250 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 30, Tam Média: 17.88, DesvPad Tam: 4.77]

  34. `NomeMicroregiao` ➔ Nulos: **42.45%** (44250 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 16, Tam Média: 7.11, DesvPad Tam: 2.47]

  35. `NomeMunicipio` ➔ Nulos: **42.45%** (44250 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **79** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 23, Tam Média: 4.81, DesvPad Tam: 2.84]

  36. `NomeUnidadeOrcamentaria` ➔ Nulos: **42.45%** (44250 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **104** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 127, Tam Média: 50.27, DesvPad Tam: 17.09]

  37. `PlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1451** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 191, Tam Média: 21.73, DesvPad Tam: 18.91]

  38. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **178** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 149, Tam Média: 39.54, DesvPad Tam: 22.58]

  39. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **88** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 62, Tam Média: 23.56, DesvPad Tam: 7.92]

  40. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1266** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 194, Tam Média: 40.43, DesvPad Tam: 24.42]

  41. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **154** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 47.17, DesvPad Tam: 15.44]

  42. `UnidadeOrcamentaria` ➔ Nulos: **42.45%** (44250 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **108** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1101.0, Máx: 80101.0, Média: 30256.87, Mediana: 31202.0, DesvPad: 16350.92]

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

  1. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **166** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 990101.0, Média: 370727.02, Mediana: 410202.0, DesvPad: 154861.25]

  2. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **18** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  3. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2066** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11452.0, Máx: 701139.0, Média: 349987.41, Mediana: 262741.5, DesvPad: 271450.85]

  4. `SiglaUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **204** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 90, Tam Média: 43.08, DesvPad Tam: 18.83]

  5. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **196** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 90, Tam Média: 45.13, DesvPad Tam: 17.48]

  6. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **12.58%** (260 zeros) | Distintos: **1807** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4788599153.95, Média: 148400530.72, Mediana: 14589310.094999999, DesvPad: 456837678.09]

  7. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **8.76%** (181 zeros) | Distintos: **1886** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4602955744.27, Média: 145198808.02, Mediana: 13982949.605, DesvPad: 446701875.47]

  8. `ValorOrcado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **1.98%** (41 zeros) | Distintos: **1988** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5426690790.98, Média: 180715626.54, Mediana: 23424071.405, DesvPad: 512446647.72]

  9. `ValorOrcadoInicial` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **3.97%** (82 zeros) | Distintos: **1904** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4351806442.0, Média: 154370221.81, Mediana: 18543344.0, DesvPad: 445060053.96]

  10. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **8.76%** (181 zeros) | Distintos: **1886** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4560087385.15, Média: 142446343.88, Mediana: 13483675.01, DesvPad: 439606208.25]

  11. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **32.09%** (663 zeros) | Distintos: **1403** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 484008397.04, Média: 6020168.42, Mediana: 384780.38, DesvPad: 26405502.19]

---

## 📂 Grupo Principal: `OrcamentosDespesaAssembleia-`

### 🔹 Período: 2021
- **Quantidade Total de Colunas:** `41`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`OrcamentosDespesaAssembleia-2021.csv`** *(ID: `dfe19849-50b5-482a-b766-2b1f0cb06a91`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **129** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 133, Tam Média: 47.71, DesvPad Tam: 23.98]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2021.0, Máx: 2021.0, Média: 2021.0, Mediana: 2021.0, DesvPad: 0.0]

  3. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 23, Tam Média: 18.14, DesvPad Tam: 0.34]

  4. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **131** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 9000.0, Média: 2285.14, Mediana: 2095.0, DesvPad: 1139.45]

  5. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 9.0, Média: 3.14, Mediana: 3.0, DesvPad: 0.35]

  6. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 99.0, Média: 38.85, Mediana: 37.0, DesvPad: 22.71]

  7. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.01%** (1 zeros) | Distintos: **30** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 675.0, Média: 179.04, Mediana: 101.0, DesvPad: 108.56]

  8. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 28.0, Média: 10.37, Mediana: 4.0, DesvPad: 8.93]

  9. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9.0, Média: 2.83, Mediana: 3.0, DesvPad: 0.85]

  10. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 40.0, Máx: 99.0, Média: 89.75, Mediana: 90.0, DesvPad: 3.73]

  11. `CodigoPlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **160** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 2297.0, Média: 288.3, Mediana: 1.0, DesvPad: 548.34]

  12. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **44** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 9999.0, Média: 253.46, Mediana: 38.0, DesvPad: 1057.52]

  13. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 32.0, Máx: 846.0, Média: 228.88, Mediana: 122.0, DesvPad: 227.24]

  14. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **15.82%** (1582 zeros) | Distintos: **477** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5396.0, Média: 2559.17, Mediana: 2695.0, DesvPad: 1360.16]

  15. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **48** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 20101.0, Máx: 370101.0, Média: 190615.49, Mediana: 220202.0, DesvPad: 116524.54]

  16. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **19.63%** (1963 zeros) | Distintos: **3047** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 97530084000107.0, Média: 10424203405202.79, Mediana: 53006260249.0, DesvPad: 16030335307082.46]

  17. `DespesaEmpenhada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **31.77%** (3177 zeros) | Distintos: **5167** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 255644449.76, Média: 225790.8, Mediana: 872.0, DesvPad: 3499844.67]

  18. `DespesaLiquidada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **37.69%** (3769 zeros) | Distintos: **4825** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 255644449.76, Média: 203945.83, Mediana: 429.205, DesvPad: 3478345.09]

  19. `DespesaPaga` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **32.15%** (3215 zeros) | Distintos: **5315** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 255644449.76, Média: 213255.65, Mediana: 797.5, DesvPad: 3495226.93]

  20. `DotacaoAtualizada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **19.51%** (1951 zeros) | Distintos: **6174** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 255644449.76, Média: 303335.76, Mediana: 2254.91, DesvPad: 4143350.19]

  21. `DotacaoInicial` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **88.42%** (8842 zeros) | Distintos: **618** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 271100000.0, Média: 237132.46, Mediana: 0.0, DesvPad: 4213481.54]

  22. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 120, Tam Média: 34.58, DesvPad Tam: 14.93]

  23. `Esfera` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  24. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3032** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 100, Tam Média: 27.89, DesvPad Tam: 16.69]

  25. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 84, Tam Média: 24.89, DesvPad Tam: 12.47]

  26. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 21, Tam Média: 13.01, DesvPad Tam: 3.21]

  27. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 23.55, DesvPad Tam: 4.16]

  28. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 7174323.0, Máx: 7184322.0, Média: 7179322.5, Mediana: 7179322.5, DesvPad: 2886.75]

  29. `Microregiao` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  30. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 129, Tam Média: 25.0, DesvPad Tam: 26.03]

  31. `Municipio` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  32. `NomeEsfera` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  33. `NomeMicroregiao` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  34. `NomeMunicipio` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  35. `NomeUnidadeOrcamentaria` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  36. `PlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **159** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 111, Tam Média: 18.13, DesvPad Tam: 14.17]

  37. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **44** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 91, Tam Média: 38.6, DesvPad Tam: 23.41]

  38. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 48, Tam Média: 21.5, DesvPad Tam: 7.05]

  39. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **461** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 184, Tam Média: 37.14, DesvPad Tam: 20.7]

  40. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 21, Tam Máx: 90, Tam Média: 50.56, DesvPad Tam: 16.47]

  41. `UnidadeOrcamentaria` ➔ Nulos: **100.0%** (10000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `Esfera`, `Microregiao`, `Municipio`, `NomeEsfera`, `NomeMicroregiao`, `NomeMunicipio`, `NomeUnidadeOrcamentaria`, `UnidadeOrcamentaria`


---