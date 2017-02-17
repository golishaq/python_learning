#demonstracja generowania liczb losowych

from treningCh6 import slownik_test

#generowanie licz z zakresu (1-6) przy pomocy dwóch metod
die1 = slownik_test.randint(1, 6)
die2 = slownik_test.randrange(6) + 1 #funkcja randrange startuje od 0

total = die1 + die2

print("Wyrzuciłeś", die1, "oraz", die2, "i uzyskałeś sume", total)

input("\nAby zakończyć wciśniej 'ENTER'")
