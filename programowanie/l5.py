#import tkinter as tk
from tkinter import ttk, Tk, Label, Button, Entry, SE, E,W,TOP, Listbox
#import requests


#s=requests.get('https://api.nbp.pl/api/exchangerates/tables/A?format=json')



# otwieramy główne okno aplikacji
root = Tk()
root.title('kalkulator walut')
root.geometry('700x500')
# przygotowujemy etykietę
txt = "KALKULATOR WALUTOWY"
lbl = Label(root, text=txt)
# umieszczamy ją u dołu ekranu
lbl.pack(side=TOP)
def quit():
    import sys; sys.exit()
def count():
    #liczy
    return "hola, soy dora"
#przyciski
btn = Button(root, text="Koniec", command=quit)
# slownik = 
lista=Listbox()
btn.pack(ipadx=10, ipady=10, anchor=SE)
btn2 = Button(root, text="Oblicz", command=count)
btn2.pack(ipadx=10, ipady=10, anchor=E) 
e1 = Entry(root)
e1.pack(ipadx=10, ipady=10, anchor=W)
lista=ttk.Combobox()




#uruchamiamy program
root.mainloop()



















