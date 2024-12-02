import streamlit as st
import pandas as pd
from db_utils import criar_tabela_servicos, inserir_servico, atualizar_servico, excluir_servico, consultar_servicos
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
aba = st.tabs(["Cadastro", "Edição", "Exclusão", "Consulta", "Relatório"])

# Aba de Cadastro
with aba[0]:
    st.header("Cadastro de Serviços")
    empresa = st.selectbox("Escolha a Fornecedor", adicionar_opcao_selecione(empresas_disponiveis))
    servico = st.selectbox("Escolha o Serviço", adicionar_opcao_selecione(servicos_disponiveis))
    setor = st.selectbox("Escolha o Setor", adicionar_opcao_selecione(setores_disponiveis))
    data = st.date_input("Data")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)

    if st.button("Cadastrar Serviço"):
        if empresa == "Selecione" or servico == "Selecione" or setor == "Selecione":
            st.error("Por favor, preencha todos os campos.")
        else:
            inserir_servico(empresa, servico, data, setor, quantidade)
            st.success("Serviço cadastrado com sucesso!")

# Aba de Edição
with aba[1]:
    st.header("Edição de Serviços")
    # Carregar os serviços ativos do banco
    df = pd.DataFrame(consultar_servicos())
    df.columns = ["ID", "Empresa", "Servico", "Data", "Setor", "Quantidade", "Ativo"]

    if not df.empty:
        id_selecionado = st.selectbox(
            "Selecione o Serviço para Editar",
            adicionar_opcao_selecione(df["ID"].astype(str).tolist()),
            key="editar_id"
        )

        if id_selecionado != "Selecione":
            servico_editar = df[df["ID"] == int(id_selecionado)].iloc[0]
            
            # Verificar e corrigir a data do banco de dados
            try:
                if isinstance(servico_editar["Data"], str):
                    # Tenta converter a data
                    data_convertida = pd.to_datetime(servico_editar["Data"], format='%Y-%m-%d', errors='coerce').date()
                elif isinstance(servico_editar["Data"], datetime):
                    # Já é um objeto datetime, converte para date
                    data_convertida = servico_editar["Data"].date()
                else:
                    # Valor inesperado
                    data_convertida = None

                # Substituir valores inválidos
                if not data_convertida or pd.isna(data_convertida):
                    st.warning(f"Formato de data inválido para o ID {servico_editar['ID']}. Substituindo pela data atual.")
                    data_convertida = datetime.today().date()

            except Exception as e:
                st.warning(f"Erro ao processar a data: {e}. Substituindo pela data atual.")
                data_convertida = datetime.today().date()

            # Exibe a data no seletor
            data = st.date_input("Data", value=data_convertida, key="editar_data")

            # Verificar e selecionar Empresa
            if servico_editar["Empresa"] in empresas_disponiveis:
                index_empresa = empresas_disponiveis.index(servico_editar["Empresa"]) + 1
            else:
                index_empresa = 0
            empresa = st.selectbox(
                "Escolha a Empresa",
                adicionar_opcao_selecione(empresas_disponiveis),
                index=index_empresa,
                key="editar_empresa"
            )

            # Verificar e selecionar Serviço
            if servico_editar["Servico"] in servicos_disponiveis:
                index_servico = servicos_disponiveis.index(servico_editar["Servico"]) + 1
            else:
                index_servico = 0
            servico = st.selectbox(
                "Escolha o Serviço",
                adicionar_opcao_selecione(servicos_disponiveis),
                index=index_servico,
                key="editar_servico"
            )

            # Verificar e selecionar Setor
            if servico_editar["Setor"] in setores_disponiveis:
                index_setor = setores_disponiveis.index(servico_editar["Setor"]) + 1
            else:
                index_setor = 0
            setor = st.selectbox(
                "Escolha o Setor",
                adicionar_opcao_selecione(setores_disponiveis),
                index=index_setor,
                key="editar_setor"
            )

            # Quantidade
            quantidade = st.number_input("Quantidade", min_value=1, step=1, value=servico_editar["Quantidade"], key="editar_quantidade")

            if st.button("Salvar Alterações", key="salvar_edicao"):
                atualizar_servico(int(id_selecionado), empresa, servico, data, setor, quantidade)
                st.success("Serviço atualizado com sucesso!")
    else:
        st.warning("Nenhum serviço disponível para edição.")
