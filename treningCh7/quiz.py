# gra turniej wiedzy, odczytujaca dane z pliku tekstowego + skillcheck7_1&7_2
# struktura pliku kwiz:
# <tytul> (jedno wystapienie)
# <kategoria>
# <pytanie>
# <odp1>
# <odp2>
# <odp3>
# <odp4>
# <prawidlowa odpowiedz>
# <wyjasnienie>
# <ilosc pkt>


import sys, pickle #modul marynowania


def open_file(filename, mode):
    """Otwórz plik z pytaniami"""
    try:
        file = open(filename, mode)
    except IOError as e: #tu ma sie zamknac jak nie znajdzie pliku
        print("Nie mozna odczytac pliku ", e, "program zostanie zakonczony")
        input("Aby zakonczyc wcisnij 'ENTER'")
        sys.exit()
    else:
        return file


def highscores(filename):
    """Plik najlepszych winikow odczyt
    Przechowuje tylko 1obiekt/nadpis
    Jesli nie ma to go tworzy"""
    file = open(filename, "wb+")
    return file

def next_line(file):
    """Zwróc kolejny wiersz pliku po sformatowaniu go"""
    line = file.readline()
    line = line.replace("/", "\n")#zawijanie dlugich wierszy
    return line

def read_high(file):
    """Odczyt najlepszego wyniku"""
    try:
        high = pickle.load(file)
        print("Najlepszy gracz", high[0], "zdobyl", high[1], "punktow. Sprobuj go pobic")
    except EOFError: #tu mi sie sypalo na pustym .dat
        print("Jesteś pierwszy który w to gra")
        high = ["Null", 0]
    return high

def save_high(file, name, score):
    """Zapis najlepszego wyniku"""
    high = [name, score]
    pickle.dump(high, file)

def next_block(file):
    """zwroc kolejny blok danych z pliku kwiz
    wg struktury pliku wedruje wierszami po bloku
    pytania i zapisuje do odpowiednich struktur
    na koncu zwraca odpowiednio opakowane"""
    category = next_line(file)#nazwa kategorii
    question = next_line(file)#pytanie
    answers = [] #lista mozliwych odpowiedzi
    for i in range(4):
        answers.append(next_line(file))

    correct = next_line(file)
    if correct:#wlasciwa odpowiedz
        correct = correct[0]

    explanation = next_line(file)#wyjasnienie
    score = next_line(file)#ilosc pkt za pytanie

    return category, question, answers, correct, explanation, score


def welcome(title):
    """Przywitanie gracza i pobierz jego nazwe
    Uzycie raz na poczatku i odczyt pierwszej linii tytularnej"""
    print("\t\t Witaj w turnieju wiedzy!")
    print("\t\t", title, "\n")
    name = input("Podaj nazwe gracza")
    return name


def main():
    trivia_file = open_file("kwiz.txt", "r")#nazwa pliku z pytaniami + parametr
    high_file = highscores("highscores.dat")#najlepszy wynik
    title = next_line(trivia_file)
    name = welcome(title)
    old_high = read_high(high_file)#zapis ostatniego najwyzszego wyniku
    final_score = 0
    # pobierz pierwszy blok
    category, question, answers, correct, explanation, score = next_block(trivia_file)
    # zadaj pytanie
    while category: #dopoki jest pierwsza kategoria bloku wyswietlamy kolejne pytania
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, answers[i])
        # uzyskaj odpowiedz
        answer = input("Jaka jest twoja odpowiedz?: ")
        # sprawdz odpowiedz
        if answer == correct:
            print("Odpowiedz prawidlowa!")
            final_score += int(score)
            print("Zdobyles:", score, "pkt.")
        else:
            print("Blad")
            print(explanation)
        # pobierz kolejny blok
        category, question, answers, correct, explanation, score = next_block(trivia_file)
    trivia_file.close()
    print("To bylo ostatnie pytanie")
    print("Twoj wynik koncowy to", final_score, "pkt.")
    #sprawdzenie czy uzyskano najwyszy wynik, jesli tak to zapis do .dat i koniec
    if final_score > old_high[1]:
        save_high(high_file, name, final_score)
        print("Gratulacje, Twój wynik jest najwyższy")
    else:
        print("Niestety nie udało Ci sie pobic najwyszego wyniku")
    high_file.close()


main()
input("ENTER for end")
