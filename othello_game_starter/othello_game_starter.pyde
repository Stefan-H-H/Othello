from game_controller import GameController
from board import Board
from player import Player
from ai import AI

HEIGHT = WIDTH = 800
SIZE = 8  # 8 x 8 board
MARGIN = HEIGHT/(SIZE + 2)
BACKGROUND_COLOR = (0, 0.4, 0)  # Green Board Background
board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
player = Player(board)
ai = AI(board)
game_controller = GameController(WIDTH, HEIGHT, player, ai, board)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)


def draw():
    background(*BACKGROUND_COLOR)
    board.display()
    game_controller.update()


def mousePressed():
    game_controller.player_make_move(mouseX - MARGIN, mouseY - MARGIN)
