# Translator slangu komputerowego
# Demonstruje używanie słowników

geek = {"404": "ignorant; od używanego w sieci WWW komunikatu o błędzie 404\n - nie znaleziono strony.",
        "Googling": "googlowanie; wyszukiwanie w internecie informacji dotyczących jakiejś osoby.",
        "Keyboard Plaque": "(skojarzone z kamieniem nazębnym)zanieczyszczenia nagromadzone w klawiaturze komputera.",
        "Link Rot": "(obumieranie linków) proces, w  wyniku którego linki do stron WWW stają się nieaktualne.",
        "Percussive Maintenance": "(konserwacja perkusyjna)naprawa urządzenia elektronicznego przez stuknięcie.",
        "Uninstalled": "(odinstalowany) zwolniony z pracy;  termin szczególnie popularny w okresie bańki internetowej."}

choice = None

while choice != "0":
    print(
        """
        Translator slangu
        1-znajdz termin
        2-dodaj termin
        3-zmien definicje
        4-usun termin
        0-zakoncz
        """
    )

    # wyszukaj wartość w słowniku
    choice = input("Wybierasz: ")
    if choice == "1":
        term = input("Podaj slowo do wyszukania")
        print(geek.get(term, "nie mam takiego slowa w slowniku"))

    # dodaj parę termin-definicja
    elif choice == "2":
        term = input("Jaki termin mam dodac?")
        if term not in geek:
            definition = input("\nPodaj definicję terminu")
            geek[term] = definition
            print("\nTermin", term, "zostal dodany")
        else:
            print("\nTermin znajduje sie juz w bazie")

    # zmiana definicji terminu
    elif choice == "3":
        term = input("Jaki termin mam przedefiniowac?")
        if term in geek:
            definition = input("Jaka jest nowa definicja?")
            geek[term] = definition
            print("\nTermin", term, "zostal zmieniony")
        else:
            print("\nTermin nie istnieje")

    # usuniece terminu
    elif choice == "4":
        term = input("Jaki termin mam usunac?")
        if term in geek:
            del geek[term]
            print("\nOK usunieto", term)
        else:
            print("\nBlad", term, "nie ma w slowniku")

    elif choice == "5":
        print(geek.keys())
        print(geek.values())
        print(geek.items())

    # koniec programu
    elif choice == "0":
        print('BYE')

    # zabezpieczenie zlego wyboru
    else:
        print(choice, " To niewlasciwa opcja")

input("\nAby zakonczyc kliknij \"Enter\"")
