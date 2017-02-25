#gra turniej wiedzy, odczytujaca dane z pliku tekstowego
import sys

def open_file(filename,mode):
    """Otwórz plik"""
    try:
        file = open(filename, mode)
    except IOError as e:
        print("Nie mozna odczytac pliku ", e, "program zostanie zakonczony" )
        input("Aby zakonczyc wcisnij 'ENTER'")
        sys.exit()
    else:
        return file

def next_line(file):
    """Zwróc kolejny wiersz pliku po sformatowaniu go"""
    line = file.readline()
    line = line.replace("/", "\n")
    return line

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

    return category, question, answers, correct, explanation

def welcome(title):
    """Przywitanie gracza i pobierz jego nazwe"""
    print("\t\t Witaj w turnieju wiedzy!")
    print("\t\t",title,"\n")

def main():
    trivia_file = open_file("kwiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    #pobierz pierwszy blok
    category, question, answers, correct, explanation = next_block(trivia_file)
    #zadaj pytanie
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t", i+1, answers[i])
        #uzyskaj odpowiedz
        answer = input("Jaka jest twoja odpowiedz?: ")
        #sprawdz odpowiedz
        if answer == correct:
            print("Odpowiedz prawidlowa!")
            score += 1
        else:
            print("Blad")
            print(explanation)
        print("Wynik:", score, "\n\n")
        #pobierz kolejny blok
        category, question, answers, correct, explanation = next_block(trivia_file)
    trivia_file.close()
    print("To bylo ostatnie pytanie")
    print("Twoj wynik koncowy to", score)

main()
input("ENTER for end")


main()
