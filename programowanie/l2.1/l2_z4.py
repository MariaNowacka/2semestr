#!pip install PyPDF2 
from PyPDF2 import PdfWriter, PdfReader
import os, math
def split_pdf(plik, pliki):
  '''funkcja rozdzielająca duży plik pdf na kilka mniejszych, 10-stonnicowych
    input : plik (str) - ścieżka do dużego pliku pdf
            pliki (str) - ścieżka do małych plików pdf'''
  reader = PdfReader(plik)
  writer = PdfWriter()
  p=0
  for page in reader.pages:
    p+=1
    print(p)
  ile=math.ceil(p/10)
#  file, ext = os.path.splitext(plik)
  for i in range(ile):
    reader = PdfReader(plik)
    writer = PdfWriter()
    for j in range(10):
      try:
        writer.add_page(reader.pages[i*10+j])
      except:
        pass
    with open(pliki+f"cz{i+1}"+".pdf", "wb") as fp:
      writer.write(fp)

plik=r"C:/Users/dell/Desktop/marysia/studia/programowanie/l2/AM2_MAT1697_prezentacja_1.pdf"
pliki=r"C:/Users/dell/Desktop/marysia/studia/programowanie/male-pliki_"
split_pdf(plik, pliki)
