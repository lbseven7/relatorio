import streamlit as st
import json
import sqlite3
from fpdf import FPDF

# Carregar dados JSON
dados_json = '''
{
  "escolas": {
    "Fundamental": [
      "CARNEIRO RIBEIRO",
      "CENTRO EDUCACIONAL DO TRABALHADOR",
      "COLEGIO LUZIA SILVA",
      "DELMINDA FARIAS DE ALMEIDA",
      "EMANOEL DE OLIVEIRA BRITO",
      "EVERALDO SOUZA SANTOS",
      "JOAQUIM NERY DE SOUZA",
      "LOURIVAL ROSA DE SENA",
      "MENANDRO MINAHIM",
      "MONTEIRO LOBATO",
      "MUNICIPAL DIANA JUSSIENE",
      "NÚCLEO",
      "PRESIDENTE CASTELO BRANCO",
      "RURAL DE IPIUNA",
      "STELA CAMARA DUBOIS",
      "TERRABRAS",
      "VICENZO GASBARRE"
    ],
    "Infantil": [
      "ARLINDA EMILIA DE ASSIS",
      "ALEGRIA DE VIVER",
      "CENTRO SOCIAL URBANO - CRECHE",
      "CRECHE M. MARLEIDE PINTO DE N. NUNES",
      "ERALDO TINOCO DE MELO",
      "GRUPO ESCOLAR LOMANTO JUNIOR",
      "MONTEIRO LOBATO",
      "MUNICIPAL IRMA DULCE",
      "NÚCLEO",
      "PRESIDENTE CASTELO BRANCO",
      "RURAL DE IPIUNA",
      "STELA CAMARA DUBOIS",
      "TERRABRAS"
    ]
  },
  "servicos": {
    "RECARGA BROTHER 3442": "R$ 49,44",
    "RECARGA BROTHER 3472": "R$ 49,44",
    "RECARGA BROTHER B021": "R$ 45,50",
    "RECARGA BROTHER TN750": "R$ 49,44",
    "RECARGA KYOCERA": "R$ 84,00",
    "RECARGA HP 85": "R$ 58,00",
    "RECARGA BROTHER 1060": "R$ 45,50",
    "RECARGA BROTHER 420": "R$ 49,44",
    "RECARGA BROTHER 5652": "R$ 49,44",
    "RECARGA HP 105W": "R$ 58,00",
    "RECARGA HP W1330": "R$ 58,00",
    "RECARGA SAMSUNG ML2885": "R$ 49,44",
    "RECARGA KYOCERA TK1175": "R$ 84,00"
  }
}
'''

# Converter JSON em dicionário Python
dados = json.loads(dados_json)

# Configuração da interface
st.title("Neemias Rios dos Anjos - Recargas")

# Selecionar Tipo de Ensino, incluindo a SMED como uma opção separada
tipo_ensino = st.selectbox("Selecione o Tipo de Ensino", ["Educação Infantil", "Ensino Fundamental", "SMED"])

# Selecionar Escola com base no tipo de ensino
if tipo_ensino == "Educação Infantil":
    opcoes_escolas = dados['escolas']['Infantil']
elif tipo_ensino == "Ensino Fundamental":
    opcoes_escolas = dados['escolas']['Fundamental']
else:
    opcoes_escolas = ["SMED"]  # Apenas SMED é exibida para esta opção

# Exibir dropdown para seleção de escola
escola = st.selectbox("Selecione o Destino", opcoes_escolas)

# Selecionar Serviço
servico = st.selectbox("Selecione o Serviço", list(dados['servicos'].keys()))

# Valor unitário é carregado automaticamente baseado no serviço escolhido
valor_unitario = dados['servicos'][servico]

# Inserir a quantidade de serviços
quantidade = st.number_input("Quantidade", min_value=1, step=1)

# Calcular o total
total = float(valor_unitario.replace("R$", "").replace(",", ".")) * quantidade

# Mostrar o total
st.write(f"Total: R$ {total:.2f}")

# Função para gravar dados no banco
def gravar_dados(escola, tipo_ensino, servico, valor_unitario, quantidade, total):
    try:
        conn = sqlite3.connect("servicos.db")
        cursor = conn.cursor()
        
        # Verificar se a tabela existe e possui as colunas corretas
        cursor.execute("PRAGMA table_info(servicos_cadastrados);")
        colunas = cursor.fetchall()
        colunas_esperadas = ['escola', 'tipo_ensino', 'servico', 'valor_unitario', 'quantidade', 'total']
        
        # Checar se as colunas esperadas estão presentes
        if not all(coluna[1] in colunas_esperadas for coluna in colunas):
            st.error("A tabela não possui a estrutura correta.")
            return

        # Verificar se a escola já possui um registro do serviço
        cursor.execute("SELECT COUNT(*) FROM servicos_cadastrados WHERE escola=? AND servico=?", (escola, servico))
        existe = cursor.fetchone()[0] > 0

        if existe:
            # Se já existe, apenas atualize a quantidade e o total
            cursor.execute("UPDATE servicos_cadastrados SET quantidade = quantidade + ?, total = total + ? WHERE escola=? AND servico=?", 
                           (quantidade, total, escola, servico))
        else:
            # Se não existe, insira um novo registro
            cursor.execute("INSERT INTO servicos_cadastrados (escola, tipo_ensino, servico, valor_unitario, quantidade, total) VALUES (?, ?, ?, ?, ?, ?)", 
                           (escola, tipo_ensino, servico, float(valor_unitario.replace("R$", "").replace(",", ".")), quantidade, total))

        conn.commit()
        conn.close()
        st.success("Serviço cadastrado com sucesso!")
    except Exception as e:
        st.error(f"Ocorreu um erro ao gravar os dados: {e}")

def ajustar_nome(nome, limite=30):
    """Corta o nome se exceder o limite e adiciona '...'."""
    if len(nome) > limite:
        return nome[:limite] + "..."
    return nome

def gerar_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=8)  # Fonte reduzida

    # Cabeçalho
    pdf.cell(0, 10, "Relatório de Serviços", ln=True, align="C")
    pdf.ln(5)  # Espaço entre o título e o conteúdo

    # Definindo cabeçalhos da tabela
    pdf.set_font("Arial", style='B', size=8)  # Fonte dos cabeçalhos
    pdf.cell(40, 8, "Escola", border=1, align="C")  # Largura reduzida da coluna "Escola"
    pdf.cell(25, 8, "Tipo de Ensino", border=1, align="C")
    pdf.cell(40, 8, "Serviço", border=1, align="C")
    pdf.cell(20, 8, "Valor Unitário", border=1, align="C")
    pdf.cell(20, 8, "Quantidade", border=1, align="C")
    pdf.cell(20, 8, "Total", border=1, align="C")
    pdf.ln()  # Nova linha após o cabeçalho

    # Conectar ao banco de dados e obter todos os registros
    conn = sqlite3.connect("servicos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT escola, tipo_ensino, servico, valor_unitario, quantidade, total FROM servicos_cadastrados")
    
    registros = cursor.fetchall()
    conn.close()

    # Checar se há registros
    if not registros:
        pdf.cell(0, 10, txt="Nenhum serviço cadastrado.", ln=True, align="C")
    else:
        # Adicionar registros ao PDF
        pdf.set_font("Arial", size=8)  # Fonte padrão para registros
        for registro in registros:
            # Ajustar nomes
            escola_ajustada = ajustar_nome(registro[0])  # Ajusta o nome da escola
            tipo_ensino_ajustado = ajustar_nome(registro[1])  # Ajusta o tipo de ensino
            servico_ajustado = ajustar_nome(registro[2])  # Ajusta o nome do serviço
            
            pdf.cell(40, 8, txt=escola_ajustada, border=1, align="C")  # Usando cell para "Escola"
            pdf.cell(25, 8, txt=tipo_ensino_ajustado, border=1, align="C")
            pdf.cell(40, 8, txt=servico_ajustado, border=1, align="C")
            pdf.cell(20, 8, txt=f"R$ {registro[3]:.2f}", border=1, align="C")
            pdf.cell(20, 8, txt=str(registro[4]), border=1, align="C")
            pdf.cell(20, 8, txt=f"R$ {registro[5]:.2f}", border=1, align="C")
            pdf.ln()  # Nova linha após cada registro

    # Salvar o PDF
    pdf.output("relatorio_servico.pdf")
    st.success("PDF Gerado com sucesso!")

# Botões para gravar dados e gerar PDF
if st.button("Cadastrar Serviço"):
    gravar_dados(escola, tipo_ensino, servico, valor_unitario, quantidade, total)

if st.button("Gerar PDF"):
    gerar_pdf()
