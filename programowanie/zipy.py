from zipfile import ZipFile
import os,datetime

def kopia_lepsza(sciezka,filtr=lambda name: 'pdf' in name):
  '''funkcja tworzy kopię zapasową plików/foderów jako plik .zip
      input : ścieżka do plików, dla których chcemy stworzyć kopię bezpieczeństwa
              ścieżka, gdzie chcemy zapisać kopię'''
  c=datetime.datetime.now()
  data=str(c.year)+"-"+str(c.month)+"-"+str(c.day)
  for c,i in enumerate(sciezka):
        sciezka_kopii=f"{os.path.basename(i)}_{data}.zip"
        with ZipFile(i, 'w') as zip_object:
          for katalog, podkatalogi, pliki in os.walk(i):
                for plik in pliki:
                      if filtr(plik):
                            sciezka_pliku = os.path.join(katalog, plik)
                            zip_object.write(sciezka_kopii)
        
      
c=datetime.datetime.now()
data=str(c.year)+"-"+str(c.month)+"-"+str(c.day)
lista=[r"E:\l2\zdjecia"]

kopia_lepsza(lista)
for c in range(len(lista)):
  if os.path.exists(lista[c]+data+".zip"):
    print("ZIP file created")
  else:
    print("ZIP file not created")
   
   
