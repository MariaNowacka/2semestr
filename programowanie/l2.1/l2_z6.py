'''program obliczający w słupku zadane działanie matematyczne: dodawanie z odejmowaniem lub mnożenie
input : działanie jakie chcemy wykonać
output : wynik działania wyświetlony w słupku'''


#a=input("wpisz zadanie matematyczne używając + i - lub *")
a=input("wprowadź działanie używając + i - LUB *")
wynik=eval(a)
a1=""
for i in range(0,len(a)):
  if ord(a[i])==43 or ord(a[i])==45 or ord(a[i])==42:
    a1+=(" ")
  else:
    a1+=(a[i])
a1=a1.split()
a3=[]
for i in range(0,len(a1)):
  a3.append(len(a1[i]))
a3.append(len(str(wynik)))
l=max(a3)+3

if "*" in a:
  if "+" in a or "-" in a:
    print("wynik to ",wynik, " ale rozwiązanie jest zbyt skomplikowane, żeby je pokazywać")
  else:
    a=a.split('*')
    print(" "*(l-len(a[0])),a[0])
    print("*"," "*((l-2)-len(a[-1])),a[-1])
    print("-"*(l+1))
    for i in range(len(a[1])):
      b=str(int(a[0])*int(a[1][i-1]))
      if i<len(a[1])-1:
        print(" "*(l-i-len(b)),b)
      else: 
        print("+"," "*(l-2-i-len(b)),b)
    print("-"*(l+1))
    print(" "*(l-len(str(wynik))),wynik)
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
        print(" "*(l-len(a[i])),a[i])
      else:
        for j in range (0,len(a[i])):
          print(" "*(l-len(a[i][j])),a[i][j])
    else:
      if type(a[i])==str:
        print("+"," "*(l-2-len(a[i])),a[i])
      else:
        for j in range (0,len(a[i])-1):
          print(" "*(l-len(a[i][j])),a[i][j])
        print("+"," "*(l-2-len(a[i][-1])),a[i][-1])    
  print((l+1)*"-")
  print(" "*(l-len(str(wynik))),wynik)

