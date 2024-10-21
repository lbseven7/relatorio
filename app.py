import streamlit as st
import pandas as pd
import sqlite3
from fpdf import FPDF
import tempfile
import json


# Carregar listas de serviços, empresas e setores do arquivo JSON
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)


# Acessando as listas
servicos_disponiveis = dados["servicos_disponiveis"]
empresas_disponiveis = dados["empresas_disponiveis"]
setores_disponiveis = dados["setores_disponiveis"]


# Conectar ao banco de dados SQLite
conn = sqlite3.connect("servicos.db")
cursor = conn.cursor()


# Criar tabela se não existir
cursor.execute("""CREATE TABLE IF NOT EXISTS servicos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Empresa TEXT,
    Servico TEXT,
    Data TEXT,
    Setor TEXT,
    Quantidade INTEGER,
    Ativo INTEGER DEFAULT 1
)""")
conn.commit()


# Inicializar o DataFrame para armazenar os dados
if 'data' not in st.session_state:
    st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)


# Função para cadastrar serviços
def cadastrar_servico():
    empresa = st.selectbox("Escolha a Empresa", ["Selecione"] + empresas_disponiveis, key="empresa_cadastro")
    servico = st.selectbox("Escolha o Serviço", ["Selecione"] + servicos_disponiveis, key="servico_cadastro")
    setor = st.selectbox("Escolha o Setor", ["Selecione"] + setores_disponiveis, key="setor_cadastro")
    data = st.date_input("Data", key="data_cadastro")
    quantidade = st.number_input("Quantidade", min_value=1, step=1, key="quantidade_cadastro")


    if st.button("Cadastrar Serviço"):
        cursor.execute("INSERT INTO servicos (Empresa, Servico, Data, Setor, Quantidade) VALUES (?, ?, ?, ?, ?) ",
                       (empresa, servico, data, setor, quantidade))
        conn.commit()
        st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)
        st.success("Serviço cadastrado com sucesso!")


# Função para editar serviços
def editar_servico():
    if not st.session_state.data.empty:
        id_editar = st.selectbox("Selecione o Serviço para Editar", st.session_state.data['Servico'].unique(), key="servico_editar")


        if id_editar:
            registros = st.session_state.data[st.session_state.data['Servico'] == id_editar]


            if not registros.empty:
                registro = registros.iloc[0]


                empresa = st.selectbox("Escolha a Empresa", empresas_disponiveis,
                                       index=empresas_disponiveis.index(registro['Empresa']) if registro['Empresa'] in empresas_disponiveis else 0)
                servico = st.selectbox("Escolha o Serviço", servicos_disponiveis,
                                       index=servicos_disponiveis.index(registro['Servico']) if registro['Servico'] in servicos_disponiveis else 0)
                setor = st.selectbox("Escolha o Setor", setores_disponiveis,
                                     index=setores_disponiveis.index(registro['Setor']) if registro['Setor'] in setores_disponiveis else 0)
                data = st.date_input("Data", value=pd.to_datetime(registro['Data']))
                quantidade = st.number_input("Quantidade", min_value=1, step=1, value=registro['Quantidade'])


                if st.button("Salvar Edição"):
                    cursor.execute("""UPDATE servicos
                        SET Empresa = ?, Servico = ?, Data = ?, Setor = ?, Quantidade = ?
                        WHERE ID = ?""", (empresa, servico, data, setor, quantidade, registro['ID']))
                    conn.commit()
                    st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)
                    st.success("Serviço editado com sucesso!")


# Função para excluir serviços (marcar como inativo)
def excluir_servico():
    if not st.session_state.data.empty:
        servico_excluir = st.selectbox("Selecione o Serviço para Excluir", st.session_state.data['Servico'].unique(), key="servico_excluir")


        if servico_excluir:
            if st.button("Excluir Serviço"):
                cursor.execute("UPDATE servicos SET Ativo = 0 WHERE Servico = ?", (servico_excluir,))
                conn.commit()
                st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)
                st.success("Serviço excluído com sucesso!")


# Função para gerar relatório em PDF por setor e serviço
def gerar_relatorio_pdf_por_setor(empresa_selecionada):
    # Consulta para obter serviços por setor
    query = """
    SELECT Setor, Servico, SUM(Quantidade) AS Total
    FROM servicos
    WHERE Empresa = ? AND Ativo = 1
    GROUP BY Setor, Servico
    ORDER BY Setor, Servico
    """
    df_resultados = pd.read_sql_query(query, conn, params=(empresa_selecionada,))
   
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Relatório de Serviços para a Empresa: {empresa_selecionada}", ln=True, align='C')
    pdf.ln(10)


    pdf.set_font("Arial", 'B', 12)
    pdf.cell(80, 10, "Setor", border=1)
    pdf.cell(80, 10, "Serviço", border=1)
    pdf.cell(40, 10, "Total de Serviços", border=1)
    pdf.ln()


    pdf.set_font("Arial", '', 12)


    # Agrupar os resultados por setor
    for setor, grupo in df_resultados.groupby('Setor'):
        pdf.cell(80, 10, setor, border=1)


        primeiro_servico = grupo.iloc[0]
        pdf.cell(80, 10, primeiro_servico["Servico"], border=1)
        pdf.cell(40, 10, str(primeiro_servico["Total"]), border=1)
        pdf.ln()


        for _, linha in grupo.iloc[1:].iterrows():
            pdf.cell(80, 10, "", border=1)
            pdf.cell(80, 10, linha["Servico"], border=1)
            pdf.cell(40, 10, str(linha["Total"]), border=1)
            pdf.ln()


    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf_file_name = tmp_file.name
        pdf.output(pdf_file_name)


    return pdf_file_name


# Função para filtrar serviços por escola
def filtrar_servicos_por_escola():
    setor_selecionado = st.selectbox("Selecione o Setor/Escola", setores_disponiveis)
   
    if setor_selecionado:
        query = """
        SELECT Servico, SUM(Quantidade) AS Total
        FROM servicos
        WHERE Setor = ? AND Ativo = 1
        GROUP BY Servico
        """
        df_servicos = pd.read_sql_query(query, conn, params=(setor_selecionado,))


        if not df_servicos.empty:
            st.dataframe(df_servicos)
        else:
            st.warning(f"Nenhum serviço encontrado para o setor {setor_selecionado}.")


# Interface do Streamlit
st.title("Sistema de Gestão de Serviços")


# Criação de abas
aba = st.tabs(["Cadastro", "Edição", "Exclusão", "Consulta", "Relatório", "Filtrar por Escola"])


with aba[0]:
    st.header("Cadastro de Serviços")
    cadastrar_servico()


with aba[1]:
    st.header("Edição de Serviços")
    editar_servico()


with aba[2]:
    st.header("Exclusão de Serviços")
    excluir_servico()


with aba[3]:
    st.header("Consulta de Serviços")
    filtrar_servicos_por_escola()


with aba[4]:
    st.header("Relatório de Serviços")
    empresa_selecionada = st.selectbox("Selecione a Empresa", ["Selecione"] + empresas_disponiveis)
   
    if st.button("Emitir Relatório em PDF"):
        pdf_file_name = gerar_relatorio_pdf_por_setor(empresa_selecionada)
        with open(pdf_file_name, "rb") as f:
            st.download_button(
                label="Baixar Relatório PDF",
                data=f,
                file_name="relatorio_servicos.pdf",
                mime="application/pdf"
            )


# Fechar conexão com o banco de dados
conn.close()



