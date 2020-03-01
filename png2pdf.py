from reportlab.pdfgen import canvas

def png2pdf(path,saveTo):
    c = canvas.Canvas(saveTo)
    c.drawImage(path, 0, 0, 595,849,mask="auto")
    c.save()