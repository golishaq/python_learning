#Demontruje odczytywanie danych z pliku tekstowego
print("Otwarcie i zamkniecie pliku")
text_file = open("read_it.txt", "r")
text_file.close()

print("\nOdczytywanie znaków z pliku")
text_file = open("read_it.txt", "r")
print(text_file.read(1))
#odczyt okreslonej liczby znakow do lancucha
print(text_file.read(7))
text_file.close()

print("\nOdczytanie calego pliku na raz")
text_file = open("read_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("\nOdczytywanie znaku z wiersza")
text_file = open("read_it.txt", "r")
print(text_file.readline())
print(text_file.readline(1))
print(text_file.readline(7))
text_file.close()

print("\nOdczytywanie po jednym wierszu na raz")
text_file = open("read_it.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nWczytanie pliku do listy")
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("\nPbieranie zawartosci pliku wieersz po wierszu przy użyicu petli")
text_file = open("read_it.txt", "r")
for line in text_file:
    print(line)
text_file.close()


