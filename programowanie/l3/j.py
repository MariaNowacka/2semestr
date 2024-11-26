import os
from time import time 
from datetime import date
from zipfile import ZipFile
import shutil
 
def lepsza_kopia(sciezka, rozszerzenie=".pdf",a=3):
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
        with ZipFile(kopia+".zip","w") as zip_object:
            for plik in pliki:
                print(plik)
                sciezka_pliku = os.path.join(sciezka, plik)
                datapliku=os.stat(sciezka_pliku).st_mtime
                if kiedy<datapliku and plik.endswith(rozszerzenie) and os.path.isfile(sciezka_pliku):
                        zip_object.write(sciezka_pliku,plik)
                elif os.path.isdir(sciezka_pliku):
                    print(sciezka_pliku, " is a directory")
                    schowane=os.listdir(sciezka_pliku)
                    print("schowane", schowane)
                    for i in schowane:
                        sciezka_i=os.path.join(sciezka_pliku,i)
                        print("i: ",sciezka_i)
                        datapliku=os.stat(sciezka_i).st_mtime
                        if kiedy<datapliku and sciezka_i.endswith(rozszerzenie):
                            os.makedirs(sciezka+"kopia", exist_ok=True)
                            print("making a new directory", sciezka+"kopia")
                            print("ok")
                            kop=os.path.join(sciezka+"kopia",i)
                            shutil.copyfile(sciezka_i, kop)
                    zip_object.write(sciezka+"kopia",compresslevel=1)
                    
lepsza_kopia(r"D:\l3\male")
                                    

                
lepsza_kopia(r"D:\l3\male",".pdf")
