class AI:
    """Computer/AI Opponent"""
    def __init__(self, board):
        self.color = 1  # AI color (White)
        self.board = board  # board object
        self.disk_count = self.count_disks()
        self.UP = (-1, 0)  # Direction: (row, column)
        self.DOWN = (1, 0)
        self.RIGHT = (0, 1)
        self.LEFT = (0, -1)
        self.LT_UP_D = (-1, -1)
        self.RT_UP_D = (-1, 1)
        self.LT_DN_D = (1, -1)
        self.RT_DN_D = (1, 1)
        self.directions = [self.UP, self.RT_UP_D, self.RIGHT, self.RT_DN_D,
                           self.DOWN, self.LT_DN_D, self.LEFT, self.LT_UP_D]
        self.legal_moves = {}  # Empty dictionary of legal moves
        self.no_move = False

    def make_move(self):
        """
        AI move on board
        """
        move = self.find_best_move()
        if move:
            row = move[0][0]
            column = move[0][1]
            flip_list = move[1]  # tuple list of flip disk locations
            self.board.ai_place_disk(row, column, self.color)
            for item in flip_list:
                self.flip_disk(item)
            self.disk_count = self.count_disks()
            self.legal_moves = {}  # once move has been made clear dictionary
            return True  # Player's Turn after computer

    def flip_disk(self, item):
        """
        'Flip' disk by changing disk object's
        color attribute.
        """
        self.board.board[item[0]][item[1]].color = self.color

    def lgl_moves(self):
        """
        Evaluate legal moves possible in a dictionary.
        """
        # Iterate through every position on the board
        for row in range(self.board.rows):
            for column in range(self.board.columns):
                # If board position is empty, it is a candidate
                # for possible move.
                if self.board.board[row][column] == 0:
                    # Iterate through all 8 directions from candidate
                    # position on the board.
                    for dirxn in self.directions:
                        # obtain a list of opponent disks to flip
                        # based on candidate position.
                        flip_list = self.find_flips(row, column, dirxn)
                        # Iterate through every disk to be flipped and add
                        # candidate position and the disks to be flipped in
                        # a dictionary.
                        for item in flip_list:
                            if (row, column) in self.legal_moves.keys():
                                self.legal_moves[(row, column)].add(item)
                            else:
                                self.legal_moves[(row, column)] = {item}

    def on_board(self, row, column):
        """
        Return a boolean evaluating whether the candidate disk
        placement location is on the board
        """
        return ((row >= 0 and row < self.board.rows) and
                (column >= 0 and column < self.board.columns))

    def find_flips(self, row, column, direction):
        """
        Returns a list of opposing disks to be flipped
        based on candidate disk placement
        """
        flip_list = []  # Initiate an empty list
        # traverse in the input direction
        r, c = row + direction[0], column + direction[1]
        # while the board position is on the board, not an empty
        # spot (represented by 0), and not the same color disk,
        # iterate and append a tuple representing the opposing
        # disk location to the empty list which would be flipped.
        # Keep moving in the same direction until same color is
        # reached.
        while (self.on_board(r, c) and self.board.board[r][c] != 0
               and self.board.board[r][c].color != self.color):
            flip_list.append((r, c))
            r, c = r + direction[0], c + direction[1]

        # If a same color disk is not found at the end
        # along a direction return an empty list.
        if self.on_board(r, c) and self.board.board[r][c] == 0:
            flip_list = []
            return flip_list
        # If same color disk is found along a direction at the end
        # return the list of tuples.
        if self.on_board(r, c) and self.board.board[r][c].color == self.color:
            return flip_list
        # If a same color disk is not found at the end
        # along a direction, return an empty list.
        if self.on_board(r, c) and self.board.board[r][c].color != self.color:
            flip_list = []
            return flip_list
        # If the last position evaluated is not on the board
        # return an empty list.
        if not self.on_board(r, c):
            flip_list = []
            return flip_list

    def count_disks(self):
        """
        Returns the count of the number of disks
        on the board
        """
        disk_count = 0  # Initiate count
        # Iterate throught the board
        for row in range(self.board.rows):
            for column in range(self.board.columns):
                # if location on board is empty continue to
                # next location
                if self.board.board[row][column] == 0:
                    continue
                # if location on board has a disk of matching color
                # increment the count
                elif self.board.board[row][column].color == self.color:
                    disk_count += 1
        return disk_count

    def find_best_move(self):
        """
        Returns a key-value pair of a single move
        that has a key of a tuple representing a
        location on the board, and corresponding value
        that is a list of tuples representing locations
        to be flipped on the board. Returns None if no
        moves are possible.
        """
        if len(self.legal_moves.items()) > 0:
            return sorted(self.legal_moves.items(),
                          key=lambda x: len(x[1]),
                          reverse=True)[0]
        else:
            return None  # No moves possible
