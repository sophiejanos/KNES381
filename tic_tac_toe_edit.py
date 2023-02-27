def print_rules():
    print("Welcome to tic-tac-toe!")
    print("How to play:")
    print("Stars and hearts will take turns putting their symbol on the board.")
    print("The first player to get 3 of their marks in a row, column or diagonally wins!")
  
    agree = input("Does that sound good? (Y/N): ")
    if agree.lower() == "n":
        print("RUDE!")

    else:
        print("AWESOME!")

# define the board  
board = [["_" for i in range(3)] for j in range(3)]

# define the player's move
def make_move(board, player, row, col):
    if board[row][col] != "_":
        print("OCCUPIED!.")
        return False
    else:
        board[row][col] = player
        return True

# define the function to check for a winner
def check_winner(board):
    # check rows
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "_":
            return board[row][0]
            
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "_":
            return board[0][col]
            
    # check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
        return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
        return board[2][0]
        
    # if there is no winner, return None
    return None

# define the function to check if the game is a draw
def check_draw(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == "_":
                return False
    return True

# define the function to play the game
def play_game():
    print_rules()
    #initialize the game
    player = "⭑"
    winner = None
    draw = False

    # loop until the game is over
    while not winner and not draw:
        # print the current board
        for row in board:
            print(" ".join(row), end="\n")
        
        #get the player's to move
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
        
        # make the move
        make_move(board, player, row, col)

        # check for a winner
        winner = check_winner(board)

        # check for a draw
        draw = check_draw(board)

        # switch players
        if player == "⭑":
            player = "♡"
        else:
            player = "⭑"

    # print the final board
    for row in board:
        print(" ".join(row), end="\n")

    # print the result of the game
    if winner:
        print(f" YAY!! Player {winner} is victorious!")
    else:
        print("The game is a draw.")
        
# play the game
play_game()
