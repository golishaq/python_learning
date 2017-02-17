#program wypluwa liste w losowej kolejnosci bez powtorzen
import random

SLOWA = ["Abarth", "BMW", "Citroen", "Dacia", "Eagle", "Ferrari", "Gumpert", "Honda", "Infiniti", "Jaguar", "Kia",
         "Lotus", "Mercedes", "Nissan", "Opel", "Peugeot", "Renault", "Saab", "Toyota", "UAZ", "VW", "Wiessmann",
         "Xinkai", "Yulon", "Zastava"]

while (len(SLOWA) > 0):
    choice = random.randrange(len(SLOWA))
    word = SLOWA.pop(choice)
    print(word)

print(SLOWA)
input("\nEnter aby zakonczyc")

