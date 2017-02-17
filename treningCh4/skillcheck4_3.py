# rozbudowana wersja mixed_letter
# komputer wybiera losowe slowo a nastepnie miesza w nim litery, gracz musi zgadnac
from treningCh6 import slownik_test

# baza slow
WORDS = ("daria", "bartek", "bercik", "anagram", "lesczynowa", "latwy", "trudny")
counter = 0

# wybor losowego slowa z sekwencji + odpowiedz prawidlowa
word = slownik_test.choice(WORDS)
correct = word

# utworz 'pomieszana' wersje slowa
twist = ""

#utworz podpowiedz
hint = word[2:-1]

# wybor litery z slowa oryginalnego i dopisanie do twist
while word:
    pos = slownik_test.randrange(len(word))
    twist += word[pos]
    word = word[:pos] + word[(pos + 1):]  # nie mozna odjac znaku z lancucha wiec tworzymy jej inna wersje

# start gry
print("Witaj, zgadnij co to za slowo?", twist)
print("Podpowiedź - wpisz HINT")
guess = input("Twoja odpowiedz:")
while guess != correct and guess != "":
    if guess == "HINT" or counter > 2:
        print("PODPODWIEDŻ", hint)
        guess = input("Twoja odpowiedz:")
    else:
        print("niestety nie zgadles")
        counter += 1
        guess = input("Twoja odpowiedz:")
if guess == correct and counter <= 2:
    print("Brawo, jestes tak zajebisty ze dostajesz 10 pkt")
else:
    print("Zajelo Ci to za duzo czasu, tylko 2 pkt")

input("\nAby zakonczyc kliknij \"Enter\"")
