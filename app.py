import streamlit as st
import pandas as pd
import altair as alt
from db_utils import criar_tabela_servicos, inserir_servico, atualizar_servico, excluir_servico, consultar_servicos
from reports import gerar_relatorio_pdf
from helpers import adicionar_opcao_selecione
import json
from datetime import datetime
import sys
from io import BytesIO
import time

# Set page config first
st.set_page_config(
    page_title="Sistema de Gestão de Serviços",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: white !important;
        color: #4CAF50 !important;
        border: 2px solid #4CAF50 !important;
    }
    .stSelectbox {
        background-color: #F0F2F6;
    }
    .st-emotion-cache-1v0mbdj {
        width: 100%;
    }
    div[data-testid="stHeader"] {
        background-color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

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
    if 'itens_pedido' not in st.session_state:
        st.session_state.itens_pedido = []
    if 'setor_atual' not in st.session_state:
        st.session_state.setor_atual = "Selecione"
    if 'empresa_atual' not in st.session_state:
        st.session_state.empresa_atual = "Selecione"
    if 'data_atual' not in st.session_state:
        st.session_state.data_atual = datetime.today().date()
    
    # Create a form container
    with st.form("cadastro_form", clear_on_submit=False):
        empresa = st.selectbox(
            "Escolha o Fornecedor",
            adicionar_opcao_selecione(empresas_disponiveis),
            index=empresas_disponiveis.index(st.session_state.empresa_atual) + 1 if st.session_state.empresa_atual in empresas_disponiveis else 0
        )
        setor = st.selectbox(
            "Escolha o Setor",
            adicionar_opcao_selecione(setores_disponiveis),
            index=setores_disponiveis.index(st.session_state.setor_atual) + 1 if st.session_state.setor_atual in setores_disponiveis else 0
        )
        servico = st.selectbox("Escolha o Serviço", adicionar_opcao_selecione(servicos_disponiveis))
        data = st.date_input("Data", value=st.session_state.data_atual)
        
        col1, col2 = st.columns(2)
        with col1:
            quantidade = st.number_input("Quantidade", min_value=1, step=1)
        with col2:
            unidade = st.selectbox(
                "Unidade de Medida",
                ["Unidade", "Metro", "Centímetro", "Milímetro", "Folha", "Pacote", "Caixa", "Litro", "Mililitro"]
            )
        
        col1, col2, col3 = st.columns(3)
        with col1:
            adicionar = st.form_submit_button("Adicionar Item")
        with col2:
            finalizar = st.form_submit_button("Finalizar Pedido")
        with col3:
            limpar = st.form_submit_button("Limpar Formulário")
        
        if adicionar:
            if empresa == "Selecione" or servico == "Selecione" or setor == "Selecione":
                st.session_state.show_error = True
            else:
                # Salvar os valores atuais
                st.session_state.empresa_atual = empresa
                st.session_state.setor_atual = setor
                st.session_state.data_atual = data
                
                item = {
                    "empresa": empresa,
                    "servico": servico,
                    "setor": setor,
                    "data": data,
                    "quantidade": quantidade,
                    "unidade": unidade
                }
                st.session_state.itens_pedido.append(item)
                st.success("Item adicionado ao pedido!")
        
        if finalizar:
            if not st.session_state.itens_pedido:
                st.error("Adicione pelo menos um item ao pedido!")
            else:
                for item in st.session_state.itens_pedido:
                    inserir_servico(
                        item["empresa"],
                        item["servico"],
                        item["data"],
                        item["setor"],
                        item["quantidade"]
                    )
                # Limpar todos os dados após finalizar
                st.session_state.itens_pedido = []
                st.session_state.empresa_atual = "Selecione"
                st.session_state.setor_atual = "Selecione"
                st.session_state.data_atual = datetime.today().date()
                st.session_state.cadastro_submitted = True
                st.success("Pedido cadastrado com sucesso!")
                st.rerun()
        
        if limpar:
            st.session_state.empresa_atual = "Selecione"
            st.session_state.setor_atual = "Selecione"
            st.session_state.data_atual = datetime.today().date()
            st.session_state.itens_pedido = []
            st.rerun()
    
    # Mostrar itens do pedido atual
    if st.session_state.itens_pedido:
        st.subheader("Itens do Pedido Atual")
        for idx, item in enumerate(st.session_state.itens_pedido, 1):
            st.write(f"**Item {idx}:**")
            st.write(f"- Fornecedor: {item['empresa']}")
            st.write(f"- Serviço: {item['servico']}")
            st.write(f"- Setor: {item['setor']}")
            st.write(f"- Data: {item['data'].strftime('%d/%m/%Y')}")
            st.write(f"- Quantidade: {item['quantidade']} {item['unidade']}")
            st.write("---")
    
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
            df.columns = ["ID", "Empresa", "Servico", "Setor", "Data", "Quantidade", "Ativo"]
            
            # Filter only active services
            df_ativos = df[df['Ativo'] == 1]
            
            if df_ativos.empty:
                st.warning("Nenhum serviço ativo disponível para exclusão.")
            else:
                # Destacando o setor no início da descrição
                servicos_para_excluir = [f"{row['Setor']} - {row['ID']} - {row['Servico']} ({row['Empresa']})" for _, row in df_ativos.iterrows()]
                
                servico_selecionado = st.selectbox(
                    "Selecione o Serviço para Excluir",
                    adicionar_opcao_selecione(servicos_para_excluir),
                    key="excluir_id"
                )

                if servico_selecionado != "Selecione":
                    id_selecionado = int(servico_selecionado.split(" - ")[1])
                    servico_excluir = df_ativos[df_ativos["ID"] == id_selecionado].iloc[0]
                    
                    st.write("Serviço a ser excluído:")
                    info_servico = {
                        "Setor/Escola": servico_excluir["Setor"],
                        "ID": servico_excluir["ID"],
                        "Empresa": servico_excluir["Empresa"],
                        "Serviço": servico_excluir["Servico"],
                        "Data": pd.to_datetime(servico_excluir["Data"]).strftime("%d/%m/%Y"),
                        "Quantidade": servico_excluir["Quantidade"]
                    }
                    
                    # Exibindo as informações na ordem correta
                    ordem_exibicao = ["Setor/Escola", "ID", "Empresa", "Serviço", "Data", "Quantidade"]
                    for campo in ordem_exibicao:
                        st.write(f"**{campo}:** {info_servico[campo]}")
                    
                    if st.button("Confirmar Exclusão", key="confirmar_exclusao"):
                        excluir_servico(int(id_selecionado))
                        st.success(f"Serviço ID {id_selecionado} excluído com sucesso!")
                        time.sleep(1)
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
            
            # Filtros avançados
            col1, col2, col3 = st.columns(3)
            with col1:
                empresa_filtro = st.selectbox(
                    "Filtrar por Empresa",
                    ["Todas as Empresas"] + list(df["Empresa"].unique()),
                    key="consulta_empresa"
                )
            with col2:
                setor_filtro = st.selectbox(
                    "Filtrar por Setor",
                    ["Todos os Setores"] + list(df["Setor"].unique()),
                    key="consulta_setor"
                )
            with col3:
                servico_filtro = st.selectbox(
                    "Filtrar por Serviço",
                    ["Todos os Serviços"] + list(df["Servico"].unique()),
                    key="consulta_servico"
                )
            
            # Filtro de data
            data_inicio, data_fim = st.columns(2)
            with data_inicio:
                start_date = st.date_input("Data Inicial", min(pd.to_datetime(df["Data"])).date())
            with data_fim:
                end_date = st.date_input("Data Final", max(pd.to_datetime(df["Data"])).date())
            
            # Aplicar filtros
            df_filtrado = df.copy()
            if empresa_filtro != "Todas as Empresas":
                df_filtrado = df_filtrado[df_filtrado["Empresa"] == empresa_filtro]
            if setor_filtro != "Todos os Setores":
                df_filtrado = df_filtrado[df_filtrado["Setor"] == setor_filtro]
            if servico_filtro != "Todos os Serviços":
                df_filtrado = df_filtrado[df_filtrado["Servico"] == servico_filtro]
            
            df_filtrado["Data"] = pd.to_datetime(df_filtrado["Data"])
            df_filtrado = df_filtrado[
                (df_filtrado["Data"].dt.date >= start_date) &
                (df_filtrado["Data"].dt.date <= end_date)
            ]
            
            # Dashboard
            st.subheader("Dashboard")
            col1, col2 = st.columns(2)
            
            with col1:
                # Gráfico de serviços por empresa
                chart_empresa = alt.Chart(df_filtrado.groupby("Empresa")["Quantidade"].sum().reset_index()).mark_bar().encode(
                    x=alt.X('Empresa:N', title='Empresa'),
                    y=alt.Y('Quantidade:Q', title='Quantidade'),
                    tooltip=['Empresa', 'Quantidade']
                ).properties(
                    title='Quantidade de Serviços por Empresa'
                )
                st.altair_chart(chart_empresa, use_container_width=True)
            
            with col2:
                # Gráfico de serviços por setor com escala de cores personalizada
                chart_setor = alt.Chart(df_filtrado.groupby("Setor")["Quantidade"].sum().reset_index()).mark_arc().encode(
                    theta=alt.Theta(field="Quantidade", type="quantitative"),
                    color=alt.Color(
                        field="Setor",
                        type="nominal",
                        scale=alt.Scale(scheme='category20')  # Usando uma escala de cores com 20 cores diferentes
                    ),
                    tooltip=['Setor', 'Quantidade']
                ).properties(
                    title='Distribuição de Serviços por Setor'
                )
                st.altair_chart(chart_setor, use_container_width=True)
            
            # Tabela com paginação
            st.subheader("Dados Detalhados")
            items_per_page = st.selectbox("Itens por página", [10, 20, 50, 100, len(df_filtrado)])
            total_pages = len(df_filtrado) // items_per_page + (1 if len(df_filtrado) % items_per_page > 0 else 0)
            page = st.number_input("Página", min_value=1, max_value=total_pages, value=1) - 1
            
            start_idx = page * items_per_page
            end_idx = start_idx + items_per_page
            
            st.dataframe(df_filtrado.iloc[start_idx:end_idx])
            st.write(f"Mostrando {start_idx + 1} a {min(end_idx, len(df_filtrado))} de {len(df_filtrado)} registros")
            
            # Exportar dados
            st.subheader("Exportar Dados")
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Exportar para Excel"):
                    output = BytesIO()
                    with pd.ExcelWriter(output, engine="openpyxl") as writer:
                        df_filtrado.to_excel(writer, index=False)
                    excel_data = output.getvalue()
                    st.download_button(
                        label="Baixar Excel",
                        data=excel_data,
                        file_name="servicos.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            
            with col2:
                if st.button("Exportar para CSV"):
                    csv = df_filtrado.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        label="Baixar CSV",
                        data=csv,
                        file_name="servicos.csv",
                        mime="text/csv"
                    )
            
    except Exception as e:
        st.error(f"Erro ao carregar os dados para consulta: {e}")

# Aba de Relatório
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
            # Converter a coluna Data para datetime antes de qualquer filtro
            df['Data'] = pd.to_datetime(df['Data'])
            
            # Filtrar registros até a data atual
            data_atual = datetime.now().date()
            df = df[df['Data'].dt.date <= data_atual]
            
            # Garantir que a lista de empresas disponíveis corresponda exatamente ao que está no banco
            empresas_banco = sorted(df['Empresa'].unique())
            
            empresa_selecionada = st.selectbox("Selecione a Empresa", 
                                             adicionar_opcao_selecione(empresas_banco), 
                                             key="relatorio_empresa")
            
            if empresa_selecionada != "Selecione":
                # Filtrar apenas por empresa e status ativo
                df_filtrado = df[
                    (df['Empresa'] == empresa_selecionada) & 
                    (df['Ativo'] == 1)
                ]
                
                if df_filtrado.empty:
                    st.warning(f"Nenhum serviço encontrado para a empresa {empresa_selecionada}.")
                else:
                    st.subheader("Prévia do Relatório")
                    
                    # Criar cópia para exibição
                    df_exibicao = df_filtrado.copy()
                    df_exibicao['Data'] = df_exibicao['Data'].dt.strftime('%d/%m/%Y')
                    
                    # Remover colunas desnecessárias
                    df_exibicao = df_exibicao.drop(['Ativo'], axis=1)
                    
                    # Informações sobre os registros
                    st.write(f"Total de registros encontrados: {len(df_exibicao)}")
                    st.write("Período dos registros:")
                    st.write(f"De: {df_filtrado['Data'].min().strftime('%d/%m/%Y')} até {df_filtrado['Data'].max().strftime('%d/%m/%Y')}")
                    
                    # Exibir dados ordenados por data
                    df_exibicao = df_exibicao.sort_values('Data')
                    st.dataframe(df_exibicao)
                    
                    # Totais por setor
                    st.subheader("Totais por Setor")
                    totais_setor = df_filtrado.groupby('Setor')['Quantidade'].sum().reset_index()
                    st.dataframe(totais_setor)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("Emitir Relatório em PDF", key="emitir_relatorio"):
                            try:
                                pdf_path = gerar_relatorio_pdf(df_filtrado, f"Relatório de {empresa_selecionada}")
                                with open(pdf_path, "rb") as pdf_file:
                                    st.download_button("Baixar Relatório", data=pdf_file, file_name="relatorio.pdf", mime="application/pdf")
                            except Exception as e:
                                st.error(f"Erro ao gerar o relatório: {e}")
            else:
                st.info("Selecione uma empresa para visualizar e gerar o relatório.")
                
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")

if __name__ == '__main__':
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Acesse o aplicativo em: http://{local_ip}:8501")
    
    # Iniciar o servidor Streamlit
    import streamlit.web.bootstrap
    streamlit.web.bootstrap.run(
        "app.py",
        "",
        [],
        flag_options={
            "server.address": "0.0.0.0",
            "server.port": 8501
        }
    )

