from disk import Disk


def test_contsructor():
    """test the constructor"""

    disk = Disk(0, 1, 1, 80, 80)
    assert disk.column == 1
    assert disk.row == 0
    assert disk.color == 1
    assert disk.tile_size == 80
    assert disk.margin == 80
    assert disk.DISK_TILE_RATIO == 0.9


def test_repr():
    disk = Disk(0, 1, 1, 80, 80)
    assert repr(disk) == ("Disk(row=0, column=1, color=1,"
                          " tile_size=80, margin=80)")


# No test_display. It has graphical functionality to display
# the disk ellipse.
