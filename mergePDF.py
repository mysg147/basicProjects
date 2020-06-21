import PyPDF2

print("Enter file names you want to merge:-")
l1=[a for a in input().split()]
pdfReader1=[]

for i in l1:
    file1=open(i,'rb')
    pdfreader=PyPDF2.PdfFileReader(file1)
    pdfReader1.append(pdfreader)

pdfWriter=PyPDF2.PdfFileWriter()


for i in pdfReader1:
    for j in range(i.numPages):
        pageObj=i.getPage(j)
        pdfWriter.addPage(pageObj)
        

newpdf=input("Name of new file you merge please enter :- ")
pdfoutputFile=open(newpdf,'wb')
pdfWriter.write(pdfoutputFile)

pdfoutputFile.close()
pdfReader1.clear()
