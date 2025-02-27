from fpdf import FPDF
import tempfile
import os

def gerar_relatorio_pdf(df, titulo):
    try:
        # Validar colunas necessárias no DataFrame
        colunas_necessarias = {"Setor", "Servico", "Data","Quantidade"}
        if not colunas_necessarias.issubset(df.columns):
            raise ValueError(f"Colunas faltando no DataFrame. Necessárias: {colunas_necessarias}, encontradas: {df.columns.tolist()}")

        # Criar PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, titulo, ln=True, align='C')
        pdf.ln(10)

        # Cabeçalhos
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(60, 10, "Setor", border=1)
        pdf.cell(60, 10, "Serviço", border=1)
        pdf.cell(40, 10, "Data", border=1)
        pdf.cell(40, 10, "Quantidade", border=1)
        pdf.ln()

        # Função para ajustar textos longos
        def ajustar_texto(texto, limite):
            return texto if len(texto) <= limite else texto[:limite-4] + "..."

        # Adicionar dados ao PDF
        pdf.set_font("Arial", '', 12)
        for _, row in df.iterrows():
            pdf.cell(60, 10, ajustar_texto(row["Setor"], 30), border=1)
            pdf.cell(60, 10, ajustar_texto(row["Servico"], 30), border=1)
            pdf.cell(40, 10, str(row["Data"]), border=1)
            pdf.cell(40, 10, str(row["Quantidade"]), border=1)
            pdf.ln()

        # Salvar o arquivo temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            pdf.output(tmp_file.name)
            if not os.path.exists(tmp_file.name):
                raise FileNotFoundError("O arquivo PDF não foi gerado corretamente.")
            return tmp_file.name
    except Exception as e:
        # Gerar mensagem de erro detalhada
        raise RuntimeError(f"Erro ao gerar o relatório em PDF: {e}")
