from flask import Blueprint, send_file, make_response
from reportlab.pdfgen import canvas
from io import BytesIO

relatorio_bp = Blueprint("relatorio", __name__)

@relatorio_bp.route("/gerar-pdf", methods=["GET"])
def gerar_pdf():
    # Create in-memory PDF
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    
    # Example content
    pdf.setFont("Helvetica", 14)
    pdf.drawString(100, 800, "Relatório de Reservas")
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 770, "Esse é um exemplo de relatório gerado usando Flask + ReportLab.")

    # TODO: plug your database queries here
    # items = db.session.query(...)

    pdf.showPage()
    pdf.save()

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="relatorio.pdf",
        mimetype="application/pdf"
    )
