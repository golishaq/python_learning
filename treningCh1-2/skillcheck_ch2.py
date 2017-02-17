#łączenie 2 ciągów
frykas1 = input("Podaj pierwszy ulubiony przysmak")
frykas2 = input("Podaj 2 ulubiony przysmak")
print("Twoje ulubione połączenie to", frykas1, "i", frykas2)

#tip generator
tip = int(input("\nPodaj kwote rachunku: "))
tip15 = tip * 0.15
tip20 = tip * 0.2
print("\nNapiwiek powinien zawierać się pomiędzy", tip15, "a", tip20)

#car dealer
price = int(input("\nPodaj cene auta: "))
dealer = 2000
transport = 500
rejestracja = price * 0.05
tax = price * 0.2
price_all = price+dealer+transport+rejestracja+tax
print("\nKoszta Twojego nowego auta to:",
      "\nopłata dealera:", dealer,
      "\nopłata transportu:", transport,
      "\nkoszt rejestracji:", rejestracja,
      "\npodatek:", tax,
      "\nRAZEM: ", price_all)

input("\nAby zakończyć kliknij \"ENTER\"")