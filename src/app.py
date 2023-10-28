import random
from flask import Flask, render_template, request
from collections import deque
import ast
import re

app = Flask(__name__)  # Creating a new flask application with name 'app'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/play/", methods=['GET', 'POST'])
def play():
    n = 6
    m = 3
    board, colors = initiatingColors(n, m)
    colored_board, origin = tiles(n, colors, board)
    game = Game(n, m)
    new_game = 0

    if not game.isBoardSolved(colored_board):
        connected_path_indx = game.is_connected_to_origin(origin, colored_board)
        connected_path_indx = list(connected_path_indx)
    return render_template("play.html", 
                           board=colored_board, 
                           colors=colors, 
                           connected_path_indx=connected_path_indx, 
                           new_game=new_game)


@app.route("/game/", methods=['GET', 'POST'])
def play_game():
    n = 6
    m = 3
    print('')
    game = Game(n, m)
    if request.method == 'POST' and request.form.get('chosen_color'):
        chosen_color = str(request.form.get('chosen_color'))
        connected_path_indx = list(request.form.getlist('connected_path_indx'))
        colored_board = request.form.getlist('colored_board')
        colors = []
        for row in colored_board:
            new_row = re.split(r"[',\[\]\s]+", str(row))
            for element in range(1, 7):
                colors.append(new_row[element])

        colored_board = [ast.literal_eval(elem) for elem in colored_board]
        connected_path_indx = [ast.literal_eval(elem) for elem in connected_path_indx]
        new_game = 1
        print('chosen_color', chosen_color)
        colored_board = flood_fill(connected_path_indx, chosen_color, colored_board)
        chosen_color = None
        origin = colored_board[0][0]
        connected_path_indx = game.is_connected_to_origin(origin, colored_board)
        if not game.isBoardSolved(colored_board):
            return render_template("game.html", 
                                   colored_board=colored_board, 
                                   colors=colors, 
                                   connected_path_indx=connected_path_indx, 
                                   new_game=new_game)
        else:
            print("You solved the Board!!")
    else:
        print("You solved the Board!!")
    return render_template("game.html", 
                           colored_board=colored_board, 
                           colors=colors, 
                           connected_path_indx=connected_path_indx, 
                           new_game=new_game)


def initiatingColors(n, m):
    colors = []
    # define all possible color values
    # color_values = [hex(i)[2:].zfill(2) for i in range(256)]
    unique_colors = ['turquoise', 'plum', 'olivedrab']
    # ['#' + ''.join(random.sample(color_values, m)) for _ in range(m)]
    # Create an empty board
    board = [[None for _ in range(n)] for _ in range(n)]
    # Assign the colors randomly to the cells
    colors = [random.choice(unique_colors) for _ in range(n*n)]
    return board, colors


def tiles(n, colors, board):
    # create a new array
    dct = {}
    for i, j in [(i, j) for i in range(n) for j in range(n)]:
        idx = (i * n) + j
        dct[(i, j)] = str(colors[idx])
    for key, value in dct.items():
        x, y = key
        board[x][y] = value
        origin = board[0][0]
    return board, origin


def flood_fill(from_color_indx, chosen_color, board):
    for elem in from_color_indx:
        board[int(elem[0])][int(elem[1])] = chosen_color
    return board


class Game:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.moves = []

    def isBoardSolved(self, colored_board):
        """
        Check if the board is already solved.
        """
        if all(colored_board[i][j] == colored_board[0][0] for i in range(len(colored_board)) 
               for j in range(len(colored_board[0]))):
            print("You solved the Board!!")
            return True
        else:
            print("Begin your Quest")
            return False

    def is_connected_to_origin(self, origin, board):
        """
        Check if the tile at (i, j) is connected to the origin tile.
        """
        # Define a set to keep track of visited tiles
        visited = set()
        connected_path = [['' for j in range(len(board[i]))] for i in range(len(board))]

        queue = deque([(0, 0)])
        while queue:
            i, j = queue.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if board[i][j] == origin:
                connected_path[i][j] = board[i][j]
                if i > 0:
                    queue.append((i-1, j))
                if i < self.n-1:
                    queue.append((i+1, j))
                if j > 0:
                    queue.append((i, j-1))
                if j < self.n-1:
                    queue.append((i, j+1))

        # Get connected path with non-empty indexes
        connected_path_indx = []
        for i in range(len(connected_path)):
            for j in range(len(connected_path[i])):
                if connected_path[i][j] != '':
                    connected_path_indx.append((i, j))
        return connected_path_indx
