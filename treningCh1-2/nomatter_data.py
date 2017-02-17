#uzyskuję dane użytkownika a następnie podaję nieistotne faktyo nim
name = input("Podaj imię: ")
age = int(input("Podaj wiek: ")) #zagnieżdżanie parametrów
weight = int(input("Podaj wagę: "))

print("\njeśli pisałbym do Ciebie maila zwróciłbym sie do Ciebie", name.lower(), "\nale jeślibyłbym wściekły to", name.upper())

called = name * 5
print("\njeśli dziecko by cię wołało to,", called)

seconds = age*365*24*60*60
print("\nżyjesz już ponad", seconds, "sekund")

moon_weight = weight /6
sun_weight = weight *27.1
print("na słońcu ważyłbyś", sun_weight, "a na księżycu", moon_weight, "kg")

input('\nAby zakończyć kliknij "ENTER"')
