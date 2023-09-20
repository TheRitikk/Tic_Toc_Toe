# Tic Toc Toe game
# Code by Ritik

def printBoard(xAxis, zAxis):
    symbols = [' ', 'X', 'O']
    board = [symbols[xAxis[i] + 2 * zAxis[i]] for i in range(9)]
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def checkWin(xAxis, zAxis):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xAxis[i] for i in win) == 3:
            return 1
        if sum(zAxis[i] for i in win) == 3:
            return 0
    return -1

xAxis = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zAxis = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def resetGame():
    global xAxis, zAxis
    xAxis = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zAxis = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def play_game():
    global xAxis, zAxis  # Declare as global to access the global variables
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")

    while True:
        player = 'X' if turn == 1 else 'O'
        printBoard(xAxis, zAxis)
        print()
        print(f"{player}'s Chance")
        try:
            value = int(input("Please enter a value: "))
            if 0 <= value < 9 and xAxis[value] + zAxis[value] == 0:
                if turn == 1:
                    xAxis[value] = 1
                else:
                    zAxis[value] = 1
            else:
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")
            continue

        cwin = checkWin(xAxis, zAxis)
        if cwin != -1:
            if cwin == 1:
                print()
                printBoard(xAxis, zAxis)
                print("X won the match")
            else:
                print()
                printBoard(xAxis, zAxis)
                print("O won the match")
            resetGame()  # Reset the game
            break
        elif all(x + z for x, z in zip(xAxis, zAxis)):
            print()
            printBoard(xAxis, zAxis)
            print("Match is a draw.")
            resetGame()  # Reset the game
            break

        turn = 1 - turn

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
