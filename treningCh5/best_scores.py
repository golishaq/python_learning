#program demonstruje metody listy
#pusta tablice i warunek while jako none
scores = [("ziomek", 20),("ziomek2", 40)]
choice = None

while choice != "0":
    print(
    """
    Najlepsze wyniki
    1-pokaz wyniki
    2-dodaj wynik
    3-usun wynik
    4-posortuje wyniki
    0-zakoncz
    """
    )

    choice = input("Wybierasz: ")
    print()

    #wypisywanie tabeli najlepszych wynikow
    if choice == "1":
        print("Najlepsze wyniki\n"
              "GRACZ\tWYNIK") #tabulator
        for entry in scores:
            name, score = entry
            print(name, "\t", score)

    #dodawanie wyników
    elif choice =="2":
        name = input("Podaj nazwe gracza:")
        score = int(input("jaki wynik uzyskal"))
        entry = (score, name)
        scores.append(entry)

    #usuwanie wynikow
    elif choice == "3":
        score = int(input("Jaki wynik chcesz usunac? "))
        for entry in scores:
            if score in entry:
                scores.remove(entry)
            else:
                print(score, "nie ma na liscie")

    #sortowanie, ustawienie wynikow malejaco
    elif choice == "4":
        scores.sort(reverse=True)
        scores = scores[:5] #pozostawianie 5 najlepszych wynikow

    #koniec programu
    elif choice == "0":
        print('BYE')

    #zabezpieczenie zlego wyboru
    else:
        print(choice ," To niewlasciwa opcja")

input("\nAby zakonczyc kliknij \"Enter\"")
