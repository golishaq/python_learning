#  demonstrate creating new chains with for loop

messege = input("Wprowadź dame:")
VOVELS = "aąeęiuoóy" #  const
new_message = ""

print()
#  creating new chains
for letter in messege:
    if letter.lower() not in VOVELS:
        new_message += letter
        print ("nNew data:", new_message)

print("\nYour text without vovels:", new_message)
input("\nAby zakonczyc kliknij \"Enter\"")