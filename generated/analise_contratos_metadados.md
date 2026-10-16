# Relatório de Análise de Metadados - CKAN

Este documento apresenta a auditoria de arquivos desatualizados, o comparativo par a par entre os grupos de metadados, as chaves presentes e a indicação de chaves internas com valores idênticos nos arquivos.

---

## ⏰ Análise de Arquivos Desatualizados (> 1 Mês)

Abaixo estão listados os arquivos cuja data de última modificação/criação é superior a 1 mês:

- 📄 **`Contratos-2027.csv`** *(ID: `d71c0ab8-8ef4-4fe5-bdaf-9dfcd44c0e86`)*
  - *Data de referência:* `2026-08-05` (aproximadamente 2 meses atrás)
- 📄 **`Contratos-2028.csv`** *(ID: `ff1b6e80-9feb-4623-a7e3-758174ecb988`)*
  - *Data de referência:* `2026-06-23` (aproximadamente 4 meses atrás)
- 📄 **`AlteracoesContratuais-2001.csv`** *(ID: `8143a07a-d141-472b-a9c0-531f4dc26d5c`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`AlteracoesContratuais-2008.csv`** *(ID: `0ce629ce-8b6c-40eb-bca5-590133c035a9`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`AlteracoesContratuais-1753.csv`** *(ID: `5bcc2b46-7d94-4d4a-aaae-7495b2c21272`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`AlteracoesContratuais-2006.csv`** *(ID: `4952d33b-3813-4b0e-b33e-7e34cec0ad99`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`AlteracoesContratuais-2009.csv`** *(ID: `33ebb82b-7a58-430a-9037-55b4431fb653`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`AlteracoesContratuais-3024.csv`** *(ID: `31ceeba6-7138-4ee5-8b8c-149e237a4269`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`Empenhos-3024.csv`** *(ID: `81ecafd8-68dd-4200-ba61-6b111a3699a9`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`AlteracoesContratuais-2032.csv`** *(ID: `caee0c6f-6a11-4c38-ab4c-ddcbcf93f9c9`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`AlteracoesContratuais-2027.csv`** *(ID: `b485281e-da1d-4d8d-a877-4d9d0feb4dbd`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`Empenhos-2027.csv`** *(ID: `c062f0c1-8668-4c4b-8623-9d8b07bfd514`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`AlteracoesContratuais-2224.csv`** *(ID: `2f9849af-afb1-4a51-8659-97991705af9c`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`AlteracoesContratuais-5024.csv`** *(ID: `426359c7-c7a6-4cab-bb77-7608261c4a87`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`Empenhos-5024.csv`** *(ID: `7cf61401-2a8f-442a-9325-caceb7604a0a`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`AlteracoesContratuais-1991.csv`** *(ID: `75b13225-35ec-4a84-a722-12a5c4895627`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`Empenhos-1991.csv`** *(ID: `24e3a501-e87e-4773-8d65-222024e588f6`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`Contratos-2224.csv`** *(ID: `db608579-ff45-41ad-b65b-8913e981d94f`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`Empenhos-2224.csv`** *(ID: `2f63817b-3602-495e-b074-abb614c72336`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)
- 📄 **`Contratos-5024.csv`** *(ID: `c0533a5f-3ef2-403d-9c31-dfeef4da40f5`)*
  - *Data de referência:* `2026-05-22` (aproximadamente 5 meses atrás)

---

## 🔄 Comparação Par a Par entre Grupos de Metadados

### Comparação: Grupo `001` vs Grupo `002`
Chaves presentes em **`001`** mas **ausentes** em **`002`**:
`ckan_url`, `ignore_hash`, `original_url`, `queue_name`, `set_url_type`, `task_created`

### Comparação: Grupo `001` vs Grupo `003`
Chaves presentes em **`001`** mas **ausentes** em **`003`**:
`ckan_url`, `delimiter`, `encoding`, `first_record_is_header`, `ignore_hash`, `original_url`, `queue_name`, `resource_id`, `set_url_type`, `task_created`

### Comparação: Grupo `001` vs Grupo `004`
Chaves presentes em **`001`** mas **ausentes** em **`004`**:
`delimiter`, `encoding`, `first_record_is_header`

### Comparação: Grupo `002` vs Grupo `001`
> *Todas as chaves do grupo `002` também estão presentes no grupo `001`.*

### Comparação: Grupo `002` vs Grupo `003`
Chaves presentes em **`002`** mas **ausentes** em **`003`**:
`delimiter`, `encoding`, `first_record_is_header`, `resource_id`

### Comparação: Grupo `002` vs Grupo `004`
Chaves presentes em **`002`** mas **ausentes** em **`004`**:
`delimiter`, `encoding`, `first_record_is_header`

### Comparação: Grupo `003` vs Grupo `001`
> *Todas as chaves do grupo `003` também estão presentes no grupo `001`.*

### Comparação: Grupo `003` vs Grupo `002`
> *Todas as chaves do grupo `003` também estão presentes no grupo `002`.*

### Comparação: Grupo `003` vs Grupo `004`
> *Todas as chaves do grupo `003` também estão presentes no grupo `004`.*

### Comparação: Grupo `004` vs Grupo `001`
> *Todas as chaves do grupo `004` também estão presentes no grupo `001`.*

### Comparação: Grupo `004` vs Grupo `002`
Chaves presentes em **`004`** mas **ausentes** em **`002`**:
`ckan_url`, `ignore_hash`, `original_url`, `queue_name`, `set_url_type`, `task_created`

### Comparação: Grupo `004` vs Grupo `003`
Chaves presentes em **`004`** mas **ausentes** em **`003`**:
`ckan_url`, `ignore_hash`, `original_url`, `queue_name`, `resource_id`, `set_url_type`, `task_created`

---

## 📂 Grupo de Metadados: `001`

- **Total de Chaves de Metadados Identificadas:** `32`
- **Quantidade de Arquivos no Grupo:** `77`

**Arquivos Vinculados ao Grupo:**
  - 📄 **`Contratos-2020.csv`** *(ID: `8f8c75b7-d22c-4110-b200-d2fbeb9dedbf`)*
  - 📄 **`Empenhos-2020.csv`** *(ID: `c77e25e0-5f94-4d5c-bf42-314415a950cc`)*
  - 📄 **`Contratos-2013.csv`** *(ID: `87afa923-9767-4244-b973-528e1ae9ebf8`)*
  - 📄 **`Empenhos-2016.csv`** *(ID: `32cbbdd2-1d4a-4c14-b3af-bfb863dec69e`)*
  - 📄 **`Empenhos-2013.csv`** *(ID: `e9a732c6-fd69-4323-a00d-c78d31541c2d`)*
  - 📄 **`Empenhos-2014.csv`** *(ID: `021fec2d-0ef3-479b-981e-ca3d5385d3a0`)*
  - 📄 **`Empenhos-2010.csv`** *(ID: `c2947dcf-b520-406b-ae1c-a50bc53072e0`)*
  - 📄 **`Empenhos-2001.csv`** *(ID: `f5291377-c675-4a98-8982-daeb1b93ca56`)*
  - 📄 **`Empenhos-1753.csv`** *(ID: `fdc3f16d-c46b-440c-9859-10435aed5894`)*
  - 📄 **`Contratos-2014.csv`** *(ID: `2951b922-fd9e-4c9a-85a1-423969127cc8`)*
  - 📄 **`Empenhos-2008.csv`** *(ID: `70be15fd-682b-4e77-9ed5-a9933512870b`)*
  - 📄 **`Empenhos-2011.csv`** *(ID: `19f3c11d-5571-4d78-980d-9606198daae3`)*
  - 📄 **`Empenhos-2017.csv`** *(ID: `02c3550d-d813-4e22-8cce-eb13a1fc41d8`)*
  - 📄 **`Empenhos-2006.csv`** *(ID: `b423d494-3c3a-42c0-8d46-03b82729e12f`)*
  - 📄 **`Empenhos-2012.csv`** *(ID: `7d8a1e2e-ca97-4c6b-b773-d946d27f4167`)*
  - 📄 **`Contratos-2018.csv`** *(ID: `479a6c98-041c-485f-8029-845672218806`)*
  - 📄 **`Empenhos-2018.csv`** *(ID: `ebacf738-848f-4de5-9d58-4362a1aa39c8`)*
  - 📄 **`Empenhos-2015.csv`** *(ID: `0205d350-0004-4c48-9e9b-a5394ab3c64f`)*
  - 📄 **`Empenhos-2019.csv`** *(ID: `cfa9f537-0545-4ee7-8a9e-f05fa902554e`)*
  - 📄 **`Empenhos-2009.csv`** *(ID: `68e97349-c39e-452d-acc8-6ff8b9c67bf8`)*
  - 📄 **`Contratos-2021.csv`** *(ID: `01eab5a5-9c8f-4dd4-bf31-dcdbae5f2b5a`)*
  - 📄 **`Empenhos-2021.csv`** *(ID: `d4c95c4e-9dea-4d87-b8bf-9c9dacbd50ca`)*
  - 📄 **`AlteracoesContratuais-2012.csv`** *(ID: `21391d94-29d8-491d-bf6f-e0b5a529557c`)*
  - 📄 **`AlteracoesContratuais-2011.csv`** *(ID: `98d16b88-2558-4203-a4cb-430e964dd9fb`)*
  - 📄 **`AlteracoesContratuais-2015.csv`** *(ID: `eca8003b-4fb2-42b0-9ae2-e823fb1b64c5`)*
  - 📄 **`AlteracoesContratuais-2010.csv`** *(ID: `2bfc9572-b695-43e6-b442-358adf62f160`)*
  - 📄 **`AlteracoesContratuais-2021.csv`** *(ID: `660503c5-8879-4f93-b44c-b8edb1f92b17`)*
  - 📄 **`AlteracoesContratuais-2016.csv`** *(ID: `8119beab-e65a-4eb6-a752-cd4fcdae1bd2`)*
  - 📄 **`AlteracoesContratuais-2020.csv`** *(ID: `3bd637c7-42c5-4096-800d-90642f4286d8`)*
  - 📄 **`AlteracoesContratuais-2013.csv`** *(ID: `5711c158-463f-4a01-9a9e-7e394aa263ed`)*
  - 📄 **`AlteracoesContratuais-2019.csv`** *(ID: `6ce5abc5-feca-4205-a682-90024a0961af`)*
  - 📄 **`AlteracoesContratuais-2014.csv`** *(ID: `654425b1-283a-4773-b3b0-16b525ade118`)*
  - 📄 **`AlteracoesContratuais-2017.csv`** *(ID: `06bef32f-ae82-4c18-9c46-736d8c688f6c`)*
  - 📄 **`AlteracoesContratuais-2018.csv`** *(ID: `086e01a9-ab6b-4df9-ad43-7a35433130ac`)*
  - 📄 **`Contratos-2022.csv`** *(ID: `f9b04d92-9b41-4379-847b-221cd03f20af`)*
  - 📄 **`AlteracoesContratuais-2022.csv`** *(ID: `ac3e6d8b-98c8-4249-acd0-b2cdea095878`)*
  - 📄 **`Empenhos-2022.csv`** *(ID: `a5f1c107-21b4-40df-b41f-576d3e566d35`)*
  - 📄 **`Contratos-2023.csv`** *(ID: `e54cca38-8bda-45ac-b342-f25c77ee0a7f`)*
  - 📄 **`AlteracoesContratuais-2023.csv`** *(ID: `edf68ba8-a232-4d1e-87b0-8b7544343b75`)*
  - 📄 **`Empenhos-2023.csv`** *(ID: `330bb165-b390-4f40-896d-203ad7be50ef`)*
  - 📄 **`Contratos-2024.csv`** *(ID: `85e4d84d-3738-4067-b2e1-a2bb8c80f84b`)*
  - 📄 **`AlteracoesContratuais-2024.csv`** *(ID: `5df70394-0990-484a-a006-9e2f8e95bfd7`)*
  - 📄 **`Empenhos-2024.csv`** *(ID: `5cfe1779-1468-4a7a-9f67-cbd006ed3475`)*
  - 📄 **`Contratos-3024.csv`** *(ID: `1b620ab8-bdba-40d5-9af7-95e78787def3`)*
  - 📄 **`Contratos-2032.csv`** *(ID: `6fe0aaeb-424d-4f23-bb63-77459f2f030d`)*
  - 📄 **`Empenhos-2032.csv`** *(ID: `5278768f-1dc9-4153-b674-31866522b598`)*
  - 📄 **`Contratos-2027.csv`** *(ID: `d71c0ab8-8ef4-4fe5-bdaf-9dfcd44c0e86`)*
  - 📄 **`Contratos-2025.csv`** *(ID: `54a632a4-cb07-4e85-98f9-5f47f1e024b7`)*
  - 📄 **`AlteracoesContratuais-2025.csv`** *(ID: `7d75a274-224b-4321-a8fe-2d47066a9381`)*
  - 📄 **`Empenhos-2025.csv`** *(ID: `d8d5b375-1b69-44ff-aadd-d5a467323918`)*
  - 📄 **`Contratos-2026.csv`** *(ID: `7b39e272-5914-4a8a-a7d6-30b174fce210`)*
  - 📄 **`AlteracoesContratuais-2026.csv`** *(ID: `780d3991-818f-4dd3-a753-3cbe7ae72cd0`)*
  - 📄 **`Empenhos-2026.csv`** *(ID: `ffd20ce7-7f30-404b-a3be-a838e6706336`)*
  - 📄 **`Contratos-1991.csv`** *(ID: `1fabe5d9-8252-432e-9506-b3d6697651f6`)*
  - 📄 **`Comissoes-1753.csv`** *(ID: `b7a159e3-5d31-4dae-b784-399b80af3853`)*
  - 📄 **`Comissoes-2001.csv`** *(ID: `a96682ec-60f9-4f23-9072-56bb00033fb2`)*
  - 📄 **`Comissoes-2006.csv`** *(ID: `30e27d07-901f-4295-ae6a-5ef1af8a7808`)*
  - 📄 **`Comissoes-2008.csv`** *(ID: `09bc6d30-7469-4f0d-b1b8-8fd747d91a30`)*
  - 📄 **`Comissoes-2009.csv`** *(ID: `0e6d7a1e-cac7-497c-a451-133b78076126`)*
  - 📄 **`Comissoes-2010.csv`** *(ID: `a15975e4-ebbd-4d8c-98e0-aed4aac8e8fa`)*
  - 📄 **`Comissoes-2011.csv`** *(ID: `5d1070ca-30eb-40e9-9110-34e14bdc0562`)*
  - 📄 **`Comissoes-2012.csv`** *(ID: `16294819-6e4f-467f-a87e-d8aac7fe2a00`)*
  - 📄 **`Comissoes-2013.csv`** *(ID: `ca7a4ff5-7a4d-4bf1-99f2-4843d6d637be`)*
  - 📄 **`Comissoes-2014.csv`** *(ID: `375e9b0d-5952-4ca9-b1fd-05a2164c65e8`)*
  - 📄 **`Comissoes-2015.csv`** *(ID: `89096f83-d0e6-4682-8c83-65529eb8854a`)*
  - 📄 **`Comissoes-2016.csv`** *(ID: `b9e60b25-559d-484b-82d5-854f0275aae4`)*
  - 📄 **`Comissoes-2017.csv`** *(ID: `01d61061-0d5c-43af-b6a3-6eb2cfe909a7`)*
  - 📄 **`Comissoes-2018.csv`** *(ID: `87eb4bd0-cb01-411e-acc1-29708e42a8df`)*
  - 📄 **`Comissoes-2019.csv`** *(ID: `6c4c3d1a-d2fa-4999-9bba-5b51de43cb2e`)*
  - 📄 **`Comissoes-2020.csv`** *(ID: `588c43bf-23bc-463c-9be6-794cdcf57cfd`)*
  - 📄 **`Comissoes-2021.csv`** *(ID: `70a90009-81f6-4bf3-b665-840a35140831`)*
  - 📄 **`Comissoes-2022.csv`** *(ID: `8918a8a2-9a6b-4e5b-8800-c5c4d6b2ef84`)*
  - 📄 **`Comissoes-2023.csv`** *(ID: `2ad8ecc6-a6b5-48c2-b6dd-014494e39d27`)*
  - 📄 **`Comissoes-2024.csv`** *(ID: `9065970b-608a-4874-bc35-bdf6516d9f3e`)*
  - 📄 **`Comissoes-2025.csv`** *(ID: `89ae9787-e943-4795-99e3-cc658e9aa9a5`)*
  - 📄 **`Comissoes-2026.csv`** *(ID: `e5a22c7e-6db9-42ba-bc65-903b0c96d9c3`)*
  - 📄 **`Contratos-2028.csv`** *(ID: `ff1b6e80-9feb-4623-a7e3-758174ecb988`)*

### 📋 Chaves de Metadados Presentes no Grupo:

`cache_last_updated`, `cache_url`, `ckan_url`, `created`, `datastore_active`, `datastore_contains_all_records_of_source_file`, `delimiter`, `description`, `encoding`, `first_record_is_header`, `format`, `hash`, `ignore_hash`, `last_modified`, `metadata_modified`, `mimetype`, `mimetype_inner`, `original_url`, `package_id`, `position`, `queue_name`, `resource_id`, `resource_type`, `set_url_type`, `size`, `state`, `task_created`, `tracking_summary`, `url`, `url_type`


---

### 🔍 Aviso: Chaves Internas com o Mesmo Valor no Arquivo

Abaixo estão indicados os casos em que chaves diferentes de um mesmo arquivo possuem exatamente o mesmo valor:

- **Chaves:** `datastore_active` e `datastore_contains_all_records_of_source_file`
    - *Apresentado nos arquivos:* `AlteracoesContratuais-2010.csv`, `AlteracoesContratuais-2011.csv`, `AlteracoesContratuais-2012.csv`, `AlteracoesContratuais-2013.csv`, `AlteracoesContratuais-2014.csv`, `AlteracoesContratuais-2015.csv`, `AlteracoesContratuais-2016.csv`, `AlteracoesContratuais-2017.csv`, `AlteracoesContratuais-2018.csv`, `AlteracoesContratuais-2019.csv`, `AlteracoesContratuais-2020.csv`, `AlteracoesContratuais-2021.csv`, `AlteracoesContratuais-2022.csv`, `AlteracoesContratuais-2023.csv`, `AlteracoesContratuais-2024.csv`, `AlteracoesContratuais-2025.csv`, `AlteracoesContratuais-2026.csv`, `Comissoes-1753.csv`, `Comissoes-2001.csv`, `Comissoes-2006.csv`, `Comissoes-2008.csv`, `Comissoes-2009.csv`, `Comissoes-2010.csv`, `Comissoes-2011.csv`, `Comissoes-2012.csv`, `Comissoes-2013.csv`, `Comissoes-2014.csv`, `Comissoes-2015.csv`, `Comissoes-2016.csv`, `Comissoes-2017.csv`, `Comissoes-2018.csv`, `Comissoes-2019.csv`, `Comissoes-2020.csv`, `Comissoes-2021.csv`, `Comissoes-2022.csv`, `Comissoes-2023.csv`, `Comissoes-2024.csv`, `Comissoes-2025.csv`, `Comissoes-2026.csv`, `Contratos-1991.csv`, `Contratos-2013.csv`, `Contratos-2014.csv`, `Contratos-2018.csv`, `Contratos-2020.csv`, `Contratos-2021.csv`, `Contratos-2022.csv`, `Contratos-2023.csv`, `Contratos-2024.csv`, `Contratos-2025.csv`, `Contratos-2026.csv`, `Contratos-2027.csv`, `Contratos-2028.csv`, `Contratos-2032.csv`, `Contratos-3024.csv`, `Empenhos-1753.csv`, `Empenhos-2001.csv`, `Empenhos-2006.csv`, `Empenhos-2008.csv`, `Empenhos-2009.csv`, `Empenhos-2010.csv`, `Empenhos-2011.csv`, `Empenhos-2012.csv`, `Empenhos-2013.csv`, `Empenhos-2014.csv`, `Empenhos-2015.csv`, `Empenhos-2016.csv`, `Empenhos-2017.csv`, `Empenhos-2018.csv`, `Empenhos-2019.csv`, `Empenhos-2020.csv`, `Empenhos-2021.csv`, `Empenhos-2022.csv`, `Empenhos-2023.csv`, `Empenhos-2024.csv`, `Empenhos-2025.csv`, `Empenhos-2026.csv`, `Empenhos-2032.csv`
    - **Aviso:** Os valores não diferem entre arquivos

- **Chaves:** `id` e `resource_id`
    - *Apresentado nos arquivos:* `AlteracoesContratuais-2010.csv`, `AlteracoesContratuais-2011.csv`, `AlteracoesContratuais-2012.csv`, `AlteracoesContratuais-2013.csv`, `AlteracoesContratuais-2014.csv`, `AlteracoesContratuais-2015.csv`, `AlteracoesContratuais-2016.csv`, `AlteracoesContratuais-2017.csv`, `AlteracoesContratuais-2018.csv`, `AlteracoesContratuais-2019.csv`, `AlteracoesContratuais-2020.csv`, `AlteracoesContratuais-2021.csv`, `AlteracoesContratuais-2022.csv`, `AlteracoesContratuais-2023.csv`, `AlteracoesContratuais-2024.csv`, `AlteracoesContratuais-2025.csv`, `AlteracoesContratuais-2026.csv`, `Comissoes-1753.csv`, `Comissoes-2001.csv`, `Comissoes-2006.csv`, `Comissoes-2008.csv`, `Comissoes-2009.csv`, `Comissoes-2010.csv`, `Comissoes-2011.csv`, `Comissoes-2012.csv`, `Comissoes-2013.csv`, `Comissoes-2014.csv`, `Comissoes-2015.csv`, `Comissoes-2016.csv`, `Comissoes-2017.csv`, `Comissoes-2018.csv`, `Comissoes-2019.csv`, `Comissoes-2020.csv`, `Comissoes-2021.csv`, `Comissoes-2022.csv`, `Comissoes-2023.csv`, `Comissoes-2024.csv`, `Comissoes-2025.csv`, `Comissoes-2026.csv`, `Contratos-1991.csv`, `Contratos-2013.csv`, `Contratos-2014.csv`, `Contratos-2018.csv`, `Contratos-2020.csv`, `Contratos-2021.csv`, `Contratos-2022.csv`, `Contratos-2023.csv`, `Contratos-2024.csv`, `Contratos-2025.csv`, `Contratos-2026.csv`, `Contratos-2027.csv`, `Contratos-2028.csv`, `Contratos-2032.csv`, `Contratos-3024.csv`, `Empenhos-1753.csv`, `Empenhos-2001.csv`, `Empenhos-2006.csv`, `Empenhos-2008.csv`, `Empenhos-2009.csv`, `Empenhos-2010.csv`, `Empenhos-2011.csv`, `Empenhos-2012.csv`, `Empenhos-2013.csv`, `Empenhos-2014.csv`, `Empenhos-2015.csv`, `Empenhos-2016.csv`, `Empenhos-2017.csv`, `Empenhos-2018.csv`, `Empenhos-2019.csv`, `Empenhos-2020.csv`, `Empenhos-2021.csv`, `Empenhos-2022.csv`, `Empenhos-2023.csv`, `Empenhos-2024.csv`, `Empenhos-2025.csv`, `Empenhos-2026.csv`, `Empenhos-2032.csv`
    - **Aviso:** Valores iguais somente ao considerar arquivos individualmente, os valores diferem entre arquivos

- **Chaves:** `ignore_hash` e `set_url_type`
    - *Apresentado nos arquivos:* `AlteracoesContratuais-2010.csv`, `AlteracoesContratuais-2011.csv`, `AlteracoesContratuais-2012.csv`, `AlteracoesContratuais-2013.csv`, `AlteracoesContratuais-2014.csv`, `AlteracoesContratuais-2015.csv`, `AlteracoesContratuais-2016.csv`, `AlteracoesContratuais-2017.csv`, `AlteracoesContratuais-2018.csv`, `AlteracoesContratuais-2019.csv`, `AlteracoesContratuais-2020.csv`, `AlteracoesContratuais-2021.csv`, `AlteracoesContratuais-2022.csv`, `AlteracoesContratuais-2023.csv`, `AlteracoesContratuais-2024.csv`, `AlteracoesContratuais-2025.csv`, `AlteracoesContratuais-2026.csv`, `Comissoes-1753.csv`, `Comissoes-2001.csv`, `Comissoes-2006.csv`, `Comissoes-2008.csv`, `Comissoes-2009.csv`, `Comissoes-2010.csv`, `Comissoes-2011.csv`, `Comissoes-2012.csv`, `Comissoes-2013.csv`, `Comissoes-2014.csv`, `Comissoes-2015.csv`, `Comissoes-2016.csv`, `Comissoes-2017.csv`, `Comissoes-2018.csv`, `Comissoes-2019.csv`, `Comissoes-2020.csv`, `Comissoes-2021.csv`, `Comissoes-2022.csv`, `Comissoes-2023.csv`, `Comissoes-2024.csv`, `Comissoes-2025.csv`, `Comissoes-2026.csv`, `Contratos-1991.csv`, `Contratos-2013.csv`, `Contratos-2014.csv`, `Contratos-2018.csv`, `Contratos-2020.csv`, `Contratos-2021.csv`, `Contratos-2022.csv`, `Contratos-2023.csv`, `Contratos-2024.csv`, `Contratos-2025.csv`, `Contratos-2026.csv`, `Contratos-2027.csv`, `Contratos-2028.csv`, `Contratos-2032.csv`, `Contratos-3024.csv`, `Empenhos-1753.csv`, `Empenhos-2001.csv`, `Empenhos-2006.csv`, `Empenhos-2008.csv`, `Empenhos-2009.csv`, `Empenhos-2010.csv`, `Empenhos-2011.csv`, `Empenhos-2012.csv`, `Empenhos-2013.csv`, `Empenhos-2014.csv`, `Empenhos-2015.csv`, `Empenhos-2016.csv`, `Empenhos-2017.csv`, `Empenhos-2018.csv`, `Empenhos-2019.csv`, `Empenhos-2020.csv`, `Empenhos-2021.csv`, `Empenhos-2022.csv`, `Empenhos-2023.csv`, `Empenhos-2024.csv`, `Empenhos-2025.csv`, `Empenhos-2026.csv`, `Empenhos-2032.csv`
    - **Aviso:** Os valores não diferem entre arquivos

- **Chaves:** `original_url` e `url`
    - *Apresentado nos arquivos:* `AlteracoesContratuais-2010.csv`, `AlteracoesContratuais-2011.csv`, `AlteracoesContratuais-2012.csv`, `AlteracoesContratuais-2013.csv`, `AlteracoesContratuais-2014.csv`, `AlteracoesContratuais-2015.csv`, `AlteracoesContratuais-2016.csv`, `AlteracoesContratuais-2017.csv`, `AlteracoesContratuais-2018.csv`, `AlteracoesContratuais-2019.csv`, `AlteracoesContratuais-2020.csv`, `AlteracoesContratuais-2021.csv`, `AlteracoesContratuais-2022.csv`, `AlteracoesContratuais-2023.csv`, `AlteracoesContratuais-2024.csv`, `AlteracoesContratuais-2025.csv`, `AlteracoesContratuais-2026.csv`, `Comissoes-1753.csv`, `Comissoes-2001.csv`, `Comissoes-2006.csv`, `Comissoes-2008.csv`, `Comissoes-2009.csv`, `Comissoes-2010.csv`, `Comissoes-2011.csv`, `Comissoes-2012.csv`, `Comissoes-2013.csv`, `Comissoes-2014.csv`, `Comissoes-2015.csv`, `Comissoes-2016.csv`, `Comissoes-2017.csv`, `Comissoes-2018.csv`, `Comissoes-2019.csv`, `Comissoes-2020.csv`, `Comissoes-2021.csv`, `Comissoes-2022.csv`, `Comissoes-2023.csv`, `Comissoes-2024.csv`, `Comissoes-2025.csv`, `Comissoes-2026.csv`, `Contratos-1991.csv`, `Contratos-2013.csv`, `Contratos-2014.csv`, `Contratos-2018.csv`, `Contratos-2020.csv`, `Contratos-2021.csv`, `Contratos-2022.csv`, `Contratos-2023.csv`, `Contratos-2024.csv`, `Contratos-2025.csv`, `Contratos-2026.csv`, `Contratos-2027.csv`, `Contratos-2028.csv`, `Contratos-2032.csv`, `Contratos-3024.csv`, `Empenhos-1753.csv`, `Empenhos-2001.csv`, `Empenhos-2006.csv`, `Empenhos-2008.csv`, `Empenhos-2009.csv`, `Empenhos-2010.csv`, `Empenhos-2011.csv`, `Empenhos-2012.csv`, `Empenhos-2013.csv`, `Empenhos-2014.csv`, `Empenhos-2015.csv`, `Empenhos-2016.csv`, `Empenhos-2017.csv`, `Empenhos-2018.csv`, `Empenhos-2019.csv`, `Empenhos-2020.csv`, `Empenhos-2021.csv`, `Empenhos-2022.csv`, `Empenhos-2023.csv`, `Empenhos-2024.csv`, `Empenhos-2025.csv`, `Empenhos-2026.csv`, `Empenhos-2032.csv`
    - **Aviso:** Valores iguais somente ao considerar arquivos individualmente, os valores diferem entre arquivos

---

## 📂 Grupo de Metadados: `002`

- **Total de Chaves de Metadados Identificadas:** `26`
- **Quantidade de Arquivos no Grupo:** `12`

**Arquivos Vinculados ao Grupo:**
  - 📄 **`Contratos-2010.csv`** *(ID: `f8c665bb-9539-4ee3-9007-6c83b1facaaf`)*
  - 📄 **`Contratos-2008.csv`** *(ID: `8415fca5-e522-499c-89e4-a4272146f7a3`)*
  - 📄 **`Contratos-2001.csv`** *(ID: `dc58e360-eeda-4dba-aaeb-23d436a89833`)*
  - 📄 **`Contratos-2016.csv`** *(ID: `52367d44-2ead-49c7-bde7-58ed3a94e80b`)*
  - 📄 **`Contratos-1753.csv`** *(ID: `a1f38833-1e18-4b6b-875e-df8a67d8909c`)*
  - 📄 **`Contratos-2019.csv`** *(ID: `31e6f40e-d1a8-4e1f-b9e0-6e08a0366b94`)*
  - 📄 **`Contratos-2011.csv`** *(ID: `e5b0e1da-1ad8-47db-9b54-91c25d0cb2eb`)*
  - 📄 **`Contratos-2017.csv`** *(ID: `f7a2ef64-2e8a-43cb-9e8d-b8c18dbfeaae`)*
  - 📄 **`Contratos-2006.csv`** *(ID: `8521e2c6-ceeb-4b53-8cec-99ce87caa4cc`)*
  - 📄 **`Contratos-2012.csv`** *(ID: `61c2911c-97cc-4c24-9cf8-f0325f5caab6`)*
  - 📄 **`Contratos-2015.csv`** *(ID: `cdc1e21c-2aca-448b-b4e4-34a0a1aa7f5d`)*
  - 📄 **`Contratos-2009.csv`** *(ID: `ca351857-d948-429c-9951-3d7a1bca81a9`)*

### 📋 Chaves de Metadados Presentes no Grupo:

`cache_last_updated`, `cache_url`, `created`, `datastore_active`, `datastore_contains_all_records_of_source_file`, `delimiter`, `description`, `encoding`, `first_record_is_header`, `format`, `hash`, `last_modified`, `metadata_modified`, `mimetype`, `mimetype_inner`, `package_id`, `position`, `resource_id`, `resource_type`, `size`, `state`, `tracking_summary`, `url`, `url_type`


---

### 🔍 Aviso: Chaves Internas com o Mesmo Valor no Arquivo

Abaixo estão indicados os casos em que chaves diferentes de um mesmo arquivo possuem exatamente o mesmo valor:

- **Chaves:** `id` e `resource_id`
    - *Apresentado nos arquivos:* `Contratos-1753.csv`, `Contratos-2001.csv`, `Contratos-2006.csv`, `Contratos-2008.csv`, `Contratos-2009.csv`, `Contratos-2010.csv`, `Contratos-2011.csv`, `Contratos-2012.csv`, `Contratos-2015.csv`, `Contratos-2016.csv`, `Contratos-2017.csv`, `Contratos-2019.csv`
    - **Aviso:** Valores iguais somente ao considerar arquivos individualmente, os valores diferem entre arquivos

---

## 📂 Grupo de Metadados: `003`

- **Total de Chaves de Metadados Identificadas:** `22`
- **Quantidade de Arquivos no Grupo:** `15`

**Arquivos Vinculados ao Grupo:**
  - 📄 **`AlteracoesContratuais-2001.csv`** *(ID: `8143a07a-d141-472b-a9c0-531f4dc26d5c`)*
  - 📄 **`AlteracoesContratuais-2008.csv`** *(ID: `0ce629ce-8b6c-40eb-bca5-590133c035a9`)*
  - 📄 **`AlteracoesContratuais-1753.csv`** *(ID: `5bcc2b46-7d94-4d4a-aaae-7495b2c21272`)*
  - 📄 **`AlteracoesContratuais-2006.csv`** *(ID: `4952d33b-3813-4b0e-b33e-7e34cec0ad99`)*
  - 📄 **`AlteracoesContratuais-2009.csv`** *(ID: `33ebb82b-7a58-430a-9037-55b4431fb653`)*
  - 📄 **`AlteracoesContratuais-3024.csv`** *(ID: `31ceeba6-7138-4ee5-8b8c-149e237a4269`)*
  - 📄 **`Empenhos-3024.csv`** *(ID: `81ecafd8-68dd-4200-ba61-6b111a3699a9`)*
  - 📄 **`AlteracoesContratuais-2032.csv`** *(ID: `caee0c6f-6a11-4c38-ab4c-ddcbcf93f9c9`)*
  - 📄 **`AlteracoesContratuais-2027.csv`** *(ID: `b485281e-da1d-4d8d-a877-4d9d0feb4dbd`)*
  - 📄 **`Empenhos-2027.csv`** *(ID: `c062f0c1-8668-4c4b-8623-9d8b07bfd514`)*
  - 📄 **`AlteracoesContratuais-2224.csv`** *(ID: `2f9849af-afb1-4a51-8659-97991705af9c`)*
  - 📄 **`AlteracoesContratuais-5024.csv`** *(ID: `426359c7-c7a6-4cab-bb77-7608261c4a87`)*
  - 📄 **`Empenhos-5024.csv`** *(ID: `7cf61401-2a8f-442a-9325-caceb7604a0a`)*
  - 📄 **`AlteracoesContratuais-1991.csv`** *(ID: `75b13225-35ec-4a84-a722-12a5c4895627`)*
  - 📄 **`Empenhos-1991.csv`** *(ID: `24e3a501-e87e-4773-8d65-222024e588f6`)*

### 📋 Chaves de Metadados Presentes no Grupo:

`cache_last_updated`, `cache_url`, `created`, `datastore_active`, `datastore_contains_all_records_of_source_file`, `description`, `format`, `hash`, `last_modified`, `metadata_modified`, `mimetype`, `mimetype_inner`, `package_id`, `position`, `resource_type`, `size`, `state`, `tracking_summary`, `url`, `url_type`


---

> *Nenhuma chave interna com valor idêntico encontrada nos arquivos deste grupo.*

---

## 📂 Grupo de Metadados: `004`

- **Total de Chaves de Metadados Identificadas:** `29`
- **Quantidade de Arquivos no Grupo:** `3`

**Arquivos Vinculados ao Grupo:**
  - 📄 **`Contratos-2224.csv`** *(ID: `db608579-ff45-41ad-b65b-8913e981d94f`)*
  - 📄 **`Empenhos-2224.csv`** *(ID: `2f63817b-3602-495e-b074-abb614c72336`)*
  - 📄 **`Contratos-5024.csv`** *(ID: `c0533a5f-3ef2-403d-9c31-dfeef4da40f5`)*

### 📋 Chaves de Metadados Presentes no Grupo:

`cache_last_updated`, `cache_url`, `ckan_url`, `created`, `datastore_active`, `datastore_contains_all_records_of_source_file`, `description`, `format`, `hash`, `ignore_hash`, `last_modified`, `metadata_modified`, `mimetype`, `mimetype_inner`, `original_url`, `package_id`, `position`, `queue_name`, `resource_id`, `resource_type`, `set_url_type`, `size`, `state`, `task_created`, `tracking_summary`, `url`, `url_type`


---

### 🔍 Aviso: Chaves Internas com o Mesmo Valor no Arquivo

Abaixo estão indicados os casos em que chaves diferentes de um mesmo arquivo possuem exatamente o mesmo valor:

- **Chaves:** `datastore_active` e `datastore_contains_all_records_of_source_file` e `ignore_hash`
    - *Apresentado nos arquivos:* `Contratos-2224.csv`, `Contratos-5024.csv`, `Empenhos-2224.csv`
    - **Aviso:** Os valores não diferem entre arquivos

- **Chaves:** `id` e `resource_id`
    - *Apresentado nos arquivos:* `Contratos-2224.csv`, `Contratos-5024.csv`, `Empenhos-2224.csv`
    - **Aviso:** Valores iguais somente ao considerar arquivos individualmente, os valores diferem entre arquivos

---