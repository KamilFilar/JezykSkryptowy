#Zadanie 1 lab01
import sys
if len(sys.argv) < 4:
    print("Po wlaczeniu skryptu podaj jako parametr najpierw zmienna a, spacja, potem dzialanie, spacja, potem zmienna b!")
else:
    a = sys.argv[1]
    znak = sys.argv[2]
    b = sys.argv[3]
    wynik = a

    if znak == "+":
        wynik = int(a) + int(b)
    if znak == "-":
        wynik = int(a) - int(b)
    if znak == "*":
        wynik = int(a) * int(b)
    if znak == "/":
        wynik = int(a) / int(b)

    print("Wynik: "+ a + znak + b + " = " + str(wynik))