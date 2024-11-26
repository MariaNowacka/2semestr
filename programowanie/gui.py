import tkinter as tk
from tkinter import ttk, Tk, Label, Button, Entry, SE, E,W,TOP,CENTER
import requests
import json

s=requests.get('https://api.nbp.pl/api/exchangerates/tables/A?format=json')
s.raise_for_status()

if s.raise_for_status()==None:
    data = s.json()
    with open('waluty.json', 'w') as json_file:
        json.dump(data, json_file)
    json_text=str()    
    with open('waluty.json',"r") as file:
        json_text=file.read()
    data = json.loads(json_text)
else:   
    with open('waluty.json',"r") as file:
        data=file.read()

# otwieramy główne okno aplikacji
root = Tk()
root.title('kalkulator walut')
root.geometry('400x400')
# przygotowujemy etykietę
txt = "KALKULATOR WALUTOWY"
lbl = Label(root, text=txt)
# umieszczamy ją u góry ekranu
lbl.pack(side=TOP)
def quit():
    import sys; sys.exit()
def count():
    pierwsza=wybrana_waluta1.get()
    druga=wybrana_waluta2.get()
    for i in range(34):
        if pierwsza==a['rates'][i]['currency']:
           wart1=a['rates'][i]['mid'] 
        if druga==a['rates'][i]['currency']:
           wart2=a['rates'][i]['mid']
    wynik = ttk.Label(text=str(float(e1.get())*wart1/wart2))
    wynik.pack(padx=5, pady=5, anchor=W)
#przyciski
btn = Button(root, text="Koniec", command=quit)
btn.pack(ipadx=5, ipady=5, anchor=SE)
btn2 = Button(root, text="Oblicz", command=count)
btn2.pack(ipadx=5, ipady=5, anchor=E) 
e1 = Entry(root)
e1.pack(ipadx=5, ipady=5, anchor=W)
#a=dict(data[0])
a=data[0]
a['rates'].append({'currency': 'polski złoty', 'code': 'PLN', 'mid': 1})
label2 = ttk.Label(text="wybierz walutę  początkową")
label2.pack(fill=tk.X, padx=5, pady=5)
wybrana_waluta1 = tk.StringVar()
wybrana_waluta2 = tk.StringVar()
waluty = ttk.Combobox(root, textvariable=wybrana_waluta1)
waluty['values'] = [a['rates'][i]['currency'] for i in range(34)]
# prevent typing a value
#waluty['state'] = 'readonly'
waluty.pack(padx=5, pady=5, anchor=CENTER)
label1 = ttk.Label(text="wybierz walutę docelową")
label1.pack(fill=tk.X, padx=5, pady=5)
waluty2 = ttk.Combobox(root, textvariable=wybrana_waluta2)
waluty2['values'] = [a['rates'][i]['currency'] for i in range(34)]
waluty2.pack(padx=5, pady=5, anchor=CENTER)

#uruchamiamy program
root.mainloop()














