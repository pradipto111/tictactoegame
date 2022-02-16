import copy

board = [['X',' ',' '], [' ',' ',' '],[' ',' ',' ']]
turn = True
winner = None
game_over = False
mode = None

def check_winner(board):
    #HORIZONTAL:
    if board[0][0] == board[0][1] == board[0][2]!= ' ':
        return True, board[0][0]
    if board[1][0] == board[1][1] == board[1][2]!= ' ':
        return True, board[1][0]
    if board[2][0] == board[2][1] == board[2][2]!= ' ':
        return True, board[2][0]

    #VERTICAL
    if board[0][0] == board[1][0] == board[2][0]!= ' ':
        return True, board[0][0]
    if board[0][1] == board[1][1] == board[2][1]!= ' ':
        return True, board[0][1]
    if board[0][2] == board[1][2] == board[2][2]!= ' ':
        return True, board[0][2]
    
    #DIAGONAL
    if board[0][0] == board[1][1] == board[2][2]!= ' ':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0]!= ' ':
        return True, board[0][2]

    draw = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                draw = False
    
    if not draw:
        return False, None
    return True, 'XO'

def score(board, turn):
    game_over, winner = check_winner(board)
    if game_over:
        if winner == 'X':
            return -1
        if winner == 'O':
            return 1
        if winner == 'XO':
            return 0
    if turn:
        c = 'X'
    else:
        c = 'O'    
    game_boards = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                game_boards.append(board.copy())
                game_boards[-1][i][j] = c
    scores = []
    for game_board in game_boards:
        print(game_board)
        scores.append(score(game_board, switch(turn)))
    
    if turn == computer:
        return min(scores)
    return max(scores)



board1 = board
game_boards = []
for i in range(3):
    for j in range(3):
        if board1[i][j] == ' ':
            board1[i][j] = 'O'
            game_boards.append(board1.copy())
            board1[i][j] = ' '
scores = []
#for game_board in game_boards:
#    scores.append(score(game_board, not turn))
        
#index = scores.index(max(scores))
#board = game_boards[index]
board = [['X','X',' '], ['O',' ','O'],['X','O','O']]
#print(score(board, True))

a = [['X','X',' '], ['O',' ','O'],['X','O','O']]
b = []
b.append(copy.deepcopy(a))
b[-1][0][2] = 'X'
print(b)
print(a)