# komputer wybiera losowe slowo a nastepnie miesza w nim litery, gracz musi zgadnac
from treningCh6 import slownik_test

# baza slow
WORDS = ("daria", "bartek", "bercik", "anagram", "lesczynowa", "latwy", "trudny")

# wybor losowego slowa z sekwencji + odpowiedz prawidlowa
word = slownik_test.choice(WORDS)
correct = word

# utworz 'pomieszana' wersje slowa
twist = ""

# wybor litery z slowa oryginalnego i dopisanie do twist
while word:
    pos = slownik_test.randrange(len(word))
    twist += word[pos]
    word = word[:pos] + word[(pos + 1):]  # nie mozna odjac znaku z lancucha wiec tworzymy jej inna wersje

# start gry
print("Witaj, zgadnij co to za slowo?", twist)
guess = input("Twoja odpowiedz:")
while guess != correct and guess != "":
    print("niestety nie zgadles")
    guess = input("Twoja odpowiedz:")
if guess == correct:
    print("Brawo")

input("\nAby zakonczyc kliknij \"Enter\"")
