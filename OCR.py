#pip install PyPDF2
import os

import PyPDF2

def pdfReader():

    pdfFullName=""
    for x in os.listdir(os.getcwd() + "\\PDF\\"):
        pdfFullName = os.getcwd() + "\\PDF\\" + x
    # pdfFullName = "./PDF/" + pdfFullName
    # pdffileobj = open(pdfFullName, 'rb')

    # create reader variable that will read the pdffileobj
    pdfreader = PyPDF2.PdfFileReader(pdfFullName)

    if pdfreader.isEncrypted:
        pdfreader.decrypt('')

    x = pdfreader.numPages
    print(x)

    pdftext = ""
    for i in range(x):
        pageobj = pdfreader.getPage(i)

        pdftext += "Page " + str(i+1) + " "
        # create text variable which will store all text datafrom pdf file
        pdftext += pageobj.extractText()

    pdftext = pdftext.strip()
    pdftext = pdftext.lstrip()
    pdftext = pdftext.rstrip()
    pdftext = pdftext.replace('\n','').replace('\r','').replace('\t', '')

    text_file = open("interimtextdata.txt", "w")
    text_file.write(pdftext)
    text_file.close()

    return pdftext

# pdfReader()