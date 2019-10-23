from PyPDF2 import PdfFileWriter, PdfFileReader
from collections import OrderedDict


def getpages(pdffile):
    dictpages = OrderedDict()
    inputpdf = PdfFileReader(open(pdffile, 'rb'))

    for pgnumber, page in enumerate(inputpdf.pages):
        dictpages[pgnumber] = page.extractText()
    return dictpages

