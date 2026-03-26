import os
import uuid
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_gap_pdf(gaps):
    filename = f"data/pdfs/{uuid.uuid4()}.pdf"

    os.makedirs("data/pdfs", exist_ok=True)

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Research Gap Analysis", styles['Title']))
    elements.append(Spacer(1, 12))

    for paper in gaps:
        elements.append(Paragraph(paper["title"], styles['Heading2']))
        elements.append(Paragraph(paper["gap"], styles['BodyText']))
        elements.append(Spacer(1, 12))

    doc.build(elements)
    return filename