import math

board = [' ' for _ in range(9)]

# Print the board
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

def winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(b[pos] == player for pos in cond) for cond in win_conditions)

def is_draw():
    return ' ' not in board

def minimax(b, depth, is_maximizing):
    if winner(b, 'O'):
        return 1
    elif winner(b, 'X'):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[move] = 'X'
        print_board()

        if winner(board, 'X'):
            print("Congratulations! You win!")
            break
        elif is_draw():
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move = best_move()
        board[ai_move] = 'O'
        print_board()

        if winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        elif is_draw():
            print("It's a draw!")
            break

play_game()
