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
        robizip=[]
        print(pliki)
    
        #print(pliki)
        for plik in pliki:
            sciezka_pliku = os.path.join(sciezka, plik)
            print(sciezka_pliku)
            if os.path.isdir(sciezka_pliku):
                #print(plik, "to folder")
                schowane=os.listdir(sciezka_pliku)
  #              os.makedirs(kopia, exist_ok=True)
                for s in schowane:
                    sciezka_s=os.path.join(sciezka_pliku,s)
                    print(sciezka_s)
                    robizip.append(sciezka_s)
            else:
                robizip.append(sciezka_pliku)
        print(robizip)
        for p in robizip:
            nazwa=str(p).split("\\")
            n=nazwa[-1]            
            with ZipFile(kopia+".zip","w") as zip_object:
                datapliku=os.stat(p).st_mtime
                print(p, datapliku, p.endswith(rozszerzenie),kiedy<datapliku)
                if kiedy<datapliku and p.endswith(rozszerzenie):
                #sciezkakopii = os.path.join(katalog, plik)
                    print("dodaję ",n)
                    zip_object.write(p)
                #print(plik, "nie jest folderem")
lepsza_kopia(r"D:\l3\male",".pdf")
