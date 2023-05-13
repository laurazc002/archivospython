from reportlab.pdfgen import canvas
import PyPDF2

#creo el archivo , aca se crea un objeto canvas, que representa el documento pdf
pdf_file = canvas.Canvas('archivo1.pdf')

#se utiliza el método drawString para agregar texto al documento en la posición (100, 750)
pdf_file.drawString(100, 750, 'archivo python')

# se guarda el archivo de PDF utilizando el método save()
pdf_file.save()
# Este código abre el archivo de PDF en modo de lectura binaria ('rb')
pdf_file = open('archivo1.pdf', 'rb')
# crea un objeto PdfFileReader con el archivo
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
# extrayendo el texto de cada página utilizando el
# método extractText() y agregándolo a una cadena de texto.
text = ''
for page_num in range(pdf_reader.getNumPages()):
     page = pdf_reader.getPage(page_num)
     text += page.extractText()

pdf_file.close()

print(text)