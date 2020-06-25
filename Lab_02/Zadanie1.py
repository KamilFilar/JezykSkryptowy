def histogram(tekst):
    dictionary = {}

    for znak in tekst:
        if znak != " ":
            if znak in dictionary:
                dictionary[znak] += 1
            else:
                dictionary[znak] = 1

    return dictionary

print("Wynik algorytmu:")
print(histogram("Jade czolgiem prze pola"))