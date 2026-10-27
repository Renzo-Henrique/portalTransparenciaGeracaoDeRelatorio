# Relatório de Auditoria de Arquivo Local (Grande Porte)

- **Caminho do Arquivo:** `arquivos/RestosAPagar-2024.csv`
- **Total de Linhas Auditadas:** `8770`
- **Total de Colunas:** `13`

---

## 🛠️ Conferência de Erros na Estrutura do Arquivo

> ✅ **Nenhum erro estrutural detectado.** A consistência das colunas foi mantida em todos os blocos do arquivo.

---

## 📋 Qualidade e Estatísticas das Colunas

1. `Ano` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **1** 🟢 [Enum] | 📊 **Numérica:** [Mín: 2024.0, Máx: 2024.0, Média: 2024.0, DesvPad: 0.0]
2. `CodigoElemento` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **80** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 319004.0, Máx: 449093.0, Média: 365059.74, DesvPad: 47899.95]
3. `CodigoPoder` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **4** 🟢 [Enum] | 📊 **Numérica:** [Mín: 1.0, Máx: 6.0, Média: 4.71, DesvPad: 0.98]
4. `CodigoUnidadeGestora` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **107** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 10101.0, Máx: 600201.0, Média: 331175.01, DesvPad: 146789.91]
5. `CpfCnpjNis` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **4766** ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 6, Tam Máx: 14, Média: 13.24]
6. `Elemento` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **46** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 8, Tam Máx: 69, Média: 34.02]
7. `Favorecido` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **4737** ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 9, Tam Máx: 100, Média: 34.69]
8. `Id` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **8770** ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 1.0, Máx: 1000.0, Média: 500.5, DesvPad: 288.67]
9. `Poder` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **4** 🟢 [Enum] | 📝 **Texto:** [Tam Mín: 15, Tam Máx: 18, Média: 15.17]
10. `UnidadeGestora` ➔ Nulos: **0.0%** | Zeros: **0.0%** | Distintos: **107** 🟢 [Enum] ⚠️ [Caso 2: >50 Distintos] | 📝 **Texto:** [Tam Mín: 3, Tam Máx: 19, Média: 5.61]
11. `ValorNaoProcessado` ➔ Nulos: **0.0%** | Zeros: **93.58%** | Distintos: **537** ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 13436140.61, Média: 49654.83, DesvPad: 519817.87]
12. `ValorNaoProcessadoLiquidado` ➔ Nulos: **0.0%** | Zeros: **97.59%** | Distintos: **203** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 2514247.55, Média: 6732.88, DesvPad: 90641.19]
13. `ValorProcessado` ➔ Nulos: **0.0%** | Zeros: **97.21%** | Distintos: **210** 🟢 [Enum] ⚠️ [Caso 1: >50 Nulos/Zeros] ⚠️ [Caso 2: >50 Distintos] | 📊 **Numérica:** [Mín: 0.0, Máx: 17900.41, Média: 33.3, DesvPad: 659.91]