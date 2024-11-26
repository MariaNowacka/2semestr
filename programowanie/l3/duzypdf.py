'''from PyPDF2 import PdfWriter, PdfReader
import os, math
def split_pdf(duzy, pliki,strony):
  reader = PdfReader(duzy)
  writer = PdfWriter()
  p=0
  for page in reader.pages:
    p+=1
  ile=math.ceil(p/strony)
  for i in range(ile):
    reader = PdfReader(duzy)
    writer = PdfWriter()
    for j in range(10):
      try:
        writer.add_page(reader.pages[i*strony+j])
      except:
        pass
    with open(pliki+f"strony{i*strony+1}-{i*strony+strony}"+".pdf", "wb") as fp:
      writer.write(fp)
'''
import os
#from PyPDF2 import PdfMerger, PdfFileReader
#sciezka="E:\l2\AM2_MAT1697_prezentacja_1.pdf"
sciezka=r"E:\l2\male"
pdfs=[]
pliki = os.listdir(sciezka)
for plik in pliki:
    pdfs.append(plik)
'''
merger = PdfMerger()
for filename in pdfs:
    merger.append(filename)
 
merger.write("duzy.pdf")
''' 
print(pdfs)