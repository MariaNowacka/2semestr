# -*- coding: utf-8 -*-
"""nawiasy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FMKForF-WOJwyKI5AfKx-AZE8FJK4Jf4
"""

znaki = "<>{}[]() "
p="<{[("
k=">}])"
a = "()r{[]}"
c=0
for i in a:
    if i in znaki:
        c+=1

if c%2 != 0:
    print ("nieodpowiednia ilość nawiasow")
else:
    for j, i in enumerate(a):
        if i in znaki:
            if (i in p) and (k[p.index(i)] not in a) or (i in k) and (p[k.index(i)] not in a):
                    print ("jakiś nawias jest zamknięty ale nie otwarty (albo na odwrót)")
            else:
                if p.
#zamyka się zanim się otworzy
#zła kolejność zamykania nawiasów
#
'''
znaki.index(")")
znaki[znaki.index(")")]
'''

#list.index(value,start,end)

"""https://newsblog.pl/jak-znalezc-indeks-elementu-na-listach-pythona/#Znajdz_indeks_elementu_listy_za_pomoca_metody_index"""