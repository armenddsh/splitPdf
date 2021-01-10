from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import os

outPutDir = "output"
if not os.path.exists(outPutDir):
    os.mkdir(outPutDir)

if __name__ == "__main__":

    if len(sys.argv) > 1:

        pdfName = sys.argv[1]
        pdfNameOnly, ext = os.path.splitext(pdfName)
        
        if os.path.exists(pdfName):

            inputpdf = PdfFileReader(open(pdfName, "rb"))

            outputPdf = f"{outPutDir}/{pdfNameOnly}"
            if not os.path.exists(outputPdf):
                os.mkdir(outputPdf)

            for i in range(inputpdf.numPages):
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i))
                with open(f"{outputPdf}/{pdfNameOnly}-page-%s.pdf" % i, "wb") as outputStream:
                    output.write(outputStream)
            else:
                print("Done.")
        else:
            raise Exception("File does not exists!")