# Relatório de Auditoria de Arquivo Local (Grande Porte)

- **Caminho do Arquivo:** `arquivos/orcamentosdespesa-2025.csv`
- **Total de Linhas Auditadas:** `72523`
- **Total de Colunas:** `42`

---

## 🛠️ Conferência de Erros na Estrutura do Arquivo

> ✅ **Nenhum erro estrutural detectado.** A consistência das colunas foi mantida em todos os blocos do arquivo.

---

## 📋 Qualidade e Estatísticas das Colunas

1. `Acao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **374** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 15, Tam Máx: 119, Média: 62.38]
2. `Ano` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **1** 🟢 [Enum] | 📊 **Numérica:** [Mín: 2025.0, Máx: 2025.0, Média: 2025.0, DesvPad: 0.0]
3. `CategoriaEconomica` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **3** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 18, Tam Máx: 19, Média: 18.09]
4. `CodigoAcao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **380** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 12.0, Máx: 4875.0, Média: 2095.78, DesvPad: 504.47]
5. `CodigoCategoriaEconomica` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **3** 🟢 [Enum] | 📊 **Numérica:** [Mín: 3.0, Máx: 4.0, Média: 3.09, DesvPad: 0.28]
6. `CodigoElementoDespesa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **57** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 3.0, Máx: 96.0, Média: 35.69, DesvPad: 18.54]
7. `CodigoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 500.0, Máx: 761.0, Média: 532.87, DesvPad: 80.57]
8. `CodigoFuncao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **25** 🟢 [Enum] | 📊 **Numérica:** [Mín: 1.0, Máx: 28.0, Média: 10.68, DesvPad: 4.32]
9. `CodigoGrupoDespesa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **7** 🟢 [Enum] | 📊 **Numérica:** [Mín: 1.0, Máx: 4.0, Média: 2.92, DesvPad: 0.64]
10. `CodigoModalidade` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **16** 🟢 [Enum] | 📊 **Numérica:** [Mín: 40.0, Máx: 91.0, Média: 75.54, DesvPad: 20.44]
11. `CodigoPlanoOrcamentario` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **1091** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 1.0, Máx: 3343.0, Média: 688.56, DesvPad: 1033.52]
12. `CodigoPrograma` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **59** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 14.0, Máx: 901.0, Média: 181.72, DesvPad: 222.85]
13. `CodigoSubFuncao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **78** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 31.0, Máx: 846.0, Média: 276.95, DesvPad: 136.8]
14. `CodigoSubelementoDespesa` ➔ Nulos: **0.0%** | Zeros: **15.67%** | Distintos: **886** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 5876.0, Média: 2141.39, DesvPad: 1709.23]
15. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **125** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 10101.0, Máx: 500101.0, Média: 432919.43, DesvPad: 142061.88]
16. `CpfCnpjNis` ➔ Nulos: **0.0%** | Zeros: **15.76%** | Distintos: **23528** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 97530084000107.0, Média: 8225694586895.28, DesvPad: 14586161201911.93]
17. `DespesaEmpenhada` ➔ Nulos: **0.0%** | Zeros: **28.17%** | Distintos: **25158** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 20000000.0, Média: 107594.51, DesvPad: 751841.83]
18. `DespesaLiquidada` ➔ Nulos: **0.0%** | Zeros: **32.67%** | Distintos: **24268** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 7419049.54, Média: 86801.06, DesvPad: 414564.04]
19. `DespesaPaga` ➔ Nulos: **0.0%** | Zeros: **26.24%** | Distintos: **28152** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 9441183.98, Média: 92020.32, DesvPad: 456036.41]
20. `DotacaoAtualizada` ➔ Nulos: **0.0%** | Zeros: **21.69%** | Distintos: **28414** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 20000000.0, Média: 128087.85, DesvPad: 814308.41]
21. `DotacaoInicial` ➔ Nulos: **0.0%** | Zeros: **91.8%** | Distintos: **1954** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 21904000.0, Média: 99768.09, DesvPad: 1033281.8]
22. `ElementoDespesa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **57** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 8, Tam Máx: 68, Média: 25.38]
23. `Emenda` ➔ Nulos: **96.4%** | Zeros: **0.0%** | Distintos: **1430** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 12, Tam Máx: 12, Média: 12.0]
24. `Esfera` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📊 **Numérica:** [Mín: 10.0, Máx: 20.0, Média: 15.04, DesvPad: 5.0]
25. `Favorecido` ➔ Nulos: **15.67%** | Zeros: **0.0%** | Distintos: **23478** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 10, Tam Máx: 89, Média: 32.08]
26. `Fonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **56** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 30, Tam Máx: 98, Média: 38.85]
27. `Funcao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **25** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 11, Tam Máx: 21, Média: 18.96]
28. `GrupoDespesa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **7** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 13, Tam Máx: 26, Média: 24.05]
29. `Id` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **72523** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 65338387.0, Máx: 65339386.0, Média: 65338886.5, DesvPad: 288.67]
30. `Microregiao` ➔ Nulos: **0.0%** | Zeros: **72.08%** | Distintos: **11** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Numérica:** [Mín: 0.0, Máx: 59.0, Média: 20.29, DesvPad: 26.15]
31. `Modalidade` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **16** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 18, Tam Máx: 129, Média: 32.66]
32. `Municipio` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **79** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 320010.0, Máx: 999999.0, Média: 753945.0, DesvPad: 326652.88]
33. `NomeEsfera` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 16, Tam Máx: 30, Média: 23.06]
34. `NomeMicroregiao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **11** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 6, Tam Máx: 16, Média: 7.91]
35. `NomeMunicipio` ➔ Nulos: **80.31%** | Zeros: **0.0%** | Distintos: **78** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 4, Tam Máx: 23, Média: 11.25]
36. `NomeUnidadeOrcamentaria` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **111** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 32, Tam Máx: 57, Média: 41.39]
37. `PlanoOrcamentario` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **1089** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 4, Tam Máx: 88, Média: 23.93]
38. `Programa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **59** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 7, Tam Máx: 111, Média: 54.26]
39. `SubFuncao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **78** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 16, Tam Máx: 41, Média: 27.15]
40. `SubelementoDespesa` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **853** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 8, Tam Máx: 119, Média: 43.48]
41. `UnidadeGestora` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **125** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 32, Tam Máx: 57, Média: 41.2]
42. `UnidadeOrcamentaria` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **111** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 1101.0, Máx: 50101.0, Média: 43642.47, DesvPad: 14280.26]