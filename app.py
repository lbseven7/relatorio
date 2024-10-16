import streamlit as st
import pandas as pd
import sqlite3
from fpdf import FPDF
import tempfile
import json
from datetime import datetime

# Carregar listas de serviços, empresas e setores do arquivo JSON
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Acessando as listas
servicos_disponiveis = ["Selecione"] + dados["servicos_disponiveis"]
empresas_disponiveis = ["Selecione"] + dados["empresas_disponiveis"]
setores_disponiveis = ["Selecione"] + dados["setores_disponiveis"]

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

# Função para formatar a data para o formato brasileiro dd/mm/yyyy
def formatar_data_para_ptbr(data):
    return data.strftime('%d/%m/%Y')

# Função para formatar a data para o formato ISO yyyy-mm-dd
def formatar_data_para_iso(data):
    return data.strftime('%Y-%m-%d')

# Função para cadastrar serviços
def cadastrar_servico():
    empresa = st.selectbox("Escolha a Empresa", empresas_disponiveis, key=f"empresa_cadastro")
    servico = st.selectbox("Escolha o Serviço", servicos_disponiveis, key=f"servico_cadastro")
    setor = st.selectbox("Escolha o Setor", setores_disponiveis, key=f"setor_cadastro")
    data = st.date_input("Data", key=f"data_cadastro")
    quantidade = st.number_input("Quantidade", min_value=1, step=1, key=f"quantidade_cadastro")

    # Formatar a data para o formato ISO antes de salvar no banco
    data_iso = formatar_data_para_iso(data)

    if st.button("Cadastrar Serviço"):
        if empresa == "Selecione" or servico == "Selecione" or setor == "Selecione":
            st.warning("Por favor, selecione todos os campos.")
        else:
            cursor.execute("INSERT INTO servicos (Empresa, Servico, Data, Setor, Quantidade) VALUES (?, ?, ?, ?, ?)",
                           (empresa, servico, data_iso, setor, quantidade))
            conn.commit()
            st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)
            st.success("Serviço cadastrado com sucesso!")

# Função para editar serviços
def editar_servico():
    if not st.session_state.data.empty:
        id_editar = st.selectbox("Selecione o ID do Serviço para Editar", st.session_state.data['ID'], key=f"id_editar")

        # Obtém o registro selecionado
        registro = st.session_state.data[st.session_state.data['ID'] == id_editar].iloc[0]

        empresa = st.selectbox("Escolha a Empresa", empresas_disponiveis, index=empresas_disponiveis.index(registro['Empresa']), key=f"empresa_editar")
        servico_index = servicos_disponiveis.index(registro['Servico']) if registro['Servico'] in servicos_disponiveis else 0
        servico = st.selectbox("Escolha o Serviço", servicos_disponiveis, index=servico_index, key=f"servico_editar")
        setor = st.selectbox("Escolha o Setor", setores_disponiveis, index=setores_disponiveis.index(registro['Setor']), key=f"setor_editar")

        # Verifica o formato da data no banco e faz a conversão necessária
        try:
            data = datetime.strptime(registro['Data'], '%d/%m/%Y')  # Se já estiver em formato pt-BR
        except ValueError:
            data = datetime.strptime(registro['Data'], '%Y-%m-%d')  # Caso esteja no formato ISO

        data_editada = st.date_input("Data", value=data, key=f"data_editar")

        quantidade = st.number_input("Quantidade", min_value=1, step=1, value=registro['Quantidade'], key=f"quantidade_editar")

        if st.button("Salvar Edição"):
            # Formatar a data para o formato ISO ao salvar
            data_editada_iso = formatar_data_para_iso(data_editada)

            cursor.execute("""UPDATE servicos
                SET Empresa = ?, Servico = ?, Data = ?, Setor = ?, Quantidade = ?
                WHERE ID = ?""", (empresa, servico, data_editada_iso, setor, quantidade, id_editar))
            conn.commit()
            st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)
            st.success("Serviço editado com sucesso!")

# Função para excluir serviços (marcar como inativo)
def excluir_servico():
    if not st.session_state.data.empty:
        id_excluir = st.selectbox("Selecione o ID do Serviço para Excluir", st.session_state.data['ID'], key=f"id_excluir")

        if st.button("Excluir Serviço"):
            cursor.execute("UPDATE servicos SET Ativo = 0 WHERE ID = ?", (id_excluir,))
            conn.commit()
            st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)
            st.success("Serviço excluído com sucesso!")

# Função para gerar relatório em PDF por setor e serviço
def gerar_relatorio_pdf_por_setor(empresa_selecionada):
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

# Função para consultar quantidade total de serviços
def consultar_quantidade_servicos():
    servico_selecionado = st.selectbox("Selecione o Serviço", servicos_disponiveis)
    
    if st.button("Consultar Quantidade"):
        quantidade = cursor.execute("SELECT SUM(Quantidade) FROM servicos WHERE Servico = ? AND Ativo = 1", (servico_selecionado,)).fetchone()[0]
        if quantidade is None:
            quantidade = 0
        st.success(f"A quantidade total de serviços '{servico_selecionado}' realizados é: {quantidade}")

# Função para consultar quantidade de serviços por empresa
def consultar_quantidade_servicos_empresa():
    empresa_selecionada = st.selectbox("Selecione a Empresa", empresas_disponiveis)
    
    if st.button("Consultar Quantidade por Empresa"):
        query = """
        SELECT Setor, Servico, SUM(Quantidade) AS Total
        FROM servicos
        WHERE Empresa = ? AND Ativo = 1
        GROUP BY Setor, Servico
        ORDER BY Setor, Servico
        """
        df_resultados = pd.read_sql_query(query, conn, params=(empresa_selecionada,))
        
        if not df_resultados.empty:
            st.write(df_resultados)

            gerar_relatorio = st.checkbox("Gerar Relatório em PDF")

            if gerar_relatorio:
                pdf_file = gerar_relatorio_pdf_por_setor(empresa_selecionada)
                with open(pdf_file, "rb") as f:
                    st.download_button("Baixar Relatório em PDF", f, file_name=f"Relatorio_{empresa_selecionada}.pdf")
        else:
            st.warning(f"Não foram encontrados serviços para a empresa '{empresa_selecionada}'.")

# Título principal da aplicação
st.title("Cadastro de Serviços por Empresa")

# Abas da aplicação
abas = st.tabs(["Cadastrar Serviço", "Editar Serviço", "Excluir Serviço", "Consultar Quantidade Total", "Consultar por Empresa"])

with abas[0]:
    cadastrar_servico()

with abas[1]:
    editar_servico()

with abas[2]:
    excluir_servico()

with abas[3]:
    consultar_quantidade_servicos()

with abas[4]:
    consultar_quantidade_servicos_empresa()
