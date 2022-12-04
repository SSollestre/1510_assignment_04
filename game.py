"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""
from title_screen import title_screen, end_screen
from map import Map
from encounter import make_character, display_character_info, execute_glowup_protocol, execute_challenge_protocol, chance_encounter
import itertools
import time


def print_scenario(create_map: Map):
    """
    Return a string description of given coordinate and location.

    :param create_map: Map class
    :return: a string
    >>> test = Map(2,2,0,0,[((0,0),(0,1)),((0,0),(1,0)),((1,0),(1,1)),((0,1),(1,1))])
    >>> print_scenario(test)
    Current location (0, 0)
    You wake up in a dark damp cave. You remember being knocked out. It seems that you have been kidnapped.
    >>> test = Map(2,2,0,1,[((0,0),(0,1)),((0,0),(1,0)),((1,0),(1,1)),((0,1),(1,1))])
    >>> print_scenario(test)
    Current location (1, 0)
    You hear scuffling and voices.
    """
    scenario = {
        (0, 0): 'You wake up in a dark damp cave. '
                'You remember being knocked out. '
                'It seems that you have been kidnapped.',
        (0, 1): 'You hear scuffling and voices.',
        (0, 2): 'It`s very dark, you can`t make out anything.',
        (0, 3): 'The cave is dark and damp',
        (0, 4): 'The cave is dark and damp',
        (0, 5): 'The cave is dark and damp',
        (0, 6): 'You hear scuffling and voices.',
        (0, 7): 'The cave is dark and damp',
        (0, 8): 'The cave is dark and damp',
        (0, 9): 'You hear scuffling and voices.',

        (1, 0): 'You hear scuffling and voices.',
        (1, 1): 'You hear scuffling and voices.',
        (1, 2): 'The cave is dark and damp',
        (1, 3): 'The cave is dark and damp',
        (1, 4): 'The cave is dark and damp',
        (1, 5): 'The cave is dark and damp',
        (1, 6): 'It`s very dark, you can`t make out anything.',
        (1, 7): 'The cave is dark and damp',
        (1, 8): 'The cave is dark and damp',
        (1, 9): 'It`s very dark, you can`t make out anything.',

        (2, 0): 'The cave is dark and damp',
        (2, 1): 'The cave is dark and damp',
        (2, 2): 'It`s very dark, you can`t make out anything.',
        (2, 3): 'The cave is dark and damp',
        (2, 4): 'The cave is dark and damp',
        (2, 5): 'The cave is dark and damp',
        (2, 6): 'You hear scuffling and voices.',
        (2, 7): 'The cave is dark and damp',
        (2, 8): 'The cave is dark and damp',
        (2, 9): 'The cave is dark and damp',

        (3, 0): 'The cave is dark and damp',
        (3, 1): 'The cave is dark and damp',
        (3, 2): 'The cave is dark and damp',
        (3, 3): 'It`s very dark, you can`t make out anything.',
        (3, 4): 'The cave is dark and damp',
        (3, 5): 'You hear scuffling and voices.',
        (3, 6): 'The cave is dark and damp',
        (3, 7): 'It`s very dark, you can`t make out anything.',
        (3, 8): 'The cave is dark and damp',
        (3, 9): 'The cave is dark and damp',

        (4, 0): 'The cave is dark and damp',
        (4, 1): 'You hear scuffling and voices.',
        (4, 2): 'The cave is dark and damp',
        (4, 3): 'The cave is dark and damp',
        (4, 4): 'It`s very dark, you can`t make out anything.',
        (4, 5): 'The cave is dark and damp',
        (4, 6): 'The cave is dark and damp',
        (4, 7): 'It`s very dark, you can`t make out anything.',
        (4, 8): 'The cave is dark and damp',
        (4, 9): 'The cave is dark and damp',

        (5, 0): 'The cave is dark and damp',
        (5, 1): 'You hear scuffling and voices.',
        (5, 2): 'The cave is dark and damp',
        (5, 3): 'The cave is dark and damp',
        (5, 4): 'It`s very dark, you can`t make out anything.',
        (5, 5): 'The cave is dark and damp',
        (5, 6): 'The cave is dark and damp',
        (5, 7): 'It`s very dark, you can`t make out anything.',
        (5, 8): 'The cave is dark and damp',
        (5, 9): 'The cave is dark and damp',

        (6, 0): 'The cave is dark and damp',
        (6, 1): 'You hear scuffling and voices.',
        (6, 2): 'The cave is dark and damp',
        (6, 3): 'The cave is dark and damp',
        (6, 4): 'It`s very dark, you can`t make out anything.',
        (6, 5): 'The cave is dark and damp',
        (6, 6): 'The cave is dark and damp',
        (6, 7): 'It`s very dark, you can`t make out anything.',
        (6, 8): 'The cave is dark and damp',
        (6, 9): 'The cave is dark and damp',

        (7, 0): 'The cave is dark and damp',
        (7, 1): 'The cave is dark and damp',
        (7, 2): 'You hear scuffling and voices.',
        (7, 3): 'The cave is dark and damp',
        (7, 4): 'The cave is dark and damp',
        (7, 5): 'It`s very dark, you can`t make out anything.',
        (7, 6): 'The cave is dark and damp',
        (7, 7): 'The cave is dark and damp',
        (7, 8): 'It`s very dark, you can`t make out anything.',
        (7, 9): 'The cave is dark and damp',

        (8, 0): 'The cave is dark and damp',
        (8, 1): 'The cave is dark and damp',
        (8, 2): 'You hear scuffling and voices.',
        (8, 3): 'The cave is dark and damp',
        (8, 4): 'The cave is dark and damp',
        (8, 5): 'It`s very dark, you can`t make out anything.',
        (8, 6): 'The cave is dark and damp',
        (8, 7): 'The cave is dark and damp',
        (8, 8): 'It`s very dark, you can`t make out anything.',
        (8, 9): 'The cave is dark and damp',

        (9, 0): 'The cave is dark and damp',
        (9, 1): 'The cave is dark and damp',
        (9, 2): 'You hear scuffling and voices.',
        (9, 3): 'The cave is dark and damp',
        (9, 4): 'The cave is dark and damp',
        (9, 5): 'You hear scuffling and voices.',
        (9, 6): 'The cave is dark and damp',
        (9, 7): 'The cave is dark and damp',
        (9, 8): 'The cave is dark and damp',
        (9, 9): 'You see light!',

    }
    row = create_map.row
    column = create_map.column
    print(f'Current location {row, column}\n{scenario[(create_map.row, create_map.column)]}')


def feet(seconds: int):
    """
    Show an animated spinner while we sleep.
    """
    walk = itertools.cycle(['  __ \n'
                            ' (  )\n'
                            ' )  (\n'
                            '(   )\n'
                            'Ooooo\n',
                            '\t\t  __\n'
                            '\t\t (  )\n'
                            '\t\t )  (\n'
                            '\t\t(   )\n'
                            '\t\tOoooo\n'

                            ])
    upper_time = time.time() + seconds
    while time.time() < upper_time:
        time.sleep(0.25)
        print(next(walk))
    print()


def game():
    """
    Run the game.
    """
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
    title_screen()
    character = make_character()
    create_map = Map(10, 10, 0, 0, paths)
    while not character['goal'] and character["health"] > 0:
        directions = ['w', 'a', 's', 'd']
        commands = ['1', '2', '3', 'q']
        print_scenario(create_map)
        execute_glowup_protocol(character)
        valid_moves = enumerate(["Display character information", "Pick a fight", "Display Map"], 1)
        print("Actions available:\n")
        for count, value in valid_moves:
            print(str(count) + ":", value)
        print("q: Quit")
        move = input("\nPlease enter an action or direction [w, a, s, d]:")
        if move not in directions and move not in commands:
            print("\n***\nThat is not a valid command.\n***\n")
            time.sleep(2)
        if move == '1':
            display_character_info(character)
        elif move == '2':
            execute_challenge_protocol(character)
        elif move == '3':
            create_map.print_map()
        elif move == 'q':
            end_screen()
            break
        elif move in directions:
            feet(1)
            create_map.move(move)
            chance_encounter(character)
    if character['goal']:
        end_screen()


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
