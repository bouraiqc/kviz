#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:27:19 2022

@author: vasigo
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 23:38:25 2022

@author: vasigo
"""

import random

class Kviz:
    def __init__(self, pitanje, tacan_odgovor, pogresan_odgovor):
        self.pitanje = pitanje
        self.tacan_odgovor = tacan_odgovor
        self.pogresan_odgovor = pogresan_odgovor


broj_pitanja_po_kvizu = 5
kviz_pitanja = [Kviz("Glavni grad američke države Merilend je:", "Anapolis", ["Dover", "Ričmond", "Vašington"]),
                Kviz("'Posle mene potop' rekao je kralj:", "Luj XV", ["Luj XVI", "Luj XIII", "Luj XVIII"]),
                Kviz("Koji program se koristi za automatsko testiranje opterećenja web sajtova?", "Apači",
                     ["Selenium", "Kindl", "Op Test"]),
                Kviz("Kojoj grupi Sijuksa je pripadao slavni vrač i poglavica Bik Koji Sedi?", "Hunkpapa",
                     ["Minekonžu", "Crna Stopala", "Oglala"]),
                Kviz("Najveći sisar je:", "Plavi kit", ["Afrički slon", "Žirafa", "Beli miš"]),
                Kviz("Rodno mesto Napoleona I Bonaparte je:", "Ajačio", ["Marsej", "Pariz", "Tulon"]),
                Kviz("Prva Napoleonova bitka je bila:", "Opsada Tulona",
                     ["Bitka kod Poatjea", "Bitka na Aralskom mostu", "Bitka za Saragosu"]),
                Kviz("Drugo svetsko prvenstvo u fudbalu održano je 1934. godine u:", "Italiji",
                     ["Francuskoj", "Španiji", "Jugoslaviji"]),
                Kviz("Postojbina točka je:", "Mesopotamija", ["Egipat", "Kina", "Fenikija"]),
                Kviz("Kako se etiopski car Hajle Selasije zvao pre krunisanja?", "Tafari Makonen",
                     ["Abebe Bikila", "Kefle Jakob", "Sahle Marjam"]),
                Kviz("Najbolji srpski film XX veka je:", "Ko to tamo peva?",
                     ["Maratonci trče počasni krug", "Lepa sela lepo gore", "Sabirni centar"])]


def pokreni_kviz():
    corrCount = 0


    random.shuffle(kviz_pitanja)
    broj_pitanja = min(broj_pitanja_po_kvizu, len(kviz_pitanja))
    k_pitanja = random.sample(kviz_pitanja, k=broj_pitanja)
    for kviz_pitanje in k_pitanja:
        print(kviz_pitanje.pitanje)
        odgovor = kviz_pitanje.pogresan_odgovor + [kviz_pitanje.tacan_odgovor]
        random.shuffle(odgovor)
        count = 0
        while count < len(odgovor):
            print(str(count + 1) + ':' + odgovor[count])
            count += 1
        print("Unesi broj pod kojim je tačan odgovor:")
        userOdg = input()
        while not userOdg.isdigit():
            print("Nisi uneo broj. Ponovi.")
            userOdg = input()
        userOdg = int(userOdg)
        while not (int(userOdg) > 0 and int(userOdg) <= len(odgovor)):
            print("Pod ovim brojem nema nijednog odgovora. Ajde ponovo.")
            userOdg = input()
        if odgovor[userOdg - 1] == kviz_pitanje.tacan_odgovor:
            print("Tačno!")
            corrCount += 1
        else:
            print("Nemaš pojma.")
            print("")
        print("")

    random.choices(kviz_pitanja, k=5)

    if corrCount == len(k_pitanja):
        print("Odgovorio si tačno na sva pitanja. Bravo!")
    elif corrCount == 0:
        print("Sve si omašio.")
    else:
        print("Odgovorio si tačno na " + str(corrCount) + " od " + str(len(kviz_pitanja)) + " pitanja.")

pokreni_kviz()
