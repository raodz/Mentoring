# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:35:39 2023

@author: rav
"""

#%% Zadanie 1

a = [1, 5, 7]
b = [2, 3, 7]
licznik = 0
for e in a:
    if e in b:
        print('a i b mają wspólny element')
        licznik = 1
        break
if licznik == 0:
    print('a i b nie mają wspólnego elementu')

#%% Zadanie 2

import random

zbior_15 = set(random.sample(range(5, 120), 15))
parzyste = set()
for e in zbior_15:
    if e % 2 == 0:
        parzyste.add(e)
print(zbior_15)
print(parzyste)

#%% Zadanie 3

slownik = {'a' : 3, 'b' : 1, 'c' : 10, 'd' : 15, 'e' : 20}
slownik = {v: k for k, v in slownik.items()}
print(slownik)

#%% Zadanie 4

robocza_lista = ['Boston 12', 'Londyn 10', 'Boston 12']
slownik = {}
for e in robocza_lista:
    miasto_opad = e.split(' ')
    miasto_opad[1] = int(miasto_opad[1])
    if miasto_opad[0] in slownik:
        slownik[miasto_opad[0]] += miasto_opad[1]
    else:
        slownik[miasto_opad[0]] = [miasto_opad[1]]
print(slownik)