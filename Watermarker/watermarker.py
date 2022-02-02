import os
import sys
import PyPDF2

pdf_to_wmark = sys.argv[1]
wtrmrk = sys.argv[2]

wmarkobject = PyPDF2.PdfFileReader(pdf_to_wmark)
no_of_pages = wmarkobject.getNumPages()
wtr = PyPDF2.PdfFileReader(wtrmrk)
wtrpag = wtr.getPage(0)
wmarked = PyPDF2.PdfFileWriter()
for i in range(no_of_pages):
    page = wmarkobject.getPage(i)
    page.mergePage(wtrpag)


with open("watermarked.pdf", "wb") as k:
    wmarked.write(k)
