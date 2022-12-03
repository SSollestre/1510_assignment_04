"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""
import sys


class Map:
    def __init__(self, height: int, width: int, player_row: int, player_column: int, paths: list):
        self.height = height
        self.width = width
        self.row = player_row
        self.column = player_column
        self.paths = paths

    def move(self, direction: str):
        if direction == "w":
            if ((self.row, self.column - 1), (self.row, self.column)) not in self.paths:
                print("Cannot go north")
            else:
                self.column -= 1
        if direction == "s":
            if ((self.row, self.column), (self.row, self.column + 1)) not in self.paths:
                print("Cannot go south")
            else:
                self.column += 1
        if direction == "d":
            if ((self.row, self.column), (self.row + 1, self.column)) not in self.paths:
                print("Cannot go east")
            else:
                self.row += 1
        if direction == "a":
            if ((self.row - 1, self.column), (self.row, self.column)) not in self.paths:
                print("Cannot go west")
            else:
                self.row -= 1

    def print_map(self):
        for column in range(0, self.height):
            # print the yth row of rooms
            for row in range(0, self.width):
                if self.row == row and self.column == column:
                    sys.stdout.write("[x]")  # this is the player's room
                else:
                    sys.stdout.write("[ ]")  # empty room
                # now see whether there's a path to the next room
                if ((row, column), (row + 1, column)) in self.paths:
                    sys.stdout.write("-")
                else:
                    sys.stdout.write(" ")
            # now that we've written the rooms, draw paths to next row
            print('')  # newline
            for row in range(0, self.width):
                sys.stdout.write(" ")  # spaces for above room
                if ((row, column), (row, column + 1)) in self.paths:
                    sys.stdout.write("|  ")
                else:
                    sys.stdout.write("   ")
            print('')


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
    create_map = Map(3, 3, 0, 0, paths)
    while True:
        directions = ['w', 'a', 's', 'd']
        move = input("\nPlease enter an action or direction [w, a, s, d]:")
        if move in directions:
            create_map.move(move)
            create_map.print_map()


if __name__ == "__main__":
    main()
