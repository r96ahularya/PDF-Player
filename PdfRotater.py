## Code to rotate a complete PDF file
import PyPDF2

file_name = '20200210225306926'
page_to_be_rotated = 1
pdf_in = open(f'{file_name}.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)

    page.rotateClockwise(180)
    pdf_writer.addPage(page)

pdf_out = open(f'{file_name}_rotated.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()