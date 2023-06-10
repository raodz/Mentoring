# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:02:29 2023

@author: rav
"""

#%% Zadanie 1

liczba_gwiazdek = [1, 2, 3, 4, 5, 4, 3, 2, 1]
for e in liczba_gwiazdek:
    print(e * '*')
    
#%% Zadanie 2

wyraz = input('Wprowadź wyraz')
if wyraz.lower() == wyraz[::-1].lower():
    print('Wyraz '+wyraz+' jest palindromem')
else:
    print('Wyraz '+wyraz+' nie jest palindromem')

#%% Zadanie 3

imiona = ['Adam', 'Stanisław', 'Joanna', 'Kornelia', 'Kacper']

for i in range(0, 4):
    for j in range(i + 1, 4):
        print(imiona[i] + ' - ' + imiona[j])

for i, j in zip(range(0, 4), range(4, 0)):
    pass

        
#%% Zadanie 4

for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            for l in range(0, 10):
                print(1000*i+100*j+10*k+l)

#%% Zadanie 5

zamowienia = {"Klient_1335" : {"nazwa_potrawy" : "rosół", "ocena" : 5, "rachunek" : 20.0}, "Klient_222" : {"nazwa_deseru" : "lody waniliowe", "rachunek" : 5.0 }}

for e in zamowienia:
    print(e + ':')
    for f in zamowienia[e]:
        print(f + ':' + str(zamowienia[e][f]))

#%% Zadanie 6

liczba = input('Podaj liczbę')
czestotliwosc = {}
for e in liczba:
    if e in czestotliwosc:
        czestotliwosc[e] += 1
    else:
        czestotliwosc[e] = 1
        
#%% Zadanie 7

fib = [0, 1]
n = 10
for e in range(0, n):
    fib.append(fib[-1]+fib[-2])
print(fib)
