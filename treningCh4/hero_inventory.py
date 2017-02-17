# demonstruje użcycie tupli/krotek
# tworzenie pustej krotki
inventory = ()

# potraktuj krotke jako warunek
if not inventory:
    print("Nie posiadasz niczego")

input("\nAby dodac itemy kliknij 'ENTER'")

# dodaj elementy do krotki
inventory = ("miecz",
             "zbroja",
             "tarcza",
             "potion")

# wysietlanie calej krotki
print("\nWykaz zawartosci")
print(inventory)

# wyswietlenie krotki element po elemencie
print("\nElementy wyposazenia")
for item in inventory:
    print(item)

# wyswietlanie dlugosci krotki
print("Twoj inwentarz zawiera", len(inventory), "elementow")
input("\nAby kontynuowac kliknij \"Enter\"")

# uzycie operatora in
if "potion" in inventory:
    print("Dozyjesz dnia kiedy stczysz walke")

# indeksowanie krotek
while True:
    index = int(input("Wybierz nr elementu inwentarza:"))
    if index <= len(inventory):
        print("Pod indexem", index, "znajduje sie", inventory[index])
        break
    else:
        print("Niewlasciwa wartosc, podaj jeszcze raz")
# wyswietl wycinek
start = int(input("Wybierz poczatek wycinka"))
finish = int(input("Wybierz koniec wycinka"))
print("inventory [", start, ":", finish, "] to", inventory[start:finish])

# konkatenacja dwoch krotek
chest = ("zloto", "klejnoty")
print("znajdujesz skrzynie z:", chest, "\nZabierasz kosztownosci ze soba")
inventory += chest
print("Masz teraz:", inventory)

input("\nAby zakonczyc kliknij \"Enter\"")
