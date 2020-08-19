from board import Board
from ai import AI


def test_contsructor():
    """test the constructor"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    ai = AI(board)

    assert ai.color == 1
    assert ai.board is board
    assert ai.disk_count == ai.count_disks()
    assert ai.UP == (-1, 0)
    assert ai.DOWN == (1, 0)
    assert ai.RIGHT == (0, 1)
    assert ai.LEFT == (0, -1)
    assert ai.LT_UP_D == (-1, -1)
    assert ai.RT_UP_D == (-1, 1)
    assert ai.LT_DN_D == (1, -1)
    assert ai.RT_DN_D == (1, 1)
    assert ai.directions == [ai.UP, ai.RT_UP_D, ai.RIGHT, ai.RT_DN_D,
                             ai.DOWN, ai.LT_DN_D, ai.LEFT, ai.LT_UP_D]
    assert ai.legal_moves == {}
    assert ai.no_move is False

# No test_make_move. It has graphical functionality when the AI
# makes a move and subsequenty calls to displaying placed disk object.


def test_flip_disk():
    """test the flip_disk method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    ai = AI(board)

    item = (4, 3)
    ai.flip_disk(item)
    assert ai.board.board[item[0]][item[1]].color == ai.color


def test_lgl_moves():
    """test the lgl_moves method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    TILE_SIZE = MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    ai = AI(board)

    ai.lgl_moves()
    assert ai.legal_moves == {(2, 4): {(3, 4)}, (3, 5): {(3, 4)},
                              (4, 2): {(4, 3)}, (5, 3): {(4, 3)}}


def test_on_board():
    """test the on_board method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    TILE_SIZE = MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    ai = AI(board)

    assert ai.on_board(0, 0) is True
    assert ai.on_board(0, 8) is False


def test_find_flips():
    """ test the find_flips method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    TILE_SIZE = MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    ai = AI(board)

    disk_location = (4, 2)  # row 4, column 2
    assert ai.find_flips(disk_location[0],
                         disk_location[1], ai.RIGHT) == [(4, 3)]


def test_count_disks():
    """test the count_disks method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    TILE_SIZE = MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    ai = AI(board)

    assert ai.count_disks() == 2


def test_find_best_move():
    """test the find_best_move method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    TILE_SIZE = MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    ai = AI(board)
    ai.lgl_moves()

    assert ai.find_best_move() == ((2, 4), {(3, 4)})
