# -*- coding: utf-8 -*-
"""
Created on Sun May 28 09:35:18 2023

@author: rav
"""

#%% Zadanie 1

zdanie = 'Napisz program, który wczytuje dowolne zdanie.'

nowe_zdanie = ""
for e in zdanie:
    if e not in (',', '.', ':', ';', '!', '?'):
        nowe_zdanie += e
zdanie = nowe_zdanie          # bez interpunkcji
zdanie = zdanie.split(' ')  # do listy
zdanie = zdanie[::-1]       # odwrotna kolejnosc
print(zdanie)

#%% Zadanie 2
import random

wynik = [12,1,45,76,50,23]

for i in range(0, len(wynik)):
    if wynik[i] > 49:
        stara_liczba = wynik[i]
        wynik[i] = random.randint(1, 49)
        print('Zamieniono liczbę '+str(stara_liczba)+' na '+str(wynik[i]))
print(wynik)

#%% Zadanie 3

lista1 = ["abc", "def", "ghi", "jkl"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["xyz", 1, '2'] 

for e in (lista1, lista2, lista3):      # Wydruk list
    print(e)

print(lista1[0])                        # Pierwszy elt lista1
print(lista1[3])                        # Czwarty elt lista1

lista2[1] = lista3[1]                   # Podmiana eltu lista2
print(lista2)

lista3[2] = input('Podaj nowy trzeci element dla lista3')  # Podmiana eltu lista3 na input
print(lista3)

lista1.append('słowo')                  # Dodanie eltu do lista1
print(lista1)

lista1.pop(2)                           # Usunięcie eltu lista1
print(lista1)

print('Liczba eltów trzeciej listy: '+str(len(lista3)))     # Długosć lista3

lista1 += lista3                        # Połączenie lista1 i lista3
print(lista1)

#%% Zadanie 4

imiona = input('Podaj imiona')
imiona = imiona.split(' ')
for e in imiona:
    print('Czesć, '+e+'!')
    
#%% Zadanie 5

zdanie = 'Napisz program, który wczytuje dowolne zdanie.'
nowe_zdanie = ""
for e in zdanie:
    if e not in (',', '.', ':', ';', '!', '?'):
        nowe_zdanie += e
zdanie = nowe_zdanie          # bez interpunkcji
zdanie = zdanie.split(' ')
print('Liczba wyrazów: '+str(len(zdanie)))
wielkoliterowe = []
for e in zdanie:
    if e[0] >= 'A' and e[0] <= 'Z': wielkoliterowe.append(e)
if wielkoliterowe == []:
    print('Brak wyrazów pisanych wielką literą w tym zdaniu')
else:
    print('Wyrazy pisane wielką literą w tym zdaniu to: ')
    for e in wielkoliterowe: print(e)

licznik = 0
for i in range(0, len(zdanie)):
    for e in ('i', 'w', 'na', 'pod', 'dla'):
        if zdanie[i] == e: 
            print(e + ' ma indeks ' + str(i))
            licznik += 1
if licznik == 0:
    print('W tym zdaniu nie ma wyrazów „i”, „w”, „na”, „pod”, „dla”')

# ujednolicenie wielkosci znaków dla posortowania alfabetycznego
for i in range(0, len(zdanie)):
    zdanie[i] = zdanie[i].lower()
zdanie = sorted(zdanie)
print('Porządek alfabetyczny:')
for e in zdanie:
    print(e)
