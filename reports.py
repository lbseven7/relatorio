from fpdf import FPDF
import tempfile

def gerar_relatorio_pdf(df, titulo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, titulo, ln=True, align='C')
    pdf.ln(10)

    # Cabeçalhos
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(60, 10, "Setor", border=1)
    pdf.cell(60, 10, "Serviço", border=1)
    pdf.cell(40, 10, "Total", border=1)
    pdf.ln()

    # Dados
    pdf.set_font("Arial", '', 12)
    for index, row in df.iterrows():
        pdf.cell(60, 10, row["Setor"], border=1)
        pdf.cell(60, 10, row["Servico"], border=1)
        pdf.cell(40, 10, str(row["Quantidade"]), border=1)
        pdf.ln()

    # Salvar arquivo temporário
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf.output(tmp_file.name)
        return tmp_file.name
