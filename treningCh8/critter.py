# podstawy OOP klasy, obiekty, metody, konstruktory, atrybuty
# +atrybuty klasy i metody statyczne


class Critter(object):  # object - wbudowany typ podstawowy
    """wirtualne zwierzaki
    powoluje obiekty, uzywa ich metod, atrybutow
    zlicza ilosc obiektow"""
    total = 0  # tworzy atrybut klasy, licznik obiektow klasy

    # konstruktor wywoluje sie automatycznie przy tworzeniu nowego obiektu - specjalna metoda inicjalizacji
    # nadaje atrybuty obiektom
    def __init__(self, name, mood, age):  # 3 parametry przekazywane sa do atrybutu
        print("\n------------------------\nUrodził sie nowy zwierzak")
        self.name = name  # tworzy atrybut publiczny
        self.__mood = mood  # tworzy atrybut prywatny
        self.__age = age # atrybut do wlasciwosci
        Critter.total += 1  # kazde powolanie nowej instacji/obiektu zwieksza wartosc licznika

    # metoda specjalna do wyswietlania obiektu
    def __str__(self):
        rep = "\n\t[ Obiekt klasy Critter ] \n"
        rep += "[ name: " + self.name + " mood: " + self.__mood + " age: " + str(self.age) + " ]"
        return rep

    # definiowane wlasnej metody (wlasna nazwa)
    # self automatycznie jako swoja wartosc otrzymuje referencje do obiektu wywolujacego metode
    # jest niezbedny dla metod obiektu
    def talk(self):  # sposob odwolywania sie do obiektu
        print("[ Czesc! Jestem egzamplarzem klasy Critter.\n"
              "Nazywam sie: ", self.name,  # wykorzystanie atrybutu publicznego
              "\nAktualnie czuje sie", self.__mood, # wykorzystanie atrybutu prywatnego
              "\nMam", self.age, "lat ]")  # wykorzystanie wlasciwosci do odczytu prywatnego atrybutu

    # definiowanie metody prywatnej
    def __private_method(self):
        print("[ To jest metoda prywatna. ", self.name, " ]")

    # dostep do metody prywatnej poprzez metode publiczna
    # zachowanie jak z atrybutami
    def public_method(self):
        print("[ To jest metoda publiczna. ", self.name, " ]")
        self.__private_method()

    # dekorator wskazuje na metode statyczna
    @staticmethod 
    # metoda statyczna (wlasna nazwa metody), bez self bo wywolywana przez klase, nie otrzyma referencji do obiektu
    def status():
        print("\n[ Ogolna ilosc zwierzakow wynosi", Critter.total, "]")

    # tworzenie wlasciwosci analogicznie jak metody statycze, dekorator + self, umozliwia odczyt prywatnego atrybutu obiektu
    @property
    def age(self):
        return self.__age

    # dekorator z atrybutem setter, sygnalizuje ze metoda bedzie mogla zmieniac wartosc prywatnego atrybutu obiektu
    @age.setter
    def age(self, new_age):
        if new_age == "":
            print("Wartosc nie moze byc pusta")
        else:
            self.__age = new_age
            print("Zmiana wartosci powiodla sie")

# główny program
print("Uzyskanie dostepu  do atrybutu klasy Critter.total:", end=" ")
print(Critter.total)

crit = Critter("Reksio", mood="happy", age=10)  # (konkretyzacja obiektu z parametrem atrybutu
crit.talk()  # wywolanie metody instancji
# print(crit.mood) // print(crit.__mood) taki kod nam sie wylozy (AttributeError)
# kod crit.private_method() // crit.__private_method nam sie wylozy
crit.public_method()

crit2 = Critter("Filemon", mood="sophisticated", age=13)
crit2.talk()
crit2.public_method()

print("\nWyswietlenie obiektu crit")
print(crit)

#dostęp do atrybutow i wlasciwosci
print("\nWyswietlenie bezposrednie wartosci atrybutu crit.name oraz wlasciwosci crit.age")
print(crit.name, ":", crit.age)


crit.age = 7
print(crit.name, "ma teraz", crit.age, "lat")

print("\nWywolanie metody statycznej Critter.status()")
Critter.status()

print("\nUzyskanie dostepu do atrybutu klasy poprzez obiekt: ", end=" ")
# mozna tylko wyswietlac wartosc atrybutu klasy w  ten sposob
# zeby ja zmienic nalezy uzyc wywolania przez klase
print(crit.total)

input('\n\nFor end press "ENTER"')
