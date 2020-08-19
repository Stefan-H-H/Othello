import re
import os


class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, HEIGHT, player, ai, board):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.player = player  # Player object
        self.ai = ai  # AI object
        self.board = board  # Board object
        self.human_player_wins = False  # Black disks (Player)
        self.ai_player_wins = False  # White disks (AI)
        self.draw = False
        self.game_over = False
        self.player_disk_count = 2
        self.ai_disk_count = 2
        self.player_turn = True
        self.timer = 120  # 2 second delay (120/60fps)
        self.game_over_timer = 120  # 2 second delay
        self.game_over = False
        self.DISK_TILE_RATIO = self.player.DISK_TILE_RATIO

    def update(self):
        """Carries out necessary actions if a player wins"""

        self.make_moves()  # display ai and player moves
        self.scoreboard()
        self.check_game_over()  # check that game is over

        if self.human_player_wins:
            fill(1, 1, 1, 0.7)  # Opaque rectangle to overlay text
            rectMode(CENTER)  # Center Align rectangle
            rect_width = rect_height = self.board.TILE_SIZE * 2
            rect(self.WIDTH//2, self.HEIGHT//2, rect_width, rect_height)
            fill(0, 0, 1)  # Blue Text
            textAlign(CENTER, CENTER)  # Center Align Text
            textSize(20)  # Initial text size
            message = ("GAME OVER!\n BLACK WINS!\n"
                       + str(self.player_disk_count) + " - "
                       + str(self.ai_disk_count))
            # calculate minimum text size to fit rectangle width
            min_txt_w = (20 / textWidth(message)) * rect_width
            # calculate minimum text size to fit rectangle height
            min_txt_h = (20 / (textAscent() + textDescent())) * rect_height
            # set text size to fit rectangle box
            textSize(min(min_txt_w, min_txt_h))
            # display text message
            text(message, self.WIDTH//2, self.HEIGHT//2)
        if self.ai_player_wins:
            fill(1, 1, 1, 0.7)
            rectMode(CENTER)
            rect_width = rect_height = self.board.TILE_SIZE * 2
            rect_height
            rect(self.WIDTH//2, self.HEIGHT//2, rect_width, rect_height)
            fill(0, 0, 1)
            textAlign(CENTER, CENTER)  # Center Align Text
            textSize(20)  # Initial text size
            message = ("GAME OVER!\n WHITE WINS!\n"
                       + str(self.ai_disk_count) + " - "
                       + str(self.player_disk_count))
            # calculate minimum text size to fit rectangle width
            min_txt_w = (20 / textWidth(message)) * rect_width
            # calculate minimum text size to fit rectangle height
            min_txt_h = (20 / (textAscent() + textDescent())) * rect_height
            # set text size to fit rectangle box
            textSize(min(min_txt_w, min_txt_h))
            # display text message
            text(message, self.WIDTH//2, self.HEIGHT//2)
        if self.draw:
            fill(1, 1, 1, 0.7)
            rectMode(CENTER)
            rect_width = rect_height = self.board.TILE_SIZE * 2
            rect(self.WIDTH//2, self.HEIGHT//2, rect_width, rect_height)
            fill(0, 0, 1)
            textAlign(CENTER, CENTER)
            textSize(20)  # Initial text size
            message = ("GAME OVER!\n TIE GAME!\n"
                       + str(self.player_disk_count) + " - "
                       + str(self.ai_disk_count))
            # calculate minimum text size to fit rectangle width
            min_txt_w = (20 / textWidth(message)) * rect_width
            # calculate minimum text size to fit rectangle height
            min_txt_h = (20 / (textAscent() + textDescent())) * rect_height
            # set text size to fit rectangle box
            textSize(min(min_txt_w, min_txt_h))
            # display text message
            text(message, self.WIDTH//2, self.HEIGHT//2)

        # Prompt user to input name to record new score
        # after game_over_timer runs out
        if self.game_over:
            self.game_over_timer -= 1
            if self.game_over_timer == 0:
                self.score()

    def player_make_move(self, mouse_x, mouse_y):
        """Places player disk on the board on mouse click"""
        if self.player_turn:
            # player_turn changes to False only if a legal move is made or a
            # move can't be made
            self.player_turn = self.player.make_move(mouse_x, mouse_y)
            # update ai disk count after move
            self.ai.disk_count = self.ai.count_disks()

    def ai_make_move(self):
        """AI makes move and/or changes turn as necessary"""

        if self.player_turn is False:
            self.ai.lgl_moves()  # Determine computer's legal moves
            if len(self.ai.legal_moves.items()) == 0:  # if ai can't make moves
                self.ai.no_move = True
                self.player_turn = True
            if self.player_turn is False:  # If AI dictionary has moves
                # player_turn changes to True a legal move is made
                self.player_turn = self.ai.make_move()
                # update player disk count after move
                self.player.disk_count = self.player.count_disks()
            # Evaluate if player has possible moves before mouse clicking
            if self.player_turn:
                self.player.lgl_moves()
                # if player can't make moves
                if len(self.player.legal_moves.items()) == 0:
                    self.player.no_move = True
                    self.player_turn = False

    def make_moves(self):
        """
        Controls AI turn based on Timer and displays whose
        turn it is to make a move.
        """
        # AI makes move when timer is at 0.
        if self.player_turn is False and self.timer == 0:
            self.ai_make_move()  # AI makes move
            self.timer = 120  # Reset Timer
        # If it' not players turn countdown timer
        # and display that it's AI's turn
        # before AI can make move
        elif self.player_turn is False:
            self.timer -= 1
            self.display_ai_turn()
        # Display player's turn when player's turn
        elif self.player_turn:
            self.display_player_turn()

    def check_game_over(self):
        """Checks if the game is over"""
        # Check if game is over
        if ((self.ai.no_move and self.player.no_move) or
           (self.board.spaces_left() == 0)):
            if self.player.disk_count > self.ai.disk_count:  # Human wins
                self.player_disk_count = self.player.disk_count
                self.ai_disk_count = self.ai.disk_count
                self.human_player_wins = True
            elif self.player.disk_count < self.ai.disk_count:  # Computer wins
                self.ai_disk_count = self.ai.disk_count
                self.player_disk_count = self.player.disk_count
                self.ai_player_wins = True
            else:  # Tie Game
                self.player_disk_count = self.player.disk_count
                self.ai_disk_count = self.ai.disk_count
                self.draw = True
            self.game_over = True

    def display_ai_turn(self):
        """Display that it is the AI's turn on screen"""
        textSize(self.board.MARGIN//2)
        message = ("Computer's Turn")
        fill(0, 0, 1)
        textAlign(CENTER, BOTTOM)
        text(message, self.WIDTH//2, self.board.MARGIN)

    def display_player_turn(self):
        """Display that it is the player's turn on screen"""
        self.player.display_possible_moves()
        textSize(self.board.MARGIN//2)
        message = ("Your Turn")
        fill(0, 0, 1)
        textAlign(CENTER, BOTTOM)
        text(message, self.WIDTH//2, self.board.MARGIN)

    def input(self, message='New Score. Please Provide Your Name:'):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def score(self):
        """ store new player score in a .txt file"""
        try:
            new_name = self.input().replace(" ", "_")
            new_score = new_name + " " + str(self.player_disk_count) + "\n"
            filename = "scores.txt"
            # if file already exists.
            if os.path.exists(filename):
                f = open(filename, "r")
                contents = f.read()
                string_score_list = re.findall(r'(\s[\d]+)', contents)
                integer_score_list = [int(score) for score
                                      in string_score_list]
                f.close()
                f = open(filename, "w")
                # check existing file is not empty
                if len(integer_score_list) > 0:
                    if self.player_disk_count >= max(integer_score_list):
                        f.write(new_score)
                        f.write(contents)
                    else:
                        f.write(contents)
                        f.write(new_score)
                else:
                    f.write(new_score)
            # If file doesn't exist write file
            else:
                f = open(filename, "w")
                f.write(new_score)
            exit()  # Exit program once score has been input
        except AttributeError:  # If player hits cancel and doesn't enter name
            exit()  # Exit program once prompt name prompt is closed/canceled.
            return

    def scoreboard(self):
        """Method that displays the active disk counts for both colors"""
        self.player_disk_count = self.player.disk_count
        self.ai_disk_count = self.ai.disk_count
        textSize((self.DISK_TILE_RATIO * self.board.TILE_SIZE)//2)
        text_height = (textAscent() + textDescent())//2
        textAlign(CENTER, BOTTOM)

        # Player score
        # Player Disk drawing
        fill(self.player.color)
        strokeWeight(0)
        ellipse(self.board.MARGIN//2,
                self.HEIGHT//2,
                self.DISK_TILE_RATIO * self.board.TILE_SIZE,
                self.DISK_TILE_RATIO * self.board.TILE_SIZE)
        # Player's Disk Count
        fill(1)
        message = (str(self.player_disk_count))
        text(message, self.board.MARGIN//2,
             self.HEIGHT//2 + text_height)

        # AI score
        # AI Disk Drawing
        fill(self.ai.color)
        strokeWeight(0)
        ellipse(self.WIDTH - (self.board.MARGIN//2),
                self.HEIGHT//2,
                self.DISK_TILE_RATIO * self.board.TILE_SIZE,
                self.DISK_TILE_RATIO * self.board.TILE_SIZE)
        # AI Disk Count
        fill(0)
        message = (str(self.ai_disk_count))
        text(message, self.WIDTH - (self.board.MARGIN//2),
             self.HEIGHT//2 + text_height)
