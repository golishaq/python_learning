# gra w kolko i krzyzyk

# global const
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def instructions():
    """Wyświetl instrukcję gry."""
    print(
        """
        Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim jest
        gra 'Kółko i krzyżyk'. Będzie to ostateczna rozgrywka między Twoim
        ludzkim mózgiem a moim krzemowym procesorem.

        Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
        Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:

                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8

        Przygotuj się, Człowieku.  Ostateczna batalia niebawem się rozpocznie. \n
        """
    )


def ask_yes_no(question):
    """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Popros o podanie liczby z odpowiedniego zakresu"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Ustal czy zaczyna gracz czy CPU"""
    go_first = ask_yes_no("Czy chcesz miec prawo do pierwszego ruchu? (t/n)")
    if go_first == "t":
        print("Zaczynasz")
        human = X
        computer = O
    else:
        print("CPU zaczyna")
        human = O
        computer = X
    return human, computer


def new_board():
    """Utworz nowa plansze gry"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Wyswietla plansze gry na ekranie"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Utworz liste prawidlowych ruchow"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Ustal zwyciezce gry"""
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None


def human_move(board, human):
    """Odczytaj ruch czlowieka"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Jaki bedzie twoj ruch(0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("To pole jest juz zajete, wybierz inne")
    return move


def computer_move(board, computer, human):
    """Wykonaj ruch CPU"""
    # tworzenei kopii roboczej glownej listy
    board = board[:]
    # najlepsze pozycje wg kolejnosci
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Wybieram pole nr", end=" ")
    # jesli CPU moze wygrac wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # ten ruch zostal sprawdzony, wycofaj go
        board[move] = EMPTY
    # jesli czlowiek moze wygrac, zablokuj go
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # ten ruch zostal sprawdzony, wycofaj go
        board[move] = EMPTY
    # poniewaz nie moze wygrac, wybierz najlepsze wolne pole
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Zmien wykonawce ruchu"""
    if turn == X:
        return O
    if turn == O:
        return X


def congrat_winner(the_winner):
    """Gratulacje dla zwyciezcy"""
    if the_winner != TIE:
        print(the_winner, "jest zwyciezca")
    else:
        print("Remis!")


def main():
    instructions()
    computer, human = pieces()
    turn = O
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner)


main()
print("\n Aby zakonczyc wcisnij 'ENTER'")
