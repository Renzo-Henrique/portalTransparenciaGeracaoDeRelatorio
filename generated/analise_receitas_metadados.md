# Relatório de Análise de Metadados - CKAN

Este documento apresenta a auditoria de arquivos desatualizados, o comparativo par a par entre os grupos de metadados, as chaves presentes e a indicação de chaves internas com valores idênticos nos arquivos.

---

## ⏰ Análise de Arquivos Desatualizados (> 1 Mês)

Abaixo estão listados os arquivos cuja data de última modificação/criação é superior a 1 mês:

- 📄 **`Receitas-2023.csv`** *(ID: `0fea9fda-9e19-4268-9a1e-e1ace5dcce3d`)*
  - *Data de referência:* `2026-08-28` (aproximadamente 2 meses atrás)
- 📄 **`Receitas-2024.csv`** *(ID: `e08d6239-0fc0-400c-8c69-256f7f2ff5fd`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`Receitas-2025.csv`** *(ID: `b499bf46-4df3-4fb7-a526-99c53c6c0902`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)

---

## 🔄 Comparação Par a Par entre Grupos de Metadados

### Comparação: Grupo `001` vs Grupo `002`
> *Todas as chaves do grupo `001` também estão presentes no grupo `002`.*

### Comparação: Grupo `001` vs Grupo `003`
Chaves presentes em **`001`** mas **ausentes** em **`003`**:
`delimiter`, `encoding`, `first_record_is_header`

### Comparação: Grupo `002` vs Grupo `001`
Chaves presentes em **`002`** mas **ausentes** em **`001`**:
`ckan_url`, `ignore_hash`, `original_url`, `queue_name`, `set_url_type`, `task_created`

### Comparação: Grupo `002` vs Grupo `003`
Chaves presentes em **`002`** mas **ausentes** em **`003`**:
`delimiter`, `encoding`, `first_record_is_header`

### Comparação: Grupo `003` vs Grupo `001`
Chaves presentes em **`003`** mas **ausentes** em **`001`**:
`ckan_url`, `ignore_hash`, `original_url`, `queue_name`, `set_url_type`, `task_created`

### Comparação: Grupo `003` vs Grupo `002`
> *Todas as chaves do grupo `003` também estão presentes no grupo `002`.*

---

## 📂 Grupo de Metadados: `001`

- **Total de Chaves de Metadados Identificadas:** `26`
- **Quantidade de Arquivos no Grupo:** `19`

**Arquivos Vinculados ao Grupo:**
  - 📄 **`receitas2020.csv`** *(ID: `254b1dbd-4eb0-429c-9a67-f5dc827d2d57`)*
  - 📄 **`receitas2018.csv`** *(ID: `5e28c8e6-464f-40ce-8c39-403a3d1344c8`)*
  - 📄 **`receitas2005.csv`** *(ID: `73aba44c-bf9a-4d27-8857-e0fa4d5ee90c`)*
  - 📄 **`receitas2007.csv`** *(ID: `8b5f5124-4e08-4cef-bfc6-1a94a180452b`)*
  - 📄 **`receitas2004.csv`** *(ID: `b6a19383-b5c0-4e03-8da0-c398e69a1b25`)*
  - 📄 **`receitas2012.csv`** *(ID: `533d9285-ce6a-42b7-a90b-70e201e52f5e`)*
  - 📄 **`receitas2013.csv`** *(ID: `86b1b10f-5457-4c5f-8d9a-3885703033c6`)*
  - 📄 **`receitas2014.csv`** *(ID: `4648ee95-b4a2-4189-8db7-8678ab5a9ef9`)*
  - 📄 **`receitas2017.csv`** *(ID: `fb0e5556-7f1b-4f08-b62f-6a2080faf5b3`)*
  - 📄 **`receitas2015.csv`** *(ID: `29181137-01d7-416d-8c74-934b89e0a49b`)*
  - 📄 **`receitas2019.csv`** *(ID: `e25110cb-31bf-47e2-aa6b-121e3ae6d3e3`)*
  - 📄 **`receitas2008.csv`** *(ID: `f5d276e6-74d8-411c-a99f-5ab9ddfab940`)*
  - 📄 **`receitas2006.csv`** *(ID: `022bc3e1-0c64-4bc8-96c7-9867e96b2fa3`)*
  - 📄 **`receitas2021.csv`** *(ID: `927c1391-5b16-4ba1-ade7-c474264bbb38`)*
  - 📄 **`receitas2023.csv`** *(ID: `d59902ff-41e5-4b61-a50d-9cf0769c74af`)*
  - 📄 **`Receitas-2023.csv`** *(ID: `0fea9fda-9e19-4268-9a1e-e1ace5dcce3d`)*
  - 📄 **`receitas2024.csv`** *(ID: `9ba06f4d-5c0e-4160-bad3-1a325e432496`)*
  - 📄 **`receitas2025.csv`** *(ID: `2dc2d874-0d72-4c01-b8a0-ecb6f392d6e4`)*
  - 📄 **`receitas2016.csv`** *(ID: `4e32b780-939e-4472-b166-00631f3b8244`)*

### 📋 Chaves de Metadados Presentes no Grupo:

`cache_last_updated`, `cache_url`, `created`, `datastore_active`, `datastore_contains_all_records_of_source_file`, `delimiter`, `description`, `encoding`, `first_record_is_header`, `format`, `hash`, `last_modified`, `metadata_modified`, `mimetype`, `mimetype_inner`, `package_id`, `position`, `resource_id`, `resource_type`, `size`, `state`, `tracking_summary`, `url`, `url_type`


---

### 🔍 Aviso: Chaves Internas com o Mesmo Valor no Arquivo

Abaixo estão indicados os casos em que chaves diferentes de um mesmo arquivo possuem exatamente o mesmo valor:

- **Chaves:** `id` e `resource_id`
    - *Apresentado nos arquivos:* `Receitas-2023.csv`, `receitas2004.csv`, `receitas2005.csv`, `receitas2006.csv`, `receitas2007.csv`, `receitas2008.csv`, `receitas2012.csv`, `receitas2013.csv`, `receitas2014.csv`, `receitas2015.csv`, `receitas2016.csv`, `receitas2017.csv`, `receitas2018.csv`, `receitas2019.csv`, `receitas2020.csv`, `receitas2021.csv`, `receitas2023.csv`, `receitas2024.csv`, `receitas2025.csv`
    - **Aviso:** Valores iguais somente ao considerar arquivos individualmente, os valores diferem entre arquivos

---

## 📂 Grupo de Metadados: `002`

- **Total de Chaves de Metadados Identificadas:** `32`
- **Quantidade de Arquivos no Grupo:** `7`

**Arquivos Vinculados ao Grupo:**
  - 📄 **`receitas2010.csv`** *(ID: `6ff68743-0b00-4d22-a5c2-400bf32ea260`)*
  - 📄 **`receitas2009.csv`** *(ID: `d2423087-21bf-4cb3-b846-2eddb43ee0e4`)*
  - 📄 **`receitas2011.csv`** *(ID: `f81fa1ba-ad88-4d3b-a4f4-f6bb7e09fd96`)*
  - 📄 **`receitas2022.csv`** *(ID: `72356e99-d084-45b4-9fd5-8347803cd68a`)*
  - 📄 **`DividaAtiva.csv`** *(ID: `016bbc36-15fb-476b-b249-d9726426c82c`)*
  - 📄 **`Receitas-2026.csv`** *(ID: `dcefa0ca-7e31-4b53-b6bd-0e559ef42d43`)*
  - 📄 **`receitas2026.csv`** *(ID: `58349543-d608-4bb6-b4a7-6483e9d2e3fb`)*

### 📋 Chaves de Metadados Presentes no Grupo:

`cache_last_updated`, `cache_url`, `ckan_url`, `created`, `datastore_active`, `datastore_contains_all_records_of_source_file`, `delimiter`, `description`, `encoding`, `first_record_is_header`, `format`, `hash`, `ignore_hash`, `last_modified`, `metadata_modified`, `mimetype`, `mimetype_inner`, `original_url`, `package_id`, `position`, `queue_name`, `resource_id`, `resource_type`, `set_url_type`, `size`, `state`, `task_created`, `tracking_summary`, `url`, `url_type`


---

### 🔍 Aviso: Chaves Internas com o Mesmo Valor no Arquivo

Abaixo estão indicados os casos em que chaves diferentes de um mesmo arquivo possuem exatamente o mesmo valor:

- **Chaves:** `datastore_active` e `datastore_contains_all_records_of_source_file`
    - *Apresentado nos arquivos:* `DividaAtiva.csv`, `Receitas-2026.csv`, `receitas2009.csv`, `receitas2010.csv`, `receitas2011.csv`, `receitas2022.csv`, `receitas2026.csv`
    - **Aviso:** Os valores não diferem entre arquivos

- **Chaves:** `id` e `resource_id`
    - *Apresentado nos arquivos:* `DividaAtiva.csv`, `Receitas-2026.csv`, `receitas2009.csv`, `receitas2010.csv`, `receitas2011.csv`, `receitas2022.csv`, `receitas2026.csv`
    - **Aviso:** Valores iguais somente ao considerar arquivos individualmente, os valores diferem entre arquivos

- **Chaves:** `ignore_hash` e `set_url_type`
    - *Apresentado nos arquivos:* `DividaAtiva.csv`, `Receitas-2026.csv`, `receitas2009.csv`, `receitas2010.csv`, `receitas2011.csv`, `receitas2022.csv`, `receitas2026.csv`
    - **Aviso:** Os valores não diferem entre arquivos

- **Chaves:** `original_url` e `url`
    - *Apresentado nos arquivos:* `DividaAtiva.csv`, `Receitas-2026.csv`, `receitas2009.csv`, `receitas2010.csv`, `receitas2011.csv`, `receitas2022.csv`, `receitas2026.csv`
    - **Aviso:** Valores iguais somente ao considerar arquivos individualmente, os valores diferem entre arquivos

---

## 📂 Grupo de Metadados: `003`

- **Total de Chaves de Metadados Identificadas:** `29`
- **Quantidade de Arquivos no Grupo:** `2`

**Arquivos Vinculados ao Grupo:**
  - 📄 **`Receitas-2024.csv`** *(ID: `e08d6239-0fc0-400c-8c69-256f7f2ff5fd`)*
  - 📄 **`Receitas-2025.csv`** *(ID: `b499bf46-4df3-4fb7-a526-99c53c6c0902`)*

### 📋 Chaves de Metadados Presentes no Grupo:

`cache_last_updated`, `cache_url`, `ckan_url`, `created`, `datastore_active`, `datastore_contains_all_records_of_source_file`, `description`, `format`, `hash`, `ignore_hash`, `last_modified`, `metadata_modified`, `mimetype`, `mimetype_inner`, `original_url`, `package_id`, `position`, `queue_name`, `resource_id`, `resource_type`, `set_url_type`, `size`, `state`, `task_created`, `tracking_summary`, `url`, `url_type`


---

### 🔍 Aviso: Chaves Internas com o Mesmo Valor no Arquivo

Abaixo estão indicados os casos em que chaves diferentes de um mesmo arquivo possuem exatamente o mesmo valor:

- **Chaves:** `datastore_active` e `datastore_contains_all_records_of_source_file` e `ignore_hash`
    - *Apresentado nos arquivos:* `Receitas-2024.csv`, `Receitas-2025.csv`
    - **Aviso:** Os valores não diferem entre arquivos

- **Chaves:** `id` e `resource_id`
    - *Apresentado nos arquivos:* `Receitas-2024.csv`, `Receitas-2025.csv`
    - **Aviso:** Valores iguais somente ao considerar arquivos individualmente, os valores diferem entre arquivos

---