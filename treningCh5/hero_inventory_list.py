# demonstruje użcycie list i ich roznice do krotek ($1)
# tworzenie pustej listy
inventory = []

# potraktuj liste jako warunek
if not inventory:
    print("Nie posiadasz niczego")

input("\nAby dodac itemy kliknij 'ENTER'")

# dodaj elementy do krotki
inventory = ["miecz",
             "zbroja",
             "tarcza",
             "potion"]

# wysietlanie calej listy
print("\nWykaz zawartosci")
print(inventory)

# wyswietlenie listy element po elemencie
print("\nElementy wyposazenia")
for item in inventory:
    print(item)

# wyswietlanie dlugosci listy
print("Twoj inwentarz zawiera", len(inventory), "elementow")
input("\nAby kontynuowac kliknij \"Enter\"")

# uzycie operatora in
if "potion" in inventory:
    print("Dozyjesz dnia kiedy stczysz walke")

# indeksowanie list
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

# konkatenacja dwoch list
chest = ("zloto", "klejnoty")
print("znajdujesz skrzynie z:", chest, "\nZabierasz kosztownosci ze soba")
inventory += chest
print("Masz teraz:", inventory)
input("\nAby kontynuowac kliknij \"Enter\"")

# $1 przypisywanie nowej wartosci
print("Wymieniasz swoj miecz na kusze")
inventory[0] = "kusza"
print("Masz teraz:", inventory)

#przypisz poprzez wycinek
print("Wymieniasz zloto i klejnoty na zakup kuli do wrozenia")
inventory[4:6] = ["kula do wrozenia"]
print("Masz teraz:", inventory)

#usuwanie elementu
print("W wielkiej bitwie zniszczyles tarcze")
del inventory[2]
print("Masz teraz:", *inventory)

#usuwanie wycinka
print("Twoja kusza i zbroja zostaly zabrane przez zlodzei")
del inventory[:2]
print("Masz teraz:", *inventory)

input("\nAby zakonczyc kliknij \"Enter\"")
