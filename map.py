"""
"""
import random
import sys
import encounter
import title_screen


class Map:
    def __init__(self, height, width, player_row, player_column, paths):
        self.height = height
        self.width = width
        self.row = player_row
        self.column = player_column
        self.paths = paths

    def move(self, direction):
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

    def print_scenario(self):
        row = self.row
        column = self.column
        print(f'Current location {row, column}\n{scenario[(self.row, self.column)]}')


scenario = {
    (0, 0): 'You wake up in a dark damp cave. '
            'You remember being knocked out. '
            'It seems that you have been kidnapped.'
            '*Safe Zone*',
    (0, 1): 'You hear scuffling and voices.*Safe Zone*',
    (0, 2): 'It`s very dark, you can`t make out anything.',
    (0, 3): 'The cave is dark and damp',
    (0, 4): 'The cave is dark and damp',
    (0, 5): 'The cave is dark and damp',
    (0, 6): 'The cave is dark and damp',
    (0, 7): 'The cave is dark and damp',
    (0, 8): 'The cave is dark and damp',
    (0, 9): 'The cave is dark and damp',

    (1, 0): 'You hear scuffling and voices.*Safe Zone*',
    (1, 1): 'You hear scuffling and voices.*Safe Zone*',
    (1, 2): 'The cave is dark and damp',
    (1, 3): 'The cave is dark and damp',
    (1, 4): 'The cave is dark and damp',
    (1, 5): 'The cave is dark and damp',
    (1, 6): 'The cave is dark and damp',
    (1, 7): 'The cave is dark and damp',
    (1, 8): 'The cave is dark and damp',
    (1, 9): 'The cave is dark and damp',

    (2, 0): 'The cave is dark and damp',
    (2, 1): 'The cave is dark and damp',
    (2, 2): 'It`s very dark, you can`t make out anything.',
    (2, 3): 'The cave is dark and damp',
    (2, 4): 'The cave is dark and damp',
    (2, 5): 'The cave is dark and damp',
    (2, 6): 'The cave is dark and damp',
    (2, 7): 'The cave is dark and damp',
    (2, 8): 'The cave is dark and damp',
    (2, 9): 'The cave is dark and damp',

    (3, 0): 'The cave is dark and damp',
    (3, 1): 'The cave is dark and damp',
    (3, 2): 'The cave is dark and damp',
    (3, 3): 'The cave is dark and damp',
    (3, 4): 'The cave is dark and damp',
    (3, 5): 'The cave is dark and damp',
    (3, 6): 'The cave is dark and damp',
    (3, 7): 'The cave is dark and damp',
    (3, 8): 'The cave is dark and damp',
    (3, 9): 'The cave is dark and damp',

    (4, 0): 'The cave is dark and damp',
    (4, 1): 'The cave is dark and damp',
    (4, 2): 'The cave is dark and damp',
    (4, 3): 'The cave is dark and damp',
    (4, 4): 'The cave is dark and damp',
    (4, 5): 'The cave is dark and damp',
    (4, 6): 'The cave is dark and damp',
    (4, 7): 'The cave is dark and damp',
    (4, 8): 'The cave is dark and damp',
    (4, 9): 'The cave is dark and damp',

    (5, 0): 'The cave is dark and damp',
    (5, 1): 'The cave is dark and damp',
    (5, 2): 'The cave is dark and damp',
    (5, 3): 'The cave is dark and damp',
    (5, 4): 'The cave is dark and damp',
    (5, 5): 'The cave is dark and damp',
    (5, 6): 'The cave is dark and damp',
    (5, 7): 'The cave is dark and damp',
    (5, 8): 'The cave is dark and damp',
    (5, 9): 'The cave is dark and damp',

    (6, 0): 'The cave is dark and damp',
    (6, 1): 'The cave is dark and damp',
    (6, 2): 'The cave is dark and damp',
    (6, 3): 'The cave is dark and damp',
    (6, 4): 'The cave is dark and damp',
    (6, 5): 'The cave is dark and damp',
    (6, 6): 'The cave is dark and damp',
    (6, 7): 'The cave is dark and damp',
    (6, 8): 'The cave is dark and damp',
    (6, 9): 'The cave is dark and damp',

    (7, 0): 'The cave is dark and damp',
    (7, 1): 'The cave is dark and damp',
    (7, 2): 'The cave is dark and damp',
    (7, 3): 'The cave is dark and damp',
    (7, 4): 'The cave is dark and damp',
    (7, 5): 'The cave is dark and damp',
    (7, 6): 'The cave is dark and damp',
    (7, 7): 'The cave is dark and damp',
    (7, 8): 'The cave is dark and damp',
    (7, 9): 'The cave is dark and damp',

    (8, 0): 'The cave is dark and damp',
    (8, 1): 'The cave is dark and damp',
    (8, 2): 'The cave is dark and damp',
    (8, 3): 'The cave is dark and damp',
    (8, 4): 'The cave is dark and damp',
    (8, 5): 'The cave is dark and damp',
    (8, 6): 'The cave is dark and damp',
    (8, 7): 'The cave is dark and damp',
    (8, 8): 'The cave is dark and damp',
    (8, 9): 'The cave is dark and damp',

    (9, 0): 'The cave is dark and damp',
    (9, 1): 'The cave is dark and damp',
    (9, 2): 'The cave is dark and damp',
    (9, 3): 'The cave is dark and damp',
    (9, 4): 'The cave is dark and damp',
    (9, 5): 'The cave is dark and damp',
    (9, 6): 'The cave is dark and damp',
    (9, 7): 'The cave is dark and damp',
    (9, 8): 'The cave is dark and damp',
    (9, 9): 'The cave is dark and damp',

}

paths = [((0, 0), (0, 1)),
         ((0, 0), (1, 0)),
         ((0, 1), (0, 2)),
         ((0, 1), (1, 1)),
         ((0, 2), (0, 3)),
         ((0, 2), (1, 2)),
         ((0, 3), (0, 4)),
         ((0, 3), (1, 3)),
         ((0, 4), (0, 5)),
         ((0, 4), (1, 4)),
         ((0, 5), (0, 6)),
         ((0, 5), (1, 5)),
         ((0, 6), (0, 7)),
         ((0, 6), (1, 6)),
         ((0, 7), (0, 8)),
         ((0, 7), (1, 7)),
         ((0, 8), (0, 9)),
         ((0, 8), (1, 8)),
         ((0, 9), (1, 9)),
         ((1, 0), (1, 1)),
         ((1, 0), (2, 0)),
         ((1, 1), (1, 2)),
         ((1, 1), (2, 1)),
         ((1, 2), (1, 3)),
         ((1, 2), (2, 2)),
         ((1, 3), (1, 4)),
         ((1, 3), (2, 3)),
         ((1, 4), (1, 5)),
         ((1, 4), (2, 4)),
         ((1, 5), (1, 6)),
         ((1, 5), (2, 5)),
         ((1, 6), (1, 7)),
         ((1, 6), (2, 6)),
         ((1, 7), (1, 8)),
         ((1, 7), (2, 7)),
         ((1, 8), (1, 9)),
         ((1, 8), (2, 8)),
         ((1, 9), (2, 9)),
         ((2, 0), (2, 1)),
         ((2, 0), (3, 0)),
         ((2, 1), (2, 2)),
         ((2, 1), (3, 1)),
         ((2, 2), (2, 3)),
         ((2, 2), (3, 2)),
         ((2, 3), (2, 4)),
         ((2, 3), (3, 3)),
         ((2, 4), (2, 5)),
         ((2, 4), (3, 4)),
         ((2, 5), (2, 6)),
         ((2, 5), (3, 5)),
         ((2, 6), (2, 7)),
         ((2, 6), (3, 6)),
         ((2, 7), (2, 8)),
         ((2, 7), (3, 7)),
         ((2, 8), (2, 9)),
         ((2, 8), (3, 8)),
         ((2, 9), (3, 9)),
         ((3, 0), (3, 1)),
         ((3, 0), (4, 0)),
         ((3, 1), (3, 2)),
         ((3, 1), (4, 1)),
         ((3, 2), (3, 3)),
         ((3, 2), (4, 2)),
         ((3, 3), (3, 4)),
         ((3, 3), (4, 3)),
         ((3, 4), (3, 5)),
         ((3, 4), (4, 4)),
         ((3, 5), (3, 6)),
         ((3, 5), (4, 5)),
         ((3, 6), (3, 7)),
         ((3, 6), (4, 6)),
         ((3, 7), (3, 8)),
         ((3, 7), (4, 7)),
         ((3, 8), (3, 9)),
         ((3, 8), (4, 8)),
         ((3, 9), (4, 9)),
         ((4, 0), (4, 1)),
         ((4, 0), (5, 0)),
         ((4, 1), (4, 2)),
         ((4, 1), (5, 1)),
         ((4, 2), (4, 3)),
         ((4, 2), (5, 2)),
         ((4, 3), (4, 4)),
         ((4, 3), (5, 3)),
         ((4, 4), (4, 5)),
         ((4, 4), (5, 4)),
         ((4, 5), (4, 6)),
         ((4, 5), (5, 5)),
         ((4, 6), (4, 7)),
         ((4, 6), (5, 6)),
         ((4, 7), (4, 8)),
         ((4, 7), (5, 7)),
         ((4, 8), (4, 9)),
         ((4, 8), (5, 8)),
         ((4, 9), (5, 9)),
         ((5, 0), (5, 1)),
         ((5, 0), (6, 0)),
         ((5, 1), (5, 2)),
         ((5, 1), (6, 1)),
         ((5, 2), (5, 3)),
         ((5, 2), (6, 2)),
         ((5, 3), (5, 4)),
         ((5, 3), (6, 3)),
         ((5, 4), (5, 5)),
         ((5, 4), (6, 4)),
         ((5, 5), (5, 6)),
         ((5, 5), (6, 5)),
         ((5, 6), (5, 7)),
         ((5, 6), (6, 6)),
         ((5, 7), (5, 8)),
         ((5, 7), (6, 7)),
         ((5, 8), (5, 9)),
         ((5, 8), (6, 8)),
         ((5, 9), (6, 9)),
         ((6, 0), (6, 1)),
         ((6, 0), (7, 0)),
         ((6, 1), (6, 2)),
         ((6, 1), (7, 1)),
         ((6, 2), (6, 3)),
         ((6, 2), (7, 2)),
         ((6, 3), (6, 4)),
         ((6, 3), (7, 3)),
         ((6, 4), (6, 5)),
         ((6, 4), (7, 4)),
         ((6, 5), (6, 6)),
         ((6, 5), (7, 5)),
         ((6, 6), (6, 7)),
         ((6, 6), (7, 6)),
         ((6, 7), (6, 8)),
         ((6, 7), (7, 7)),
         ((6, 8), (6, 9)),
         ((6, 8), (7, 8)),
         ((6, 9), (7, 9)),
         ((7, 0), (7, 1)),
         ((7, 0), (8, 0)),
         ((7, 1), (7, 2)),
         ((7, 1), (8, 1)),
         ((7, 2), (7, 3)),
         ((7, 2), (8, 2)),
         ((7, 3), (7, 4)),
         ((7, 3), (8, 3)),
         ((7, 4), (7, 5)),
         ((7, 4), (8, 4)),
         ((7, 5), (7, 6)),
         ((7, 5), (8, 5)),
         ((7, 6), (7, 7)),
         ((7, 6), (8, 6)),
         ((7, 7), (7, 8)),
         ((7, 7), (8, 7)),
         ((7, 8), (7, 9)),
         ((7, 8), (8, 8)),
         ((7, 9), (8, 9)),
         ((8, 0), (8, 1)),
         ((8, 0), (9, 0)),
         ((8, 1), (8, 2)),
         ((8, 1), (9, 1)),
         ((8, 2), (8, 3)),
         ((8, 2), (9, 2)),
         ((8, 3), (8, 4)),
         ((8, 3), (9, 3)),
         ((8, 4), (8, 5)),
         ((8, 4), (9, 4)),
         ((8, 5), (8, 6)),
         ((8, 5), (9, 5)),
         ((8, 6), (8, 7)),
         ((8, 6), (9, 6)),
         ((8, 7), (8, 8)),
         ((8, 7), (9, 7)),
         ((8, 8), (8, 9)),
         ((8, 8), (9, 8)),
         ((8, 9), (9, 9)),
         ((9, 0), (9, 1)),
         ((9, 1), (9, 2)),
         ((9, 2), (9, 3)),
         ((9, 3), (9, 4)),
         ((9, 4), (9, 5)),
         ((9, 5), (9, 6)),
         ((9, 6), (9, 7)),
         ((9, 7), (9, 8)),
         ((9, 8), (9, 9))]
m = Map(10, 10, 0, 0, paths)


# def chance_encounter(char):
#     number = random.randint(0, 10)
#     if char["level"] == 1 and number <= 2:
#         encounter.execute_challenge_protocol(char)
#     elif char["level"] == 2 and number <= 5:
#         encounter.execute_challenge_protocol(char)
#     elif char["level"] == 3 and number <= 8:
#         encounter.execute_challenge_protocol(char)
#     else:
#         print("Nobody notices you.")


def main():
    title_screen.title_screen()
    character = encounter.make_character()
    while True:
        directions = ['w', 'a', 's', 'd']
        # commands = ['1','2','3','q']
        m.print_scenario()
        encounter.execute_glowup_protocol(character)
        valid_moves = enumerate(["Display character information", "Pick a fight", "Display Map"], 1)
        print("Actions available:\n")
        for count, value in valid_moves:
            print(str(count) + ":", value)
        print("q: Quit")
        move = input("\nPlease enter an action or direction [w, a, s, d]:")
        if move == '1':
            encounter.display_character_info(character)
        elif move == '2':
            encounter.execute_challenge_protocol(character)
        elif move == '3':
            m.print_map()
        elif move == 'q':
            break
        elif move in directions:
            m.move(move)
            chance_encounter(character)


if __name__ == "__main__":
    main()
