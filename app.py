from flask import Flask, render_template, request, redirect
import copy, random

app = Flask(__name__)
app.debug = True

board = [[' ',' ',' '], [' ',' ',' '],[' ',' ',' ']]
turn = 'X'
winner = None
game_over = False
mode = None
computer = 'O'
player = 'X'

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
        if winner == computer:
            return 1
        if winner == player:
            return -1
        if winner == 'XO':
            return 0
 
    game_boards = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                game_boards.append(copy.deepcopy(board))
                game_boards[-1][i][j] = turn
    
    scores = []
    for game_board in game_boards:
        scores.append(score(game_board, switch(turn)))
    
    if turn == computer:
        return max(scores)
    return min(scores)


def switch(turn):
    if turn == 'X':
        return 'O'
    return 'X'    



@app.route("/", methods=["GET"])
def index():
    global board, turn, game_over, winner, mode, computer, player
    board = [[' ',' ',' '], [' ',' ',' '],[' ',' ',' ']]
    turn = 'X'
    winner = None
    game_over = False
    mode = None
    computer = 'O'
    player = 'X'
    return render_template('index.html')

@app.route("/mode", methods=["POST"])
def mode():
    global board, turn, game_over, winner, mode, computer, player
    mode = int(request.form.get("mode"))
    if mode == 0:
        return render_template('board.html', board = board, turn = turn)
    return render_template('mode.html')

@app.route("/newgame", methods=["POST"])
def newgame():
    global board, turn, game_over, winner, mode, computer, player
    player = (request.form.get("player"))
    if player == 'O':
        computer = 'X'
        seq = [0,2,6,8]
        choice = random.choice(seq)
        i = int(choice/3)
        j = choice%3
        board[i][j] = 'X'
        turn = switch(turn)
    return render_template('board.html', board = board, turn = turn)

@app.route("/update_board", methods=["POST"])
def update_board():
    global board, turn, game_over, winner, mode, computer, player
    value = None
    for key in request.form:
        if key.startswith('c.'):
            value = key.partition('.')[-1]
    i = int(value[0])
    j = int(value[1])
    print(i,j)
    if not board[i][j] == ' ':
        return render_template('board.html', board = board, turn = turn)
    
    board[i][j] = turn
    
    game_over, winner = check_winner(board)
    if game_over:
        return render_template('game_over.html', board = board, winner = winner)

    if mode == 1:
        turn = switch(turn)
        game_boards = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    game_boards.append(copy.deepcopy(board))
                    game_boards[-1][i][j] = turn
        scores = []
        for game_board in game_boards:
            scores.append(score(game_board, switch(turn)))
        
        index = scores.index(max(scores))
        board = game_boards[index]
    
    turn = switch(turn)
    game_over, winner = check_winner(board)

    if not game_over:
        return render_template('board.html', board = board, turn = turn)
    print(board)
    return render_template('game_over.html', board = board, winner = winner)