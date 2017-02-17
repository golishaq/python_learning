#odgadnij liczbę wylosowaną przez komputer
#wersja 2.0 posiadasz ograniczoną liczbę prób
#losowanie liczby z zakresu 1-100
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
input("\nAby zakończyć wciśniej 'ENTER'")

# #inne podejście (wersja 1.0):
# liczba = random.randint(1,100)
# ask = int(input("Podaj liczbe"))
# count = 1
# #pętla zgadywania:
# while ask != liczba:
#     if ask > liczba:
#         print("Za duża...")
#     else:
#         print("Za mała...")
#
#     ask = int(input("Podaj liczbe"))
#     count += 1
# print("Gratuluje!, Wylosowana liczba to", liczba
#       , "\nPotrzebowałeś", count, "prób.")
