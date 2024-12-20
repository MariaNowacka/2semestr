# -*- coding: utf-8 -*-
"""l1.1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1br6f503TJjbg9VFSDuHnA4rY8Cm4UwBm
"""

import numpy as np
import random
import math

class Vector:
    def __init__(self,arg=3):
      ''' funkcja tworzy obiekt klasy Vector o podanym wymiarze
          input: wymiar wektora (domyślnie 3)'''
      self.v=list(np.zeros(arg))
      self.arg=arg
        
    def __str__(self):
      ''' funkcja print
          output : wektor - lista '''
      return str(self.v)

    def gen (self):
      ''' metoda generuje losowy wektor i przypisuje go do danego obiektu
          output : zmieniony wektor '''
      for i in range (self.arg):
        self.v[i]=random.random()*int(random.choice([1,10,100]))
      return self.v
    
    def wczyt (self,lista):
      ''' funkcja wczytująca podaną listę jako nowy wektor
          input : lista, która ma być wektorem
          output : zmieniony wektor '''
      if len(lista)!=self.arg:
        raise ValueError('nieodpowiednia długość listy')
      else:
        self.v=lista
        return self.v

    def __add__(self,other):
      ''' funkcja specjalna dodawanie, uruchamiana przy pomocy symbolu +
          input : wektor który chcemy dodać do wektora 'self'
          output : wektor 'self' po dodaniu drugiego wektora (suma wektorów) '''
      if other.arg!=self.arg:
        raise ValueError('nieodpowiednia długość wektorów')
      else:
        for i in range(len(self.v)):
          self.v[i]+=other.v[i]
      return self.v

    def __sub__(self,other):
      ''' funkcja specjalna odejmowanie, uruchamiana przy pomocy symbolu -
          input : wektor który chcemy odjąć od wektora 'self'
          output : wektor 'self' po zmianie -  różnica wektorów '''
      if other.arg!=self.arg:
        raise ValueError('nieodpowiednia długość wektorów')
      else:
        for i in range(len(self.v)):
          self.v[i]=self.v[i]-other.v[i]
        return self.v      
    
    def __mul__(self,x):
      ''' metoda obliczająca wektor skalarny lub, zależnie odtypu zmiennej,
          wynik mnożenia wektora przez skalar, przy użyciu symbolu *
          input : wektor lub skalar, przez który chcemy przemnżyć wektor 'self' '''
      if x.arg!=self.arg:
        raise ValueError('nieodpowiednia długość wektorów')
      else:
        if type(self)==type(x):
          for i in range(len(self.v)):
            self.v[i]=self.v[i]*(x.v[i])
          return sum(self.v)
        else:
          for i in range(len(self.v)):
           self.v[i]=self.v[i]*x
          return self.v

#    def __len__(self):
#      return self.arg

    def __contains__(self,x):
      ''' operator in, sprawdzający, czy podany element znajduje się w wektorze
          input : element, który sprawdzamy (liczba, float)
          output : wartość bool, która mówi czy dany element przynależy (true),
          lub nie przynależy (false) do wektora '''
      return x in self.v

    def dl(self):
      ''' funkcja obliczająca długość wektora
          output : długość wektora (float) '''
      k=[]
      for i in range (self.arg):
        k.append(self.v[i]**2)
      print(k)
      d=math.sqrt(sum(k))
      return d

    def suma(self):
      ''' funkcja zwraca sumę elementów wektora
          output : suma elementów, float '''
      return sum(self.v)

    def __getitem__(self,x):
      ''' funkcja wprowadzjąca operator [], dzięki któremu uzyskujemy dostęp
          do konkretnych elementów wektora
          input : pozycja (indeks, int), do której chcemy uzyskać dostęp
          output : element wektora znajdujący się w podanej komórce '''
      return self.v[x] 
    

v1=Vector()
v2=Vector()
v3=Vector(2)
print('v1 ',v1)
v1.wczyt(v1.gen())
print('v1 ',v1)
v2.wczyt(v2.gen())
print('v2 ',v2)
print('suma ',v1+v2)
print('rozn ',v1-v2)
print('v*5 ',v1*5)
v3.wczyt([1,2])
print('v3 ',v3)
print(2 in v3)
print('v1 : ',v1)
print('dlugosc: ',v1.dl())
print('mnoz ',v1*v2)
print(v1)
print(v1[1])

"""https://www.tutorialsteacher.com/python/magic-methods-in-python 
https://www.geeksforgeeks.org/python-__add__-magic-method/
https://tomaszgolan.github.io/js-python/wyklady/js-python_w10/
http://prac.im.pwr.wroc.pl/~szwabin/assets/prog/lec/4.pdf

http://prac.im.pwr.wroc.pl/~szwabin/assets/prog/lec/4.pdf
"""

