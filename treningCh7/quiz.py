# gra turniej wiedzy, odczytujaca dane z pliku tekstowego
import sys, pickle


def open_file(filename, mode):
    """Otwórz plik"""
    try:
        file = open(filename, mode)
    except IOError as e:
        print("Nie mozna odczytac pliku ", e, "program zostanie zakonczony")
        input("Aby zakonczyc wcisnij 'ENTER'")
        sys.exit()
    else:
        return file


def highscores(filename):
    """Plik najlepszych winikow odczyt"""
    file = open(filename, "wb+")
    return file

def next_line(file):
    """Zwróc kolejny wiersz pliku po sformatowaniu go"""
    line = file.readline()
    line = line.replace("/", "\n")
    return line

def read_high(file):
    """Odczyt najlepszego wyniku"""
    try:
        high = pickle.load(file)
        print("Najlepszy gracz", high[0], "zdobyl", high[1], "punktow. Sprobuj go pobic")
    except EOFError:
        print("Jesteś pierwszy który w to gra")
        high = ["Null", 0]
    return high

def save_high(file, name, score):
    """Zapis najlepszego wyniku"""
    high = [name, score]
    pickle.dump(high, file)

def next_block(file):
    """zwroc kolejny blok danych z pliku kwiz"""
    category = next_line(file)
    question = next_line(file)
    answers = []
    for i in range(4):
        answers.append(next_line(file))

    correct = next_line(file)
    if correct:
        correct = correct[0]

    explanation = next_line(file)
    score = next_line(file)

    return category, question, answers, correct, explanation, score


def welcome(title):
    """Przywitanie gracza i pobierz jego nazwe"""
    print("\t\t Witaj w turnieju wiedzy!")
    print("\t\t", title, "\n")
    name = input("Podaj nazwe gracza")
    return name


def main():
    trivia_file = open_file("kwiz.txt", "r")
    high_file = highscores("highscores.dat")
    title = next_line(trivia_file)
    name = welcome(title)
    old_high = read_high(high_file)
    final_score = 0
    # pobierz pierwszy blok
    category, question, answers, correct, explanation, score = next_block(trivia_file)
    # zadaj pytanie
    while category:
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
    if final_score > old_high[1]:
        save_high(high_file, name, final_score)
        print("Gratulacje, Twój wynik jest najwyższy")
    else:
        print("Niestety nie udało Ci sie pobic najwyszego wyniku")
    high_file.close()


main()
input("ENTER for end")
