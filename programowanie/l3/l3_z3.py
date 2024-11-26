from PyPDF2 import PdfWriter, PdfReader, PdfMerger
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

def duzypdf(sciezka):
  """funkcja łączy pliki pdf z podanego katalogu w jeden duży pdf
      input : sciezka - ścieżka dostępu do katalogu"""
  pdfs=[]
  pliki = os.listdir(sciezka)
  for plik in pliki:
    pdfs.append(plik)
    merger = PdfMerger()
    for filename in pdfs:
      p=open(sciezka+"\\"+filename,"rb")
      merger.append(p)
    merger.write("duzy.pdf")
      
duzy="D:\l2\AM2_MAT1697_prezentacja_1.pdf"
male = "D:\l3\male\male_pliki_"
#split_pdf(duzy,male,15)
sciezka=r"E:\l3\male"
duzypdf(sciezka)

