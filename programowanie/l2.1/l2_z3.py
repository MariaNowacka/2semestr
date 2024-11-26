from datetime import datetime
from zipfile import ZipFile
import shutil, os

def kopia(sciezka, sciezka_kopii):
  '''funkcja tworzy kopię zapasową plików/foderów jako plik .zip
      input : ścieżka do plików, dla których chcemy stworzyć kopię bezpieczeństwa
              ścieżka, gdzie chcemy zapisać kopię''' 
  if type(sciezka) == list:
    for c,i in enumerate(sciezka):
      sciezka_kopii=sciezka[c]+data
      if os.path.isfile(i):
        shutil.copyfile(i, sciezka_kopii)
      if os.path.isdir(i):
        shutil.copytree(i, sciezka_kopii)
      with ZipFile(sciezka_kopii+".zip", 'w') as zip_object:
        for katalog, podkatalogi, pliki in os.walk(sciezka_kopii):
          for plik in pliki:
            sciezka_pliku = os.path.join(katalog, plik)
            zip_object.write(sciezka_pliku, os.path.basename(str(katalog+data)))
        
      
c=datetime.now()
data=str(c.year)+"-"+str(c.month)+"-"+str(c.day)
lista=[r"C:\Users\dell\Desktop\marysia\studia\programowanie\l2\zdjecia",r"C:\Users\dell\Desktop\marysia\studia\programowanie\l2\pliki"]



kopia(lista, data)
for c in range(len(lista)):
  if os.path.exists(lista[c]+data+".zip"):
    print("ZIP file created")
  else:
    print("ZIP file not created")
   
   
'''    
  else:
    if sciezka.isfile():
        shutil.copyfile(sciezka, sciezka_kopii)
    if sciezka.isdir():
        shutil.copytree(sciezka, sciezka_kopii)
'''