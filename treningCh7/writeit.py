#Demonstruje zapis do pliku tekstowego
print("Tworzenie pliku textowego za pomoca metody write().")
text_file = open("write_it.txt", "w")
text_file.write("Wiersz 1\n")
text_file.write("To jest wiersz 2\n")
text_file.write("Ten tekst tworzy wiersz 3\n")
text_file.close()

print("Odczyt weryfikujacy plik")
text_file = open("write_it.txt" , "r")
print(text_file.read())
text_file.close()

print("Utworzennie pliku za pomoca metody writelines().")
text_file=open("writelines_it", "w")
lines = ["Wiersz1\n",
         "To jest wiersz2\n",
         "Ten tekst tworzy wiesz 3"]
text_file.writelines(lines)
text_file.close()


