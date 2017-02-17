#tworzenie nowej postaci, przydzial pkt atrybutow

attributes = {"strenght": 0,
              "life":0,
              "mana": 0,
              "agility":0}
score = 30
print("Posiadasz 30pkt umiejetnosci, mozesz przydzielic je pomiedzy sile, zdrowie, wole, zrecznosc")
choice = None

while choice != 0 and score > 0:
    print(
    """
    Przydzial pkt
    1-pokaz
    2-dodaj pkt
    3-usun pkt
    4-wyczysc
    0-zakoncz
    """
    )
    choice = input("Wybierasz: ")
    if choice == "1":
        print(attributes.items())
        print(score)
    elif choice == "2":
        term = input("Gdzie mam dodac pkt?")
        definition = input("\nPodaj ilość pkt")
        pkt = int(definition)
        if (score-pkt) > 0:
            attributes[term] = pkt
            score -= pkt
            print("\nTermin", term, "zostal dodany")
        else:
            print("nie maszy tylu pkt")
    elif choice == "3":
        term = input("Gdzie mam odjac pkt?")
        definition = input("\nPodaj ilość pkt")
        pkt = int(definition)
        attributes[term] = pkt
        score += pkt
        print("\nTermin", term, "zostal dodany")


    else:
        print(choice, " To niewlasciwa opcja")

input("\nAby zakonczyc kliknij \"Enter\"")

