# Relatório de Auditoria de Arquivo Local (Grande Porte)

- **Caminho do Arquivo:** `arquivos/Receitas-2025.csv`
- **Total de Linhas Auditadas:** `1004745`
- **Total de Colunas:** `48`

---

## 🛠️ Conferência de Erros na Estrutura do Arquivo

> ✅ **Nenhum erro estrutural detectado.** A consistência das colunas foi mantida em todos os blocos do arquivo.

---

## 📋 Qualidade e Estatísticas das Colunas

1. `_id` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **100000** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 1.0, Máx: 1001000.0, Média: 500500.5, DesvPad: 316227.9]
2. `ano` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **1** 🟢 [Enum] | 📊 **Numérica:** [Mín: 2025.0, Máx: 2025.0, Média: 2025.0, DesvPad: 0.0]
3. `codigoCategoria` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **3** 🟢 [Enum] | 📊 **Numérica:** [Mín: 1.0, Máx: 7.0, Média: 1.07, DesvPad: 0.61]
4. `codigoDetalhamento1` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **61** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 1112.0, Máx: 7922.0, Média: 1265.15, DesvPad: 669.62]
5. `codigoDetalhamento2` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **131** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 111251.0, Máx: 792299.0, Média: 126557.41, DesvPad: 66957.14]
6. `codigoDetalhamento3` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **150** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 1112510.0, Máx: 7922990.0, Média: 1265574.89, DesvPad: 669571.41]
7. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** | Zeros: **46.13%** | Distintos: **123** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 901001.0, Média: 20239.3, DesvPad: 59771.11]
8. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **257** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 500.0, Máx: 899.000675, Média: 538.42, DesvPad: 94.02]
9. `codigoEspecie` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **37** 🟢 [Enum] | 📊 **Numérica:** [Mín: 111.0, Máx: 792.0, Média: 126.17, DesvPad: 66.96]
10. `codigoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **59** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 500.0, Máx: 899.0, Média: 538.4, DesvPad: 94.02]
11. `codigoGrupoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **4** 🟢 [Enum] | 📊 **Numérica:** [Mín: 5.0, Máx: 8.0, Média: 5.32, DesvPad: 0.8]
12. `codigoIdUso` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📊 **Numérica:** [Mín: 1.0, Máx: 1.0, Média: 1.0, DesvPad: 0.0]
13. `codigoNatureza` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **188** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 11125101.0, Máx: 79229901.0, Média: 12655750.42, DesvPad: 6695713.99]
14. `codigoOrigem` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **17** 🟢 [Enum] | 📊 **Numérica:** [Mín: 11.0, Máx: 79.0, Média: 12.49, DesvPad: 6.68]
15. `codigoTipo` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **188** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 11125101.0, Máx: 79229901.0, Média: 12655750.42, DesvPad: 6695713.99]
16. `codigoUG` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 10101.0, Máx: 800102.0, Média: 731684.16, DesvPad: 165500.46]
17. `codigoUGEmitente` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **121** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 10101.0, Máx: 800102.0, Média: 723816.0, DesvPad: 177784.46]
18. `contaContabil` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **10** 🟢 [Enum] | 📊 **Numérica:** [Mín: 111113001.0, Máx: 621350000.0, Média: 461819809.4, DesvPad: 236142404.49]
19. `dataContabilizacao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **25574** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 19, Tam Máx: 19, Média: 19.0]
20. `dataEmissao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **287** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 19, Tam Máx: 19, Média: 19.0]
21. `descricaoCategoria` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **3** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 18, Tam Máx: 37, Média: 18.2]
22. `descricaoContaContabil` ➔ Nulos: **31.84%** | Zeros: **0.0%** | Distintos: **9** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Texto:** [Tam Mín: 17, Tam Máx: 45, Média: 19.27]
23. `descricaoDetalhamento1` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **49** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 10, Tam Máx: 169, Média: 52.93]
24. `descricaoDetalhamento2` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 10, Tam Máx: 145, Média: 57.36]
25. `descricaoDetalhamento3` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **132** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 10, Tam Máx: 154, Média: 113.81]
26. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **244** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 12, Tam Máx: 184, Média: 53.91]
27. `descricaoEspecie` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **31** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 5, Tam Máx: 68, Média: 12.0]
28. `descricaoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **59** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 26, Tam Máx: 141, Média: 36.64]
29. `descricaoGrupoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **1** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 50, Tam Máx: 50, Média: 50.0]
30. `descricaoIdUso` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 30, Tam Máx: 30, Média: 30.0]
31. `descricaoNatureza` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **179** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 22, Tam Máx: 195, Média: 117.94]
32. `descricaoOrigem` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **13** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 13, Tam Máx: 43, Média: 39.55]
33. `descricaoTipo` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **179** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 22, Tam Máx: 195, Média: 117.94]
34. `descricaoUG` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 16, Tam Máx: 87, Média: 37.19]
35. `descricaoUGEmitente` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **121** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 3, Tam Máx: 23, Média: 20.18]
36. `documento` ➔ Nulos: **0.0%** | Zeros: **0.04%** | Distintos: **10090** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 11, Tam Máx: 11, Média: 11.0]
37. `tipo` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **7** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 14, Tam Máx: 18, Média: 16.03]
38. `tipoLancamento` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 1, Tam Máx: 1, Média: 1.0]
39. `valorArrecadada` ➔ Nulos: **0.0%** | Zeros: **100.0%** | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Numérica:** [Mín: 0.0, Máx: 0.0, Média: 0.0, DesvPad: 0.0]
40. `valorArrecadadaBruta` ➔ Nulos: **0.0%** | Zeros: **79.81%** | Distintos: **18303** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: -35497191.47, Máx: 54306817.17, Média: 28274.59, DesvPad: 1017961.1]
41. `valorArrecadadaDeducao` ➔ Nulos: **0.0%** | Zeros: **96.28%** | Distintos: **10512** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: -12803550.0, Máx: 20617.95, Média: -7011.12, DesvPad: 159581.98]
42. `valorArrecadadaLiquida` ➔ Nulos: **0.0%** | Zeros: **76.09%** | Distintos: **21002** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: -13915960.02, Máx: 16538004.75, Média: 20519.73, DesvPad: 443798.17]
43. `valorPrevista` ➔ Nulos: **0.0%** | Zeros: **100.0%** | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Numérica:** [Mín: 0.0, Máx: 0.0, Média: 0.0, DesvPad: 0.0]
44. `valorPrevistaBruta` ➔ Nulos: **0.0%** | Zeros: **99.93%** | Distintos: **605** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 24001286.0, Média: 3785.57, DesvPad: 239912.66]
45. `valorPrevistaDeducao` ➔ Nulos: **0.0%** | Zeros: **99.99%** | Distintos: **50** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Numérica:** [Mín: 0.0, Máx: 0.0, Média: 0.0, DesvPad: 0.0]
46. `valorPrevistaLiquida` ➔ Nulos: **0.0%** | Zeros: **99.92%** | Distintos: **654** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 1983274603.0, Média: 377669.92, DesvPad: 23044186.63]
47. `valorRecolhida` ➔ Nulos: **0.0%** | Zeros: **100.0%** | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Numérica:** [Mín: 0.0, Máx: 0.0, Média: 0.0, DesvPad: 0.0]
48. `valorRecolhidaBruta` ➔ Nulos: **0.0%** | Zeros: **47.97%** | Distintos: **39774** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: -38410649.9, Máx: 50513444.23, Média: 41938.77, DesvPad: 1379515.15]

---

> **⚠️ Aviso: Colunas com exatamente as mesmas estatísticas de dados (possíveis colunas duplicadas com nomes diferentes):**

> - `codigoNatureza`, `codigoTipo`

> - `descricaoNatureza`, `descricaoTipo`

> - `valorArrecadada`, `valorPrevista`, `valorRecolhida`
