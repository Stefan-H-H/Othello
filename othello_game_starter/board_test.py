from disk import Disk
from board import Board


def test_contsructor():
    """test the constructor"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)

    assert board.WIDTH == 320  # Width of board
    assert board.HEIGHT == 320  # Height of board
    assert board.MARGIN == 40  # Margin around board
    assert board.TILE_SIZE == 40  # Size of tile
    assert board.rows == 8
    assert board.columns == 8

    start_col = board.columns//2 - 1
    start_row = board.rows//2 - 1
    end_col = board.columns//2
    end_row = board.rows//2
    assert board.board[start_row][start_col] != 0
    assert board.board[start_row][end_col] != 0
    assert board.board[end_row][start_col] != 0
    assert board.board[end_row][end_col] != 0

# No test_place_disk. It has graphical functionality to update
# update the board.

# No test_update. It has graphical functionality to update
# the board.

# No test_display. It has graphical functionality to display
# the board.


def test_init_board():

    HEIGHT = WIDTH = 400
    SIZE = 8
    MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)

    start_col = board.columns//2 - 1
    start_row = board.rows//2 - 1
    end_col = board.columns//2
    end_row = board.rows//2
    assert board.board[start_row][start_col] != 0
    assert board.board[start_row][end_col] != 0
    assert board.board[end_row][start_col] != 0
    assert board.board[end_row][end_col] != 0


def test_spaces_left():
    HEIGHT = WIDTH = 400
    SIZE = 8
    MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)

    assert board.spaces_left() == 60

# No test_ai_place_disk. It has graphical functionality to update the board.
