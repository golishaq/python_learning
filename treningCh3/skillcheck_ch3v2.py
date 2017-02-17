from treningCh6 import slownik_test

liczba = slownik_test.randint(1, 100)
count = 1

#pętla pyta użytkownika o odpowiedź i sprawdza czy odgadł
while True:
    ask = int(input("Podaj liczbę:"))
    #licznik żyć
    if count == 10:
        print("koniec żyć, liczba to ",liczba)
        break

    if liczba > ask:
        print("Wylosowano większą liczbę\n")
        count += 1
    elif liczba < ask:
        print("Wylosowano mniejsza liczbe\n")
        count += 1
    else:
        print("Gratuluje!, Wylosowana liczba to", liczba
              ,"\nPotrzebowałeś", count, "prób.")
        break

#odwrotna wersja zgadywania liczb, podajesz liczbę komputer zgaduje

liczba = slownik_test.randint(1, 100)
x = liczba  #zmienna pomocnicza
ask = int(input("Podaj liczbe 1-100 \n"))
count = 1
top = 100 # najwyższa wartość

#pętla zgadywania:
while ask != liczba:
    if ask < liczba:
        top = liczba
        liczba //= 2
    else:
        liczba = liczba + ((top - liczba)//2)
    count += 1
print("Twoja licza to", ask, "\nMoja to", x, "\nPotrzebowalem", count, "prób")

input("\nAby zakończyć wciśniej 'ENTER'")
