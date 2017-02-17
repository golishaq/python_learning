#ciastko z wróżbą
print("Wróżbita Maciej mówi że dziś:")
from treningCh6 import slownik_test

prediction = slownik_test.randrange(5)
if prediction==0:
    print("wpadniesz pod autobus")
elif prediction==1:
    print("zgwałcą cię")
elif prediction==2:
    print("stracisz wzrok")
elif prediction==3:
    print("kupisz multiplę")
elif prediction==4:
    print("masz raka")

#100 rzutów monetą i podanie liczby reszek i orłów
jump = 0
orzeł = 0
reszka = 0
while jump < 100:
    option = slownik_test.randint(1, 2)
    if option == 1:
        orzeł += 1
        jump += 1
    else:
        reszka += 1
        jump += 1
print("\nOrzeł:", orzeł, "Reszka:", reszka)

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
