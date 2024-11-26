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
    empresa = st.selectbox("Escolha a Fornecedor", empresas_disponiveis, key="empresa_cadastro")
    servico = st.selectbox("Escolha o Serviço", servicos_disponiveis, key="servico_cadastro")
    setor = st.selectbox("Escolha o Setor", setores_disponiveis, key="setor_cadastro")
    data = st.date_input("Data", key="data_cadastro")
    quantidade = st.number_input("Quantidade", min_value=1, step=1, key="quantidade_cadastro")

    if st.button("Cadastrar Serviço"):
        cursor.execute("INSERT INTO servicos (Empresa, Servico, Data, Setor, Quantidade) VALUES (?, ?, ?, ?, ?) ",
                       (empresa, servico, data, setor, quantidade))
        conn.commit()
        st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)
        st.success("Serviço cadastrado com sucesso!")

# Função para editar serviços
from datetime import datetime

from datetime import datetime

def editar_servico():
    if not st.session_state.data.empty:
        # Adicionar "Selecione" como opção padrão
        opcoes_servico = ["Selecione"] + st.session_state.data['Servico'].unique().tolist()
        id_editar = st.selectbox("Selecione o Serviço para Editar", opcoes_servico, key="servico_editar")

        if id_editar != "Selecione":
            registros = st.session_state.data[st.session_state.data['Servico'] == id_editar]

            if not registros.empty:
                registro = registros.iloc[0]

                # Empresa
                opcoes_empresa = ["Selecione"] + empresas_disponiveis
                empresa = st.selectbox("Escolha a Empresa", opcoes_empresa,
                                       index=opcoes_empresa.index(registro['Empresa']) + 1 if registro['Empresa'] in empresas_disponiveis else 0)

                # Serviço
                opcoes_servico_edit = ["Selecione"] + servicos_disponiveis
                servico = st.selectbox("Escolha o Serviço", opcoes_servico_edit,
                                       index=opcoes_servico_edit.index(registro['Servico']) + 1 if registro['Servico'] in servicos_disponiveis else 0)

                # Setor
                opcoes_setor = ["Selecione"] + setores_disponiveis
                setor = st.selectbox("Escolha o Setor", opcoes_setor,
                                     index=opcoes_setor.index(registro['Setor']) + 1 if registro['Setor'] in setores_disponiveis else 0)

                # Data do Serviço
                data = st.date_input("Data do Serviço", value=pd.to_datetime(registro['Data']).date())

                # Quantidade
                quantidade = st.number_input("Quantidade", min_value=1, step=1, value=registro['Quantidade'])

                # Salvar Edição
                if st.button("Salvar Edição"):
                    # Validar data futura
                    if data > datetime.now().date():
                        st.error("A data do serviço não pode ser uma data futura. Por favor, insira uma data válida.")
                    
                    # Validar campos obrigatórios
                    elif empresa == "Selecione" or servico == "Selecione" or setor == "Selecione":
                        st.error("Por favor, preencha todos os campos antes de salvar.")
                    
                    else:
                        # Verificar duplicação no banco de dados
                        query = """SELECT COUNT(*) FROM servicos 
                                   WHERE Empresa = ? AND Servico = ? AND Setor = ? AND Data = ? AND ID != ?"""
                        cursor.execute(query, (empresa, servico, setor, data, registro['ID']))
                        duplicados = cursor.fetchone()[0]
                        
                        if duplicados > 0:
                            st.error("Registro duplicado! Já existe um serviço com esses mesmos dados e data.")
                        else:
                            # Tentar realizar a atualização e confirmar
                            cursor.execute("""UPDATE servicos
                                SET Empresa = ?, Servico = ?, Data = ?, Setor = ?, Quantidade = ?
                                WHERE ID = ?""", (empresa, servico, data, setor, quantidade, registro['ID']))
                            conn.commit()
                            
                            # Verificar se a atualização foi bem-sucedida
                            registros_atualizados = cursor.rowcount
                            if registros_atualizados > 0:
                                st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)
                                st.success("Serviço editado com sucesso!")
                            else:
                                st.error("Erro ao atualizar o serviço. Por favor, tente novamente.")



# Função para excluir serviços (marcar como inativo)
def excluir_servico():
    if not st.session_state.data.empty:
        # Exibir os registros ativos para seleção
        servicos_excluir = st.session_state.data[st.session_state.data['Ativo'] == 1][['ID', 'Servico', 'Empresa', 'Data', 'Setor']]
        servicos_excluir['Descricao'] = servicos_excluir.apply(lambda row: f"ID: {row['ID']} - {row['Servico']} ({row['Empresa']}, {row['Setor']}, {row['Data']})", axis=1)

        # Selecione o serviço a ser excluído
        opcoes = ["Selecione"] + servicos_excluir['Descricao'].tolist()
        servico_selecionado = st.selectbox("Selecione o Serviço para Excluir", opcoes)

        if servico_selecionado != "Selecione":
            # Extrair o ID do registro selecionado
            id_excluir = int(servico_selecionado.split(' ')[1])

            if st.button("Excluir Serviço"):
                # Marcar o registro como inativo em vez de excluí-lo
                cursor.execute("UPDATE servicos SET Ativo = 0 WHERE ID = ?", (id_excluir,))
                conn.commit()

                # Atualizar a sessão de dados para não mostrar registros inativos
                st.session_state.data = pd.read_sql_query("SELECT * FROM servicos WHERE Ativo = 1", conn)
                st.success(f"Serviço com ID {id_excluir} marcado como inativo!")





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
    pdf.cell(0, 10, f"Relatório de Serviços: {empresa_selecionada}", ln=True, align='C')
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
aba = st.tabs(["Cadastro", "Edição", "Exclusão", "Consulta", "Relatório"])

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
    empresa_selecionada = st.selectbox("Selecione a Empresa", empresas_disponiveis)
   
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
