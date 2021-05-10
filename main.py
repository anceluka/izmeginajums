f = open('aste.txt', 'r', encoding="utf-8")
skaits = 0
while True: 
    skaits += 1
    # ja rinda ir tukša

    linija = f.readline()
    if not linija:
        break
    if skaits == 3 or skaits == 5:
        print("rinda{}: {}".format(skaits, linija.strip()))
f.close()