import os
from time import time 
from datetime import date
from zipfile import ZipFile
 
def lepsza_kopia(sciezka, rozszerzenie,a=3):
        """funkcja tworzy kopię zapasową plików z ostatnich 3 dni o wybranym rozszerzeniu jako plik .zip
              input : sciezka - ścieżka do plików, dla których chcemy stworzyć kopię bezpieczeństwa
                      rozszerzenie - wybrane rozszerzenie plików"""
        dni=time()-(60*60*24*a)
        data = date.today()
        kopia="D:\l3\Backup\copy-"+str(data)
        os.makedirs(kopia, exist_ok=True)
 
        pliki = os.listdir(sciezka)
        for plik in pliki:
            sciezkapliku = os.path.join(sciezka, plik)
            datapliku=os.stat(sciezkapliku).st_mtime
            
            with ZipFile(kopia+".zip", 'w') as zip_object:
 
                for katalog, podkatalogi, pliki2 in os.walk(sciezka):
                    for plik in pliki2:
                        if dni<datapliku and sciezkapliku.endswith(rozszerzenie):
                            sciezkakopii = os.path.join(katalog, plik)
                            print("dodaję ", plik)
                            zip_object.write(sciezkakopii, plik)
                            

lepsza_kopia(r"D:\l3\male",".pdf")
print("done")
