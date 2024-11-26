
from datetime import datetime
from zipfile import ZipFile
import shutil, os

def kopia(sciezka, sciezka_kopii):
  if type(sciezka) == list:
    for i in sciezka:
      if os.path.isfile(i):
        shutil.copyfile(i, sciezka_kopii)
      if os.path.isdir(i):
        shutil.copytree(i, sciezka_kopii)
  else:
    if sciezka.isfile():
        shutil.copyfile(sciezka, sciezka_kopii)
    if sciezka.isdir():
        shutil.copytree(sciezka, sciezka_kopii)
  with ZipFile(sciezka_kopii+".zip", 'w') as zip_object:
    for katalog, podkatalogi, pliki in os.walk(sciezka_kopii):
      for plik in pliki:
         sciezka_pliku = os.path.join(katalog, plik)
         zip_object.write(sciezka_pliku, os.path.basename(str(katalog+data+"okk")))
         
c=datetime.now()
data=str(c.year)+r"/"+str(c.month)+r"/"+str(c.day)

lista=[r"C:\Users\dell\Desktop\marysia\studia\programowanie\zdjecia"]
print(str(lista))
kopia(lista, lista[0]+data)
if os.path.exists(lista[0]+data+".zip"):
   print("ZIP file created")
else:
   print("ZIP file not created")