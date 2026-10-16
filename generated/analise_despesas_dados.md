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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **865** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 121, Tam Média: 34.16, DesvPad Tam: 11.43]

  2. `AgenciaOrigem` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  3. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2004.0, Máx: 2013.0, Média: 2010.86, Mediana: 2011.0, DesvPad: 1.63]

  4. `AnoLicitacao` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  5. `BancoOrigem` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  6. `CargoFuncao` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  7. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.04, DesvPad Tam: 0.21]

  8. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.83%** (5829 zeros) | Distintos: **1661** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 8684.0, Média: 2392.13, Mediana: 2510.0, DesvPad: 1620.4]

  9. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.04, Mediana: 3.0, DesvPad: 0.21]

  10. `CodigoConvenioConcedido` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  11. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  12. `CodigoDetalhamentoFonte` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  13. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **176** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 469092.0, Média: 9903.15, Mediana: 30.0, DesvPad: 58225.53]

  14. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.83%** (5829 zeros) | Distintos: **51** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 274.0, Média: 145.32, Mediana: 102.0, DesvPad: 73.07]

  15. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.83%** (5829 zeros) | Distintos: **49** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 28.0, Média: 13.42, Mediana: 12.0, DesvPad: 8.39]

  16. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **80.57%** (165829 zeros) | Distintos: **481** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 3402.0, Média: 322.39, Mediana: 0.0, DesvPad: 659.36]

  17. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.83%** (5829 zeros) | Distintos: **76** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 60201.0, Média: 19747.9, Mediana: 1.0, DesvPad: 23949.4]

  18. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **18** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 46.0, Média: 3.59, Mediana: 3.0, DesvPad: 5.29]

  19. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **36** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 20.0, Máx: 4690.0, Média: 178.03, Mediana: 90.0, DesvPad: 569.08]

  20. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.83%** (5829 zeros) | Distintos: **99** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 80000.0, Média: 45210.36, Mediana: 42000.0, DesvPad: 19076.3]

  21. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  22. `CodigoProcesso` ➔ Nulos: **15.25%** (31389 nulos) | Zeros: **2.83%** (5830 zeros) | Distintos: **42750** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 17, Tam Média: 8.94, DesvPad Tam: 1.86]

  23. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.83%** (5829 zeros) | Distintos: **288** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 905.0, Média: 602.93, Mediana: 800.0, DesvPad: 282.22]

  24. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.83%** (5829 zeros) | Distintos: **135** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 846.0, Média: 295.36, Mediana: 244.0, DesvPad: 249.94]

  25. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.83%** (5829 zeros) | Distintos: **982** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 46907126.0, Média: 32986754.33, Mediana: 33901414.0, DesvPad: 6109802.47]

  26. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **97.19%** (200052 zeros) | Distintos: **13** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 12.0, Média: 0.11, Mediana: 0.0, DesvPad: 0.92]

  27. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **226** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 100101.0, Máx: 800103.0, Média: 461026.02, Mediana: 440901.0, DesvPad: 176875.27]

  28. `Contrato` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  29. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.83%** (5829 zeros) | Distintos: **19479** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 14, Tam Média: 12.97, DesvPad Tam: 2.39]

  30. `CredorRetencao` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  31. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1283** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  32. `DescricaoElementoDespesa` ➔ Nulos: **97.17%** (200000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 26, Tam Média: 26.0, DesvPad Tam: 0.0]

  33. `DescricaoEsfera` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  34. `DescricaoIdUso` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  35. `DetalhamentoFonte` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  36. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **85577** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  37. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **38540** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  38. `DomicilioBancarioOrigem` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  39. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 49, Tam Média: 27.37, DesvPad Tam: 13.07]

  40. `Embasamento` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  41. `Emenda` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  42. `Esfera` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  43. `Favorecido` ➔ Nulos: **19.43%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16346** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 45, Tam Média: 27.64, DesvPad Tam: 9.45]

  44. `Fonte` ➔ Nulos: **0.01%** (11 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **27** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 103, Tam Média: 26.77, DesvPad Tam: 12.18]

  45. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 26, Tam Média: 13.29, DesvPad Tam: 5.37]

  46. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.65, DesvPad Tam: 2.51]

  47. `HistoricoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **111237** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 231, Tam Média: 109.32, DesvPad Tam: 55.48]

  48. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **205829** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 196144748.0, Máx: 198890830.0, Média: 197514869.05, Mediana: 197576305.0, DesvPad: 979452.81]

  49. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **25018** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314692.0, Máx: 8390866.0, Média: 8334371.33, Mediana: 8334434.0, DesvPad: 12367.88]

  50. `IdUso` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  51. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 129, Tam Média: 21.99, DesvPad Tam: 13.87]

  52. `NomeCredorRetencao` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  53. `NomeTipoRetencao` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  54. `NumeroLicitacao` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  55. `NumeroProcesso` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  56. `Orgao` ➔ Nulos: **97.17%** (200000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 26, Tam Média: 26.0, DesvPad Tam: 0.0]

  57. `PlanoOrcamentario` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  58. `Processo` ➔ Nulos: **20.95%** (43125 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **31409** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 488, Tam Média: 91.35, DesvPad Tam: 42.58]

  59. `ProcessoAssunto` ➔ Nulos: **23.78%** (48953 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **406** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 41, Tam Média: 11.14, DesvPad Tam: 5.24]

  60. `Programa` ➔ Nulos: **12.38%** (25485 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **212** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 149, Tam Média: 35.98, DesvPad Tam: 20.78]

  61. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **75** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 56, Tam Média: 23.23, DesvPad Tam: 6.95]

  62. `SubelementoDespesa` ➔ Nulos: **5.72%** (11783 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **487** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 45, Tam Média: 30.18, DesvPad Tam: 8.46]

  63. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 26, Tam Média: 6.76, DesvPad Tam: 3.48]

  64. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **2.83%** (5829 zeros) | Distintos: **9** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 4.0, Média: 1.86, Mediana: 2.0, DesvPad: 0.78]

  65. `TipoLicitacao` ➔ Nulos: **2.83%** (5829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 52, Tam Média: 21.0, DesvPad Tam: 8.91]

  66. `TipoRetencao` ➔ Nulos: **100.0%** (205829 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  67. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **196** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 2, Tam Máx: 89, Tam Média: 37.06, DesvPad Tam: 16.65]

  68. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **80.23%** (165134 zeros) | Distintos: **19671** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1959182420.08, Média: 195195.46, Mediana: 0.0, DesvPad: 10247368.23]

  69. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **65.11%** (134022 zeros) | Distintos: **37063** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -21600000.0, Máx: 1959182420.08, Média: 181820.92, Mediana: 0.0, DesvPad: 10107636.56]

  70. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **50.68%** (104306 zeros) | Distintos: **57293** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -35000000.0, Máx: 1945104598.71, Média: 181834.83, Mediana: 0.0, DesvPad: 9940440.82]

  71. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **98.55%** (202849 zeros) | Distintos: **2384** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -74841.8, Máx: 1837946.65, Média: 158.17, Mediana: 0.0, DesvPad: 6997.32]


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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **428** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 97, Tam Média: 33.73, DesvPad Tam: 9.83]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2013.0, Máx: 2013.0, Média: 2013.0, Mediana: 2013.0, DesvPad: 0.0]

  3. `CargoFuncao` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  4. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.04, DesvPad Tam: 0.19]

  5. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **691** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 9.0, Máx: 8684.0, Média: 3239.03, Mediana: 2715.0, DesvPad: 1573.77]

  6. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.04, Mediana: 3.0, DesvPad: 0.19]

  7. `CodigoConvenioConcedido` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  8. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  9. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **46** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 96.0, Média: 27.79, Mediana: 30.0, DesvPad: 17.38]

  10. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 274.0, Média: 136.3, Mediana: 102.0, DesvPad: 63.92]

  11. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 28.0, Média: 12.87, Mediana: 10.0, DesvPad: 7.12]

  12. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (40000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  13. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **36** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 60201.0, Média: 23398.49, Mediana: 31201.0, DesvPad: 20840.91]

  14. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 6.0, Média: 2.75, Mediana: 3.0, DesvPad: 0.75]

  15. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 30.0, Máx: 91.0, Média: 88.46, Mediana: 90.0, DesvPad: 8.03]

  16. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10000.0, Máx: 80000.0, Média: 38046.85, Mediana: 42000.0, DesvPad: 11252.0]

  17. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  18. `CodigoProcesso` ➔ Nulos: **12.9%** (5159 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13932** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 606910936285530.0, Média: 55595924050.09, Mediana: 60908041.0, DesvPad: 5625728067357.85]

  19. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **96** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 905.0, Média: 613.2, Mediana: 800.0, DesvPad: 261.7]

  20. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **62** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 61.0, Máx: 846.0, Média: 223.98, Mediana: 122.0, DesvPad: 155.84]

  21. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **445** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31900101.0, Máx: 46907126.0, Média: 34015361.52, Mediana: 33903004.0, DesvPad: 2261617.25]

  22. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (40000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  23. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 100101.0, Máx: 800103.0, Média: 377739.99, Mediana: 420101.0, DesvPad: 111618.58]

  24. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8997** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 14, Tam Média: 13.57, DesvPad Tam: 1.05]

  25. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **259** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  26. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  27. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **16980** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  28. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7570** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  29. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **46** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 45, Tam Média: 28.86, DesvPad Tam: 13.48]

  30. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9130** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 45, Tam Média: 29.56, DesvPad Tam: 9.5]

  31. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 109, Tam Média: 24.12, DesvPad Tam: 13.6]

  32. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 21, Tam Média: 11.19, DesvPad Tam: 5.18]

  33. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.7, DesvPad Tam: 2.32]

  34. `HistoricoDocumento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30358** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 231, Tam Média: 110.36, DesvPad Tam: 46.95]

  35. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **40000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 339897548.0, Máx: 339937547.0, Média: 339917547.5, Mediana: 339917547.5, DesvPad: 11547.01]

  36. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9156** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314694.0, Máx: 8390841.0, Média: 8338801.13, Mediana: 8337404.0, DesvPad: 15840.2]

  37. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 129, Tam Média: 21.07, DesvPad Tam: 15.4]

  38. `NumeroProcesso` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  39. `Orgao` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  40. `PlanoOrcamentario` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  41. `Processo` ➔ Nulos: **14.81%** (5924 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11907** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 476, Tam Média: 88.25, DesvPad Tam: 43.37]

  42. `ProcessoAssunto` ➔ Nulos: **14.81%** (5924 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **296** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 49, Tam Média: 11.6, DesvPad Tam: 6.05]

  43. `Programa` ➔ Nulos: **0.17%** (67 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **91** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 149, Tam Média: 35.51, DesvPad Tam: 18.97]

  44. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **62** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 56, Tam Média: 23.6, DesvPad Tam: 8.07]

  45. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **393** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 45, Tam Média: 30.85, DesvPad Tam: 9.19]

  46. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 6, Tam Média: 6.0, DesvPad Tam: 0.0]

  47. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 4.0, Média: 1.73, Mediana: 2.0, DesvPad: 0.69]

  48. `TipoLicitacao` ➔ Nulos: **0.01%** (5 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **9** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 52, Tam Média: 21.38, DesvPad Tam: 9.24]

  49. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 89, Tam Média: 41.11, DesvPad Tam: 16.27]

  50. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **87.59%** (35035 zeros) | Distintos: **2244** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 472250380.94, Média: 28852.15, Mediana: 0.0, DesvPad: 2529504.44]

  51. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **58.93%** (23573 zeros) | Distintos: **8781** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -111779684.77, Máx: 114214829.48, Média: 28058.23, Mediana: 0.0, DesvPad: 1168333.51]

  52. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **56.76%** (22705 zeros) | Distintos: **9794** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -614534.48, Máx: 39404759.57, Média: 16137.8, Mediana: 0.0, DesvPad: 322338.79]

  53. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **96.72%** (38687 zeros) | Distintos: **1144** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -5842762.3, Máx: 2102306.91, Média: 771.89, Mediana: 0.0, DesvPad: 36467.45]


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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1427** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 178, Tam Média: 48.22, DesvPad Tam: 20.22]

  2. `AgenciaOrigem` ➔ Nulos: **84.03%** (436975 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 3665.0, Média: 880.28, Mediana: 675.0, DesvPad: 884.38]

  3. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2014.0, Máx: 2026.0, Média: 2020.0, Mediana: 2020.0, DesvPad: 3.74]

  4. `AnoLicitacao` ➔ Nulos: **53.85%** (280000 nulos) | Zeros: **37.61%** (195580 zeros) | Distintos: **42** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2302.0, Média: 374.24, Mediana: 0.0, DesvPad: 785.5]

  5. `BancoOrigem` ➔ Nulos: **84.03%** (436975 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 104.0, Média: 19.4, Mediana: 21.0, DesvPad: 6.88]

  6. `CargoFuncao` ➔ Nulos: **100.0%** (520000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  7. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.03, DesvPad Tam: 0.18]

  8. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1519** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 8684.0, Média: 2444.19, Mediana: 2119.0, DesvPad: 1294.28]

  9. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.03, Mediana: 3.0, DesvPad: 0.18]

  10. `CodigoConvenioConcedido` ➔ Nulos: **53.52%** (278311 nulos) | Zeros: **46.04%** (239425 zeros) | Distintos: **989** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 260760.0, Média: 2024.55, Mediana: 0.0, DesvPad: 21139.43]

  11. `CodigoConvenioRecebido` ➔ Nulos: **99.68%** (518311 nulos) | Zeros: **0.32%** (1689 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  12. `CodigoDetalhamentoFonte` ➔ Nulos: **53.85%** (280000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **396** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.000114, Média: 410.18, Mediana: 500.0, DesvPad: 203.25]

  13. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **105** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 98.0, Média: 32.56, Mediana: 33.0, DesvPad: 22.8]

  14. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **193** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 101.0, Máx: 899.0, Média: 276.49, Mediana: 155.0, DesvPad: 200.79]

  15. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 28.0, Média: 10.81, Mediana: 10.0, DesvPad: 6.47]

  16. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (520000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  17. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **135** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 60201.0, Média: 23018.88, Mediana: 28201.0, DesvPad: 22016.81]

  18. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 6.0, Média: 2.57, Mediana: 3.0, DesvPad: 0.89]

  19. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 20.0, Máx: 95.0, Média: 88.49, Mediana: 90.0, DesvPad: 8.04]

  20. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **58** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 80.0, Média: 36.53, Mediana: 42.0, DesvPad: 15.43]

  21. `CodigoPlanoOrcamentario` ➔ Nulos: **99.68%** (518311 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 1821.0, Máx: 1821.0, Média: 1821.0, Mediana: 1821.0, DesvPad: 0.0]

  22. `CodigoProcesso` ➔ Nulos: **0.07%** (350 nulos) | Zeros: **0.08%** (433 zeros) | Distintos: **171058** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 17, Tam Média: 10.38, DesvPad Tam: 2.12]

  23. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **237** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9999.0, Média: 283.94, Mediana: 53.0, DesvPad: 379.36]

  24. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **157** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31.0, Máx: 846.0, Média: 230.53, Mediana: 125.0, DesvPad: 159.79]

  25. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.04%** (228 zeros) | Distintos: **1921** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5903.0, Média: 3042.63, Mediana: 2737.0, DesvPad: 959.73]

  26. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **78.09%** (406059 zeros) | Distintos: **22** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 59.0, Média: 11.58, Mediana: 0.0, DesvPad: 21.91]

  27. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **256** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 364527.75, Mediana: 420201.0, DesvPad: 154314.09]

  28. `Contrato` ➔ Nulos: **53.85%** (280000 nulos) | Zeros: **33.49%** (174168 zeros) | Distintos: **12917** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 26004589.0, Média: 5899872.84, Mediana: 0.0, DesvPad: 9692295.06]

  29. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **37336** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 14, Tam Média: 12.08, DesvPad Tam: 3.42]

  30. `CredorRetencao` ➔ Nulos: **95.01%** (494028 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1159** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 191.0, Máx: 92892256000411.0, Média: 15447242727956.96, Mediana: 3323840000183.0, DesvPad: 17867435681476.16]

  31. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3620** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  32. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (520000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  33. `DescricaoEsfera` ➔ Nulos: **92.31%** (480000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 30, Tam Média: 20.21, DesvPad Tam: 6.42]

  34. `DescricaoIdUso` ➔ Nulos: **53.85%** (280000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 21, Tam Máx: 95, Tam Média: 33.14, DesvPad Tam: 4.2]

  35. `DetalhamentoFonte` ➔ Nulos: **53.85%** (280000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **354** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 215, Tam Média: 45.05, DesvPad Tam: 29.09]

  36. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **240708** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  37. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **73201** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  38. `DomicilioBancarioOrigem` ➔ Nulos: **84.03%** (436975 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **396** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 10, Tam Média: 8.29, DesvPad Tam: 1.43]

  39. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **101** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 120, Tam Média: 32.39, DesvPad Tam: 14.53]

  40. `Embasamento` ➔ Nulos: **53.85%** (280002 nulos) | Zeros: **0.0%** (2 zeros) | Distintos: **11989** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 250, Tam Média: 51.18, DesvPad Tam: 19.37]

  41. `Emenda` ➔ Nulos: **99.86%** (519250 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **676** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 12, Tam Média: 12.0, DesvPad Tam: 0.0]

  42. `Esfera` ➔ Nulos: **53.85%** (280000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 20.0, Média: 13.17, Mediana: 10.0, DesvPad: 4.65]

  43. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **42142** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 104, Tam Média: 33.54, DesvPad Tam: 13.96]

  44. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **201** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 150, Tam Média: 43.35, DesvPad Tam: 29.19]

  45. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **25** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 21, Tam Média: 12.08, DesvPad Tam: 5.46]

  46. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.83, DesvPad Tam: 2.24]

  47. `HistoricoDocumento` ➔ Nulos: **11.35%** (59036 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **371331** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 1182, Tam Média: 171.66, DesvPad Tam: 119.93]

  48. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **520000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 199445987.0, Máx: 218240599.0, Média: 204624728.88, Mediana: 203416004.5, DesvPad: 4804167.13]

  49. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49693** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314694.0, Máx: 8431649.0, Média: 8362531.2, Mediana: 8370046.0, DesvPad: 27682.42]

  50. `IdUso` ➔ Nulos: **53.85%** (280000 nulos) | Zeros: **15.36%** (79894 zeros) | Distintos: **5** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 6.0, Média: 0.72, Mediana: 1.0, DesvPad: 0.55]

  51. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 129, Tam Média: 22.26, DesvPad Tam: 18.86]

  52. `NomeCredorRetencao` ➔ Nulos: **95.01%** (494028 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1190** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 100, Tam Média: 31.2, DesvPad Tam: 14.15]

  53. `NomeTipoRetencao` ➔ Nulos: **95.01%** (494028 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **139** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 100, Tam Média: 36.81, DesvPad Tam: 17.78]

  54. `NumeroLicitacao` ➔ Nulos: **53.86%** (280068 nulos) | Zeros: **39.32%** (204470 zeros) | Distintos: **2954** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 15, Tam Média: 4.11, DesvPad Tam: 2.02]

  55. `NumeroProcesso` ➔ Nulos: **99.68%** (518311 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **343** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 54728045.0, Máx: 2020024240778.0, Média: 1777356310428.04, Mediana: 2020014896979.0, DesvPad: 654883386779.99]

  56. `Orgao` ➔ Nulos: **100.0%** (520000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  57. `PlanoOrcamentario` ➔ Nulos: **99.68%** (518311 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 22, Tam Máx: 22, Tam Média: 22.0, DesvPad Tam: 0.0]

  58. `Processo` ➔ Nulos: **65.34%** (339780 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **41802** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 493, Tam Média: 101.35, DesvPad Tam: 49.26]

  59. `ProcessoAssunto` ➔ Nulos: **65.34%** (339748 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **535** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 100, Tam Média: 13.11, DesvPad Tam: 6.56]

  60. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **214** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 149, Tam Média: 34.66, DesvPad Tam: 21.26]

  61. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **85** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 51, Tam Média: 23.61, DesvPad Tam: 8.26]

  62. `SubelementoDespesa` ➔ Nulos: **0.04%** (212 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1410** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 200, Tam Média: 42.8, DesvPad Tam: 21.62]

  63. `Subtitulo` ➔ Nulos: **15.38%** (80000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 16, Tam Média: 7.23, DesvPad Tam: 2.52]

  64. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **8** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 4.0, Média: 1.95, Mediana: 2.0, DesvPad: 0.73]

  65. `TipoLicitacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **30** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 70, Tam Média: 20.42, DesvPad Tam: 9.4]

  66. `TipoRetencao` ➔ Nulos: **95.01%** (494028 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **123** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 387.0, Média: 77.12, Mediana: 78.0, DesvPad: 83.04]

  67. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **156** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 42.44, DesvPad Tam: 16.21]

  68. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **83.63%** (434889 zeros) | Distintos: **34833** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -1909489066.2, Máx: 330969000.0, Média: 15259.2, Mediana: 0.0, DesvPad: 2939771.44]

  69. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **58.48%** (304096 zeros) | Distintos: **115647** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -150464263.83, Máx: 123579913.98, Média: 18806.81, Mediana: 0.0, DesvPad: 746970.87]

  70. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **59.36%** (308691 zeros) | Distintos: **115271** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -13176291.65, Máx: 129426684.24, Média: 23827.9, Mediana: 0.0, DesvPad: 550328.95]

  71. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **98.52%** (512324 zeros) | Distintos: **6617** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -1179854.19, Máx: 26205762.39, Média: 750.15, Mediana: 0.0, DesvPad: 59392.94]


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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **297** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 159, Tam Média: 44.71, DesvPad Tam: 18.5]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2024.0, Máx: 2024.0, Média: 2024.0, Mediana: 2024.0, DesvPad: 0.0]

  3. `AnoLicitacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **71.19%** (56952 zeros) | Distintos: **27** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2323.0, Média: 582.5, Mediana: 0.0, DesvPad: 915.88]

  4. `CargoFuncao` ➔ Nulos: **100.0%** (80000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  5. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 19, Tam Média: 18.04, DesvPad Tam: 0.2]

  6. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **307** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 8683.0, Média: 2302.46, Mediana: 2136.0, DesvPad: 1026.61]

  7. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 4.0, Média: 3.04, Mediana: 3.0, DesvPad: 0.2]

  8. `CodigoConvenioConcedido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **99.69%** (79754 zeros) | Distintos: **136** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 240866.0, Média: 662.66, Mediana: 0.0, DesvPad: 12216.12]

  9. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** (80000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  10. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **151** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.00011, Média: 534.42, Mediana: 500.1001, DesvPad: 80.66]

  11. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **54** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 96.0, Média: 34.48, Mediana: 36.0, DesvPad: 22.73]

  12. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **44** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 500.0, Máx: 899.0, Média: 534.38, Mediana: 500.0, DesvPad: 80.66]

  13. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 28.0, Média: 10.67, Mediana: 10.0, DesvPad: 6.35]

  14. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **100.0%** (80000 zeros) | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 0.0, Média: 0.0, Mediana: 0.0, DesvPad: 0.0]

  15. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **54** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 60201.0, Média: 21981.7, Mediana: 22901.0, DesvPad: 21925.89]

  16. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 6.0, Média: 2.74, Mediana: 3.0, DesvPad: 0.76]

  17. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 40.0, Máx: 92.0, Média: 88.63, Mediana: 90.0, DesvPad: 7.75]

  18. `CodigoOrgao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **29** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 80.0, Média: 36.85, Mediana: 44.0, DesvPad: 15.07]

  19. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** (80000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  20. `CodigoProcesso` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.02%** (18 zeros) | Distintos: **31941** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 2, Tam Máx: 15, Tam Média: 10.67, DesvPad Tam: 1.75]

  21. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 1000.0, Média: 144.0, Mediana: 53.0, DesvPad: 233.9]

  22. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31.0, Máx: 846.0, Média: 252.24, Mediana: 181.0, DesvPad: 174.06]

  23. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **773** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1721.0, Máx: 5820.0, Média: 3166.57, Mediana: 2769.0, DesvPad: 1049.94]

  24. `CodigoSubtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **79.26%** (63407 zeros) | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 59.0, Média: 10.99, Mediana: 0.0, DesvPad: 21.54]

  25. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **112** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 800102.0, Média: 366960.5, Mediana: 440901.0, DesvPad: 150807.81]

  26. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **12745** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 14, Tam Média: 12.69, DesvPad Tam: 2.96]

  27. `CredorRetencao` ➔ Nulos: **87.66%** (70131 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **673** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 191.0, Máx: 92892256000179.0, Média: 12943355683164.05, Mediana: 442521707.0, DesvPad: 17219550174694.74]

  28. `Data` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **314** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 19, Tam Máx: 19, Tam Média: 19.0, DesvPad Tam: 0.0]

  29. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** (80000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  30. `DetalhamentoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **137** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 213, Tam Média: 56.03, DesvPad Tam: 28.95]

  31. `Documento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33721** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  32. `DocumentoEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10691** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 11, Tam Média: 11.0, DesvPad Tam: 0.0]

  33. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **54** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 120, Tam Média: 29.61, DesvPad Tam: 12.73]

  34. `Embasamento` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3419** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 249, Tam Média: 47.97, DesvPad Tam: 20.98]

  35. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13001** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 100, Tam Média: 33.42, DesvPad Tam: 12.94]

  36. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **44** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 26, Tam Máx: 150, Tam Média: 42.33, DesvPad Tam: 26.06]

  37. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **24** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 21, Tam Média: 11.91, DesvPad Tam: 5.6]

  38. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 24.67, DesvPad Tam: 2.41]

  39. `HistoricoDocumento` ➔ Nulos: **16.24%** (12990 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **56373** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 1146, Tam Média: 217.33, DesvPad Tam: 139.75]

  40. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **80000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1906764725.0, Máx: 1906851251.0, Média: 1906804914.77, Mediana: 1906804724.5, DesvPad: 23424.93]

  41. `IdFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13047** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 8314695.0, Máx: 8424969.0, Média: 8370736.29, Mediana: 8371818.0, DesvPad: 31062.15]

  42. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **10** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 129, Tam Média: 21.47, DesvPad Tam: 16.96]

  43. `NomeCredorRetencao` ➔ Nulos: **87.66%** (70131 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **671** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 97, Tam Média: 29.68, DesvPad Tam: 12.72]

  44. `NomeTipoRetencao` ➔ Nulos: **87.66%** (70131 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **96** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 15, Tam Máx: 94, Tam Média: 37.31, DesvPad Tam: 18.14]

  45. `NumeroLicitacao` ➔ Nulos: **0.0%** (1 nulos) | Zeros: **77.72%** (62173 zeros) | Distintos: **1594** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 15, Tam Média: 4.32, DesvPad Tam: 2.9]

  46. `NumeroProcesso` ➔ Nulos: **100.0%** (80000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  47. `Orgao` ➔ Nulos: **100.0%** (80000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  48. `PlanoOrcamentario` ➔ Nulos: **100.0%** (80000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  49. `Processo` ➔ Nulos: **99.04%** (79234 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **94** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 238, Tam Média: 131.81, DesvPad Tam: 60.69]

  50. `ProcessoAssunto` ➔ Nulos: **99.04%** (79232 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **57** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 36, Tam Média: 18.03, DesvPad Tam: 5.74]

  51. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 111, Tam Média: 31.81, DesvPad Tam: 22.14]

  52. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 48, Tam Média: 23.86, DesvPad Tam: 8.69]

  53. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **883** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 200, Tam Média: 43.82, DesvPad Tam: 20.89]

  54. `Subtitulo` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 16, Tam Média: 7.13, DesvPad Tam: 2.43]

  55. `TipoFavorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **4** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 4.0, Média: 1.84, Mediana: 2.0, DesvPad: 0.68]

  56. `TipoLicitacao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **17** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 70, Tam Média: 21.65, DesvPad Tam: 9.02]

  57. `TipoRetencao` ➔ Nulos: **87.66%** (70131 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **96** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 380.0, Média: 82.26, Mediana: 79.0, DesvPad: 81.53]

  58. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **111** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 41.12, DesvPad Tam: 15.0]

  59. `ValorEmpenho` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **83.59%** (66874 zeros) | Distintos: **5859** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -39500000.0, Máx: 126639121.0, Média: 24540.86, Mediana: 0.0, DesvPad: 891614.18]

  60. `ValorLiquidado` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **55.31%** (44250 zeros) | Distintos: **20724** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -98907632.3, Máx: 115308905.34, Média: 12516.7, Mediana: 0.0, DesvPad: 936341.98]

  61. `ValorPago` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **63.54%** (50830 zeros) | Distintos: **19227** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -13095836.39, Máx: 129884794.92, Média: 22568.88, Mediana: 0.0, DesvPad: 619724.69]

  62. `ValorRap` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **97.56%** (78046 zeros) | Distintos: **1807** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: -1500053.4, Máx: 15038098.05, Média: 1136.17, Mediana: 0.0, DesvPad: 61405.73]


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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1380** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 178, Tam Média: 51.62, DesvPad Tam: 25.55]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **13** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2014.0, Máx: 2026.0, Média: 2021.73, Mediana: 2022.0, DesvPad: 3.08]

  3. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 23, Tam Média: 18.16, DesvPad Tam: 0.37]

  4. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1746** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9999.0, Média: 2442.99, Mediana: 2153.0, DesvPad: 1378.57]

  5. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **6** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 9.0, Média: 3.16, Mediana: 3.0, DesvPad: 0.37]

  6. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **113** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 99.0, Média: 37.72, Mediana: 37.0, DesvPad: 21.5]

  7. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (2 zeros) | Distintos: **212** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 899.0, Média: 337.47, Mediana: 301.0, DesvPad: 219.54]

  8. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **51** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 99.0, Média: 12.25, Mediana: 12.0, DesvPad: 7.14]

  9. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9.0, Média: 2.96, Mediana: 3.0, DesvPad: 0.76]

  10. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **33** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 20.0, Máx: 99.0, Média: 85.78, Mediana: 90.0, DesvPad: 12.99]

  11. `CodigoPlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2859** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 3565.0, Média: 548.69, Mediana: 1.0, DesvPad: 898.03]

  12. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **235** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9999.0, Média: 195.91, Mediana: 47.0, DesvPad: 396.45]

  13. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **169** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 31.0, Máx: 999.0, Média: 287.57, Mediana: 302.0, DesvPad: 199.49]

  14. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **15.6%** (56115 zeros) | Distintos: **2038** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5903.0, Média: 2699.71, Mediana: 2695.0, DesvPad: 1496.23]

  15. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **264** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10101.0, Máx: 990101.0, Média: 346115.31, Mediana: 400901.0, DesvPad: 138503.31]

  16. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **16.29%** (58586 zeros) | Distintos: **63107** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 14, Tam Média: 10.11, DesvPad Tam: 4.63]

  17. `DespesaEmpenhada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **30.05%** (108117 zeros) | Distintos: **119255** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1934113298.69, Média: 335553.58, Mediana: 1120.0, DesvPad: 7439259.88]

  18. `DespesaLiquidada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **34.94%** (125710 zeros) | Distintos: **118503** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1934113298.69, Média: 309586.88, Mediana: 644.575, DesvPad: 7375888.76]

  19. `DespesaPaga` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **27.21%** (97896 zeros) | Distintos: **135821** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1933589024.12, Média: 321556.32, Mediana: 1302.71, DesvPad: 7360050.26]

  20. `DotacaoAtualizada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **21.41%** (77032 zeros) | Distintos: **138176** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 1934113298.69, Média: 405625.09, Mediana: 2348.95, DesvPad: 7931798.3]

  21. `DotacaoInicial` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **90.79%** (326603 zeros) | Distintos: **8821** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 2121654518.0, Média: 329358.89, Mediana: 0.0, DesvPad: 9050644.09]

  22. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 120, Tam Média: 30.46, DesvPad Tam: 15.32]

  23. `Emenda` ➔ Nulos: **97.43%** (350504 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5141** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 12, Tam Máx: 12, Tam Média: 12.0, DesvPad Tam: 0.0]

  24. `Esfera` ➔ Nulos: **33.29%** (119750 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 20.0, Média: 12.2, Mediana: 10.0, DesvPad: 4.14]

  25. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (1 zeros) | Distintos: **52395** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 104, Tam Média: 27.78, DesvPad Tam: 15.89]

  26. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **160** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 150, Tam Média: 37.73, DesvPad Tam: 23.9]

  27. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **26** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 23, Tam Média: 11.71, DesvPad Tam: 5.18]

  28. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **7** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 23.16, DesvPad Tam: 4.47]

  29. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **359750** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 327967.0, Máx: 67029671.0, Média: 44087709.19, Mediana: 65358511.5, DesvPad: 30758872.79]

  30. `Microregiao` ➔ Nulos: **33.29%** (119750 nulos) | Zeros: **48.85%** (175749 zeros) | Distintos: **22** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 59.0, Média: 14.22, Mediana: 0.0, DesvPad: 23.58]

  31. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **18** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 129, Tam Média: 23.91, DesvPad Tam: 19.54]

  32. `Municipio` ➔ Nulos: **33.29%** (119750 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **79** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 320010.0, Máx: 999999.0, Média: 878346.05, Mediana: 999999.0, DesvPad: 260547.07]

  33. `NomeEsfera` ➔ Nulos: **33.29%** (119750 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 30, Tam Média: 19.08, DesvPad Tam: 5.8]

  34. `NomeMicroregiao` ➔ Nulos: **33.29%** (119750 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Estatísticas (Texto):** [Tam Mín: 6, Tam Máx: 16, Tam Média: 7.45, DesvPad Tam: 2.68]

  35. `NomeMunicipio` ➔ Nulos: **33.29%** (119750 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **79** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 23, Tam Média: 5.25, DesvPad Tam: 3.48]

  36. `NomeUnidadeOrcamentaria` ➔ Nulos: **33.29%** (119750 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **118** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 133, Tam Média: 44.91, DesvPad Tam: 19.3]

  37. `PlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **2584** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 3, Tam Máx: 216, Tam Média: 21.96, DesvPad Tam: 19.11]

  38. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **231** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 149, Tam Média: 36.74, DesvPad Tam: 22.09]

  39. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **89** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 62, Tam Média: 23.53, DesvPad Tam: 8.42]

  40. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1560** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 200, Tam Média: 41.18, DesvPad Tam: 26.49]

  41. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **161** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 16, Tam Máx: 90, Tam Média: 46.22, DesvPad Tam: 16.82]

  42. `UnidadeOrcamentaria` ➔ Nulos: **33.29%** (119750 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **122** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1101.0, Máx: 80104.0, Média: 34741.73, Mediana: 40901.0, DesvPad: 13799.57]

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

  1. `Acao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **326** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 11, Tam Máx: 135, Tam Média: 51.07, DesvPad Tam: 21.07]

  2. `Ano` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **1** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 2021.0, Máx: 2021.0, Média: 2021.0, Mediana: 2021.0, DesvPad: 0.0]

  3. `CategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 18, Tam Máx: 23, Tam Média: 18.15, DesvPad Tam: 0.36]

  4. `CodigoAcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **322** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 10.0, Máx: 9000.0, Média: 2574.69, Mediana: 2184.0, DesvPad: 1525.46]

  5. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **3** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 3.0, Máx: 9.0, Média: 3.15, Mediana: 3.0, DesvPad: 0.36]

  6. `CodigoElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 99.0, Média: 40.33, Mediana: 39.0, DesvPad: 21.55]

  7. `CodigoFonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (1 zeros) | Distintos: **72** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 675.0, Média: 163.69, Mediana: 104.0, DesvPad: 104.9]

  8. `CodigoFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 28.0, Média: 12.08, Mediana: 10.0, DesvPad: 6.52]

  9. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 9.0, Média: 2.96, Mediana: 3.0, DesvPad: 0.73]

  10. `CodigoModalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📊 **Estatísticas (Numérica):** [Mín: 20.0, Máx: 99.0, Média: 84.63, Mediana: 90.0, DesvPad: 14.1]

  11. `CodigoPlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **632** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 1.0, Máx: 2318.0, Média: 440.0, Mediana: 1.0, DesvPad: 713.14]

  12. `CodigoPrograma` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 2.0, Máx: 9999.0, Média: 173.34, Mediana: 47.0, DesvPad: 630.59]

  13. `CodigoSubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 32.0, Máx: 846.0, Média: 287.57, Mediana: 302.0, DesvPad: 175.32]

  14. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **13.56%** (5424 zeros) | Distintos: **760** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 5410.0, Média: 2910.44, Mediana: 2762.0, DesvPad: 1507.53]

  15. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **94** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 20101.0, Máx: 450202.0, Média: 357194.87, Mediana: 420101.0, DesvPad: 118708.16]

  16. `CpfCnpjNis` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **14.51%** (5805 zeros) | Distintos: **11207** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 1, Tam Máx: 14, Tam Média: 10.83, DesvPad Tam: 4.65]

  17. `DespesaEmpenhada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **26.35%** (10538 zeros) | Distintos: **19288** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 508409728.88, Média: 281593.43, Mediana: 2157.465, DesvPad: 4175181.91]

  18. `DespesaLiquidada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **30.2%** (12078 zeros) | Distintos: **18639** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 508409728.88, Média: 261133.63, Mediana: 1408.85, DesvPad: 4117876.49]

  19. `DespesaPaga` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **25.27%** (10109 zeros) | Distintos: **19757** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 508410473.84, Média: 264475.65, Mediana: 2389.5, DesvPad: 4131011.09]

  20. `DotacaoAtualizada` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **17.22%** (6889 zeros) | Distintos: **21998** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 508409728.88, Média: 359993.93, Mediana: 4737.4, DesvPad: 4671162.19]

  21. `DotacaoInicial` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **92.8%** (37120 zeros) | Distintos: **1253** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 0.0, Máx: 700000000.0, Média: 264248.66, Mediana: 0.0, DesvPad: 6481025.31]

  22. `ElementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **49** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 8, Tam Máx: 120, Tam Média: 30.2, DesvPad Tam: 15.3]

  23. `Esfera` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  24. `Favorecido` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **11148** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 104, Tam Média: 29.36, DesvPad Tam: 16.26]

  25. `Fonte` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **71** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 132, Tam Média: 35.85, DesvPad Tam: 21.7]

  26. `Funcao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **23** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 21, Tam Média: 9.74, DesvPad Tam: 4.55]

  27. `GrupoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **5** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 13, Tam Máx: 26, Tam Média: 23.3, DesvPad Tam: 4.32]

  28. `Id` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **40000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Estatísticas (Numérica):** [Mín: 7174323.0, Máx: 7214322.0, Média: 7194322.5, Mediana: 7194322.5, DesvPad: 11547.01]

  29. `Microregiao` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  30. `Modalidade` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **14** 🟢 [Enum] | 📝 **Estatísticas (Texto):** [Tam Mín: 9, Tam Máx: 129, Tam Média: 25.88, DesvPad Tam: 21.6]

  31. `Municipio` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  32. `NomeEsfera` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  33. `NomeMicroregiao` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  34. `NomeMunicipio` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  35. `NomeUnidadeOrcamentaria` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]

  36. `PlanoOrcamentario` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **631** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 4, Tam Máx: 216, Tam Média: 19.83, DesvPad Tam: 15.83]

  37. `Programa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 91, Tam Média: 33.21, DesvPad Tam: 21.46]

  38. `SubFuncao` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **69** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 7, Tam Máx: 48, Tam Média: 24.21, DesvPad Tam: 9.14]

  39. `SubelementoDespesa` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **729** ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 5, Tam Máx: 184, Tam Média: 43.89, DesvPad Tam: 31.3]

  40. `UnidadeGestora` ➔ Nulos: **0.0%** (0 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **91** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Estatísticas (Texto):** [Tam Mín: 20, Tam Máx: 90, Tam Média: 44.38, DesvPad Tam: 17.96]

  41. `UnidadeOrcamentaria` ➔ Nulos: **100.0%** (40000 nulos) | Zeros: **0.0%** (0 zeros) | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]


> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `Esfera`, `Microregiao`, `Municipio`, `NomeEsfera`, `NomeMicroregiao`, `NomeMunicipio`, `NomeUnidadeOrcamentaria`, `UnidadeOrcamentaria`


---