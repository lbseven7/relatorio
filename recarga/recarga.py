from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Dados da tabela
data = [
    ["07", "SMED", "RECARGA BROTHER 3442", "R$ 49,44", "R$ 346,08"],
    ["02", "SMED", "RECARGA BROTHER B021", "R$ 45,50", "R$ 91,00"],
    ["02", "SMED", "RECARGA BROTHER TN750", "R$ 49,44", "R$ 98,88"],
    ["03", "SMED", "RECARGA KYOCERA", "R$ 84,00", "R$ 252,00"],
    ["01", "SMED", "RECARGA HP 85", "R$ 58,00", "R$ 58,00"],
    ["01", "STELA DUBOIS", "RECARGA BROTHER 1060", "R$ 45,50", "R$ 45,50"],
    ["01", "STELA DUBOIS", "RECARGA BROTHER 3442", "R$ 49,44", "R$ 49,44"],
    ["11", "ERALDO TINOCO DE MELO", "RECARGA BROTHER B021", "R$ 49,44", "R$ 543,84"],
    ["04", "TERRABRÁS", "RECARGA BROTHER TN750", "R$ 49,90", "R$ 199,60"],
    ["02", "TERRABRÁS", "RECARGA BROTHER 3442", "R$ 49,44", "R$ 98,88"],
    ["02", "TERRABRÁS", "RECARGA BROTHER 420", "R$ 49,44", "R$ 98,88"],
    ["01", "PRESIDENTE CASTELO BRANCO", "RECARGA BROTHER 3442", "R$ 49,44", "R$ 49,44"],
    ["03", "MENANDRO MINAHIM", "RECARGA BROTHER 1060", "R$ 45,50", "R$ 136,50"],
    ["07", "MENANDRO MINAHIM", "RECARGA BROTHER 3442", "R$ 49,44", "R$ 346,08"],
    ["01", "MENANDRO MINAHIM", "RECARGA BROTHER B021", "R$ 45,50", "R$ 45,50"],
    ["03", "MENANDRO MINAHIM", "RECARGA HP 85", "R$ 58,00", "R$ 174,00"],
    ["03", "MENANDRO MINAHIM", "RECARGA BROTHER 3472", "R$ 49,44", "R$ 148,32"],
    ["02", "MENANDRO MINAHIM", "RECARGA BROTHER 750", "R$ 49,44", "R$ 98,88"],
    ["01", "JOAQUIM NERY DE SOUZA", "RECARGA BROTHER 3442", "R$ 49,44", "R$ 49,44"],
    ["02", "JOAQUIM NERY DE SOUZA", "RECARGA HP 105W", "R$ 58,00", "R$ 116,00"],
    ["01", "CET", "RECARGA BROTHER 3442", "R$ 49,44", "R$ 49,44"],
    ["04", "CET", "RECARGA BROTHER B021", "R$ 45,50", "R$ 182,00"],
    ["01", "CET", "RECARGA HP 85A", "R$ 58,00", "R$ 58,00"],
    ["02", "DIANA JUSSIENE", "RECARGA BROTHER 3442", "R$ 49,44", "R$ 98,88"],
    ["02", "DIANA JUSSIENE", "RECARGA BROTHER 5652", "R$ 49,44", "R$ 98,88"],
    ["02", "DIANA JUSSIENE", "RECARGA BROTHER TN750", "R$ 49,44", "R$ 98,88"],
    ["01", "DIANA JUSSIENE", "RECARGA BROTHER 3442", "R$ 49,44", "R$ 49,44"],
    ["02", "EVERALDO SOUZA SANTOS", "RECARGA BROTHER 3442", "R$ 49,44", "R$ 98,88"]
]

# Cabeçalho da tabela
headers = ["QTD", "SETOR", "ITEM", "UNITÁRIO", "TOTAL"]

# Adicionando o cabeçalho aos dados
table_data = [headers] + data

# Criando o arquivo PDF
pdf_file = "tabela_servicos.pdf"
pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

# Estilo da tabela
table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])

# Criando a tabela
table = Table(table_data)
table.setStyle(table_style)

# Build the PDF
elements = [table]
pdf.build(elements)

print(f"PDF gerado com sucesso: {pdf_file}")
