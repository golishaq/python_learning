# demonstrate indexing of charchain
from treningCh6 import slownik_test

word = "index"
print("---", word, "---\n")

high = len(word)  # create max and min position index 
low = -len(word)  # minus counting word backwards

for i in range(10):
    position = slownik_test.randrange(low, high)  # used values strict for word length
    print("word[", position, "]\t", word[position])  # printing randomly choices position in word

input("\nAby zakonczyc kliknij \"Enter\"")
