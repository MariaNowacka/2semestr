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
        for plik in pliki:
                with ZipFile(kopia+".zip", 'w') as zip_object:
                        if os.path.isdir(plik):
                                for katalog, podkatalogi, pliki in os.walk(plik):
                                        for plik1 in pliki:
                                                sciezkapliku = os.path.join(sciezka, plik)
                                        datapliku=os.stat(sciezkapliku).st_mtime
                                        print(plik, datapliku, sciezkapliku.endswith(rozszerzenie),kiedy<datapliku)
                                        if kiedy<datapliku and sciezkapliku.endswith(rozszerzenie):
                                                sciezkakopii = os.path.join(katalog, plik)
                                                print("dodaję ",sciezkakopii)
                                                zip_object.write(sciezkakopii, plik)
                        for katalog, podkatalogi, pliki in os.walk(sciezka):
                                for plik in pliki:
                                        sciezkapliku = os.path.join(sciezka, plik)
                                        datapliku=os.stat(sciezkapliku).st_mtime
                                        print(plik, datapliku, sciezkapliku.endswith(rozszerzenie),kiedy<datapliku)
                                        if kiedy<datapliku and sciezkapliku.endswith(rozszerzenie):
                                                sciezkakopii = os.path.join(katalog, plik)
                                                print("dodaję ",sciezkakopii)
                                                zip_object.write(sciezkakopii, plik)

lepsza_kopia(r"D:\l3\male",".pdf")
