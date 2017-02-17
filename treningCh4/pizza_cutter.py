#  demonstrate wordchains sliing
print("Podaj poczatkowy i koncowy indeks wycinka lancucha 'pizza'")
print("\nAby zakonczyc wcisnij ENTER prezd podaniem wartosci")

word="pizza"
start = None
while start != "":
    start = (input("\nPoczatek"))

    if start:
        start = int(start)

        finish = int(input("Koniec"))

        print("word[", start, ":", finish, "] to", end=" ")
        print(word[start:finish])

input("\nAby zakonczyc kliknij \"Enter\"")