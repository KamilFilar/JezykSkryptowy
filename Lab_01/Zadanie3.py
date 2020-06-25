#Zadanie 3 lab01
import sys

if len(sys.argv) < 2:
    print("Uruchamiajac skrypt podaj co najmniej jeden parametr!")
else:
    ilosc = 0
    wyrazy = []
    for x in range(1, len(sys.argv)):
        if (len(sys.argv[x]) >= 3):
            ilosc += 1
            wyrazy.insert(0, sys.argv[x])

    print("Ilosc argumentow ktorych dlugosc jest wieksza badz rowna 3 = " + str(ilosc))
    print("Argumenty (3 argumenty) dluzsze lub rowne 3 wypisane od konca = " + " ".join(wyrazy))