#Zadanie 2 lab01
import sys
from datetime import date

if len(sys.argv) < 2:
    print("Uruchamiajac skrypt podaj jako parametr date rrrr-mm-dd!")
else:
    data = date.fromisoformat(sys.argv[1])
    today = date.today()

    datediff = today - data

    print("Dzisiaj jest: " + str(today))
    print("Wczytana data: " + str(data))
    print("Roznica dni: " + str(datediff))
