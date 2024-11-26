import requests, webbrowser
from bs4 import BeautifulSoup
def los_art(a=7):
  """funkcja losuje artykuły z wikipedii i wyświetla (wybrane) w przeglądarce
      input : a maksymalna ilość prób"""
  for i in range (a):
    s=requests.get('https://en.wikipedia.org/wiki/Special:Random')
    #s.encoding='utf-8'
    soup=BeautifulSoup(s.text,"html.parser")
    print(soup.title.string)
    o=input("czy chcesz przeczytać ten artykuł? [t/n]")
    if o == "t":
      webbrowser.open_new(s)
      o2=input("czy chcesz losować dalej? [t/n]")
      if o2=='n':
        break
    elif o == 'n':
      pass
     
los_art()
