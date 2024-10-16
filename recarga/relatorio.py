import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Dados das recargas
data = [
    {"QTD": 7, "SETOR": "SMED", "ITEM": "RECARGA BROTHER 3442", "UNITÁRIO": 49.44, "TOTAL": 346.08},
    {"QTD": 2, "SETOR": "SMED", "ITEM": "RECARGA BROTHER B021", "UNITÁRIO": 45.50, "TOTAL": 91.00},
    {"QTD": 2, "SETOR": "SMED", "ITEM": "RECARGA BROTHER TN750", "UNITÁRIO": 49.44, "TOTAL": 98.88},
    {"QTD": 3, "SETOR": "SMED", "ITEM": "RECARGA KYOCERA", "UNITÁRIO": 84.00, "TOTAL": 252.00},
    {"QTD": 1, "SETOR": "SMED", "ITEM": "RECARGA HP 85", "UNITÁRIO": 58.00, "TOTAL": 58.00},
    {"QTD": 1, "SETOR": "STELA DUBOIS", "ITEM": "RECARGA BROTHER 1060", "UNITÁRIO": 45.50, "TOTAL": 45.50},
    {"QTD": 1, "SETOR": "STELA DUBOIS", "ITEM": "RECARGA BROTHER 3442", "UNITÁRIO": 49.44, "TOTAL": 49.44},
    {"QTD": 11, "SETOR": "ERALDO TINOCO DE MELO", "ITEM": "RECARGA BROTHER B021", "UNITÁRIO": 49.44, "TOTAL": 543.84},
    {"QTD": 4, "SETOR": "TERRABRÁS", "ITEM": "RECARGA BROTHER TN750", "UNITÁRIO": 49.90, "TOTAL": 199.60},
    {"QTD": 2, "SETOR": "TERRABRÁS", "ITEM": "RECARGA BROTHER 3442", "UNITÁRIO": 49.44, "TOTAL": 98.88},
    {"QTD": 2, "SETOR": "TERRABRÁS", "ITEM": "RECARGA BROTHER 420", "UNITÁRIO": 49.44, "TOTAL": 98.88},
]

# Criando o DataFrame com os dados
df = pd.DataFrame(data)

# Agrupando por valor unitário e somando a quantidade
relatorio_por_valor = df.groupby("UNITÁRIO").agg({"QTD": "sum", "TOTAL": "sum"}).reset_index()

# Função para gerar o relatório em PDF
def gerar_pdf(relatorio, nome_arquivo):
    doc = SimpleDocTemplate(nome_arquivo, pagesize=A4)
    story = []
    
    # Estilos para o título e o conteúdo
    styles = getSampleStyleSheet()
    titulo = Paragraph("Relatório de Recargas Agrupadas por Valor Unitário", styles['Title'])
    story.append(titulo)
    
    # Criando a tabela para o relatório
    dados_tabela = [["Valor Unitário", "Quantidade", "Total"]]
    
    # Adicionando os dados da tabela
    for index, row in relatorio.iterrows():
        dados_tabela.append([f"R$ {row['UNITÁRIO']:.2f}", int(row['QTD']), f"R$ {row['TOTAL']:.2f}"])
    
    # Estilizando a tabela
    tabela = Table(dados_tabela)
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    # Adicionando a tabela ao documento
    story.append(tabela)
    
    # Construindo o PDF
    doc.build(story)
    print(f"Relatório PDF '{nome_arquivo}' gerado com sucesso!")

# Gerando o relatório em PDF
gerar_pdf(relatorio_por_valor, "relatorio_recargas_por_valor.pdf")
