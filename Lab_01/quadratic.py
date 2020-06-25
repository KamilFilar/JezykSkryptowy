#Zadanie 4 lab01
import sys
import math

if len(sys.argv) < 4:
    print("Uruchamiajac skrypt podaj zmienne a,b,c")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    delta = b * b - (4 * a * c)

    if delta < 0:
        print("Wynik: ")
        print(0)
    if delta == 0:
        print("Wynik: ")
        print("X0: "+str((-b) / (2 * a)))
    if delta > 0:
        print("Wynik: ")
        print("X1: "+str((-b - math.sqrt(delta)) / (2 * a)) + "     X2: " + str((-b + math.sqrt(delta)) / (2 * a)))