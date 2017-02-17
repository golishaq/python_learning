#  program liczy za uzytkownika. Podaj zakres liczb i odstep miedzy liczbami
start = int(input("Podaj poczatek"))
end = int(input("Podaj koniec"))
krok = input("Podaj odstęp, 'ENTER' dla 1")
if krok == "":
    for i in range(start,end+1):
        print (i, end = " ")
else:
    krok = int(krok)
    for i in range(start,end+1, krok):
        print (i, end = " ")

#   zwracanie komunikatu w odwrotnej formie
slowo = input("Podaj slowo")
owols = slowo[::-1]
print("Twoje slowo to", owols)
