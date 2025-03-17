import streamlit as st
import pandas as pd
from db_utils import criar_tabela_servicos, inserir_servico, atualizar_servico, excluir_servico, consultar_servicos
from reports import gerar_relatorio_pdf
from helpers import adicionar_opcao_selecione
import json
from datetime import datetime
import sys

sys.setrecursionlimit(5000)

# Inicializar banco de dados
criar_tabela_servicos()

# Carregar dados estáticos
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)
servicos_disponiveis = dados["servicos_disponiveis"]
empresas_disponiveis = dados["empresas_disponiveis"]
setores_disponiveis = dados["setores_disponiveis"]

# Interface Streamlit
st.title("Sistema de Gestão de Serviços")

# Navegação por abas
aba = st.tabs(["Cadastro", "Edição", "Exclusão", "Consulta", "Relatório"])

# Aba de Cadastro
with aba[0]:
    st.header("Cadastro de Serviços")
    
    # Initialize session states
    if 'cadastro_submitted' not in st.session_state:
        st.session_state.cadastro_submitted = False
    if 'show_error' not in st.session_state:
        st.session_state.show_error = False
    
    # Create a form container
    with st.form("cadastro_form", clear_on_submit=True):
        empresa = st.selectbox("Escolha a Fornecedor", adicionar_opcao_selecione(empresas_disponiveis))
        servico = st.selectbox("Escolha o Serviço", adicionar_opcao_selecione(servicos_disponiveis))
        setor = st.selectbox("Escolha o Setor", adicionar_opcao_selecione(setores_disponiveis))
        data = st.date_input("Data")
        quantidade = st.number_input("Quantidade", min_value=1, step=1)
        
        submitted = st.form_submit_button("Cadastrar Serviço")
        
        if submitted:
            if empresa == "Selecione" or servico == "Selecione" or setor == "Selecione":
                st.session_state.show_error = True
            else:
                st.session_state.show_error = False
                inserir_servico(empresa, servico, data, setor, quantidade)
                st.session_state.cadastro_submitted = True
                st.success("Serviço cadastrado com sucesso!")
                st.rerun()
    
    # Show error message outside the form if needed
    if st.session_state.show_error:
        st.error("Por favor, preencha todos os campos.")
        st.session_state.show_error = False
    
    # Reset the submission state when the form is cleared
    if st.session_state.cadastro_submitted:
        st.session_state.cadastro_submitted = False

# Aba de Edição
with aba[1]:
    st.header("Edição de Serviços")
    try:
        df = pd.DataFrame(consultar_servicos())
        if df.empty:
            st.warning("Nenhum serviço disponível para edição.")
        else:
            df.columns = ["ID", "Empresa", "Servico", "Data", "Setor", "Quantidade", "Ativo"]

            servicos_para_editar = [f"{row['ID']} - {row['Servico']}" for _, row in df.iterrows()]
            
            servico_selecionado = st.selectbox(
                "Selecione o Serviço para Editar",
                adicionar_opcao_selecione(servicos_para_editar),
                key="editar_id"
            )

            if servico_selecionado != "Selecione":
                id_selecionado = int(servico_selecionado.split(" - ")[0])
                servico_editar = df[df["ID"] == id_selecionado].iloc[0]

                try:
                    data_convertida = pd.to_datetime(servico_editar["Data"], errors='coerce').date()
                    if pd.isnull(data_convertida):
                        raise ValueError("Data inválida")
                except:
                    st.warning("Formato de data inválido. Substituindo pela data atual.")
                    data_convertida = datetime.today().date()

                empresa = st.selectbox(
                    "Escolha a Empresa",
                    adicionar_opcao_selecione(empresas_disponiveis),
                    index=empresas_disponiveis.index(servico_editar["Empresa"]) + 1 if servico_editar["Empresa"] in empresas_disponiveis else 0,
                    key="editar_empresa"
                )
                servico = st.selectbox(
                    "Escolha o Serviço",
                    adicionar_opcao_selecione(servicos_disponiveis),
                    index=servicos_disponiveis.index(servico_editar["Servico"]) + 1 if servico_editar["Servico"] in servicos_disponiveis else 0,
                    key="editar_servico"
                )
                setor = st.selectbox(
                    "Escolha o Setor",
                    adicionar_opcao_selecione(setores_disponiveis),
                    index=setores_disponiveis.index(servico_editar["Setor"]) + 1 if servico_editar["Setor"] in setores_disponiveis else 0,
                    key="editar_setor"
                )
                data = st.date_input("Data", value=data_convertida, key="editar_data")
                quantidade = st.number_input("Quantidade", min_value=1, step=1, value=servico_editar["Quantidade"], key="editar_quantidade")

                if st.button("Salvar Alterações", key="salvar_edicao"):
                    atualizar_servico(int(id_selecionado), empresa, servico, data, setor, quantidade)
                    st.success("Serviço atualizado com sucesso!")
                    st.rerun()
    except Exception as e:
        st.error(f"Erro ao carregar os dados para edição: {e}")

# Aba de Exclusão
with aba[2]:
    st.header("Exclusão de Serviços")
    try:
        df = pd.DataFrame(consultar_servicos())
        if df.empty:
            st.warning("Nenhum serviço disponível para exclusão.")
        else:
            df.columns = ["ID", "Empresa", "Servico", "Data", "Setor", "Quantidade", "Ativo"]
            
            # Filter only active services
            df_ativos = df[df['Ativo'] == 1]
            
            if df_ativos.empty:
                st.warning("Nenhum serviço ativo disponível para exclusão.")
            else:
                servicos_para_excluir = [f"{row['ID']} - {row['Servico']} ({row['Empresa']})" for _, row in df_ativos.iterrows()]
                
                servico_selecionado = st.selectbox(
                    "Selecione o Serviço para Excluir",
                    adicionar_opcao_selecione(servicos_para_excluir),
                    key="excluir_id"
                )

                if servico_selecionado != "Selecione":
                    id_selecionado = int(servico_selecionado.split(" - ")[0])
                    servico_a_excluir = df[df["ID"] == id_selecionado].iloc[0]
                    
                    st.write("Serviço a ser excluído:")
                    st.write({
                        "ID": servico_a_excluir["ID"],
                        "Empresa": servico_a_excluir["Empresa"],
                        "Serviço": servico_a_excluir["Servico"],
                        "Data": servico_a_excluir["Data"],
                        "Setor": servico_a_excluir["Setor"],
                        "Quantidade": servico_a_excluir["Quantidade"]
                    })

                    if st.button("Confirmar Exclusão", key="confirmar_exclusao"):
                        try:
                            excluir_servico(id_selecionado)
                            st.success(f"Serviço ID {id_selecionado} excluído com sucesso!")
                            time.sleep(1)  # Give user time to see the success message
                            st.rerun()
                        except Exception as e:
                            st.error(f"Erro ao excluir o serviço: {e}")
    except Exception as e:
        st.error(f"Erro ao carregar os dados para exclusão: {e}")

# Aba de Consulta
with aba[3]:
    st.header("Consulta de Serviços")
    try:
        df = pd.DataFrame(consultar_servicos())
        
        if df.empty:
            st.warning("Nenhum serviço disponível para consulta.")
        else:
            df.columns = ["ID", "Empresa", "Servico", "Setor", "Data", "Quantidade", "Ativo"]
            st.dataframe(df)
    except Exception as e:
        st.error(f"Erro ao carregar os dados para consulta: {e}")

# Aba de Relatório
with aba[4]:
    st.header("Relatório de Serviços")
    try:
        dados = consultar_servicos()
        colunas = ["ID", "Empresa", "Servico", "Setor","Data", "Quantidade", "Ativo"]
        df = pd.DataFrame(dados, columns=colunas)

        if df.empty:
            st.warning("Nenhum serviço disponível para gerar relatório.")
        else:
            empresa_selecionada = st.selectbox("Selecione a Empresa", adicionar_opcao_selecione(empresas_disponiveis), key="relatorio_empresa")
            
            if st.button("Emitir Relatório em PDF", key="emitir_relatorio"):
                if empresa_selecionada == "Selecione":
                    st.error("Por favor, selecione uma empresa.")
                else:
                    try:
                        df_filtrado = df[df['Empresa'] == empresa_selecionada]
                        if df_filtrado.empty:
                            st.warning(f"Nenhum serviço encontrado para a empresa {empresa_selecionada}.")
                        else:
                            pdf_path = gerar_relatorio_pdf(df_filtrado, f"Relatório de {empresa_selecionada}")
                            with open(pdf_path, "rb") as pdf_file:
                                st.download_button("Baixar Relatório", data=pdf_file, file_name="relatorio.pdf", mime="application/pdf")
                    except Exception as e:
                        st.error(f"Erro ao gerar o relatório: {e}")
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")

