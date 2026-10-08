from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from io import BytesIO

def create_letter_pdf(letter_text: str) -> BytesIO:
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        rightMargin=0.8*inch, leftMargin=0.8*inch,
        topMargin=0.8*inch, bottomMargin=0.8*inch
    )
    styles = getSampleStyleSheet()
    body_style = ParagraphStyle(
        'Body', parent=styles['Normal'],
        fontSize=11, leading=16, spaceAfter=8
    )
    story = []
    for line in letter_text.split("\n"):
        if line.strip():
            safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            story.append(Paragraph(safe, body_style))
        else:
            story.append(Spacer(1, 8))
    doc.build(story)
    buffer.seek(0)
    return buffer