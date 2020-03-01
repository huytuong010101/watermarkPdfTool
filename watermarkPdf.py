from PyPDF2 import PdfFileWriter, PdfFileReader
import os

def startMark(pathInput, pathOutput, watermark, listPage):
    # Get the watermark file you just created
    watermark = PdfFileReader(open(watermark, "rb"))

    # Get our files ready
    output_file = PdfFileWriter()
    input_file = PdfFileReader(open(pathInput, "rb"))


    # Number of pages in input document
    page_count = input_file.getNumPages()

    # Go through all the input file pages to add a watermark to them
    if len(listPage) == 0:
        listPage = range(page_count)
    for page_number in range(page_count):

        # merge the watermark with the page
        input_page = input_file.getPage(page_number)

        watermark.getPage(0).scaleTo(width=float(input_page.mediaBox[2]), height=float(input_page.mediaBox[3]))
        if page_number in listPage:
            input_page.mergePage(watermark.getPage(0))


        # add page from input file to output document
        output_file.addPage(input_page)

    # finally, write "output" to document-output.pdf
    if pathOutput == "/":
        pathOutput = pathInput[0:-4] + "_.pdf"
    else:
        pathOutput = pathOutput + "/" + pathInput.split("/")[-1]

    with open(pathOutput, "wb") as outputStream:
        output_file.write(outputStream)

