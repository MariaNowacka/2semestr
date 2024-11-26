#!pip install PyPDF2 
from PyPDF2 import PdfWriter, PdfReader
import os, math
def split_pdf(plik, pliki,strony):
  '''funkcja rozdzielająca duży plik pdf na kilka mniejszych, 10-stonnicowych
    input : plik (str) - ścieżka do dużego pliku pdf
            pliki (str) - ścieżka do małych plików pdf'''
  reader = PdfReader(plik)
  writer = PdfWriter()
  p=0
  for page in reader.pages:
    p+=1
  ile=math.ceil(p/strony)
#  file, ext = os.path.splitext(plik)
  for i in range(ile):
    reader = PdfReader(plik)
    writer = PdfWriter()
    for j in range(10):
      try:
        writer.add_page(reader.pages[i*strony+j])
      except:
        pass
    with open(pliki+f"strony{i*strony+1}-{i*strony+strony}"+".pdf", "wb") as fp:
      writer.write(fp)

plik=r"E:\l2\AM2_MAT1697_prezentacja_1.pdf"
pliki=r"E:\l2/male-pliki_"
split_pdf(plik, pliki,5)
