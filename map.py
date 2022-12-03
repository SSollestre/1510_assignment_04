"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""
import sys


class Map:
    """
    This simple Map has a height, width, player_column coordinate, player_row coordinate, and a list of available paths.
    """

    def __init__(self, height: int, width: int, player_column: int, player_row: int, paths: list):
        """
        Initialize height, width, player_column, player_row, and paths.

        :param height: height of map as an int >= 0
        :param width: width of map as an int >= 0
        :param player_column: column player starts on as an int >= 0
        :param player_row: row player starts on as an int >= 0
        :param paths: the paths the player can take as a list of tuples
        """
        if height < 0:
            raise ValueError("weight cannot be less than 0")
        else:
            self.height = height

        if width < 0:
            raise ValueError("width cannot be less than 0")
        else:
            self.width = width

        if player_column < 0:
            raise ValueError("player_column cannot be less than 0")
        else:
            self.column = player_column

        if player_row < 0:
            raise ValueError("player_row cannot be less than 0")
        else:
            self.row = player_row

        self.paths = paths

    def move(self, direction: str):
        """
        Move player in a given direction.

        :param direction: 'w', 'a', 's', 'd' string input for north, west, south, and west.
        :postcondition: move player to correct new row,column coordinate
        """
        if direction == "w":
            if ((self.column, self.row - 1), (self.column, self.row)) not in self.paths:
                print("Cannot go north")
            else:
                self.row -= 1
        if direction == "s":
            if ((self.column, self.row), (self.column, self.row + 1)) not in self.paths:
                print("Cannot go south")
            else:
                self.row += 1
        if direction == "d":
            if ((self.column, self.row), (self.column + 1, self.row)) not in self.paths:
                print("Cannot go east")
            else:
                self.column += 1
        if direction == "a":
            if ((self.column - 1, self.row), (self.column, self.row)) not in self.paths:
                print("Cannot go west")
            else:
                self.column -= 1

    def print_map(self):
        """
        Print map according to the parameters given and current player location

        :postcondition: print map
        """
        for row in range(0, self.height):
            for column in range(0, self.width):
                if self.column == column and self.row == row:
                    sys.stdout.write("[x]")
                else:
                    sys.stdout.write("[ ]")
                if ((column, row), (column + 1, row)) in self.paths:
                    sys.stdout.write("-")
                else:
                    sys.stdout.write(" ")
            print('')
            for column in range(0, self.width):
                sys.stdout.write(" ")
                if ((column, row), (column, row + 1)) in self.paths:
                    sys.stdout.write("|  ")
                else:
                    sys.stdout.write("   ")
            print('')

    def __str__(self):
        """
        return Map class object information in a formatted string.

        :return: a string
        """
        return f"The map dimensions are {self.height} by {self.width}.\n\
The player coordinates are ({self.column},{self.row}).\n\
The paths available are {self.paths} "

    def __repr__(self):
        """
        return a string representing Map class object.

        :return: a string
        """
        return f"Map({self.height}, {self.width}, {self.column}, {self.row}, {self.paths})"


def main():
    """
    Drive Program.
    """
    paths = [((0, 0), (0, 1)),
             ((0, 0), (1, 0)),
             ((0, 1), (0, 2)),
             ((0, 1), (1, 1)),
             ((0, 2), (1, 2)),
             ((1, 0), (1, 1)),
             ((1, 1), (1, 2)),
             ((1, 0), (2, 0)),
             ((2, 0), (2, 1)),
             ((2, 1), (2, 2)),
             ((1, 1), (2, 1)),
             ((1, 2), (2, 2))]
    create_map = Map(3, 3, 1, 0, paths)

    print(create_map)
    print(repr(create_map))

    while True:
        directions = ['w', 'a', 's', 'd']
        move = input("\nPlease enter an action or direction [w, a, s, d]:")
        if move in directions:
            create_map.move(move)
            create_map.print_map()


if __name__ == "__main__":
    main()
