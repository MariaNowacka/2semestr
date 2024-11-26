from PIL import Image
import os
def min(sciezkapliku, sciezka_min, rozm=(160,90)):
  '''funkcja tworząca miniaturę zdjęcia
    input : sciezkapliku (sts) - ścieżka do pliku, którego miniaturę chcemy stworzyć
            sciezka_min (str) - ścieżka do miniatury
            rozm (int,int) - maksymalne wymiary miniatury (program zachowuje proporcje zdjęcia), 
            domyślnie 160x90'''
  file, ext = os.path.splitext(sciezkapliku)
  with Image.open(sciezkapliku) as im:
    im.thumbnail(rozm)
    im.save(sciezka_min)
  
min(r"C:\Users\dell\Desktop\marysia\studia\programowanie\l2\1679605846690.jpg", r"C:\Users\dell\Desktop\marysia\studia\programowanie\l2\1679605846690miniatura.jpg")
#C:\Users\dell\Desktop\marysia\studia\programowanie\1679605846690.jpg
