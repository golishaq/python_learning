#demonstruje obsluge wyjatkow
try:
    num = float(input("Podaj liczbe: "))
except ValueError:
    print("wystapil blad, to nie była liczba")

#kilka typow wyjatkow
for value in (None, "hej", 10):
    try:
        print("Proba konwersji:",value,"-->", end=" ")
        print(float(value))
    except ValueError:
        print("wystapil blad, to nie była liczba")
    except TypeError:
        print("wystapil blad, niewlasciwy typ danych")

#wykorzystanie warunku wyjatku
try:
    num = float(input("Podaj liczbe: "))
except ValueError as e:
    print("wystapil blad, wywoales blad", e)
