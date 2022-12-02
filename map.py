"""
"""
import random
import sys
import encounter


class Map:
    def __init__(self, height, width, player_x, player_y, paths):
        self.height = height
        self.width = width
        self.x = player_x
        self.y = player_y
        self.paths = paths

    def move(self, direction):
        if direction == "n":
            if ((self.x, self.y - 1), (self.x, self.y)) not in self.paths:
                print("Cannot go north")
            else:
                self.y -= 1
        if direction == "s":
            if ((self.x, self.y), (self.x, self.y + 1)) not in self.paths:
                print("Cannot go south")
            else:
                self.y += 1
        if direction == "e":
            if ((self.x, self.y), (self.x + 1, self.y)) not in self.paths:
                print("Cannot go east")
            else:
                self.x += 1
        if direction == "w":
            if ((self.x - 1, self.y), (self.x, self.y)) not in self.paths:
                print("Cannot go west")
            else:
                self.x -= 1

    def print_map(self):
        for y in range(0, self.height):
            # print the yth row of rooms
            for x in range(0, self.width):
                if self.x == x and self.y == y:
                    sys.stdout.write("[x]")  # this is the player's room
                else:
                    sys.stdout.write("[ ]")  # empty room
                # now see whether there's a path to the next room
                if ((x, y), (x + 1, y)) in self.paths:
                    sys.stdout.write("-")
                else:
                    sys.stdout.write(" ")
            # now that we've written the rooms, draw paths to next row
            print('')  # newline
            for x in range(0, self.width):
                sys.stdout.write(" ")  # spaces for above room
                if ((x, y), (x, y + 1)) in self.paths:
                    sys.stdout.write("|  ")
                else:
                    sys.stdout.write("   ")
            print('')

    def print_scenario(self):
        x = self.x
        y = self.y
        print(f'Current location {x, y}\n{scenario[(self.x, self.y)]}')


scenario = {
    (0, 0): 'You wake up in a dark damp cave. '
            'You remember being knocked out. '
            'It seems that you have been kidnapped.'
            '*Safe Zone*',
    (0, 1): 'You hear scuffling and voices.*Safe Zone*',
    (0, 2): 'It`s very dark, you can`t make out anything.',
    (0, 3): '',
    (0, 4): '',
    (0, 5): '',
    (0, 6): '',
    (0, 7): '',
    (0, 8): '',
    (0, 9): '',

    (1, 0): 'You hear scuffling and voices.*Safe Zone*',
    (1, 1): 'You hear scuffling and voices.*Safe Zone*',
    (1, 2): '',
    (1, 3): '',
    (1, 4): '',
    (1, 5): '',
    (1, 6): '',
    (1, 7): '',
    (1, 8): '',
    (1, 9): '',

    (2, 0): '',
    (2, 1): '',
    (2, 2): 'It`s very dark, you can`t make out anything.',
    (2, 3): '',
    (2, 4): '',
    (2, 5): '',
    (2, 6): '',
    (2, 7): '',
    (2, 8): '',
    (2, 9): '',

    (3, 0): '',
    (3, 1): '',
    (3, 2): '',
    (3, 3): '',
    (3, 4): '',
    (3, 5): '',
    (3, 6): '',
    (3, 7): '',
    (3, 8): '',
    (3, 9): '',

    (4, 0): '',
    (4, 1): '',
    (4, 2): '',
    (4, 3): '',
    (4, 4): '',
    (4, 5): '',
    (4, 6): '',
    (4, 7): '',
    (4, 8): '',
    (4, 9): '',

    (5, 0): '',
    (5, 1): '',
    (5, 2): '',
    (5, 3): '',
    (5, 4): '',
    (5, 5): '',
    (5, 6): '',
    (5, 7): '',
    (5, 8): '',
    (5, 9): '',

    (6, 0): '',
    (6, 1): '',
    (6, 2): '',
    (6, 3): '',
    (6, 4): '',
    (6, 5): '',
    (6, 6): '',
    (6, 7): '',
    (6, 8): '',
    (6, 9): '',

    (7, 0): '',
    (7, 1): '',
    (7, 2): '',
    (7, 3): '',
    (7, 4): '',
    (7, 5): '',
    (7, 6): '',
    (7, 7): '',
    (7, 8): '',
    (7, 9): '',

    (8, 0): '',
    (8, 1): '',
    (8, 2): '',
    (8, 3): '',
    (8, 4): '',
    (8, 5): '',
    (8, 6): '',
    (8, 7): '',
    (8, 8): '',
    (8, 9): '',

    (9, 0): '',
    (9, 1): '',
    (9, 2): '',
    (9, 3): '',
    (9, 4): '',
    (9, 5): '',
    (9, 6): '',
    (9, 7): '',
    (9, 8): '',
    (9, 9): '',

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


def chance_encounter():
    number = random.randint(0, 10)
    for char["level"] in range(0, 4):
        if char["level"] == 1 and number >= 5:
            execute_challenge_protocol(char)
        elif char["level"] == 2 and number >= 5:
            execute_challenge_protocol(char)
        else:
            execute_challenge_protocol(char)


def main():
    character = encounter.make_character()
    while True:
        m.print_map()
        m.print_scenario()
        direction = input("What direction do you want to move? [n/e/s/w] ")
        m.move(direction)
        encounter.execute_glowup_protocol(character)
        valid_moves = enumerate(["Display character information", "Start encounter"], 1)
        print("Actions available:\n")
        for count, value in valid_moves:
            print(str(count) + ":", value)
        print("q: Quit")
        move = input("\nPlease enter an action:")
        if move == '1':
            encounter.display_character_info(character)
        elif move == '2':
            encounter.execute_challenge_protocol(character)
        elif move == 'q':
            break


if __name__ == "__main__":
    main()
