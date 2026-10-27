# Relatório de Auditoria de Arquivo Local (Grande Porte)

- **Caminho do Arquivo:** `arquivos/orcamentosexecucoes-2025.csv`
- **Total de Linhas Auditadas:** `125`
- **Total de Colunas:** `11`

---

## 🛠️ Conferência de Erros na Estrutura do Arquivo

> ✅ **Nenhum erro estrutural detectado.** A consistência das colunas foi mantida em todos os blocos do arquivo.

---

## 📋 Qualidade e Estatísticas das Colunas

1. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **125** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 10101.0, Máx: 800104.0, Média: 363622.26, DesvPad: 159947.34]
2. `Data` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **1** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 19, Tam Máx: 19, Média: 19.0]
3. `Id` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **125** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 693635.0, Máx: 693759.0, Média: 693697.0, DesvPad: 36.08]
4. `SiglaUnidadeGestora` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **125** ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 4, Tam Máx: 90, Média: 44.62]
5. `UnidadeGestora` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **125** ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 16, Tam Máx: 90, Média: 47.45]
6. `ValorEmpenho` ➔ Nulos: **0.0%** | Zeros: **7.2%** | Distintos: **117** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 4788599153.95, Média: 248761444.97, DesvPad: 686463456.78]
7. `ValorLiquidado` ➔ Nulos: **0.0%** | Zeros: **7.2%** | Distintos: **117** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 4602955744.27, Média: 234497116.09, DesvPad: 660298201.45]
8. `ValorOrcado` ➔ Nulos: **0.0%** | Zeros: **4.0%** | Distintos: **120** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 5426690790.98, Média: 282424846.65, DesvPad: 745470629.5]
9. `ValorOrcadoInicial` ➔ Nulos: **0.0%** | Zeros: **4.0%** | Distintos: **119** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 4133596213.0, Média: 236144757.18, DesvPad: 652022151.89]
10. `ValorPago` ➔ Nulos: **0.0%** | Zeros: **7.2%** | Distintos: **117** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 4560087385.15, Média: 230664832.55, DesvPad: 652913089.38]
11. `ValorRap` ➔ Nulos: **0.0%** | Zeros: **12.8%** | Distintos: **110** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 484008397.04, Média: 14668530.62, DesvPad: 53832596.7]