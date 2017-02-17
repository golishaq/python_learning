# demonstrate len function and in operator
message = input("Podaj slowo:")
print ("\nDlugosc Twojego komunikatu to", len(message))

if 'a' in message:
    print ("\nLitera 'a' wystapila w Twoim slowie:")
else:
    print ("\nLitera 'a' nie wystąpila w Twoim slowie")

input("\nAby zakonczyc kliknij \"Enter\"")