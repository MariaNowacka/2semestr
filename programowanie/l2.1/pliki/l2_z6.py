# -*- coding: utf-8 -*-
"""l2.z6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nji-lxW2YTfCaWKvM5XhqS11lqPLS0P9
"""

#a=input("wpisz zadanie matematyczne używając + i - lub *")
a=input("wprowadź działanie używając + i - LUB *")
wynik=eval(a)
print(wynik)
if "*" in a:
  if "+" in a or "-" in a:
    print("wynik to : ",wynik, " rozwiązanie jest zbyt skomplikowane, żeby je pokazywać")
  else:
    a=a.split('*')
    print(" "*(10-len(a[0])),a[0])
    print("*"," "*(8-len(a[-1])),a[-1])
    print("-"*11)
    for i in range(len(a[1])):
      b=str(int(a[0])*int(a[1][i-1]))
      if i<len(a[1])-1:
        print(" "*(10-i-len(b)),b)
      else: 
        print("+"," "*(8-i-len(b)),b)
    print("-"*11)
    print(" "*(10-len(str(wynik))),wynik)
else:
  a=a.split("+")
  for i in range(0,len(a)):
    if "-" in a[i]:
      a[i]=a[i].split("-")
      for k in range(1,len(a[i])):
        a[i][k]="-"+a[i][k]
  for i in range(0,len(a)):
    if i<len(a)-1:
      if type(a[i])==str:
        print(" "*(10-len(a[i])),a[i])
      else:
        for j in range (0,len(a[i])):
          print(" "*(10-len(a[i][j])),a[i][j])
    else:
      if type(a[i])==str:
        print("+"," "*(8-len(a[i])),a[i])
      else:
        for j in range (0,len(a[i])-1):
          print(" "*(10-len(a[i][j])),a[i][j])
        print("+"," "*(8-len(a[i][j])),a[i][j])    
  print(11*"-")
  print(" "*(10-len(str(wynik))),wynik)
