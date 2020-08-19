from game_controller import GameController
from player import Player
from ai import AI
from board import Board


def test_constructor():
    """Test the constructor"""

    HEIGHT = WIDTH = 400
    SIZE = 4
    MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    player = Player(board)
    ai = AI(board)
    gc = GameController(WIDTH, HEIGHT, player, ai, board)

    assert gc.WIDTH == 400
    assert gc.HEIGHT == 400
    assert gc.player is player
    assert gc.ai is ai
    assert gc.board is board
    assert gc.human_player_wins is False
    assert gc.ai_player_wins is False
    assert gc.draw is False
    assert gc.game_over is False
    assert gc.player_disk_count == 2
    assert gc.ai_disk_count == 2
    assert gc.player_turn is True
    assert gc.timer == 120
    assert gc.game_over_timer == 120
    assert gc.game_over is False
    assert gc.DISK_TILE_RATIO == 0.9


# No test_update. It has graphical functionality.

# No test_player_make_move. It has graphical functionality when displaying
# placed disk object.

# No test_ai_make_move method. It has graphical functionality when displaying
# placed disk object.

# No test_make_moves  method. It has graphical functionality when the ai makes
# a move and subsequenty calls to displaying placed disk object.

# No test_player_make_move. It has graphical functionality when the player
# makes a move an subsequentlly call to display the disk object.

def test_check_game_over():
    """ test the check_game_over method"""

    HEIGHT = WIDTH = 400
    SIZE = 8
    MARGIN = HEIGHT/(SIZE + 2)
    board = Board(WIDTH, HEIGHT, SIZE, MARGIN)
    player = Player(board)
    ai = AI(board)
    gc = GameController(WIDTH, HEIGHT, player, ai, board)

    assert gc.board.spaces_left() == 60
    assert gc.ai.no_move is False
    assert gc.player.no_move is False


# NO test_display_ai_turn. It has graphical functionality.

# No test_display_player_turn. It has graphical functionality.

# No test_input. It has graphical functionality.

# No test_scoreboard. It has graphical functionality.
