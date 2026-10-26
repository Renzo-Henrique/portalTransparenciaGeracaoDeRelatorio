# Relatório de Auditoria de Arquivo Único (Grande Porte)

- **ID do Recurso:** `2dc2d874-0d72-4c01-b8a0-ecb6f392d6e4`
- **Total de Linhas Auditadas:** `1004745`
- **Total de Colunas:** `47`

---

## 🛠️ Conferência de Erros na Estrutura do Arquivo

> ✅ **Nenhum erro estrutural detectado.** A integridade e consistência das colunas foram mantidas em todas as páginas.

---

## 📋 Qualidade e Estatísticas das Colunas

1. `ano` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **1** 🟢 [Enum] | 📊 **Númerica:** [Mín: 2025.0, Máx: 2025.0, Média: 2025.0, DesvPad: 0.0]
2. `codigoCategoria` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **3** 🟢 [Enum] | 📊 **Númerica:** [Mín: 1.0, Máx: 7.0, Média: 1.08, DesvPad: 0.69]
3. `codigoDetalhamento1` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **61** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: 1112.0, Máx: 7923.0, Média: 1285.96, DesvPad: 739.07]
4. `codigoDetalhamento2` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **131** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: 111251.0, Máx: 792399.0, Média: 128637.95, DesvPad: 73901.25]
5. `codigoDetalhamento3` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **150** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: 1112510.0, Máx: 7923990.0, Média: 1286380.25, DesvPad: 739012.5]
6. `codigoDetalhamentoFonte` ➔ Nulos: **0.0%** | Zeros: **46.13%** | Distintos: **123** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: 0.0, Máx: 901001.0, Média: 21175.92, DesvPad: 64693.8]
7. `codigoDetalhamentoFonteAux` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **257** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: 500.0, Máx: 899.000675, Média: 541.19, DesvPad: 97.18]
8. `codigoEspecie` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **37** 🟢 [Enum] | 📊 **Númerica:** [Mín: 111.0, Máx: 792.0, Média: 128.26, DesvPad: 73.91]
9. `codigoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **59** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: 500.0, Máx: 899.0, Média: 541.17, DesvPad: 97.17]
10. `codigoGrupoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **4** 🟢 [Enum] | 📊 **Númerica:** [Mín: 5.0, Máx: 8.0, Média: 5.35, DesvPad: 0.83]
11. `codigoIdUso` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📊 **Númerica:** [Mín: 1.0, Máx: 2.0, Média: 1.0, DesvPad: 0.01]
12. `codigoNatureza` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **188** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: 11125101.0, Máx: 79239901.0, Média: 12863804.03, DesvPad: 7390124.87]
13. `codigoOrigem` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **17** 🟢 [Enum] | 📊 **Númerica:** [Mín: 11.0, Máx: 79.0, Média: 12.7, DesvPad: 7.38]
14. `codigoTipo` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **188** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: 11125101.0, Máx: 79239901.0, Média: 12863804.03, DesvPad: 7390124.87]
15. `codigoUG` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: 10101.0, Máx: 800102.0, Média: 727458.6, DesvPad: 173500.34]
16. `codigoUGEmitente` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **121** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: 10101.0, Máx: 800102.0, Média: 718821.68, DesvPad: 186440.0]
17. `contaContabil` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **10** 🟢 [Enum] | 📊 **Númerica:** [Mín: 111113001.0, Máx: 621390000.0, Média: 458631424.49, DesvPad: 237562825.59]
18. `dataContabilizacao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **46165** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 19, Tam Máx: 19, Média: 19.0]
19. `dataEmissao` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **287** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 19, Tam Máx: 19, Média: 19.0]
20. `descricaoCategoria` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **3** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 18, Tam Máx: 37, Média: 18.25]
21. `descricaoContaContabil` ➔ Nulos: **31.84%** | Zeros: **0.0%** | Distintos: **9** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📝 **Texto:** [Tam Mín: 17, Tam Máx: 45, Média: 19.2]
22. `descricaoDetalhamento1` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **49** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 10, Tam Máx: 169, Média: 52.67]
23. `descricaoDetalhamento2` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 10, Tam Máx: 145, Média: 57.19]
24. `descricaoDetalhamento3` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **132** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 10, Tam Máx: 154, Média: 112.43]
25. `descricaoDetalhamentoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **244** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 12, Tam Máx: 219, Média: 54.01]
26. `descricaoEspecie` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **31** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 5, Tam Máx: 84, Média: 12.21]
27. `descricaoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **59** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 26, Tam Máx: 141, Média: 36.75]
28. `descricaoGrupoFonte` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **1** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 50, Tam Máx: 50, Média: 50.0]
29. `descricaoIdUso` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 30, Tam Máx: 33, Média: 30.0]
30. `descricaoNatureza` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **179** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 22, Tam Máx: 195, Média: 116.65]
31. `descricaoOrigem` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **13** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 13, Tam Máx: 43, Média: 39.26]
32. `descricaoTipo` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **179** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 22, Tam Máx: 195, Média: 116.65]
33. `descricaoUG` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **116** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 16, Tam Máx: 90, Média: 37.12]
34. `descricaoUGEmitente` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **121** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 3, Tam Máx: 23, Média: 20.07]
35. `documento` ➔ Nulos: **0.0%** | Zeros: **0.04%** | Distintos: **18984** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 11, Tam Máx: 11, Média: 11.0]
36. `tipo` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **7** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 14, Tam Máx: 18, Média: 16.03]
37. `tipoLancamento` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **2** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 1, Tam Máx: 1, Média: 1.0]
38. `valorArrecadada` ➔ Nulos: **0.0%** | Zeros: **100.0%** | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Númerica:** [Mín: 0.0, Máx: 0.0, Média: 0.0, DesvPad: 0.0]
39. `valorArrecadadaBruta` ➔ Nulos: **0.0%** | Zeros: **79.81%** | Distintos: **167276** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: -200746979.69, Máx: 1059074681.87, Média: 42763.67, DesvPad: 2554779.25]
40. `valorArrecadadaDeducao` ➔ Nulos: **0.0%** | Zeros: **96.28%** | Distintos: **33156** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: -103580184.16, Máx: 9551885.1, Média: -10931.32, DesvPad: 491228.48]
41. `valorArrecadadaLiquida` ➔ Nulos: **0.0%** | Zeros: **76.09%** | Distintos: **169078** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: -200746979.69, Máx: 1059074681.87, Média: 31832.35, DesvPad: 2601756.59]
42. `valorPrevista` ➔ Nulos: **0.0%** | Zeros: **100.0%** | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Númerica:** [Mín: 0.0, Máx: 0.0, Média: 0.0, DesvPad: 0.0]
43. `valorPrevistaBruta` ➔ Nulos: **0.0%** | Zeros: **99.93%** | Distintos: **605** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: -991959.09, Máx: 10309951685.0, Média: 41759.5, DesvPad: 12379447.2]
44. `valorPrevistaDeducao` ➔ Nulos: **0.0%** | Zeros: **99.99%** | Distintos: **50** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Númerica:** [Mín: -4113462213.0, Máx: 0.0, Média: -10478.92, DesvPad: 5307636.92]
45. `valorPrevistaLiquida` ➔ Nulos: **0.0%** | Zeros: **99.92%** | Distintos: **654** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: -4113462213.0, Máx: 10309951685.0, Média: 31280.58, DesvPad: 13469320.62]
46. `valorRecolhida` ➔ Nulos: **0.0%** | Zeros: **100.0%** | Distintos: **1** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] | 📊 **Númerica:** [Mín: 0.0, Máx: 0.0, Média: 0.0, DesvPad: 0.0]
47. `valorRecolhidaBruta` ➔ Nulos: **0.0%** | Zeros: **47.97%** | Distintos: **242911** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Númerica:** [Mín: -517900920.81, Máx: 1059074681.87, Média: 42626.72, DesvPad: 3850796.32]