
def znak(plik, rodzaj):
  """funkcja zmienia znaki końca linii z windowsowych na uniksowe (lub odwrotnie)
    input : plik - plik .txt, w którym chcemy zmienić znak końca linii
            rodzaj - rodzaj znaku nowej linii na jaki chcemy zmienić : w dla windowsa i u dla unixa"""
  if rodzaj.lower()=="w":
    zn="\r\n"
  if rodzaj.lower()=="u":
    zn="\n" 
  x=open(plik,"r").read()
  bylo=open(plik,"rb").read()
  f=open(plik, "w", newline=zn)
  f.write(x)
  f.close()
  jest=open(plik, "rb").read()
  print(bylo, "\n->\n",jest)

znak("plik.txt","u")
