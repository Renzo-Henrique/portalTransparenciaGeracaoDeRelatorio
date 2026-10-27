# Relatório de Auditoria de Arquivo Local (Grande Porte)

- **Caminho do Arquivo:** `arquivos/despesas-2025.csv`
- **Total de Linhas Auditadas:** `1456562`
- **Total de Colunas:** `71`

---

## 🛠️ Conferência de Erros na Estrutura do Arquivo

> ✅ **Nenhum erro estrutural detectado.** A consistência das colunas foi mantida em todos os blocos do arquivo.

---

## 📋 Qualidade e Estatísticas das Colunas

1. `Acao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **324** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 13, Tam Máx: 178, Média: 52.32]
2. `AgenciaOrigem` ➔ Nulos: **68.92%** | Zeros: **0.0%** | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Texto:** [Tam Mín: 1, Tam Máx: 4, Média: 3.87]
3. `Ano` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **1** 🟢 [Enum] | 📊 **Numérica:** [Mín: 2025.0, Máx: 2025.0, Média: 2025.0, DesvPad: 0.0]
4. `AnoLicitacao` ➔ Nulos: **0.0%** | Zeros: **72.36%** | Distintos: **34** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Numérica:** [Mín: 0.0, Máx: 2025.0, Média: 577.2, DesvPad: 913.63]
5. `BancoOrigem` ➔ Nulos: **68.92%** | Zeros: **0.0%** | Distintos: **4** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Texto:** [Tam Mín: 1, Tam Máx: 3, Média: 2.91]
6. `CargoFuncao` ➔ Nulos: **100.0%** | Zeros: **0.0%** | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]
7. `CategoriaEconomica` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 18, Tam Máx: 19, Média: 18.04]
8. `CodigoAcao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **334** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 3.0, Máx: 8683.0, Média: 2247.5, DesvPad: 901.78]
9. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📊 **Numérica:** [Mín: 3.0, Máx: 4.0, Média: 3.04, DesvPad: 0.21]
10. `CodigoConvenioConcedido` ➔ Nulos: **0.0%** | Zeros: **99.03%** | Distintos: **1085** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 250827.0, Média: 2550.81, DesvPad: 24474.41]
11. `CodigoConvenioRecebido` ➔ Nulos: **100.0%** | Zeros: **0.0%** | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]
12. `CodigoDetalhamentoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **221** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 500.0, Máx: 899.000113, Média: 535.44, DesvPad: 82.45]
13. `CodigoElementoDespesa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 1.0, Máx: 96.0, Média: 34.09, DesvPad: 22.61]
14. `CodigoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 500.0, Máx: 899.0, Média: 535.4, DesvPad: 82.46]
15. `CodigoFuncao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **24** 🟢 [Enum] | 📊 **Numérica:** [Mín: 1.0, Máx: 28.0, Média: 10.59, DesvPad: 6.31]
16. `CodigoFuncionalProgramatica` ➔ Nulos: **0.0%** | Zeros: **100.0%** | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Numérica:** [Mín: 0.0, Máx: 0.0, Média: 0.0, DesvPad: 0.0]
17. `CodigoGestaoEmitente` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **60** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 1.0, Máx: 60201.0, Média: 21812.92, DesvPad: 22040.56]
18. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **6** 🟢 [Enum] | 📊 **Numérica:** [Mín: 1.0, Máx: 6.0, Média: 2.75, DesvPad: 0.76]
19. `CodigoModalidade` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **13** 🟢 [Enum] | 📊 **Numérica:** [Mín: 20.0, Máx: 92.0, Média: 88.92, DesvPad: 6.92]
20. `CodigoOrgao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **30** 🟢 [Enum] | 📊 **Numérica:** [Mín: 1.0, Máx: 80.0, Média: 36.78, DesvPad: 15.2]
21. `CodigoPlanoOrcamentario` ➔ Nulos: **100.0%** | Zeros: **0.0%** | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]
22. `CodigoProcesso` ➔ Nulos: **0.01%** | Zeros: **0.01%** | Distintos: **38846** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 2, Tam Máx: 15, Média: 10.6]
23. `CodigoPrograma` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **58** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 2.0, Máx: 1000.0, Média: 151.07, DesvPad: 242.97]
24. `CodigoSubFuncao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **74** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 31.0, Máx: 846.0, Média: 244.99, DesvPad: 170.09]
25. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **885** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 1721.0, Máx: 5882.0, Média: 3172.67, DesvPad: 1071.99]
26. `CodigoSubtitulo` ➔ Nulos: **0.0%** | Zeros: **81.96%** | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Numérica:** [Mín: 0.0, Máx: 59.0, Média: 9.75, DesvPad: 20.54]
27. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **118** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 10101.0, Máx: 800102.0, Média: 366712.01, DesvPad: 152153.74]
28. `Contrato` ➔ Nulos: **0.0%** | Zeros: **71.08%** | Distintos: **10066** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 25005779.0, Média: 6740006.16, DesvPad: 10497834.86]
29. `CpfCnpjNis` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **13923** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 6, Tam Máx: 14, Média: 12.78]
30. `CredorRetencao` ➔ Nulos: **89.83%** | Zeros: **0.0%** | Distintos: **1338** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 191.0, Máx: 92892256000179.0, Média: 14155428872312.06, DesvPad: 17605764568825.84]
31. `Data` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **338** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 19, Tam Máx: 19, Média: 19.0]
32. `DescricaoElementoDespesa` ➔ Nulos: **100.0%** | Zeros: **0.0%** | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]
33. `DescricaoEsfera` ➔ Nulos: **100.0%** | Zeros: **0.0%** | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]
34. `DescricaoIdUso` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 30, Tam Máx: 33, Média: 30.19]
35. `DetalhamentoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **207** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 12, Tam Máx: 185, Média: 56.04]
36. `Documento` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **41354** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 11, Tam Máx: 11, Média: 11.0]
37. `DocumentoEmpenho` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **11807** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 11, Tam Máx: 11, Média: 11.0]
38. `DomicilioBancarioOrigem` ➔ Nulos: **68.92%** | Zeros: **0.0%** | Distintos: **450** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 1, Tam Máx: 10, Média: 7.94]
39. `ElementoDespesa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 8, Tam Máx: 120, Média: 32.27]
40. `Embasamento` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **6243** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 1, Tam Máx: 223, Média: 48.56]
41. `Emenda` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **970** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 1, Tam Máx: 12, Média: 1.05]
42. `Esfera` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📊 **Numérica:** [Mín: 10.0, Máx: 20.0, Média: 13.06, DesvPad: 4.61]
43. `Favorecido` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **14266** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 7, Tam Máx: 104, Média: 33.87]
44. `Fonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **55** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 26, Tam Máx: 141, Média: 41.58]
45. `Funcao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **24** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 5, Tam Máx: 21, Média: 12.23]
46. `GrupoDespesa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **6** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 13, Tam Máx: 26, Média: 24.62]
47. `HistoricoDocumento` ➔ Nulos: **0.03%** | Zeros: **0.0%** | Distintos: **67381** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 1, Tam Máx: 1024, Média: 189.52]
48. `Id` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **100000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 255610263.0, Máx: 257011262.0, Média: 256310762.5, DesvPad: 432049.48]
49. `IdFavorecido` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **14306** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 8314695.0, Máx: 8426646.0, Média: 8374789.01, DesvPad: 33165.32]
50. `IdUso` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📊 **Numérica:** [Mín: 1.0, Máx: 2.0, Média: 1.06, DesvPad: 0.24]
51. `Modalidade` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **13** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 18, Tam Máx: 129, Média: 20.88]
52. `NomeCredorRetencao` ➔ Nulos: **89.83%** | Zeros: **0.0%** | Distintos: **1334** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 3, Tam Máx: 97, Média: 30.5]
53. `NomeTipoRetencao` ➔ Nulos: **89.83%** | Zeros: **0.0%** | Distintos: **133** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 15, Tam Máx: 100, Média: 37.52]
54. `NumeroLicitacao` ➔ Nulos: **0.0%** | Zeros: **78.31%** | Distintos: **2810** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 1, Tam Máx: 15, Média: 4.15]
55. `NumeroProcesso` ➔ Nulos: **100.0%** | Zeros: **0.0%** | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]
56. `Orgao` ➔ Nulos: **100.0%** | Zeros: **0.0%** | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]
57. `PlanoOrcamentario` ➔ Nulos: **100.0%** | Zeros: **0.0%** | Distintos: **0** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros]
58. `Processo` ➔ Nulos: **99.03%** | Zeros: **0.0%** | Distintos: **202** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 13, Tam Máx: 238, Média: 141.36]
59. `ProcessoAssunto` ➔ Nulos: **99.03%** | Zeros: **0.0%** | Distintos: **94** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 3, Tam Máx: 42, Média: 17.75]
60. `Programa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **58** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 7, Tam Máx: 111, Média: 31.41]
61. `SubFuncao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **74** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 7, Tam Máx: 48, Média: 23.63]
62. `SubelementoDespesa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **852** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 5, Tam Máx: 159, Média: 43.94]
63. `Subtitulo` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **11** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 6, Tam Máx: 16, Média: 7.01]
64. `TipoFavorecido` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **4** 🟢 [Enum] | 📊 **Numérica:** [Mín: 1.0, Máx: 4.0, Média: 1.81, DesvPad: 0.68]
65. `TipoLicitacao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **17** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 6, Tam Máx: 70, Média: 22.45]
66. `TipoRetencao` ➔ Nulos: **89.83%** | Zeros: **0.0%** | Distintos: **133** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 1.0, Máx: 387.0, Média: 82.38, DesvPad: 84.92]
67. `UnidadeGestora` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **118** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 16, Tam Máx: 90, Média: 42.13]
68. `ValorEmpenho` ➔ Nulos: **0.0%** | Zeros: **87.85%** | Distintos: **11346** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: -130012891.5, Máx: 33475542.4, Média: 4694.36, DesvPad: 1156682.04]
69. `ValorLiquidado` ➔ Nulos: **0.0%** | Zeros: **43.23%** | Distintos: **28154** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: -67059764.45, Máx: 48036834.17, Média: 16678.39, DesvPad: 800128.96]
70. `ValorPago` ➔ Nulos: **0.0%** | Zeros: **71.06%** | Distintos: **23739** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: -355617.19, Máx: 25200000.0, Média: 14692.74, DesvPad: 300761.82]
71. `ValorRap` ➔ Nulos: **0.0%** | Zeros: **97.85%** | Distintos: **11738** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: -303947.44, Máx: 1709320.79, Média: 1312.62, DesvPad: 30862.07]

---

> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `CargoFuncao`, `CodigoConvenioRecebido`, `CodigoPlanoOrcamentario`, `DescricaoElementoDespesa`, `DescricaoEsfera`, `NumeroProcesso`, `Orgao`, `PlanoOrcamentario`
