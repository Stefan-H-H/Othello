from board import Board
from player import Player


def test_contsructor():
    """test the constructor"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    player = Player(board)

    assert player.color == 0
    assert player.board is board
    assert player.disk_count == player.count_disks()
    assert player.UP == (-1, 0)
    assert player.DOWN == (1, 0)
    assert player.RIGHT == (0, 1)
    assert player.LEFT == (0, -1)
    assert player.LT_UP_D == (-1, -1)
    assert player.RT_UP_D == (-1, 1)
    assert player.LT_DN_D == (1, -1)
    assert player.RT_DN_D == (1, 1)
    assert player.directions == [player.UP, player.RT_UP_D, player.RIGHT,
                                 player.RT_DN_D, player.DOWN, player.LT_DN_D,
                                 player.LEFT, player.LT_UP_D]
    assert player.legal_moves == {(2, 3): {(3, 3)}, (3, 2): {(3, 3)},
                                  (4, 5): {(4, 4)}, (5, 4): {(4, 4)}}
    assert player.no_move is False
    assert player.DISK_TILE_RATIO == 0.9

# No test_make_move. It has graphical functionality when the player
# makes a move and subsequenty calls to displaying placed disk object.


def test_flip_disk():
    """test the flip_disk method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    player = Player(board)

    item = (3, 3)
    player.flip_disk(item)
    assert player.board.board[item[0]][item[1]].color == player.color


def test_lgl_moves():
    """test the lgl_moves method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    TILE_SIZE = MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    player = Player(board)
    player.legal_moves = {}  # clear dictionary
    player.lgl_moves()
    assert player.legal_moves == {(2, 3): {(3, 3)}, (3, 2): {(3, 3)},
                                  (4, 5): {(4, 4)}, (5, 4): {(4, 4)}}


def test_on_board():
    """test the on_board method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    TILE_SIZE = MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    player = Player(board)

    assert player.on_board(0, 0) is True
    assert player.on_board(0, 8) is False


def test_find_flips():
    """ test the find_flips method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    TILE_SIZE = MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    player = Player(board)

    disk_location = (2, 3)  # row 2, column 3
    assert player.find_flips(disk_location[0],
                             disk_location[1],
                             player.DOWN) == [(3, 3)]


def test_count_disks():
    """test the count_disks method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    TILE_SIZE = MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    player = Player(board)

    assert player.count_disks() == 2

# No test_display_possible_moves. It has graphical functionality by calling
# possible_move to draw elipses for every possible move.

# No test_possible_move. It has graphical functionality to draw an elispe.
