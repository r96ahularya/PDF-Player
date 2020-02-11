## Code to add two or more PDFs to create one a PDF file

from PyPDF2 import PdfFileMerger

pdfs = ['sample.pdf', 'newsample.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()