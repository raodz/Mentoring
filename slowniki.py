# -*- coding: utf-8 -*-
"""
Created on Sun May 28 07:07:08 2023

@author: rav
"""

#%% Zadanie 1

slownik = {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}

for e in slownik.keys(): print(e) # klucze

album = input('Podaj tytuł albumu')

if album in slownik.keys():
    print('Wykonawcą albumu '+album+' jest '+slownik[album])
else:
    print('Brak danych')
    
#%% Zadanie 2

slownik = {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}

tryb = input('Podaj tryb działania programu: (D)odawanie albumu, (U)suwanie albumu, (W)yswietlanie wykonawcy')

if tryb == 'W':
    album = input('Podaj tytuł albumu do wyswietlenia wykonawcy')

    if album in slownik.keys():
        print('Wykonawcą albumu '+album+' jest '+slownik[album])
    else:
        print('Brak danych')
elif tryb == 'D':
    album = input('Podaj tytuł albumu do dodania')
    wyk = input('Podaj wykonawcę')
    slownik[album] = wyk
    print(slownik)
elif tryb == 'U':
    album = input('Podaj tytuł albumu do usunięcia')
    slownik.pop(album)
    print(slownik)
#%% Zadanie 3

tekst = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."
nowy_tekst = ""
for e in tekst:
    if e not in (',', '.', ':', ';', '!', '?'):
        nowy_tekst += e
tekst = nowy_tekst          # bez interpunkcji
tekst = tekst.split(' ')    # tekst jako lista
unikalne = list(set(tekst)) # lista bez duplikatów
slownik = {}
for e in unikalne:
    slownik[e] = tekst.count(e)
print(slownik)

#%% Zadanie 4

slownik = {'kos' : 'Turdus merula', 'wilga' : 'Oriolus oriolus', 'rudzik' : 'Erithacus rubecula', 'kukulka' : 'Cuculus canorus', 'pleszka' : 'Phoenicurus phoenicurus', 'bogatka' : 'Parus major', 'drozd' : 'Turdus philomelos', 'zieba' : 'Fringilla coelebs', 'dzwoniec' : 'Chloris chloris', 'szczygiel' : 'Carduelis carduelis', 'szpak' : 'Sturnus vulgaris', 'kopciuszek' : 'Phoenicurus ochruros'}
tekst = 'W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik, a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi sie bogatka. Wraz ze wschodem slonca, o czwartej godzinie, swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim kopciuszek. Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel.'

zin = tekst.split(' ')      # tekst jako lista z zachowaną interpunkcją
nowy_tekst = ""
for e in tekst:
    if e not in (',', '.', ':', ';', '!', '?'):
        nowy_tekst += e
tekst = nowy_tekst          # bez interpunkcji
tekst = tekst.split(' ')    # tekst jako lista
wynik = ''
for i in range(0, len(tekst)):
    if tekst[i] in slownik:
        wynik += zin[i] + ' (' + slownik[tekst[i]]+')' + ' '
    else:
        wynik += zin[i] + ' '
print(wynik)
# W niektórych miejscach kropki i przecinki są przed nawiasami zamiast po
# Nie znalazłem prostej drogi, żeby to poprawić

#%% Zadanie 5

n = int(input('Podaj liczbę'))
slownik = {}
for i in range(1, n+1):
    slownik[i] = i*i
print(slownik)

#%% Zadanie 6

# Listy i słowniki

#%% Zadanie 7

lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}

people = {**lovers,**friends}
print(people)

#%% Zadanie 8

slownik = { "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }
unikalne = []
for e in slownik.values():
    if list(slownik.values()).count(e) == 1:
        unikalne.append(e)
print(unikalne)