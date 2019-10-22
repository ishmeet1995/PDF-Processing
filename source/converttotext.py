
from PyPDF2 import PdfFileWriter, PdfFileReader
from collections import OrderedDict

def getpages(pdffile):

    dictpages = OrderedDict()
    
    inputpdf = PdfFileReader(open(pdffile,'rb'))
    for i in range(inputpdf.numPages):
        objpdf = PdfFileWriter()
        objpdf.addPage(inputpdf.getPage(i))
        dictpages[objpdf] = ''
    return dictpages


# col  = getpages('sample.pdf')

# for t in col:
#     print(type(t))