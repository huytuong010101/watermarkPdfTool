from pdf2image import convert_from_path

def pdf2png(path,saveTo):
    images = convert_from_path(path)
    images[0].save(saveTo + 'pdfModel.png', 'PNG')