
class Disk:
    """A disk"""
    def __init__(self, row, column, color, tile_size, margin):
        self.column = column
        self.row = row
        self.color = color
        self.tile_size = tile_size
        self.margin = margin
        self.DISK_TILE_RATIO = 0.9

    def __repr__(self):
        return ("Disk(row={}, column={}, color={}, tile_size={},"
                " margin={})".format(self.row, self.column,
                                     self.color, self.tile_size,
                                     self.margin))

    def display(self):
        """Display disk"""
        fill(self.color)
        ellipse(self.margin + self.column * self.tile_size + self.tile_size//2,
                self.margin + self.row * self.tile_size + self.tile_size//2,
                self.DISK_TILE_RATIO * self.tile_size,
                self.DISK_TILE_RATIO * self.tile_size)
