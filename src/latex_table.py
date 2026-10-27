from queries_headers import agrupar_recursos_dataset, analisar_colunas_por_periodo

_RECEITAS_ID = "3210df25-0dfe-414b-aed4-844ddcdf87bb"
_DESPESAS_ID = "99e16b13-0e6f-4504-8544-00de842ab1fd"
_CONTRATOS_ID = "36f4bfc0-48f2-4cf9-a812-5249724da742"
_PREFIXO_ARQUIVO_SAIDA = "tabela_latex"


def transformar_string_para_latex(texto):
    """Transforma caracteres especiais em LaTeX para evitar erros de compilação."""
    if not texto:
        return ""
    # Substituições comuns de caracteres especiais
    substituicoes = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for char, latex_equiv in substituicoes.items():
        texto = texto.replace(char, latex_equiv)
    return texto

def gerar_latex_tabelas_periodos(analise_dict):
    """Gera o código LaTeX de tabelas de mapeamento de colunas para cada período e grupo

    a partir do dicionário retornado por 'analisar_colunas_por_periodo'.
    """
    linhas_latex = []

    for nome_grupo, grupos in analise_dict.items():
        # Adiciona a subseção para o grupo de arquivo
        linhas_latex.append(f"\\subsubsection{{{transformar_string_para_latex(nome_grupo)}}}\n\n")

        for grupo in grupos:
            periodo_inicio = grupo.get("PeriodoInicio")
            periodo_fim = grupo.get("PeriodoFim")

            # Trata o formato dos anos para o texto da caption e a label
            if periodo_inicio is None and periodo_fim is None:
                str_periodo_caption = "período não especificado"
                str_label_periodo = "periodo-unico"
            elif periodo_inicio == periodo_fim:
                str_periodo_caption = f"no ano de {periodo_inicio}"
                str_label_periodo = f"periodo-{periodo_inicio}"
            else:
                str_periodo_caption = (
                    f"no período de {periodo_inicio} até {periodo_fim}"
                )
                str_label_periodo = f"periodo-{periodo_inicio}-{periodo_fim}"

            # Formata o nome base do arquivo para a caption (ex: receitas<Ano>.csv)
            # Se o grupo contiver traço ou diferenciação, adapta o nome base
            # if nome_grupo == "DividaAtiva":
            #     nome_base_arquivo = "DividaAtiva.csv"
            # else:
            #     nome_base_arquivo = f"{nome_grupo}\\textless{{}}Ano\\textgreater{{}}.csv"
            nome_base_arquivo = f"{nome_grupo}"


            # Início da tabela longtable
            linhas_latex.append("\\small\n")
            linhas_latex.append(
                "\\begin{longtable}{|p{4.0cm}|p{5.0cm}|p{5.5cm}|}\n"
            )
            linhas_latex.append(
                f"\\caption{{Colunas referentes ao arquivo \\textbf{{{transformar_string_para_latex(nome_base_arquivo)}}} {transformar_string_para_latex(str_periodo_caption)}}}\n"
            )
            linhas_latex.append(
                f"\\label{{tabela-mapeamento-base-grupo-{transformar_string_para_latex(nome_grupo.replace('_', ''))}-{transformar_string_para_latex(str_label_periodo)}}} \\\\ \n"
            )  # Nota: mantido \\ no final se necessário conforme seu template, ajuste se preferir
            linhas_latex.append("    \\hline\n")
            linhas_latex.append(
                "    \\textbf{Coluna no Arquivo} & \\textbf{Entidade / Atributo}"
                " & \\textbf{Observações} \\\\ \\hline\n"
            )
            linhas_latex.append("    \\endhead\n\n")
            linhas_latex.append(
                "    \\hline \\multicolumn{3}{r}{\\textit{Continua na próxima"
                " página}} \\\\ \\hline\n"
            )
            linhas_latex.append("    \\endfoot\n\n")
            linhas_latex.append("    \\hline\n")
            linhas_latex.append("    \\endlastfoot\n\n")

            # Adiciona cada coluna do período usando o comando reutilizável \tabelaMapeamentoItem
            colunas = grupo.get("ColunasAtual", [])
            if not colunas:
                # \texttt{#1} & \texttt{#2} & #3 \\ \hline
                linhas_latex.append(r"    \texttt{Nenhuma coluna encontrada} &  & \\ \hline "+'\n')
            else:
                for coluna in colunas:
                    linhas_latex.append(f"    \\texttt{{\\seqsplit{{{transformar_string_para_latex(coluna)}}}}}" +r" & \texttt{}  & \texttt{} \\ \hline "+'\n')
                    #linhas_latex.append(f"    \\tabelaMapeamentoItem{{{coluna}}}{{{{}}{{}}}}\n")

            linhas_latex.append("\\end{longtable}\n")
            linhas_latex.append("\\normalsize\n\n")
            linhas_latex.append("\\vspace{0.5cm}\n\n")

    return "".join(linhas_latex)

def gerar_latex_tabelas_periodos_para_dataset(dataset_id, nome_arquivo_saida="generated/apendice_gerado.tex"):
    """Gera o código LaTeX de tabelas de mapeamento de colunas para cada período e grupo
    a partir do dataset_id fornecido.
    """
    dict_header = analisar_colunas_por_periodo(agrupar_recursos_dataset(dataset_id))
    codigo_latex = gerar_latex_tabelas_periodos(dict_header)
    with open(nome_arquivo_saida, "w", encoding="utf-8") as f:
         f.write(codigo_latex)
    return codigo_latex

if __name__ == "__main__":
  
  gerar_latex_tabelas_periodos_para_dataset(dataset_id = _RECEITAS_ID, nome_arquivo_saida="generated/latex/apendice_gerado_receitas.tex")
  gerar_latex_tabelas_periodos_para_dataset(dataset_id = _DESPESAS_ID, nome_arquivo_saida="generated/latex/apendice_gerado_despesas.tex")
  gerar_latex_tabelas_periodos_para_dataset(dataset_id = _CONTRATOS_ID, nome_arquivo_saida="generated/latex/apendice_gerado_contratos.tex")
