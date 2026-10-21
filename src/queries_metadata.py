import requests
from pathlib import Path
from ckanapi import RemoteCKAN
from tqdm import tqdm
import time


_TEMPO_LIMITE = 20  # segundos

# Tentativa de importação das bibliotecas para conversão de PDF
try:
  import markdown
  from weasyprint import HTML
  SUPORTE_PDF = True
except ImportError:
  SUPORTE_PDF = False

from datetime import datetime

def _verificar_arquivos_desatualizados(grupos_metadados, limite_meses=1):
  """Identifica quais arquivos possuem a data de atualização (last_modified ou created)

  superior a 1 mês (ou limite especificado) em relação à data atual.
  """
  arquivos_antigos = []
  data_atual = datetime.now()

  for dados in grupos_metadados.values():
    for rec in dados.get("recursos", []):
      nome_arq = rec.get("name")
      res_id = rec.get("id")
      
      # Tenta pegar 'last_modified', se vazio tenta 'created'
      data_str = rec.get("last_modified") or rec.get("created")
      
      if data_str:
        try:
          # Formato comum de data do CKAN (ex: 2023-05-10T... ou YYYY-MM-DD)
          data_limpa = data_str.split("T")[0]
          data_recurso = datetime.strptime(data_limpa, "%Y-%m-%d")
          
          # Calcula a diferença aproximada em meses
          diferenca_meses = (data_atual.year - data_recurso.year) * 12 + (data_atual.month - data_recurso.month)
          
          if diferenca_meses >= limite_meses:
            arquivos_antigos.append({
                "name": nome_arq,
                "id": res_id,
                "data": data_limpa,
                "meses": diferenca_meses
            })
        except Exception:
          pass

  return arquivos_antigos

def agrupar_recursos_por_metadados(dataset_id, portal_url="https://dados.es.gov.br/"):
  """Consulta um dataset no CKAN, extrai os metadados de cada recurso/arquivo,

  os agrupa com base na similaridade de suas chaves e atribui uma nomenclatura
  sequencial (001, 002, 003...).
  """
  rc = RemoteCKAN(portal_url)
  grupos_temporarios = {}

  inicio_tentativa = time.time()
  tentativa = 1
  dataset = None
  sucesso_requisicao = False

  # Loop de retry limitado a 20 segundos para a chamada principal do dataset
  while (time.time() - inicio_tentativa) < _TEMPO_LIMITE:
    try:
      dataset = rc.action.package_show(id=dataset_id)
      sucesso_requisicao = True
      break
    except requests.exceptions.RequestException as e:
      tempo_decorrido = int(time.time() - inicio_tentativa)
      print(
          f"⚠️ [Erro de Rede - Tentativa {tentativa}] Falha ao acessar o dataset {dataset_id} "
          f"({tempo_decorrido}s decorridos): {e}"
      )
      tentativa += 1
      time.sleep(3)  # Pausa de 3 segundos entre as tentativas
    except Exception as e:
      print(f"❌ [Erro na API] Erro não recuperável ao buscar o dataset {dataset_id}: {e}")
      break

  # Se estourar o tempo limite de 20s por falha de rede, pula a requisição do dataset
  if not sucesso_requisicao:
    print(
        f"❌ [Timeout / Pulado] A requisição do dataset {dataset_id} falhou após {_TEMPO_LIMITE}s de tentativas de rede. Pulando..."
    )
    return {}
  
  
  # Processamento do recurso que foi obtido
  try:
    recursos = dataset.get("resources", [])

    for recurso in recursos:
      if recurso.get("format") != "CSV":
        continue  # Ignora recursos que não são CSV

      res_id = recurso.get("id")
      res_name = recurso.get("name")

      if not res_name and recurso.get("url"):
        res_name = recurso.get("url").split("/")[-1].split("?")[0]

      if not res_name:
        res_name = f"recurso_{res_id}"

      # Coleta todos os metadados disponíveis do recurso
      metadados_recurso = {
          "id": res_id,
          "name": res_name,
          "description": recurso.get("description", ""),
          "format": recurso.get("format", ""),
          "mimetype": recurso.get("mimetype", ""),
          "created": recurso.get("created", ""),
          "last_modified": recurso.get("last_modified", ""),
          "cache_url": recurso.get("cache_url", ""),
          "state": recurso.get("state", ""),
          "size": recurso.get("size", None)
      }

      # Adiciona quaisquer extras/propriedades customizadas presentes no CKAN
      for k, v in recurso.items():
        if k not in metadados_recurso:
          metadados_recurso[k] = v

      # Define uma assinatura baseada nas chaves de metadados presentes
      keys_tuple = tuple(sorted(metadados_recurso.keys()))

      if keys_tuple not in grupos_temporarios:
        grupos_temporarios[keys_tuple] = {
            "chaves_metadados": list(keys_tuple),
            "recursos": []
        }
      grupos_temporarios[keys_tuple]["recursos"].append(metadados_recurso)

    # Atribui nomes sequenciais formatados (001, 002, 003...) aos grupos encontrados
    grupos_finais = {}
    for idx, (k_tuple, dados) in enumerate(grupos_temporarios.items(), 1):
      nome_grupo = f"{idx:03d}"
      grupos_finais[nome_grupo] = dados

    return grupos_finais

  except Exception as e:
    print(f"❌ [Erro Interno] Erro inesperado ao processar os recursos do dataset {dataset_id}: {e}")
  return {}


def enriquecer_analise_metadados(grupos_metadados):
  """Analisa cada arquivo individualmente para identificar quais chaves internas

  diferentes possuem exatamente o mesmo valor, agrupando os arquivos e avaliando
  se os valores diferem ou são idênticos entre os arquivos.
  """
  analise_consolidada = {}

  for chave_grupo, dados in grupos_metadados.items():
    recursos = dados.get("recursos", [])
    chaves = dados.get("chaves_metadados", [])

    # Dicionário temporário: par_chaves -> { valor_interno: [lista_de_arquivos] }
    mapeamento_par_valores = {}

    for rec in recursos:
      res_name = rec.get("name")
      
      # Mapeia valor -> lista de chaves que possuem esse mesmo valor dentro deste arquivo
      valores_no_arquivo = {}
      for k in chaves:
        val = rec.get(k)
        if val is None or val == "" or val == "N/A":
          continue
        if isinstance(val, (list, dict)):
          val = str(val)
        
        val_str = str(val)
        valores_no_arquivo.setdefault(val_str, []).append(k)

      pares_processados_no_arquivo = set()

      for val, lista_chaves in valores_no_arquivo.items():
        if len(lista_chaves) > 1:
          par_chaves = tuple(sorted(lista_chaves))
          
          if par_chaves not in pares_processados_no_arquivo:
            pares_processados_no_arquivo.add(par_chaves)
            mapeamento_par_valores.setdefault(par_chaves, {}).setdefault(val, []).append(res_name)

    igualdades_internas_processadas = []

    for par_chaves, val_dict in mapeamento_par_valores.items():
      # Coleta todos os arquivos envolvidos para este par de chaves
      todos_arquivos = []
      for arqs in val_dict.values():
        todos_arquivos.extend(arqs)
      todos_arquivos = sorted(list(set(todos_arquivos)))

      # Verifica se há mais de um valor global diferente para este mesmo par de chaves entre os arquivos
      # Se houver mais de uma entrada em val_dict, significa que os valores mudam dependendo do arquivo.
      # Se houver apenas 1 entrada em val_dict, significa que o valor exato é o mesmo em todos os arquivos.
      if len(val_dict) > 1:
        tipo_aviso = "individuais_diferem"
      else:
        tipo_aviso = "nao_diferem"

      igualdades_internas_processadas.append({
          "par_chaves": par_chaves,
          "arquivos": todos_arquivos,
          "tipo_aviso": tipo_aviso
      })

    analise_consolidada[chave_grupo] = {
        "chaves_metadados": chaves,
        "recursos": recursos,
        "igualdades_internas": igualdades_internas_processadas
    }

  return analise_consolidada


def gerar_analise_metadados(
    dataset_id,
    nome_arquivo_saida="metadados_analisados.md",
    caminho_saida="./",
):
  """Gera os arquivos .md e .pdf com a análise de arquivos desatualizados,

  comparação par a par entre os grupos, chaves e avisos de igualdades internas.
  """
  grupos_brutos = agrupar_recursos_por_metadados(dataset_id)
  analise_dict = enriquecer_analise_metadados(grupos_brutos)

  linhas = []
  linhas.append("# Relatório de Análise de Metadados - CKAN")
  linhas.append(
      "\nEste documento apresenta a auditoria de arquivos desatualizados, o comparativo "
      "par a par entre os grupos de metadados, as chaves presentes e a indicação de chaves internas "
      "com valores idênticos nos arquivos.\n"
  )
  linhas.append("---")

  # ---------------------------------------------------------
  # NOVA SEÇÃO: Análise de Arquivos com Atualização > 1 Mês
  # ---------------------------------------------------------
  linhas.append("\n## ⏰ Análise de Arquivos Desatualizados (> 1 Mês)\n")
  arquivos_desatualizados = _verificar_arquivos_desatualizados(grupos_brutos, limite_meses=1)
  
  if arquivos_desatualizados:
    linhas.append("Abaixo estão listados os arquivos cuja data de última modificação/criação é superior a 1 mês:\n")
    for arq in arquivos_desatualizados:
      linhas.append(f"- 📄 **`{arq['name']}`** *(ID: `{arq['id']}`)*")
      linhas.append(f"  - *Data de referência:* `{arq['data']}` (aproximadamente {arq['meses']} meses atrás)")
    linhas.append("")
  else:
    linhas.append("> *Nenhum arquivo com mais de 1 mês de defasagem de atualização encontrado.*\n")
  
  linhas.append("---")

  # ---------------------------------------------------------
  # Comparação Par a Par entre Grupos (X vs Y e Y vs X)
  # ---------------------------------------------------------
  linhas.append("\n## 🔄 Comparação Par a Par entre Grupos de Metadados\n")
  
  nomes_grupos = list(analise_dict.keys())
  if len(nomes_grupos) > 1:
    for i, grupo_x in enumerate(nomes_grupos):
      for j, grupo_y in enumerate(nomes_grupos):
        if i == j:
          continue
        
        chaves_x = set(analise_dict[grupo_x].get("chaves_metadados", []))
        chaves_y = set(analise_dict[grupo_y].get("chaves_metadados", []))
        
        diferenca = sorted(list(chaves_x - chaves_y))
        
        linhas.append(f"### Comparação: Grupo `{grupo_x}` vs Grupo `{grupo_y}`")
        if diferenca:
          linhas.append(f"Chaves presentes em **`{grupo_x}`** mas **ausentes** em **`{grupo_y}`**:")
          chaves_fmt = [f"`{c}`" for c in diferenca if c not in ("id", "name")]
          if chaves_fmt:
            linhas.append(", ".join(chaves_fmt) + "\n")
          else:
            linhas.append("*Nenhuma chave adicional (além de id/name).*\n")
        else:
          linhas.append(f"> *Todas as chaves do grupo `{grupo_x}` também estão presentes no grupo `{grupo_y}`.*\n")
    linhas.append("---")
  else:
    linhas.append("> *Apenas um grupo de metadados detectado. Comparação par a par não aplicável.*\n")
    linhas.append("---")

  # ---------------------------------------------------------
  # Detalhamento de Cada Grupo
  # ---------------------------------------------------------
  for chave_grupo, dados in tqdm(analise_dict.items(), desc="Compilando Relatório de Metadados"):
    linhas.append(f"\n## 📂 Grupo de Metadados: `{chave_grupo}`\n")
    
    chaves = dados.get("chaves_metadados", [])
    linhas.append(f"- **Total de Chaves de Metadados Identificadas:** `{len(chaves)}`")
    
    recursos = dados.get("recursos", [])
    linhas.append(f"- **Quantidade de Arquivos no Grupo:** `{len(recursos)}`\n")

    linhas.append("**Arquivos Vinculados ao Grupo:**")
    for rec in recursos:
      linhas.append(f"  - 📄 **`{rec.get('name')}`** *(ID: `{rec.get('id')}`)*")

    # Listagem das chaves de metadados do grupo em um único parágrafo, separadas por vírgula
    linhas.append("\n### 📋 Chaves de Metadados Presentes no Grupo:\n")
    chaves_filtradas = [f"`{chave}`" for chave in chaves if chave not in ("id", "name")]
    if chaves_filtradas:
      linhas.append(", ".join(chaves_filtradas) + "\n")
    else:
      linhas.append("*Nenhuma chave adicional encontrada.*\n")

    # Seção de igualdades internas com os avisos específicos solicitados
    igualdades_internas = dados.get("igualdades_internas", [])
    if igualdades_internas:
      linhas.append("\n---")
      linhas.append("\n### 🔍 Aviso: Chaves Internas com o Mesmo Valor no Arquivo\n")
      linhas.append("Abaixo estão indicados os casos em que chaves diferentes de um mesmo arquivo possuem exatamente o mesmo valor:\n")
      
      for item in igualdades_internas:
        par_chaves = item["par_chaves"]
        arques = item["arquivos"]
        tipo_aviso = item["tipo_aviso"]

        chaves_str = " e ".join([f"`{c}`" for c in par_chaves])
        arquivos_str = ", ".join([f"`{arq}`" for arq in sorted(arques)])
        
        linhas.append(f"- **Chaves:** {chaves_str}")
        linhas.append(f"    - *Apresentado nos arquivos:* {arquivos_str}")
        
        if tipo_aviso == "individuais_diferem":
          linhas.append(f"    - **Aviso:** Valores iguais somente ao considerar arquivos individualmente, os valores diferem entre arquivos")
        else:
          linhas.append(f"    - **Aviso:** Os valores não diferem entre arquivos")
        
        linhas.append("")
    else:
      linhas.append("\n---")
      linhas.append("\n> *Nenhuma chave interna com valor idêntico encontrada nos arquivos deste grupo.*\n")

    linhas.append("---")

  conteudo_md = "\n".join(linhas)

  try:
    diretorio = Path(caminho_saida)
    diretorio.mkdir(parents=True, exist_ok=True)

    caminho_completo_md = diretorio / nome_arquivo_saida
    caminho_completo_md.write_text(conteudo_md, encoding="utf-8")
    #print(f"Arquivo .md de metadados gerado com sucesso em: '{caminho_completo_md}'")

    if SUPORTE_PDF:
      conteudo_html = markdown.markdown(conteudo_md, extensions=["fenced_code", "tables"])
      html_completo = f"""
          <!DOCTYPE html>
          <html lang="pt-BR">
          <head>
              <meta charset="UTF-8">
              <style>
                  body {{ font-family: Helvetica, Arial, sans-serif; margin: 30px; color: #333; line-height: 1.5; font-size: 13px; }}
                  h1 {{ color: #004080; border-bottom: 2px solid #004080; padding-bottom: 5px; font-size: 20px; }}
                  h2 {{ color: #0059b3; margin-top: 25px; font-size: 16px; }}
                  h3 {{ color: #222; font-size: 14px; margin-top: 15px; }}
                  hr {{ border: 0; border-top: 1px solid #ddd; margin: 15px 0; }}
                  code {{ background: #f6f8fa; padding: 2.3px 4px; border-radius: 3px; font-size: 11px; }}
              </style>
          </head>
          <body>
              {conteudo_html}
          </body>
          </html>
          """
      caminho_completo_pdf = diretorio / Path(nome_arquivo_saida).with_suffix(".pdf").name
      HTML(string=html_completo).write_pdf(caminho_completo_pdf)
      #print(f"Arquivo .pdf de metadados gerado com sucesso em: '{caminho_completo_pdf}'")

  except Exception as e:
    print(f"Erro ao salvar os arquivos de relatório de metadados: {e}")

  return analise_dict