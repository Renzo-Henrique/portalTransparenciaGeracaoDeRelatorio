# Relatório de Análise Estrutural e Qualidade de Dados - CKAN

Este documento apresenta um resumo consolidado das bases de dados por período, evolução das colunas, métricas de qualidade e estatísticas numéricas consolidadas com marcação de alertas (Caso 1: Nulos/Zeros > 50 e Caso 2: Distintos > 50). Foram utilizados apenas `50000 registros por recurso`

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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **823** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 121, Tam Média: 36.94, DesvPad Tam: 12.03]

  2. `AgenciaOrigem` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  3. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2004.0, Máx: 2013.0, Média: 2010.89, Mediana: 2011.0, DesvPad: 1.59]

  4. `AnoLicitacao` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  5. `BancoOrigem` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  6. `CargoFuncao` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  7. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.03, DesvPad Tam: 0.18]

  8. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.28%** (5829 zeros) | Distintos: **1368** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 8684.0, Média: 2325.87, Mediana: 2380.0, DesvPad: 1721.03]

  9. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.03, Mediana: 3.0, DesvPad: 0.18]

  10. `CodigoConvenioConcedido` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  11. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  12. `CodigoDetalhamentoFonte` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  13. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **173** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 469092.0, Média: 7980.56, Mediana: 36.0, DesvPad: 52372.09]

  14. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.28%** (5829 zeros) | Distintos: **50** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 274.0, Média: 143.46, Mediana: 135.0, DesvPad: 66.41]

  15. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.28%** (5829 zeros) | Distintos: **38** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 28.0, Média: 14.65, Mediana: 10.0, DesvPad: 8.77]

  16. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **80.46%** (205829 zeros) | Distintos: **316** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 3426.0, Média: 330.78, Mediana: 0.0, DesvPad: 673.97]

  17. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.28%** (5829 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 60201.0, Média: 21877.65, Mediana: 1.0, DesvPad: 24497.95]

  18. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **18** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 46.0, Média: 3.5, Mediana: 3.0, DesvPad: 4.75]

  19. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **35** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 20.0, Máx: 4690.0, Média: 154.88, Mediana: 90.0, DesvPad: 512.72]

  20. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.28%** (5829 zeros) | Distintos: **68** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 80000.0, Média: 52505.33, Mediana: 46000.0, DesvPad: 19400.13]

  21. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  22. `CodigoProcesso` ➔ Nulos: **19.88%** (50866 nulos) | Zeros: **2.28%** (5841 zeros) | Distintos: **55937** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 17, Tam Média: 8.84, DesvPad Tam: 1.81]

  23. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.28%** (5829 zeros) | Distintos: **215** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 905.0, Média: 618.84, Mediana: 800.0, DesvPad: 289.58]

  24. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.28%** (5829 zeros) | Distintos: **105** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 846.0, Média: 382.43, Mediana: 302.0, DesvPad: 287.15]

  25. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.28%** (5829 zeros) | Distintos: **953** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 46907126.0, Média: 33105219.49, Mediana: 33901414.0, DesvPad: 5455238.34]

  26. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **92.7%** (237160 zeros) | Distintos: **13** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 12.0, Média: 0.35, Mediana: 0.0, DesvPad: 1.69]

  27. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **186** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 100101.0, Máx: 800103.0, Média: 531989.93, Mediana: 460101.0, DesvPad: 180303.88]

  28. `Contrato` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  29. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.28%** (5829 zeros) | Distintos: **21325** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 14, Tam Média: 13.14, DesvPad Tam: 2.19]

  30. `CredorRetencao` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  31. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1261** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  32. `DescricaoElementoDespesa` ➔ Nulos: **97.72%** (250000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 26, Tam Média: 26.0, DesvPad Tam: 0.0]

  33. `DescricaoEsfera` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  34. `DescricaoIdUso` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  35. `DetalhamentoFonte` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  36. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **98482** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  37. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **37912** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  38. `DomicilioBancarioOrigem` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  39. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **88** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 49, Tam Média: 27.55, DesvPad Tam: 12.5]

  40. `Embasamento` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  41. `Emenda` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  42. `Esfera` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  43. `Favorecido` ➔ Nulos: **19.54%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **15011** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 45, Tam Média: 26.63, DesvPad Tam: 9.02]

  44. `Fonte` ➔ Nulos: **0.0%** (11 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **31** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 109, Tam Média: 26.76, DesvPad Tam: 11.5]

  45. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 26, Tam Média: 14.1, DesvPad Tam: 5.87]

  46. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.75, DesvPad Tam: 2.12]

  47. `HistoricoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **125868** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 369, Tam Média: 108.3, DesvPad Tam: 58.42]

  48. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **255829** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 222029752.0, Máx: 244914830.0, Média: 239549386.49, Mediana: 243468546.0, DesvPad: 8652256.53]

  49. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26521** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314692.0, Máx: 8390866.0, Média: 8334275.55, Mediana: 8334656.0, DesvPad: 12118.94]

  50. `IdUso` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 129, Tam Média: 21.68, DesvPad Tam: 11.09]

  52. `NomeCredorRetencao` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  53. `NomeTipoRetencao` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  54. `NumeroLicitacao` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  55. `NumeroProcesso` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  56. `Orgao` ➔ Nulos: **97.72%** (250000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 26, Tam Média: 26.0, DesvPad Tam: 0.0]

  57. `PlanoOrcamentario` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  58. `Processo` ➔ Nulos: **28.23%** (72228 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **39807** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 483, Tam Média: 97.97, DesvPad Tam: 39.92]

  59. `ProcessoAssunto` ➔ Nulos: **30.51%** (78054 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **378** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 49, Tam Média: 11.58, DesvPad Tam: 4.94]

  60. `Programa` ➔ Nulos: **19.5%** (49890 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **197** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 149, Tam Média: 39.0, DesvPad Tam: 18.54]

  61. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **71** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 56, Tam Média: 25.46, DesvPad Tam: 7.8]

  62. `SubelementoDespesa` ➔ Nulos: **7.73%** (19785 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **483** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 45, Tam Média: 31.46, DesvPad Tam: 8.39]

  63. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 26, Tam Média: 6.94, DesvPad Tam: 3.41]

  64. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.28%** (5829 zeros) | Distintos: **9** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4.0, Média: 1.91, Mediana: 2.0, DesvPad: 0.7]

  65. `TipoLicitacao` ➔ Nulos: **2.28%** (5829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 52, Tam Média: 18.78, DesvPad Tam: 9.13]

  66. `TipoRetencao` ➔ Nulos: **100.0%** (255829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  67. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **195** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 2, Tam Máx: 89, Tam Média: 35.48, DesvPad Tam: 15.23]

  68. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **69.79%** (178542 zeros) | Distintos: **28934** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1959182420.08, Média: 172268.94, Mediana: 0.0, DesvPad: 9455935.42]

  69. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **76.14%** (194780 zeros) | Distintos: **31043** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -4170000.0, Máx: 1959182420.08, Média: 144598.86, Mediana: 0.0, DesvPad: 9061055.02]

  70. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **50.79%** (129930 zeros) | Distintos: **84055** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -101300429.43, Máx: 1945104598.71, Média: 160950.33, Mediana: 0.0, DesvPad: 8961743.4]

  71. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **98.92%** (253059 zeros) | Distintos: **2246** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -5842762.3, Máx: 6466420.62, Média: 398.08, Mediana: 0.0, DesvPad: 28325.34]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `AgenciaOrigem`, `AnoLicitacao`, `BancoOrigem`, `CargoFuncao`, `CodigoConvenioConcedido`, `CodigoConvenioRecebido`, `CodigoDetalhamentoFonte`, `CodigoPlanoOrcamentario`, `Contrato`, `CredorRetencao`, `DescricaoEsfera`, `DescricaoIdUso`, `DetalhamentoFonte`, `DomicilioBancarioOrigem`, `Embasamento`, `Emenda`, `Esfera`, `IdUso`, `NomeCredorRetencao`, `NomeTipoRetencao`, `NumeroLicitacao`, `NumeroProcesso`, `PlanoOrcamentario`, `TipoRetencao`

> - `DescricaoElementoDespesa`, `Orgao`


---
### 🔹 Período: 2013
- **Quantidade Total de Colunas:** `53`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`Despesas-2013.csv`** *(ID: `a0401328-dc70-4b6b-9972-03ee47f37574`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **448** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 97, Tam Média: 33.69, DesvPad Tam: 9.81]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2013.0, Máx: 2013.0, Média: 2013.0, Mediana: 2013.0, DesvPad: 0.0]

  3. `CargoFuncao` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  4. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.04, DesvPad Tam: 0.19]

  5. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **720** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 9.0, Máx: 8684.0, Média: 3234.65, Mediana: 2716.0, DesvPad: 1576.68]

  6. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.04, Mediana: 3.0, DesvPad: 0.19]

  7. `CodigoConvenioConcedido` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  8. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  9. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **46** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 96.0, Média: 27.82, Mediana: 30.0, DesvPad: 17.43]

  10. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **25** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 274.0, Média: 135.51, Mediana: 102.0, DesvPad: 63.31]

  11. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 28.0, Média: 12.73, Mediana: 10.0, DesvPad: 7.05]

  12. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  13. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **36** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 60201.0, Média: 23442.47, Mediana: 31201.0, DesvPad: 20969.6]

  14. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 6.0, Média: 2.75, Mediana: 3.0, DesvPad: 0.75]

  15. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 30.0, Máx: 95.0, Média: 88.48, Mediana: 90.0, DesvPad: 7.97]

  16. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10000.0, Máx: 80000.0, Média: 38293.06, Mediana: 42000.0, DesvPad: 11211.25]

  17. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  18. `CodigoProcesso` ➔ Nulos: **13.2%** (6599 nulos) | Zeros: **0.0%** (1 zeros) | Distintos: **16334** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 606910936285530.0, Média: 61050788830.44, Mediana: 60908084.0, DesvPad: 5825661465122.98]

  19. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **100** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 905.0, Média: 609.77, Mediana: 800.0, DesvPad: 262.21]

  20. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **65** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 61.0, Máx: 846.0, Média: 224.96, Mediana: 122.0, DesvPad: 156.47]

  21. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **455** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31900101.0, Máx: 46907126.0, Média: 34012674.1, Mediana: 33903007.0, DesvPad: 2262519.93]

  22. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (50000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  23. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 100101.0, Máx: 800103.0, Média: 380184.36, Mediana: 420101.0, DesvPad: 111218.77]

  24. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9994** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 14, Tam Média: 13.57, DesvPad Tam: 1.05]

  25. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **262** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  26. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  27. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **19445** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  28. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8441** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  29. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **46** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 45, Tam Média: 28.87, DesvPad Tam: 13.45]

  30. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10164** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 45, Tam Média: 29.56, DesvPad Tam: 9.53]

  31. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **25** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 109, Tam Média: 23.96, DesvPad Tam: 13.3]

  32. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 21, Tam Média: 11.21, DesvPad Tam: 5.22]

  33. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.7, DesvPad Tam: 2.32]

  34. `HistoricoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **37943** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 231, Tam Média: 109.98, DesvPad Tam: 47.42]

  35. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **50000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 339897548.0, Máx: 339947547.0, Média: 339922547.5, Mediana: 339922547.5, DesvPad: 14433.76]

  36. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10193** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314694.0, Máx: 8390841.0, Média: 8338891.72, Mediana: 8337536.0, DesvPad: 15856.8]

  37. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 129, Tam Média: 21.02, DesvPad Tam: 15.28]

  38. `NumeroProcesso` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  39. `Orgao` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  40. `PlanoOrcamentario` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  41. `Processo` ➔ Nulos: **15.12%** (7559 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13852** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 476, Tam Média: 88.58, DesvPad Tam: 43.51]

  42. `ProcessoAssunto` ➔ Nulos: **15.12%** (7559 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **313** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 49, Tam Média: 11.6, DesvPad Tam: 6.02]

  43. `Programa` ➔ Nulos: **0.24%** (119 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **95** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 149, Tam Média: 35.49, DesvPad Tam: 18.93]

  44. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **65** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 56, Tam Média: 23.75, DesvPad Tam: 8.14]

  45. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **400** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 45, Tam Média: 30.83, DesvPad Tam: 9.21]

  46. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 6, Tam Média: 6.0, DesvPad Tam: 0.0]

  47. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 4.0, Média: 1.74, Mediana: 2.0, DesvPad: 0.69]

  48. `TipoLicitacao` ➔ Nulos: **0.01%** (5 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 52, Tam Média: 21.28, DesvPad Tam: 9.28]

  49. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 89, Tam Média: 41.04, DesvPad Tam: 16.25]

  50. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **87.06%** (43529 zeros) | Distintos: **2868** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 472250380.94, Média: 24837.45, Mediana: 0.0, DesvPad: 2265741.15]

  51. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **60.27%** (30134 zeros) | Distintos: **10512** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -111779684.77, Máx: 114214829.48, Média: 28387.77, Mediana: 0.0, DesvPad: 1182556.35]

  52. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **55.73%** (27865 zeros) | Distintos: **12222** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -614534.48, Máx: 39404759.57, Média: 16005.57, Mediana: 0.0, DesvPad: 344208.75]

  53. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **96.94%** (48472 zeros) | Distintos: **1318** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -5842762.3, Máx: 2102306.91, Média: 722.57, Mediana: 0.0, DesvPad: 32965.86]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `CargoFuncao`, `CodigoConvenioConcedido`, `CodigoConvenioRecebido`, `CodigoPlanoOrcamentario`, `DescricaoElementoDespesa`, `NumeroProcesso`, `Orgao`, `PlanoOrcamentario`

> - `CodigoFuncionalProgramatica`, `CodigoSubtitulo`


---
### 🔹 Período: 2014 até 2026
- **Quantidade Total de Colunas:** `71`
  - *Colunas removidas/alteradas:* Nenhuma

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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1500** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 178, Tam Média: 47.93, DesvPad Tam: 20.41]

  2. `AgenciaOrigem` ➔ Nulos: **86.64%** (563169 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **32** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 3665.0, Média: 894.51, Mediana: 675.0, DesvPad: 895.75]

  3. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2014.0, Máx: 2026.0, Média: 2020.0, Mediana: 2020.0, DesvPad: 3.74]

  4. `AnoLicitacao` ➔ Nulos: **53.85%** (350000 nulos) | Zeros: **37.71%** (245099 zeros) | Distintos: **44** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2302.0, Média: 369.98, Mediana: 0.0, DesvPad: 782.03]

  5. `BancoOrigem` ➔ Nulos: **86.64%** (563169 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 104.0, Média: 19.3, Mediana: 21.0, DesvPad: 6.73]

  6. `CargoFuncao` ➔ Nulos: **100.0%** (650000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  7. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.04, DesvPad Tam: 0.19]

  8. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1579** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 8684.0, Média: 2494.19, Mediana: 2153.0, DesvPad: 1296.82]

  9. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.04, Mediana: 3.0, DesvPad: 0.19]

  10. `CodigoConvenioConcedido` ➔ Nulos: **53.45%** (347436 nulos) | Zeros: **46.1%** (299638 zeros) | Distintos: **1209** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 260752.0, Média: 2092.94, Mediana: 0.0, DesvPad: 21469.32]

  11. `CodigoConvenioRecebido` ➔ Nulos: **99.61%** (647436 nulos) | Zeros: **0.39%** (2564 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  12. `CodigoDetalhamentoFonte` ➔ Nulos: **53.85%** (350000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **418** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.000113, Média: 410.04, Mediana: 500.0, DesvPad: 202.15]

  13. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **105** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 98.0, Média: 33.56, Mediana: 36.0, DesvPad: 22.35]

  14. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **205** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.0, Média: 272.71, Mediana: 143.0, DesvPad: 200.24]

  15. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 28.0, Média: 11.04, Mediana: 10.0, DesvPad: 6.35]

  16. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (650000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  17. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **136** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 60201.0, Média: 23168.37, Mediana: 28203.0, DesvPad: 21803.05]

  18. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 6.0, Média: 2.64, Mediana: 3.0, DesvPad: 0.84]

  19. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **28** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 20.0, Máx: 95.0, Média: 88.25, Mediana: 90.0, DesvPad: 8.55]

  20. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **58** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 80.0, Média: 37.29, Mediana: 44.0, DesvPad: 14.35]

  21. `CodigoPlanoOrcamentario` ➔ Nulos: **99.61%** (647436 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 1821.0, Máx: 1821.0, Média: 1821.0, Mediana: 1821.0, DesvPad: 0.0]

  22. `CodigoProcesso` ➔ Nulos: **0.05%** (337 nulos) | Zeros: **0.06%** (393 zeros) | Distintos: **203087** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 17, Tam Média: 10.29, DesvPad Tam: 2.1]

  23. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **248** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9999.0, Média: 283.07, Mediana: 53.0, DesvPad: 385.69]

  24. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **159** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31.0, Máx: 846.0, Média: 236.54, Mediana: 128.0, DesvPad: 159.99]

  25. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.14%** (898 zeros) | Distintos: **1940** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5899.0, Média: 3058.03, Mediana: 2746.0, DesvPad: 970.06]

  26. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **76.98%** (500352 zeros) | Distintos: **22** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 59.0, Média: 12.17, Mediana: 0.0, DesvPad: 22.32]

  27. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **257** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 372161.55, Mediana: 440901.0, DesvPad: 143591.82]

  28. `Contrato` ➔ Nulos: **53.85%** (350000 nulos) | Zeros: **33.52%** (217884 zeros) | Distintos: **13969** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 26004714.0, Média: 5888076.95, Mediana: 0.0, DesvPad: 9687923.05]

  29. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **40614** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 14, Tam Média: 12.39, DesvPad Tam: 3.21]

  30. `CredorRetencao` ➔ Nulos: **95.83%** (622877 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1188** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 191.0, Máx: 97538270000192.0, Média: 14787865252520.21, Mediana: 1772939000137.0, DesvPad: 17555970052536.43]

  31. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3679** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  32. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (650000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  33. `DescricaoEsfera` ➔ Nulos: **92.31%** (600000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 30, Tam Média: 20.25, DesvPad Tam: 6.44]

  34. `DescricaoIdUso` ➔ Nulos: **53.85%** (350000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 21, Tam Máx: 96, Tam Média: 33.13, DesvPad Tam: 4.2]

  35. `DetalhamentoFonte` ➔ Nulos: **53.85%** (350000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **380** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 215, Tam Média: 45.15, DesvPad Tam: 29.13]

  36. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **275847** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  37. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **82391** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  38. `DomicilioBancarioOrigem` ➔ Nulos: **86.64%** (563169 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **382** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 10, Tam Média: 8.31, DesvPad Tam: 1.44]

  39. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **101** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 120, Tam Média: 31.93, DesvPad Tam: 14.27]

  40. `Embasamento` ➔ Nulos: **53.85%** (350007 nulos) | Zeros: **0.0%** (3 zeros) | Distintos: **13575** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 250, Tam Média: 51.11, DesvPad Tam: 19.44]

  41. `Emenda` ➔ Nulos: **99.85%** (649048 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **829** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 12, Tam Média: 12.0, DesvPad Tam: 0.0]

  42. `Esfera` ➔ Nulos: **53.85%** (350000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 20.0, Média: 13.19, Mediana: 10.0, DesvPad: 4.66]

  43. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (1 zeros) | Distintos: **46318** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 104, Tam Média: 33.55, DesvPad Tam: 13.71]

  44. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **209** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 150, Tam Média: 43.88, DesvPad Tam: 29.36]

  45. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **25** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 21, Tam Média: 11.89, DesvPad Tam: 5.55]

  46. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.77, DesvPad Tam: 2.31]

  47. `HistoricoDocumento` ➔ Nulos: **11.29%** (73369 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **469501** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1024, Tam Média: 174.6, DesvPad Tam: 118.19]

  48. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **650000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 222624908.0, Máx: 241639732.0, Média: 227824820.04, Mediana: 226599925.5, DesvPad: 4850044.24]

  49. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **54816** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314694.0, Máx: 8431720.0, Média: 8361309.18, Mediana: 8369620.0, DesvPad: 28229.14]

  50. `IdUso` ➔ Nulos: **53.85%** (350000 nulos) | Zeros: **15.36%** (99840 zeros) | Distintos: **5** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 6.0, Média: 0.71, Mediana: 1.0, DesvPad: 0.55]

  51. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 129, Tam Média: 21.99, DesvPad Tam: 17.75]

  52. `NomeCredorRetencao` ➔ Nulos: **95.83%** (622877 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1220** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 97, Tam Média: 30.98, DesvPad Tam: 13.77]

  53. `NomeTipoRetencao` ➔ Nulos: **95.83%** (622877 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **151** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 100, Tam Média: 37.24, DesvPad Tam: 17.93]

  54. `NumeroLicitacao` ➔ Nulos: **53.86%** (350106 nulos) | Zeros: **39.43%** (256294 zeros) | Distintos: **3151** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 15, Tam Média: 4.12, DesvPad Tam: 2.03]

  55. `NumeroProcesso` ➔ Nulos: **99.61%** (647436 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **428** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 54728045.0, Máx: 2020024272164.0, Média: 1774060145076.85, Mediana: 2020014994636.5, DesvPad: 658587103190.77]

  56. `Orgao` ➔ Nulos: **100.0%** (650000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  57. `PlanoOrcamentario` ➔ Nulos: **99.61%** (647436 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 22, Tam Média: 22.0, DesvPad Tam: 0.0]

  58. `Processo` ➔ Nulos: **61.96%** (402715 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49726** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 493, Tam Média: 101.7, DesvPad Tam: 48.6]

  59. `ProcessoAssunto` ➔ Nulos: **61.95%** (402672 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **536** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 100, Tam Média: 13.32, DesvPad Tam: 6.84]

  60. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **223** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 149, Tam Média: 33.66, DesvPad Tam: 20.22]

  61. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **86** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 56, Tam Média: 23.83, DesvPad Tam: 8.36]

  62. `SubelementoDespesa` ➔ Nulos: **0.14%** (882 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1417** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 200, Tam Média: 43.17, DesvPad Tam: 22.1]

  63. `Subtitulo` ➔ Nulos: **15.38%** (100000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 16, Tam Média: 7.29, DesvPad Tam: 2.57]

  64. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 4.0, Média: 1.91, Mediana: 2.0, DesvPad: 0.7]

  65. `TipoLicitacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **31** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 70, Tam Média: 19.78, DesvPad Tam: 9.54]

  66. `TipoRetencao` ➔ Nulos: **95.83%** (622877 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **134** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 387.0, Média: 77.91, Mediana: 79.0, DesvPad: 81.68]

  67. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **157** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 42.24, DesvPad Tam: 16.11]

  68. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **83.65%** (543698 zeros) | Distintos: **43481** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -373250122.2, Máx: 567526000.0, Média: 18704.65, Mediana: 0.0, DesvPad: 1681849.35]

  69. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **58.46%** (379986 zeros) | Distintos: **140410** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -129426684.24, Máx: 158461275.4, Média: 15841.88, Mediana: 0.0, DesvPad: 698602.95]

  70. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **59.97%** (389783 zeros) | Distintos: **133724** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -21846991.54, Máx: 103912215.18, Média: 20925.27, Mediana: 0.0, DesvPad: 511005.99]

  71. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **97.93%** (636533 zeros) | Distintos: **11179** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -909826.0, Máx: 10028758.74, Média: 895.46, Mediana: 0.0, DesvPad: 42532.84]


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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **302** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 159, Tam Média: 44.68, DesvPad Tam: 18.48]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2024.0, Máx: 2024.0, Média: 2024.0, Mediana: 2024.0, DesvPad: 0.0]

  3. `AnoLicitacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **71.1%** (71105 zeros) | Distintos: **28** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2323.0, Média: 584.26, Mediana: 0.0, DesvPad: 916.7]

  4. `CargoFuncao` ➔ Nulos: **100.0%** (100000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  5. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.04, DesvPad Tam: 0.2]

  6. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **312** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 8683.0, Média: 2306.17, Mediana: 2149.0, DesvPad: 1033.56]

  7. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.04, Mediana: 3.0, DesvPad: 0.2]

  8. `CodigoConvenioConcedido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.7%** (99697 zeros) | Distintos: **153** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 240882.0, Média: 659.41, Mediana: 0.0, DesvPad: 12193.73]

  9. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (100000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  10. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **157** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.00011, Média: 534.31, Mediana: 500.1001, DesvPad: 80.53]

  11. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 96.0, Média: 34.46, Mediana: 36.0, DesvPad: 22.68]

  12. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 534.28, Mediana: 500.0, DesvPad: 80.54]

  13. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 28.0, Média: 10.66, Mediana: 10.0, DesvPad: 6.35]

  14. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (100000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  15. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 60201.0, Média: 21973.45, Mediana: 22901.0, DesvPad: 21934.94]

  16. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 6.0, Média: 2.74, Mediana: 3.0, DesvPad: 0.76]

  17. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 40.0, Máx: 92.0, Média: 88.61, Mediana: 90.0, DesvPad: 7.78]

  18. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **29** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 80.0, Média: 36.84, Mediana: 44.0, DesvPad: 15.12]

  19. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (100000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  20. `CodigoProcesso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.02%** (24 zeros) | Distintos: **36991** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 2, Tam Máx: 15, Tam Média: 10.67, DesvPad Tam: 1.76]

  21. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 1000.0, Média: 144.05, Mediana: 53.0, DesvPad: 233.89]

  22. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31.0, Máx: 846.0, Média: 252.41, Mediana: 181.0, DesvPad: 174.35]

  23. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **788** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1721.0, Máx: 5820.0, Média: 3166.01, Mediana: 2769.0, DesvPad: 1049.27]

  24. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **79.32%** (79319 zeros) | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 59.0, Média: 10.95, Mediana: 0.0, DesvPad: 21.51]

  25. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **114** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 366879.33, Mediana: 440901.0, DesvPad: 151278.14]

  26. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13833** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 14, Tam Média: 12.7, DesvPad Tam: 2.95]

  27. `CredorRetencao` ➔ Nulos: **87.57%** (87571 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **758** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 191.0, Máx: 92892256000179.0, Média: 12972741254795.85, Mediana: 1970293454.0, DesvPad: 17128702505331.04]

  28. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **317** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  29. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (100000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  30. `DetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **143** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 213, Tam Média: 55.99, DesvPad Tam: 28.89]

  31. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **38466** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  32. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11782** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  33. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 120, Tam Média: 29.64, DesvPad Tam: 12.73]

  34. `Embasamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3831** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 249, Tam Média: 47.94, DesvPad Tam: 20.97]

  35. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14144** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 100, Tam Média: 33.4, DesvPad Tam: 12.91]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **45** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 150, Tam Média: 42.33, DesvPad Tam: 26.06]

  37. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 21, Tam Média: 11.91, DesvPad Tam: 5.59]

  38. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.67, DesvPad Tam: 2.4]

  39. `HistoricoDocumento` ➔ Nulos: **16.22%** (16220 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69371** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 1146, Tam Média: 217.69, DesvPad Tam: 140.0]

  40. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **100000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1906764725.0, Máx: 1906875076.0, Média: 1906815151.88, Mediana: 1906814724.5, DesvPad: 29607.43]

  41. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14197** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314695.0, Máx: 8424969.0, Média: 8370783.67, Mediana: 8371818.0, DesvPad: 31069.96]

  42. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 129, Tam Média: 21.45, DesvPad Tam: 16.89]

  43. `NomeCredorRetencao` ➔ Nulos: **87.57%** (87571 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **754** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 97, Tam Média: 29.62, DesvPad Tam: 12.69]

  44. `NomeTipoRetencao` ➔ Nulos: **87.57%** (87571 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **106** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 94, Tam Média: 37.36, DesvPad Tam: 18.15]

  45. `NumeroLicitacao` ➔ Nulos: **0.0%** (3 nulos) | Zeros: **77.66%** (77662 zeros) | Distintos: **1702** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 15, Tam Média: 4.32, DesvPad Tam: 2.9]

  46. `NumeroProcesso` ➔ Nulos: **100.0%** (100000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Orgao` ➔ Nulos: **100.0%** (100000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `PlanoOrcamentario` ➔ Nulos: **100.0%** (100000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  49. `Processo` ➔ Nulos: **99.03%** (99028 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **103** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 238, Tam Média: 129.03, DesvPad Tam: 59.98]

  50. `ProcessoAssunto` ➔ Nulos: **99.03%** (99026 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **62** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 36, Tam Média: 18.0, DesvPad Tam: 5.87]

  51. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 111, Tam Média: 31.81, DesvPad Tam: 22.14]

  52. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 48, Tam Média: 23.84, DesvPad Tam: 8.7]

  53. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **901** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 200, Tam Média: 43.84, DesvPad Tam: 20.91]

  54. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 16, Tam Média: 7.12, DesvPad Tam: 2.42]

  55. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 4.0, Média: 1.84, Mediana: 2.0, DesvPad: 0.68]

  56. `TipoLicitacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **17** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 70, Tam Média: 21.65, DesvPad Tam: 9.01]

  57. `TipoRetencao` ➔ Nulos: **87.57%** (87571 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **106** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 380.0, Média: 82.0, Mediana: 79.0, DesvPad: 81.63]

  58. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **113** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 41.1, DesvPad Tam: 14.99]

  59. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **83.73%** (83725 zeros) | Distintos: **7041** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -39500000.0, Máx: 126639121.0, Média: 22849.22, Mediana: 0.0, DesvPad: 822134.83]

  60. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **54.94%** (54940 zeros) | Distintos: **25463** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -98907632.3, Máx: 115308905.34, Média: 14568.56, Mediana: 0.0, DesvPad: 932980.64]

  61. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **63.78%** (63777 zeros) | Distintos: **23324** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -13095836.39, Máx: 129884794.92, Média: 21984.86, Mediana: 0.0, DesvPad: 569406.9]

  62. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **97.56%** (97558 zeros) | Distintos: **2235** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -1500053.4, Máx: 15038098.05, Média: 1150.81, Mediana: 0.0, DesvPad: 56330.99]


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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1419** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 178, Tam Média: 51.41, DesvPad Tam: 24.87]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2014.0, Máx: 2026.0, Média: 2021.88, Mediana: 2022.0, DesvPad: 2.97]

  3. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 23, Tam Média: 18.15, DesvPad Tam: 0.36]

  4. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1770** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9999.0, Média: 2454.45, Mediana: 2175.0, DesvPad: 1353.76]

  5. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 9.0, Média: 3.15, Mediana: 3.0, DesvPad: 0.36]

  6. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **113** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 99.0, Média: 37.87, Mediana: 37.0, DesvPad: 21.73]

  7. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (2 zeros) | Distintos: **214** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 899.0, Média: 340.15, Mediana: 301.0, DesvPad: 217.98]

  8. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **51** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 99.0, Média: 11.99, Mediana: 10.0, DesvPad: 6.87]

  9. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9.0, Média: 2.95, Mediana: 3.0, DesvPad: 0.75]

  10. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 20.0, Máx: 99.0, Média: 85.64, Mediana: 90.0, DesvPad: 13.19]

  11. `CodigoPlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2948** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 3568.0, Média: 543.36, Mediana: 1.0, DesvPad: 890.83]

  12. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **237** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9999.0, Média: 186.27, Mediana: 47.0, DesvPad: 372.89]

  13. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **170** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31.0, Máx: 999.0, Média: 285.29, Mediana: 302.0, DesvPad: 193.02]

  14. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **15.02%** (65903 zeros) | Distintos: **2086** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5903.0, Média: 2718.64, Mediana: 2695.0, DesvPad: 1485.29]

  15. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **267** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 990101.0, Média: 353617.75, Mediana: 420101.0, DesvPad: 136999.0]

  16. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **15.73%** (69015 zeros) | Distintos: **70973** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 14, Tam Média: 10.18, DesvPad Tam: 4.58]

  17. `DespesaEmpenhada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **29.2%** (128097 zeros) | Distintos: **142188** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1934113298.69, Média: 333353.47, Mediana: 1128.0, DesvPad: 7014568.44]

  18. `DespesaLiquidada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **33.91%** (148768 zeros) | Distintos: **141961** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1934113298.69, Média: 308313.1, Mediana: 672.0, DesvPad: 6956936.29]

  19. `DespesaPaga` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **26.41%** (115843 zeros) | Distintos: **162398** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1933589024.12, Média: 320035.86, Mediana: 1308.0, DesvPad: 6917374.56]

  20. `DotacaoAtualizada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **20.94%** (91838 zeros) | Distintos: **164191** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1934113298.69, Média: 396093.42, Mediana: 2275.4, DesvPad: 7455521.75]

  21. `DotacaoInicial` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **91.11%** (399668 zeros) | Distintos: **10179** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2121654518.0, Média: 322911.0, Mediana: 0.0, DesvPad: 8643939.38]

  22. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 120, Tam Média: 30.17, DesvPad Tam: 15.17]

  23. `Emenda` ➔ Nulos: **97.53%** (427817 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5960** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 12, Tam Média: 12.0, DesvPad Tam: 0.0]

  24. `Esfera` ➔ Nulos: **31.61%** (138659 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 20.0, Média: 12.55, Mediana: 10.0, DesvPad: 4.36]

  25. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (1 zeros) | Distintos: **58904** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 104, Tam Média: 27.92, DesvPad Tam: 15.76]

  26. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **160** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 150, Tam Média: 38.72, DesvPad Tam: 25.27]

  27. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 23, Tam Média: 11.53, DesvPad Tam: 5.27]

  28. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 23.27, DesvPad Tam: 4.36]

  29. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **438659** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 327967.0, Máx: 67364692.0, Média: 45217617.2, Mediana: 65369057.0, DesvPad: 30385293.33]

  30. `Microregiao` ➔ Nulos: **31.61%** (138659 nulos) | Zeros: **48.53%** (212865 zeros) | Distintos: **22** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 59.0, Média: 15.47, Mediana: 0.0, DesvPad: 24.25]

  31. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **18** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 129, Tam Média: 23.88, DesvPad Tam: 19.33]

  32. `Municipio` ➔ Nulos: **31.61%** (138659 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **79** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 320010.0, Máx: 999999.0, Média: 862773.76, Mediana: 999999.0, DesvPad: 272834.33]

  33. `NomeEsfera` ➔ Nulos: **31.61%** (138659 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 30, Tam Média: 19.57, DesvPad Tam: 6.1]

  34. `NomeMicroregiao` ➔ Nulos: **31.61%** (138659 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 16, Tam Média: 7.55, DesvPad Tam: 2.73]

  35. `NomeMunicipio` ➔ Nulos: **31.61%** (138659 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **79** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 23, Tam Média: 5.49, DesvPad Tam: 3.86]

  36. `NomeUnidadeOrcamentaria` ➔ Nulos: **31.61%** (138659 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **118** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 133, Tam Média: 42.92, DesvPad Tam: 19.1]

  37. `PlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2647** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 216, Tam Média: 21.97, DesvPad Tam: 18.82]

  38. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **234** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 149, Tam Média: 36.12, DesvPad Tam: 21.97]

  39. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 62, Tam Média: 23.73, DesvPad Tam: 8.57]

  40. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1583** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 200, Tam Média: 41.5, DesvPad Tam: 26.56]

  41. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **162** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 45.18, DesvPad Tam: 16.49]

  42. `UnidadeOrcamentaria` ➔ Nulos: **31.61%** (138659 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **122** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1101.0, Máx: 80104.0, Média: 35596.82, Mediana: 42101.0, DesvPad: 13535.23]

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

  3. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2066** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 11452.0, Máx: 702861.0, Média: 350089.93, Mediana: 262741.5, DesvPad: 271583.72]

  4. `SiglaUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **204** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 90, Tam Média: 43.08, DesvPad Tam: 18.83]

  5. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **196** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 90, Tam Média: 45.13, DesvPad Tam: 17.48]

  6. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **12.58%** (260 zeros) | Distintos: **1807** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4788599153.95, Média: 148521526.86, Mediana: 14589310.094999999, DesvPad: 457108162.15]

  7. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **8.76%** (181 zeros) | Distintos: **1886** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4602955744.27, Média: 145707612.53, Mediana: 13982949.605, DesvPad: 448421821.99]

  8. `ValorOrcado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **1.98%** (41 zeros) | Distintos: **1988** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5426690790.98, Média: 180720401.1, Mediana: 23424071.405, DesvPad: 512384510.85]

  9. `ValorOrcadoInicial` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **3.97%** (82 zeros) | Distintos: **1904** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4351806442.0, Média: 154370221.81, Mediana: 18543344.0, DesvPad: 445060053.96]

  10. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **8.76%** (181 zeros) | Distintos: **1886** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4560087385.15, Média: 142683748.34, Mediana: 13483675.01, DesvPad: 440243802.33]

  11. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **32.09%** (663 zeros) | Distintos: **1403** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 484008397.04, Média: 6020818.83, Mediana: 384780.38, DesvPad: 26405764.05]

---

## 📂 Grupo Principal: `OrcamentosDespesaAssembleia-`

### 🔹 Período: 2021
- **Quantidade Total de Colunas:** `41`
  - *Colunas removidas/alteradas:* Nenhuma

**Arquivos Vinculados ao Período:**
  - 📄 **`OrcamentosDespesaAssembleia-2021.csv`** *(ID: `dfe19849-50b5-482a-b766-2b1f0cb06a91`)*

**Análise de Qualidade das Colunas (Consolidada por Período):**

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **354** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 135, Tam Média: 51.01, DesvPad Tam: 21.29]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2021.0, Máx: 2021.0, Média: 2021.0, Mediana: 2021.0, DesvPad: 0.0]

  3. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 23, Tam Média: 18.13, DesvPad Tam: 0.34]

  4. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **348** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 9999.0, Média: 2568.5, Mediana: 2184.0, DesvPad: 1398.59]

  5. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 9.0, Média: 3.13, Mediana: 3.0, DesvPad: 0.34]

  6. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 99.0, Média: 42.02, Mediana: 39.0, DesvPad: 23.4]

  7. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (1 zeros) | Distintos: **74** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 675.0, Média: 162.9, Mediana: 104.0, DesvPad: 105.3]

  8. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 99.0, Média: 11.34, Mediana: 10.0, DesvPad: 6.21]

  9. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9.0, Média: 2.96, Mediana: 3.0, DesvPad: 0.68]

  10. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 20.0, Máx: 99.0, Média: 85.3, Mediana: 90.0, DesvPad: 13.39]

  11. `CodigoPlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **670** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 2318.0, Média: 423.69, Mediana: 1.0, DesvPad: 681.31]

  12. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 9999.0, Média: 190.67, Mediana: 47.0, DesvPad: 578.33]

  13. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **72** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 32.0, Máx: 999.0, Média: 279.43, Mediana: 302.0, DesvPad: 164.04]

  14. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **12.08%** (6039 zeros) | Distintos: **793** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5410.0, Média: 2940.8, Mediana: 2778.0, DesvPad: 1445.53]

  15. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **106** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 20101.0, Máx: 800104.0, Média: 376369.52, Mediana: 420120.0, DesvPad: 113216.22]

  16. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **12.84%** (6420 zeros) | Distintos: **16070** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 14, Tam Média: 10.92, DesvPad Tam: 4.4]

  17. `DespesaEmpenhada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **24.08%** (12041 zeros) | Distintos: **21936** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 508409728.88, Média: 247426.86, Mediana: 1456.0, DesvPad: 3890225.11]

  18. `DespesaLiquidada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **28.01%** (14006 zeros) | Distintos: **21393** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 508409728.88, Média: 228898.17, Mediana: 913.8, DesvPad: 3839690.86]

  19. `DespesaPaga` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **23.32%** (11659 zeros) | Distintos: **22851** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 508410473.84, Média: 232720.01, Mediana: 1500.0, DesvPad: 3851370.1]

  20. `DotacaoAtualizada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **15.97%** (7983 zeros) | Distintos: **24943** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 508409728.88, Média: 314169.2, Mediana: 3060.06, DesvPad: 4322496.81]

  21. `DotacaoInicial` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **93.51%** (46755 zeros) | Distintos: **1386** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 700000000.0, Média: 243001.43, Mediana: 0.0, DesvPad: 6138870.0]

  22. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 120, Tam Média: 30.28, DesvPad Tam: 14.83]

  23. `Esfera` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  24. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **15997** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 104, Tam Média: 29.13, DesvPad Tam: 15.56]

  25. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **73** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 132, Tam Média: 35.96, DesvPad Tam: 21.85]

  26. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 23, Tam Média: 10.76, DesvPad Tam: 5.19]

  27. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 23.53, DesvPad Tam: 4.06]

  28. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **50000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 7174323.0, Máx: 7224322.0, Média: 7199322.5, Mediana: 7199322.5, DesvPad: 14433.76]

  29. `Microregiao` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  30. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 129, Tam Média: 24.75, DesvPad Tam: 20.18]

  31. `Municipio` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  32. `NomeEsfera` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  33. `NomeMicroregiao` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  34. `NomeMunicipio` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  35. `NomeUnidadeOrcamentaria` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  36. `PlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **668** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 216, Tam Média: 20.78, DesvPad Tam: 16.48]

  37. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 91, Tam Média: 32.41, DesvPad Tam: 20.17]

  38. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **72** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 48, Tam Média: 23.87, DesvPad Tam: 9.38]

  39. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **759** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 184, Tam Média: 43.12, DesvPad Tam: 29.69]

  40. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **103** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 20, Tam Máx: 90, Tam Média: 44.01, DesvPad Tam: 16.49]

  41. `UnidadeOrcamentaria` ➔ Nulos: **100.0%** (50000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `Esfera`, `Microregiao`, `Municipio`, `NomeEsfera`, `NomeMicroregiao`, `NomeMunicipio`, `NomeUnidadeOrcamentaria`, `UnidadeOrcamentaria`


---