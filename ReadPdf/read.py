
# importing required modules
import PyPDF2
  
# creating a pdf file object
pdfFileObj = open('MV_CV.pdf', 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  
# printing number of pages in pdf file
print(pdfReader.numPages)
  
# creating a page object
pageObj1 = pdfReader.getPage(0)
pageObj2 = pdfReader.getPage(1)
  
# extracting text from page
print(pageObj1.extractText())
print(pageObj2.extractText())
# closing the pdf file object
pdfFileObj.close()
