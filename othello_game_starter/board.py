from disk import Disk


class Board:
    """Draws the board and handles interaction between users"""
    def __init__(self, WIDTH, HEIGHT, SIZE, MARGIN):
        self.WIDTH = WIDTH - 2 * MARGIN  # Width of board
        self.HEIGHT = HEIGHT - 2 * MARGIN  # Height of board
        self.MARGIN = MARGIN  # Margin around board
        self.TILE_SIZE = WIDTH//(SIZE + 2)  # Size of tile
        self.rows = self.columns = SIZE
        self.board = self.init_board()  # Initialize game board

    def place_disk(self, mouse_x, mouse_y, color):
        """ Places disk on the board on mouse click"""
        column = mouse_x//self.TILE_SIZE  # column based on mouse x position
        row = mouse_y//self.TILE_SIZE  # row based on mouse y position
        # If location on board is filled, remains player turn
        if self.board[row][column] != 0:
            return
        else:
            # fill location with a Disk object
            self.board[row][column] = Disk(row, column, color,
                                           self.TILE_SIZE, self.MARGIN)

        self.update()  # update board

    def update(self):
        """Make necessary per-frame updates"""
        # Iterate through each location on board
        for row in range(self.rows):
            for column in range(self.columns):
                # if location is empty continue to
                # next location
                if self.board[row][column] == 0:
                    continue
                else:
                    # If board location is a disk,
                    # display it
                    self.board[row][column].display()

    def display(self):
        """Display the board"""
        self.update()  # update the board

        # Draw the vertical board lines
        for i in range(self.columns + 1):
            strokeWeight(4)
            line(self.TILE_SIZE * (i+1), self.MARGIN,
                 self.TILE_SIZE * (i+1),
                 self.TILE_SIZE * (self.columns + 1))

        # Draw horizontal board lines
        for i in range(self.rows + 1):
            strokeWeight(4)
            line(self.MARGIN, self.TILE_SIZE * (i+1),
                 self.TILE_SIZE * (self.rows + 1),
                 self.TILE_SIZE * (i+1))

    def init_board(self):
        """
        Initialize board with 4 middle disks pieces.
        """
        board = [[0] * self.columns for i in range(self.rows)]
        start_col = self.columns//2 - 1
        start_row = self.rows//2 - 1
        end_col = self.columns//2
        end_row = self.rows//2
        # White Upper left middle disk
        board[start_row][start_col] = Disk(start_row, start_col, 1,
                                           self.TILE_SIZE, self.MARGIN)
        # Black Lower right left middle disk
        board[start_row][end_col] = Disk(start_row, end_col, 0,
                                         self.TILE_SIZE, self.MARGIN)
        # Black Lower left middle disk
        board[end_row][start_col] = Disk(end_row, start_col, 0,
                                         self.TILE_SIZE, self.MARGIN)
        # White Lower right middle disk
        board[end_row][end_col] = Disk(end_row, end_col, 1,
                                       self.TILE_SIZE, self.MARGIN)
        return board

    def spaces_left(self):
        """Returns the number of remaing spaces on the board"""
        spaces = 0  # Initialize counter
        # Iterate through each location on board
        for row in range(self.rows):
            for column in range(self.columns):
                # If board location is empty
                # increment count
                if self.board[row][column] == 0:
                    spaces += 1
        return spaces

    def ai_place_disk(self, row, column, color):
        """Computer places disk on the board"""
        self.board[row][column] = Disk(row, column, color,
                                       self.TILE_SIZE, self.MARGIN)
        self.update()  # update board
