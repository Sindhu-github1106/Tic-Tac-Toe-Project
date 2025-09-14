WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def show_board(cells):
    def symbol(i):
        if cells[i] != " ":
            return cells[i]
        else:
            return str(i + 1)
    divider = "\n---+---+---\n"
    layout = [
        " " + symbol(0) + " | " + symbol(1) + " | " + symbol(2) + " ",
        " " + symbol(3) + " | " + symbol(4) + " | " + symbol(5) + " ",
        " " + symbol(6) + " | " + symbol(7) + " | " + symbol(8) + " ",
    ]
    print("\n" + divider.join(layout) + "\n")

def find_winner(cells):
    for a, b, c in WIN_LINES:
        if cells[a] != " " and cells[a] == cells[b] and cells[b] == cells[c]:
            return cells[a]
    return None

def full_board(cells):
    for c in cells:
        if c == " ":
            return False
    if find_winner(cells):
        return False
    else:
        return True

def ask_move(cells, mark):
    while True:
        move = input("Player " + mark + ", choose a position (1-9): ").strip()
        if move.lower() in ("q", "quit", "exit"):
            raise KeyboardInterrupt
        if not move.isdigit():
            print(" → Enter a number from 1 to 9.")
            continue
        pos = int(move) - 1
        if pos not in range(9):
            print(" → Invalid position.")
        else:
            if cells[pos] != " ":
                print(" → That spot is already taken.")
            else:
                return pos

def play_game():
    cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    turn = "X"
    while True:
        show_board(cells)
        try:
            idx = ask_move(cells, turn)
        except KeyboardInterrupt:
            print("\nGame stopped by user.")
            return None
        cells[idx] = turn
        winner = find_winner(cells)
        if winner:
            show_board(cells)
            print("Player " + winner + " wins!")
            return winner
        if full_board(cells):
            show_board(cells)
            print("It's a draw!")
            return "Draw"
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 = X, Player 2 = O")
    try:
        while True:
            outcome = play_game()
            if outcome is None:
                break
            again = input("Play again? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                print("Thanks for playing!")
                break
    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    main()
