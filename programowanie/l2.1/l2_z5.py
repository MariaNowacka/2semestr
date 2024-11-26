from PIL import Image 
from PIL import ImageEnhance

tlo = Image.open(r"C:\Users\dell\Desktop\marysia\studia\programowanie\l2\1679605846690.jpg")
#tlo.show()
znak=Image.open(r"C:\Users\dell\Desktop\marysia\studia\programowanie\l2\1679605822857_miniatura.jpg")
#znak.show()
def znak_wodny(tlo, znak):
    '''funkcja dodaje znak wodny do zdjęcia
        input : tlo - ścieżka do pliku, do którego chcemy dodać znak wodny
                znak - ścieżka zo zdjęcia, które jest znakiem wodnym'''
    znak = znak.convert("RGBA")
    tlo = tlo.convert("RGBA")
    a=70
    nowe=[]
    dane = znak.getdata()
    for i in dane:
        nowe.append((i[0], i[1], i[2], a))
    znak.putdata(nowe)
    znak.save(r"C:\Users\dell\Desktop\marysia\studia\programowanie\l2\przezroczyte.png", "PNG")
    szer = (tlo.width - znak.width) // 2
    wys = (tlo.height - znak.height) // 2
    tlo.paste(znak, (szer, wys), znak)
    tlo.save(r"C:\Users\dell\Desktop\marysia\studia\programowanie\l2\nowy.png", format="png")
    tlo.show()
znak_wodny(tlo, znak)