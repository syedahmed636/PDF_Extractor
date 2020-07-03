import PyPDF2
object = open('The_Living_World.pdf','rb')
reader = PyPDF2.PdfFileReader(object)
print(reader.numPages)
for i in range(reader.numPages):
    page = reader.getPage(i)
    print(page.extractText())