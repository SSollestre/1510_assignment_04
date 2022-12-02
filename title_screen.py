"""

"""
import sys
import os


def title_screen_selections():
    option = input('>')
    if option.lower() == 'play':
        return
    elif option.lower() == 'help':
        help_menu()
    elif option.lower() == 'quit':
        sys.exit()
    while option.lower() not in ['play', 'quit']:
        print('Please enter a valid command.')
        option = input('>')
        if option.lower() == 'play':
            return
        elif option.lower() == 'help':
            help_menu()
        elif option.lower() == 'quit':
            sys.exit()


def title_screen():
    os.system('clear')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('           -Play-           ')
    print('           -Help-           ')
    print('           -Quit-           ')
    print('    Made by Sean & Emily    ')
    title_screen_selections()


def help_menu():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('-Use w(up), a(left), s(down), d(right) to move')
    print('-Type your commands to do them')
    print('-Use look to inspect something')
    print('-Good luck and Have fun!')
    title_screen_selections()


def end_screen():
    print('##################################')
    print('# Thank you for Playing our DEMO #')
    print('#      Stay tuned for more       #')
    print('##################################')
    title_screen_selections()


def main():
    """
    """


if __name__ == "__main__":
    main()
