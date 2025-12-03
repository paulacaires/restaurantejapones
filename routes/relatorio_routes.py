import os
from flask import Blueprint, send_file
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from io import BytesIO
from reportlab.lib.utils import ImageReader

# Para fontes diferentes
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("Asimovian", "static/Asimovian-Regular.ttf"))

relatorio_bp = Blueprint("relatorio", __name__)

# Função para desenhar cabeçalho
def draw_header(pdf):
    width, height = A4

    logo_path = "static/images/logo_sem_fundo.png"

    # Carregar imagem
    logo = ImageReader(logo_path)

    original_w, original_h = logo.getSize()

    scale = 0.08
    logo_width = original_w * scale
    logo_height = original_h * scale

    # Inserir logo no canto superior esquerdo
    logo_x = 40
    logo_y = height - 85

    pdf.drawImage(
        logo,
        x=logo_x,
        y=logo_y,
        width=logo_width,
        height=logo_height,
        mask='auto'
    )
    
    # DESLOCAR o título para depois do logo
    titulo_x = logo_x + logo_width + 25 
    titulo_y = logo_y + 20

    pdf.setFont("Asimovian", 18)
    pdf.setFillColor(HexColor("#b52e35"))
    pdf.drawString(titulo_x, titulo_y, "Relatório Restaurante Japonês da UFSCar")
    
    # Linha abaixo do cabeçalho
    pdf.setStrokeColor(HexColor("#3f395b"))
    pdf.setLineWidth(2)
    pdf.line(0, logo_y, width, logo_y)


@relatorio_bp.route("/gerar-pdf", methods=["GET"])
def gerar_pdf():
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Cabeçalho da página
    draw_header(pdf)

    # Relatório financeiro
    y = height - 120

    # Cardápios
   
    # 🔹 Conteúdo de exemplo
   
    # 🔹 Finaliza e salva
    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=False,
        download_name="relatorio.pdf",
        mimetype="application/pdf"
    )
