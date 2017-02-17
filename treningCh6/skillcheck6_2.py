# odgadnij liczbę wylosowaną przez komputer
# wersja 2.0 posiadasz ograniczoną liczbę prób
# losowanie liczby z zakresu 1-100
import random

liczba = random.randint(1, 100)


def ask_number(question):
    """Popros o podanie liczby z odpowiedniego zakresu"""
    response = int(input(question))
    return response


def main():
    # pętla pyta użytkownika o odpowiedź i sprawdza czy odgadł
    count = 1
    while True:
        ask = ask_number("Podaj liczbę:")

        if liczba > ask:
            print("Wylosowano większą liczbę\n")
            count += 1
        elif liczba < ask:
            print("Wylosowano mniejsza liczbe\n")
            count += 1
        else:
            print("Gratuluje!, Wylosowana liczba to", liczba
                  , "\nPotrzebowałeś", count, "prób.")
            break
        # licznik żyć
        if count == 10:
            print("koniec żyć, liczba to ", liczba)
            break


main()
input("\nAby zakończyć wciśniej 'ENTER'")
