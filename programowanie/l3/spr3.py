import os
from time import time 
from datetime import date
from zipfile import ZipFile
 
def lepsza_kopia(sciezka, rozszerzenie,a=3):
        """funkcja tworzy kopię zapasową plików z ostatnich 3 dni o wybranym rozszerzeniu jako plik .zip
              input : sciezka - ścieżka do plików, dla których chcemy stworzyć kopię bezpieczeństwa
                      rozszerzenie - wybrane rozszerzenie plików"""
        kiedy=time()-(60*60*24*a)
        data = date.today()
        kopia="D:\l3\Backup\copy-"+str(data)
        os.makedirs(kopia, exist_ok=True)
 
        pliki = os.listdir(sciezka)
        with ZipFile(kopia+".zip","w") as zip_object:
            for plik in pliki:
                sciezka_pliku = os.path.join(sciezka, plik)
                if os.path.isdir(sciezka_pliku):
                    schowane=os.listdir(sciezka_pliku)
                    #print("tworzę folder", sciezka_pliku)
                    #zip_object.write(sciezka_pliku, os.path.basename(sciezka_pliku))
                    for s in schowane:
                        sciezka_s=os.path.join(sciezka_pliku,s)
                        datapliku=os.stat(sciezka_s).st_mtime
                        if kiedy<datapliku and s.endswith(rozszerzenie):
                            a=os.path.join(zip_object.filename,plik)
                            zip_object.write(os.path.join(a,sciezka_s))
                else:
                    datapliku=os.stat(sciezka_pliku).st_mtime
                    #print(sciezka_pliku, datapliku, sciezka_pliku.endswith(rozszerzenie),kiedy<datapliku)
                    if kiedy<datapliku and sciezka_pliku.endswith(rozszerzenie):
                        zip_object.write(sciezka_pliku,os.path.basename(sciezka_pliku))

                
lepsza_kopia(r"D:\l3\male",".pdf")
