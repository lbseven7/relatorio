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
    empresa = st.selectbox("Escolha a Empresa", ["Selecione"] + empresas_disponiveis, key=f"empresa_cadastro")
    servico = st.selectbox("Escolha o Serviço", ["Selecione"] + servicos_disponiveis, key=f"servico_cadastro")
    setor = st.selectbox("Escolha o Setor", ["Selecione"] + setores_disponiveis, key=f"setor_cadastro")
    data = st.date_input("Data", key=f"data_cadastro")
    quantidade = st.number_input("Quantidade", min_value=1, step=1, key=f"quantidade_cadastro")

    if st.button("Cadastrar Serviço"):
        if empresa != "Selecione" and servico != "Selecione" and setor != "Selecione":
            cursor.execute("INSERT INTO servicos (Empresa, Servico, Data, Setor, Quantidade) VALUES (?, ?, ?, ?, ?) ",
                           (empresa, servico, data, setor, quantidade))
            conn.commit()
            st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)
            st.success("Serviço cadastrado com sucesso!")
        else:
            st.warning("Por favor, selecione todos os campos obrigatórios.")

# Função para editar serviços
def editar_servico():
    if not st.session_state.data.empty:
        id_editar = st.selectbox("Selecione o ID do Serviço para Editar", ["Selecione"] + list(st.session_state.data['ID']), key=f"id_editar")

        if id_editar != "Selecione":
            # Obtém o registro selecionado
            registro = st.session_state.data[st.session_state.data['ID'] == id_editar].iloc[0]

            empresa = st.selectbox("Escolha a Empresa", ["Selecione"] + empresas_disponiveis, index=empresas_disponiveis.index(registro['Empresa']) + 1, key=f"empresa_editar")
            servico_index = servicos_disponiveis.index(registro['Servico']) + 1 if registro['Servico'] in servicos_disponiveis else 0
            servico = st.selectbox("Escolha o Serviço", ["Selecione"] + servicos_disponiveis, index=servico_index, key=f"servico_editar")
            setor = st.selectbox("Escolha o Setor", ["Selecione"] + setores_disponiveis, index=setores_disponiveis.index(registro['Setor']) + 1, key=f"setor_editar")
            data = st.date_input("Data", value=pd.to_datetime(registro['Data']), key=f"data_editar")
            quantidade = st.number_input("Quantidade", min_value=1, step=1, value=registro['Quantidade'], key=f"quantidade_editar")

            if st.button("Salvar Edição"):
                if empresa != "Selecione" and servico != "Selecione" and setor != "Selecione":
                    cursor.execute("""UPDATE servicos
                        SET Empresa = ?, Servico = ?, Data = ?, Setor = ?, Quantidade = ?
                        WHERE ID = ?""", (empresa, servico, data, setor, quantidade, id_editar))
                    conn.commit()
                    st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)
                    st.success("Serviço editado com sucesso!")
                else:
                    st.warning("Por favor, selecione todos os campos obrigatórios.")

# Função para excluir serviços (marcar como inativo)
def excluir_servico():
    if not st.session_state.data.empty:
        # Adiciona a opção "Selecione" na seleção de serviços
        id_excluir = st.selectbox("Selecione o ID do Serviço para Excluir", ["Selecione"] + list(st.session_state.data['ID']), key=f"id_excluir")

        if id_excluir != "Selecione":
            if st.button("Excluir Serviço"):
                cursor.execute("UPDATE servicos SET Ativo = 0 WHERE ID = ?", (id_excluir,))
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
        # Adicionar o nome do setor uma vez
        pdf.cell(80, 10, setor, border=1)

        # Para o primeiro serviço, mostra o nome do serviço e total
        primeiro_servico = grupo.iloc[0]
        pdf.cell(80, 10, primeiro_servico["Servico"], border=1)
        pdf.cell(40, 10, str(primeiro_servico["Total"]), border=1)
        pdf.ln()

        # Adicionar os demais serviços do mesmo setor
        for _, linha in grupo.iloc[1:].iterrows():
            pdf.cell(80, 10, "", border=1)  # Espaço vazio para a coluna de setor
            pdf.cell(80, 10, linha["Servico"], border=1)
            pdf.cell(40, 10, str(linha["Total"]), border=1)
            pdf.ln()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf_file_name = tmp_file.name
        pdf.output(pdf_file_name)

    return pdf_file_name

# Função para consultar quantidade total de serviços
def consultar_quantidade_servicos():
    servico_selecionado = st.selectbox("Selecione o Serviço", ["Selecione"] + servicos_disponiveis)
    
    if st.button("Consultar Quantidade"):
        if servico_selecionado != "Selecione":
            quantidade = cursor.execute("SELECT SUM(Quantidade) FROM servicos WHERE Servico = ? AND Ativo = 1", (servico_selecionado,)).fetchone()[0]
            if quantidade is None:
                quantidade = 0
            st.success(f"A quantidade total de serviços '{servico_selecionado}' realizados é: {quantidade}")
        else:
            st.warning("Por favor, selecione um serviço.")

# Função para consultar quantidade de serviços por empresa
def consultar_quantidade_servicos_empresa():
    empresa_selecionada = st.selectbox("Selecione a Empresa", ["Selecione"] + empresas_disponiveis)
    
    if st.button("Consultar Quantidade por Empresa"):
        if empresa_selecionada != "Selecione":
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
            else:
                st.warning("Nenhum serviço encontrado para esta empresa.")
        else:
            st.warning("Por favor, selecione uma empresa.")

# Exibir opções na barra lateral
st.sidebar.title("Gerenciamento de Serviços")
opcao = st.sidebar.selectbox("Escolha uma opção", ["Cadastrar Serviço", "Editar Serviço", "Excluir Serviço", "Consultar Quantidade", "Consultar por Empresa"])

if opcao == "Cadastrar Serviço":
    st.title("Cadastrar Serviço")
    cadastrar_servico()
elif opcao == "Editar Serviço":
    st.title("Editar Serviço")
    editar_servico()
elif opcao == "Excluir Serviço":
    st.title("Excluir Serviço")
    excluir_servico()
elif opcao == "Consultar Quantidade":
    st.title("Consultar Quantidade de Serviços")
    consultar_quantidade_servicos()
elif opcao == "Consultar por Empresa":
    st.title("Consultar Quantidade de Serviços por Empresa")
    consultar_quantidade_servicos_empresa()

# Fechar a conexão ao final
conn.close()
