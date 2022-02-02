import PyPDF2
import sys

i = 1
pdflist = []
while True:
    try:
        while True:
            pdflist.append(sys.argv[i])
            i += 1
    except IndexError:
        break


def pdf_merger(pdflist):
    mergedpdf = PyPDF2.PdfFileWriter()
    for pdf in pdflist:
        pdfobject = PyPDF2.PdfFileReader(f"{pdf}", "rb")
        for pagenumber in range(pdfobject.getNumPages()):
            page = pdfobject.getPage(pagenumber)
            mergedpdf.addPage(page)

    with open("mergedpdf.pdf", 'wb') as outputpdf:
        mergedpdf.write(outputpdf)


pdf_merger(pdflist)
# i spent 30 minutes making this and realised there is an inbuilt module for it


def pdf_merger2(pdf_list):
    mergedpdf = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        mergedpdf.append(pdf)
    mergedpdf.write("mergedpdf2.pdf")


pdf_merger2(pdflist)
