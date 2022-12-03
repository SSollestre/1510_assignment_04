"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""
import sys


def title_screen_selections():
    while True:
        option = input('>').lower()
        if option not in ['play', 'quit', 'help']:
            print('Please enter a valid command.')
            continue
        if option == 'play':
            return
        elif option == 'help':
            help_menu()
        elif option == 'quit':
            end_screen()
            sys.exit()


def title_screen():
    print('##################################')
    print('#    Welcome to the Text RPG!    #')
    print('#       Made by Sean & Emily     #')
    print('##################################')
    print('              -Play-              ')
    print('              -Help-              ')
    print('              -Quit-              ')
    title_screen_selections()


def help_menu():
    print('##################################')
    print('#       Help Documentation       #')
    print('##################################')
    print('-Use w, a, s, d to move')
    print('-Type your commands to do them')
    print('-Good luck and Have fun!')
    title_screen_selections()


def end_screen():
    print('##################################')
    print('# Thank you for Playing our DEMO #')
    print('#      Stay tuned for more       #')
    print('##################################')


def main():
    """
    Drive the program.
    """
    title_screen()


if __name__ == "__main__":
    main()
