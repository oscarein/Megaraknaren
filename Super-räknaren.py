import math
from statistics import *

def binary_converter(bi):
    binary = bi
    denary = 0
    for digit in binary:
        denary = denary * 2 + int(digit)
    print("Ditt decimala tal är: " + str(denary))

def denery_convert(dec):
    denary = dec
    binary = ""
    while denary>0:
        binary = str(denary%2) + binary
        denary = denary//2
    print("Ditt binära tal är: " + binary)

def plus (x, y, z):
    print(f"Svaret är: {x+y+z}")

def minus (x, y, z):
    print(f"Svaret är: {x-y-z}")

def gånger (x, y, z):
    print(f"Svaret är: {x*y*z}")

def gånger2 (x, y):
    print(f"Svaret är: {x*y}")

def delat (x, y):
    print(f"Svaret är: {x/y}")

def roten (x):
    print(f"Svaret är: {math.sqrt(x)}")

def velocity (s, t):
    if t == 0:
        print("Det går ej att dela med 0!")
    else:
        print(s/t)

def time (s, v):
    if v == 0:
        print("Det går ej att dela med 0!")
    else:
        print(s/v)

def segment (v, t):
    print(v * t)

def medel(siffror):
    print(f"Medelvärdet är: {(mean(siffror))}")

siffror = []

Q = True

while Q:
    print("\n--------------------")
    print("1. Addera")
    print("2. Subtrahera")
    print("3. Multiplicera")
    print("4. Dividera")
    print("5. Roten ur")
    print("6. Medelvärdet")
    print("7. Kryptera")
    print("8. Avkryptera")
    print("9. SVT formeln")
    print("10. Binära tal")
    print("11. Avsluta")
    print("--------------------")
    val = int(input("Vad vill du göra? "))


    if val == 1:
        AT1 = int(input("Skriv in term 1: "))
        AT2 = int(input("Skriv in term 2: "))

        T3 = input("Vill du ha en till term? (Ja/Nej) ")

        if T3.lower() == "ja":
            AT3 = int(input("Skriv in term 3: "))
            plus(AT1, AT2, AT3)
        
        elif T3.lower() == "nej":
            AT3 = 0
            plus(AT1, AT2, AT3)

    elif val == 2:
        ST1 = int(input("Skriv in term 1: "))
        ST2 = int(input("Skriv in term 2:"))

        T3 = input("Vill du ha en till term? (Ja/Nej) ")

        if T3.lower() == "ja":
            ST3 = int(input("Skriv in term 3: "))
            minus(ST1, ST2, ST3)

        elif T3.lower() == "nej":
            ST3 = 0
            minus(ST1, ST2, ST3)

        else:
            print('Vänligen skriv "Ja" eller "Nej"')

    elif  val == 3:
        MF1 = int(input("Skriv in faktor 1: "))
        MF2 = int(input("Skriv in faktor 2: "))

        F3 = input("Vill du ha en till faktor? (Ja/Nej) ")

        if F3.lower() == "ja":
            MF3 = int(input("Skriv in term 3: "))
            gånger(MF1, MF2, MF3)

        elif F3.lower() == "nej":
            gånger2(MF1, MF2)

        else:
            print('Vänligen skriv "Ja" eller "Nej"')

    elif val == 4:
        DT = int(input("Skriv in täljaren: "))
        DN = int(input("Skriv in nämnaren: "))

        if DN == 0:
            print("Det går ej att dividera med noll!")

        else:
            delat(DT, DN)

    elif val == 5:
        R = int(input("Skriv in ditt tal: "))
        roten(R)

    elif val == 6:
        print("--------------------")
        print(siffror)
        print("Vad vill du göra?")
        print("1. Lägg till tal till listan")
        print("2. Ta bort tal från listan")
        print("3. Ta medelvärdet av listan")
        print("--------------------")

        mval = int(input("Välj: "))

        if mval == 1:
            tillägg1 = int(input("Talet du vill lägga till: "))
            siffror.append(tillägg1)
            en_till = input("Vill du lägga till ett till? ")

            if en_till.lower() == "ja":
                tillägg2 = int(input("Talet du vill lägga till: "))
                siffror.append(tillägg2)

            else:
                print("Okej!")

        elif mval == 2:
            röttkort = int(input("Talet du vill ta bort: "))
            siffror.remove(röttkort)
            ben_till = input("Vill du ta bort en till? ")

            if ben_till.lower() == "ja":
                röttkort2 = int(input("Talet du vill ta bort: "))
                siffror.remove(röttkort2)

            else:
                print("Okej!")

        elif mval == 3:
            medel(siffror)

        else:
            print("Vänligen skriv 1, 2 eller 3!")

    elif val == 7:
        meddelande = input("Vad för meddelande vill du kryptera?\n")

        for bokstav in meddelande:
            print(ord(bokstav), end = " ")

    elif val == 8:
        krypterat_meddelande = input("\nVad för meddelande vill du avkryptera?\n")

        krypterat_meddelande = krypterat_meddelande.split()

        for siffra in krypterat_meddelande:

            print(chr(int(siffra)), end="")

    elif val == 9:
        print("Vad vill du ränka ut?")
        print("1. Sträckan")
        print("2. Hastigheten")
        print("3. Tiden")
        valsvt = int(input("Välj: "))

        if valsvt == 1:
            H = int(input("Ange hastighet: "))
            T = int(input("Ange tid: "))
            segment(H, T)

        #fortsätt här
        
    elif val == 10:
        valbd = input("Omvandla till eller från binära tal? (Till/Från) ")

        if valbd.lower() == "från":
            btal = input("Ditt binära tal: ")
            binary_converter(btal)

        elif valbd.lower() == "till":
            dtal = int(input("Ditt decimala tal: "))
            denery_convert(dtal)

        else:
              print('Vänligen skriv "Ja" eller "Nej"')

    elif val == 11:
        säker = input("Är du säker på att du vill lämna denna fantastiska plats?\n")
        if säker.lower() == "ja":
            print("Okej, hejdå! Hoppas vi ses snart igen.")
            Q = False
        else:
            print("Najs")

    else:
        print("Vänligen välj ett av alternativen nedan.")      
