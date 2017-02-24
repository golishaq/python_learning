#demonstruje marynowanie danych
import pickle, shelve
#pickle - marynowanie i przechowywanie w pliku bardziej zlozonych danych
#shelve - magazynowanie zamarynowanych obiektow w pliku i swobodny dostep
print("Marynowanie list")
variety = ["lagodny", "pikantny", "kwaszony"]
shape = ["cały", "krojony wzdluz", "w plasterkach"]
brand = ["Dawtona", "Wloclawek", "Pudliszki"]

#dane w pliku binarnym
f = open("pickle1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

#odczyt danych z pliku
print("Odmarynowanie list")
f = open("pickle1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

print("Odkladanie list na polke")
#parametr dostepu defaultowo - c
s = shelve.open("pickle2")
#dodanie 3 list na polke
s["variety"] = ['lagodny', 'pikantny', 'kwaszony']
s["shape"] = ["cały", "krojony wzdluz", "w plasterkach"]
s["brand"] = ["Dawtona", "Wloclawek", "Pudliszki"]
s.sync() #aktualizacja polki

print("Pobieranie list z polki")
print("marka:", s["brand"])
print("ksztalt:", s["shape"])
print("odmiana:", s["variety"])

s.close()

