# -*- coding: utf-8 -*-
"""
Created on Sat May 27 22:40:00 2023

@author: rav
"""

#%% Zadanie 1

lst = ['zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny', 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony']

zb = set(lst)

print(len(lst)) # liczba eltów listy
print(len(zb)) # licza różnych kolorów
for e in lst: print(e) # wyswietlenie w oddzielnych liniach
zb.add('amarantowy') # dodanie eltu do zbioru
print(zb)
zb.remove('indygo') # usunięcie eltu ze zbioru
print(zb)

#%% Zadanie 2

zdanie = input("Wprowadź zdanie")
nowe_zdanie = ""
for e in zdanie:
    if e not in (',', '.', ':', ';', '!', '?'):
        nowe_zdanie += e
zdanie = nowe_zdanie # zdanie bez interpunkcji

krotka = tuple(zdanie.split(' '))

print(len(krotka)) # liczba słów w zdaniu
print(krotka[0]) # pierwszy wyraz
print(krotka[3]) # czwarty wyraz
zb = set(krotka)
print(len(zb)) # liczba unikatowych wyrazów
print(zb)
print(tuple(zb)[0]) # pierwszy wyraz zbioru
print(tuple(zb)[3]) # czwarty wyraz zbioru
print(tuple(zb)[0] == krotka[0])
print(tuple(zb)[3] == krotka[3]) # czy zgadza się porządek krotki i zbioru

#%% Zadanie 3

#podane = input("Podaj ulubione kolory")
#podane = set(tuple(podane.split(' ')))
podane = set(('czarny', 'niebieski', 'zielony'))
moje = set(('czarny', 'niebieski', 'amarantowy'))
if podane == moje:
    print('Zbiory są identyczne')
else:
    print('W obu zbiorach są:')
    for e in podane: 
        if e in moje: print(e)
    print('Tylko Twoje ulubione kolory to:')
    for e in podane: 
        if e not in moje: print(e)
    print('Tylko moje ulubione kolory to:')
    for e in moje: 
        if e not in podane: print(e)
        
#%% Zadanie 4

#n = input("Podaj liczbę naturalną")
n = 30
A = []
for e in range(0, n, 2):
    A.append(e)
A = set(A)
B = []
for e in range(0, n):
    if e % 3 == 2: B.append(e)
B = set(B)
C = A | B
D = A & B
E = A - B
F = A ^ B
zbiory = (A, B, C, D, E, F)
for i in range(0, 6):
    print('Nazwa: '+chr(ord('A')+i))
    print('Wielkość: '+str(len(zbiory[i])))
    print('Elementy: '+str(zbiory[i]))

wartosc = True
for e in B:
    if e not in A: wartosc = False
if wartosc: print("B zawiera się w A")
else: print("B nie zawiera się w A")