# demonstrate for loop using wich charchain
word = input("Podaj slowo")

print("\noto litery twojego slowa:")
for letter in word:
    print(letter)

# demonstrate range function
print("\nLiczenie:")
for i in range(10):
    print(i, end=" ")  # spaces beetwen numbers

print("\nLiczenie co 5:")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\nLiczenie do tylu:")
for i in range(10, 0, -1):
    print(i, end=" ")
input("\nAby zakonczyc kliknij \"Enter\"")
