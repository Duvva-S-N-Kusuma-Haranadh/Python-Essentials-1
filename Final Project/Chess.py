from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status and prints it out to the console.
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print("|", end = "")
        for j in range(3):
            print("  ",board[i][j],"  |", end = "")
        print("\n|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, checks the input, and updates the board according to the user's decision.
    turn = 0
    while True:
        if turn == 9 and draw_move(board):
            print("It's a draw!")
            break
        if turn % 2 == 0:
            move = randrange(1, 10)
            sign = 'X'
        else:
            move = int(input("Enter your move: "))
            sign = 'O'
        if move in make_list_of_free_fields(board):
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        board[i][j] = sign
                        display_board(board)
                        if victory_for(board, 'X'):
                            print("Computer Wins!")
                            return
                        if victory_for(board, 'O'):
                            print("You Win!")
                            return
                        turn += 1
        else:
            continue

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in board:
        for j in i:
            if isinstance(j, int):
                free_fields.append(j)
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    if victory_for(board, 'X') == victory_for(board, 'O') == False:
        return True
    return False

board = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
enter_move(board)
