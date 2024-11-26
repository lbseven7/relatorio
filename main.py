import json
import os
from collections import defaultdict
from fpdf import FPDF
import streamlit as st
import pandas as pd
import unidecode

# Especifica o diretório onde estão os arquivos JSON
diretorio_json = "C:/Users/Aux Administrativo/Documents/leob/relatorio/JSON/dados"

# Inicializa a contagem total de vagas de professores e lista de professores com observações
total_vagas_com_observacoes = 0
professores_com_observacoes = []
observacoes_por_tipo = defaultdict(set)

# Função para contar e armazenar as vagas de professores que possuem observações
def contar_professores_com_observacoes(dados, chave, instituicao):
    vagas_com_observacoes = []
    if chave in dados and dados[chave]:
        for item in dados[chave]:
            observacao = item.get("observacoes")
            if observacao and isinstance(observacao, str) and observacao.strip():  # Verifica se a observação não está vazia
                item["instituicao"] = instituicao  # Adiciona o nome da instituição ao item
                vagas_com_observacoes.append(item)
    return vagas_com_observacoes

# Percorre todos os arquivos no diretório JSON
for nome_arquivo in os.listdir(diretorio_json):
    if nome_arquivo.endswith('.json'):
        caminho_json = os.path.join(diretorio_json, nome_arquivo)

        # Carrega o arquivo JSON
        try:
            with open(caminho_json, 'r', encoding='utf-8') as arquivo_json:
                dados = json.load(arquivo_json)
        except json.JSONDecodeError as e:
            print(f"Erro ao carregar o arquivo JSON '{nome_arquivo}': {e}")
            continue

        # Verifica se os dados foram carregados corretamente
        if not dados:
            print(f"Arquivo '{nome_arquivo}' está vazio ou não foi carregado corretamente.")
            continue

        instituicao = dados.get("escola")
        if not instituicao:
            print(f"Erro: A chave 'escola' não foi encontrada no arquivo '{nome_arquivo}'.")
            continue

        # Conta as vagas nas chaves "docentes", "professores_desdobrados" e "professores" que possuem observações
        servidores_efetivos = dados.get("servidores_efetivos", {})
        professores_com_observacoes.extend(contar_professores_com_observacoes(servidores_efetivos, "docentes", instituicao))
        professores_com_observacoes.extend(contar_professores_com_observacoes(servidores_efetivos, "professores_desdobrados", instituicao))

        servidores_contratados = dados.get("servidores_contratados", {})
        professores_com_observacoes.extend(contar_professores_com_observacoes(servidores_contratados, "professores", instituicao))

# Calcula o total de vagas com observações
total_vagas_com_observacoes = len(professores_com_observacoes)

# Classifica as observações por tipo
for professor in professores_com_observacoes:
    nome = professor.get("nome", "Desconhecido")
    observacoes = professor.get("observacoes", "Nenhuma observação")
    instituicao = professor.get("instituicao")
    observacoes_por_tipo[observacoes].add((nome, instituicao))

# Cria o PDF para salvar as informações
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Adiciona o título
titulo = "Total de vagas reais de professores com observações: " + str(total_vagas_com_observacoes)
pdf.cell(200, 10, txt=unidecode.unidecode(titulo), ln=True, align='C')

# Adiciona as informações dos professores que têm observações
for tipo, infos in observacoes_por_tipo.items():
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(200, 10, txt=unidecode.unidecode(f"Observação: {tipo}"), ln=True)
    pdf.set_font('Arial', '', 12)
    for nome, instituicao in infos:
        pdf.cell(200, 10, txt=unidecode.unidecode(f"  Nome: {nome}, Instituição: {instituicao}"), ln=True)

# Salva o PDF
pdf.output("professores_com_observacoes.pdf")

# Exibe o total de vagas de professores com observações
print(f"Total de vagas reais de professores com observações: {total_vagas_com_observacoes}")

# Salva as informações dos professores com observações em um arquivo de saída (TXT)
with open("professores_com_observacoes.txt", 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(f"Total de vagas reais de professores com observações: {total_vagas_com_observacoes}\n\n")
    for tipo, infos in observacoes_por_tipo.items():
        arquivo_saida.write(f"Observação: {tipo}\n")
        for nome, instituicao in infos:
            arquivo_saida.write(f"  Nome: {nome}, Instituição: {instituicao}\n")

# Cria uma interface usando Streamlit para visualizar os dados
st.title("Relatório de Vagas de Professores com Observações")

# Converte os dados para um DataFrame para exibição
dados_lista = [
    {"Nome": nome, "Instituição": instituicao, "Observação": tipo}
    for tipo, infos in observacoes_por_tipo.items()
    for nome, instituicao in infos
]

df = pd.DataFrame(dados_lista)

# Adiciona filtros à interface
observacao_filtrada = st.multiselect("Filtrar por Observação", options=df["Observação"].unique(), default=df["Observação"].unique())
instituicao_filtrada = st.multiselect("Filtrar por Instituição", options=df["Instituição"].unique(), default=df["Instituição"].unique())

# Aplica os filtros ao DataFrame
filtro_df = df[(df["Observação"].isin(observacao_filtrada)) & (df["Instituição"].isin(instituicao_filtrada))]

# Exibe o DataFrame filtrado
st.dataframe(filtro_df)

# Permite o download do PDF gerado
with open("professores_com_observacoes.pdf", "rb") as pdf_file:
    st.download_button(label="Baixar PDF com Observações", data=pdf_file, file_name="professores_com_observacoes.pdf", mime="application/pdf")
