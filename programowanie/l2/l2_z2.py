# -*- coding: utf-8 -*-
"""l2.z2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lU_g9Ic0OzqS_9IOMS6zZSEJu7LsTN3c
"""

from PIL import Image
import os
def min(sciezkapliku, sciezka_min):
  rozm=160,90
  file, ext = os.path.splitext(sciezkapliku)
  with Image.open(sciezkapliku) as im:
    im.thumbnail(rozm)
    im.save(sciezka_min)
  
min(r"D:\programowanie\l2\1679605822857.jpg", r"D:\programowanie\l2\1679605822857miniatura.jpg")
#C:\Users\dell\Desktop\marysia\studia\programowanie\1679605846690.jpg
#D:\programowanie\l2\1679605822857.jpg
