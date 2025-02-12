import streamlit as st
import pandas as pd
from db_utils import criar_tabela_servicos, inserir_servico, atualizar_servico, excluir_servico, consultar_servicos, adicionar_tarefas, inserir_tarefa
from reports import gerar_relatorio_pdf
from helpers import adicionar_opcao_selecione
import json
from datetime import datetime

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
aba = st.tabs(["Cadastro", "Edição", "Exclusão", "Consulta", "Relatório", "Tarefas"])

# Aba de Cadastro
with aba[0]:
    st.header("Cadastro de Serviços")
    empresa = st.selectbox("Escolha a Fornecedor", adicionar_opcao_selecione(empresas_disponiveis), key="cadastro_empresa")
    servico = st.selectbox("Escolha o Serviço", adicionar_opcao_selecione(servicos_disponiveis), key="cadastro_servico")
    setor = st.selectbox("Escolha o Setor", adicionar_opcao_selecione(setores_disponiveis), key="cadastro_setor")
    data = st.date_input("Data", key="cadastro_data")
    quantidade = st.number_input("Quantidade", min_value=1, step=1, key="cadastro_quantidade")

    if st.button("Cadastrar Serviço", key="cadastro_botao"):
        if empresa == "Selecione" or servico == "Selecione" or setor == "Selecione":
            st.error("Por favor, preencha todos os campos.")
        else:
            inserir_servico(empresa, servico, data, setor, quantidade)
            st.success("Serviço cadastrado com sucesso!")

# Aba de Edição
with aba[1]:
    st.header("Edição de Serviços")
    # Carregar os serviços ativos do banco
    try:
        df = pd.DataFrame(consultar_servicos())
        if df.empty:
            st.warning("Nenhum serviço disponível para edição.")
        else:
            df.columns = ["ID", "Empresa", "Servico", "Data", "Setor", "Quantidade", "Ativo"]

            id_selecionado = st.selectbox(
                "Selecione o Serviço para Editar",
                adicionar_opcao_selecione(df["ID"].astype(str).tolist()),
                key="editar_id"
            )

            if id_selecionado != "Selecione":
                servico_editar = df[df["ID"] == int(id_selecionado)].iloc[0]

                # Verificar e corrigir a data do banco de dados
                try:
                    data_convertida = pd.to_datetime(servico_editar["Data"], errors='coerce').date()
                    if pd.isnull(data_convertida):
                        raise ValueError("Data inválida")
                except:
                    st.warning("Formato de data inválido. Substituindo pela data atual.")
                    data_convertida = datetime.today().date()

                # Exibir campos para edição
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

            id_selecionado = st.selectbox(
                "Selecione o Serviço para Excluir",
                adicionar_opcao_selecione(df["ID"].astype(str).tolist()),
                key="excluir_id"
            )

            if id_selecionado != "Selecione":
                if st.button("Confirmar Exclusão", key="confirmar_exclusao"):
                    excluir_servico(int(id_selecionado))
                    st.success("Serviço excluído com sucesso!")
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
            df.columns = ["ID", "Empresa", "Servico", "Data", "Setor", "Quantidade", "Ativo"]
            st.dataframe(df)
    except Exception as e:
        st.error(f"Erro ao carregar os dados para consulta: {e}")

# Aba de Relatório
with aba[4]:
    st.header("Relatório de Serviços")
    try:
        # Obter os dados do banco de dados
        dados = consultar_servicos()

        # Definir colunas para o DataFrame (ajustar a ordem se necessário)
        colunas = ["ID", "Empresa", "Servico", "Data", "Setor", "Quantidade", "Ativo"]
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
                        # Filtrar DataFrame
                        df_filtrado = df[df['Empresa'] == empresa_selecionada]
                        if df_filtrado.empty:
                            st.warning(f"Nenhum serviço encontrado para a empresa {empresa_selecionada}.")
                        else:
                            # Gerar PDF
                            pdf_path = gerar_relatorio_pdf(df_filtrado, f"Relatório de {empresa_selecionada}")
                            with open(pdf_path, "rb") as pdf_file:
                                st.download_button("Baixar Relatório", data=pdf_file, file_name="relatorio.pdf", mime="application/pdf")
                    except Exception as e:
                        st.error(f"Erro ao gerar o relatório: {e}")
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")

# Aba de Tarefas
with aba[5]:
    st.header("Tarefas do SMED-TI")
    
    # Formulário para adicionar nova tarefa
    st.subheader("Adicionar Nova Tarefa")
    tarefa_texto = st.text_area("Descrição da Tarefa", key="tarefa_texto")
    funcionarios = ["Leo", "Luiz", "Vanderson"]
    funcionario_selecionado = st.selectbox("Selecione o Funcionário", adicionar_opcao_selecione(funcionarios), key="funcionario_selecionado")

    if st.button("Adicionar Tarefa", key="adicionar_tarefa"):
        if not tarefa_texto or funcionario_selecionado == "Selecione":
            st.error("Por favor, preencha todos os campos.")
        else:
            # Lógica para inserir a tarefa no banco de dados
            inserir_tarefa(tarefa_texto, funcionario_selecionado)
            st.success("Tarefa adicionada com sucesso!")

    # Exibir tarefas existentes
    st.subheader("Tarefas Existentes")
    try:
        df = pd.DataFrame(adicionar_tarefas())
        if df.empty:
            st.warning("Nenhuma tarefa disponível.")
        else:
            df.columns = ["ID", "Descrição", "Funcionário", "Data"]
            st.dataframe(df)
    except Exception as e:
        st.error(f"Erro ao carregar os dados de tarefas: {e}")