from zipfile import ZipFile
import os
from datetime import date
from time import time

def kopia_lepsza(sciezka,filtr=lambda name: 'pdf' in name):
  ''''''
#  c=datetime.datetime.now()
#  data=str(c.year)+"-"+str(c.month)+"-"+str(c.day)
  dni=time()-(60*60*24*20)
  data = date.today()
  for c,i in enumerate(sciezka):
        sciezka_kopii=f"D\Backup\cop-{data}\{os.path.basename(i)}.zip"
        with ZipFile(i, 'w') as zip_object:
          for katalog, podkatalogi, pliki in os.walk(i):
                for plik in pliki:
                  sciezkapliku = os.path.join(sciezka, plik)
                  datapliku=os.stat(sciezkapliku).st_mtime
                  if dni<datapliku:
                      if filtr(plik):
                            sciezka_pliku = os.path.join(katalog, plik)
                            zip_object.write(sciezka_kopii)
            
lista=[r"D:\l3\male",""]

kopia_lepsza(lista)

   
   
