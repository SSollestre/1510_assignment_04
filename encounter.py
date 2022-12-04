"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""
import time
import random
from title_screen import end_screen


def make_character() -> dict:
    """
    Generate a character sheet as dictionary for a player character.

    :return: a dictionary representing a character's statistics as attributes
    """
    name = input("What is your name?\n")
    character_board = {
        "name": name,
        "max_health": 50,
        "health": 50,
        "strength": 10,
        "defense": 10,
        "dexterity": 10,
        "level": 1,
        "exp": 0,
        "goal": False,
        "skills": {
            "Basic Attack": attack
        }
    }
    return character_board


def attack(char: dict, enemy: dict) -> dict:
    """
    Cause damage to an enemy.

    :param char: a character dictionary
    :param enemy: an enemy dictionary
    :precondition: char must be a dictionary representing a character
    :precondition: char must be a dictionary representing a target
    :postcondition: the enemy dictionary's health attribute is reduced based on
                    strength and defense statistics
    :return: the enemy dictionary with reduced health
    >>> character =  {
    ... "name": "dummy",
    ... "max_health": 50,
    ... "health": 50,
    ... "strength": 10,
    ... "defense": 10,
    ... "dexterity": 10,
    ... "level": 1,
    ... "exp": 0,
    ... "goal": False,
    ... "skills": {
    ...    "Basic Attack": attack
    ...  }
    ... }
    >>> target = {
    ... "name": "Bandit",
    ... "health": 50,
    ... "strength": 10,
    ... "defense": 10,
    ... "dexterity": 10,
    ...  "level": 1,
    ...    "goal": False,
    ...   "exp": 25
    ...  }
    >>> attack(character, target)
    dummy strikes Bandit for 7.5 damage!
    {'name': 'Bandit', 'health': 42.5, 'strength': 10, 'defense': 10, 'dexterity': 10, 'level': 1, 'goal': False,\
 'exp': 25}
    >>> character =  {
    ... "name": "dummy",
    ... "max_health": 50,
    ... "health": 50,
    ... "strength": 15,
    ... "defense": 10,
    ... "dexterity": 10,
    ... "level": 1,
    ... "exp": 0,
    ... "goal": False,
    ... "skills": {
    ...     "Basic Attack": attack
    ...  }
    ... }
    >>> target = {
    ... "name": "Bandit",
    ... "health": 50,
    ... "strength": 10,
    ... "defense": 10,
    ... "dexterity": 10,
    ... "level": 1,
    ... "goal": False,
    ... "exp": 25
    ...  }
    >>> attack(character, target)
    dummy strikes Bandit for 12.5 damage!
    {'name': 'Bandit', 'health': 37.5, 'strength': 10, 'defense': 10, 'dexterity': 10, 'level': 1, 'goal': False,\
 'exp': 25}

    """
    damage = char["strength"] - (0.25 * enemy["defense"])
    enemy["health"] -= damage
    time.sleep(0.25)
    print(char["name"], "strikes", enemy["name"], "for", damage, "damage!")
    return enemy


def double_strike(char: dict, enemy: dict) -> dict:
    """
    Cause damage twice to an enemy.

    :param char: a character dictionary
    :param enemy: an enemy dictionary
    :precondition: char must be a dictionary representing a character
    :precondition: enemy must be a dictionary representing a target
    :postcondition: the enemy dictionary's health attribute is reduced based on
                    strength and defense statistics
    :return: the enemy dictionary with reduced health
    >>> character =  {
    ... "name": "dummy",
    ... "max_health": 50,
    ... "health": 50,
    ... "strength": 10,
    ... "defense": 10,
    ... "dexterity": 10,
    ... "level": 1,
    ... "exp": 0,
    ... "goal": False,
    ... "skills": {
    ...     "Basic Attack": attack
    ... }
    ... }
    >>> target = {
    ... "name": "Bandit",
    ... "health": 50,
    ... "strength": 10,
    ... "defense": 10,
    ... "dexterity": 10,
    ... "level": 1,
    ... "goal": False,
    ... "exp": 25
    ... }
    >>> double_strike(character, target)
    dummy strikes Bandit for 5.625 damage!
    dummy strikes Bandit for 5.625 damage!
    {'name': 'Bandit', 'health': 38.75, 'strength': 10, 'defense': 10, 'dexterity': 10, 'level': 1, \
'goal': False, 'exp': 25}
    >>> character =  {
    ... "name": "dummy",
    ... "max_health": 50,
    ... "health": 50,
    ... "strength": 15,
    ... "defense": 10,
    ... "dexterity": 10,
    ... "level": 1,
    ... "exp": 0,
    ... "goal": False,
    ... "skills": {
    ...     "Basic Attack": attack
    ...  }
    ... }
    >>> target = {
    ... "name": "Bandit",
    ... "health": 50,
    ... "strength": 10,
    ... "defense": 10,
    ... "dexterity": 10,
    ... "level": 1,
    ... "goal": False,
    ... "exp": 25
    ... }
    >>> double_strike(character, target)
    dummy strikes Bandit for 9.375 damage!
    dummy strikes Bandit for 9.375 damage!
    {'name': 'Bandit', 'health': 31.25, 'strength': 10, 'defense': 10, 'dexterity': 10, 'level': 1, 'goal': False,\
 'exp': 25}
    """
    damage = (char["strength"] - (0.25 * enemy["defense"])) * 0.75
    enemy["health"] -= damage * 2
    time.sleep(0.25)
    print(char["name"], "strikes", enemy["name"], "for", damage, "damage!")
    time.sleep(0.25)
    print(char["name"], "strikes", enemy["name"], "for", damage, "damage!")
    return enemy


def guard(char: dict, enemy: dict) -> dict:
    """
    Restore character health.

    :param char: a character dictionary
    :param enemy: an enemy dictionary
    :precondition: char must be a dictionary representing a character
    :precondition: char must be a dictionary representing a target
    :postcondition: the enemy dictionary's health attribute is reduced based on
                    strength and defense statistics
    :return: the character dictionary with increased health
    """
    time.sleep(0.25)
    print(f"{char['name']} raises their guard.")
    damage = (enemy["strength"] - (0.25 * char["defense"])) * 1.5
    char["health"] += damage
    return char


def return_entity(level: int) -> dict:
    """
    Generates an enemy dictionary based on level.

    :param level: an integer representing a level attribute of a character
    :precondition: level must be an integer representing a level attribute
    :postcondition: select which enemy to return based on level passed as argument
    :return: an enemy dictionary based on level
    >>> return_entity(1)
    {'name': 'Bandit', 'health': 50, 'strength': 10, 'defense': 10, 'dexterity': 10, 'level': 1,\
 'goal': False, 'exp': 25}
    >>> return_entity(2)
    {'name': 'Bandit Lieutenant', 'health': 50, 'strength': 30, 'defense': 10, 'dexterity': 10,\
 'level': 2, 'goal': False, 'exp': 25}
    """
    enemies = [
        {
            "name": "Bandit",
            "health": 50,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "goal": False,
            "exp": 25
        },

        {
            "name": "Bandit Lieutenant",
            "health": 50,
            "strength": 30,
            "defense": 10,
            "dexterity": 10,
            "level": 2,
            "goal": False,
            "exp": 25
        },

        {
            "name": "Bandit Chief",
            "health": 150,
            "strength": 30,
            "defense": 20,
            "dexterity": 10,
            "level": 3,
            "goal": True,
            "exp": 25
        }]

    for bandit in enemies:
        if level == bandit['level']:
            return bandit


def display_character_info(char: dict) -> None:
    """
    Display character information.

    :param char: a character dictionary
    :precondition: char must be a dictionary representing a character
    :postcondition: print a character sheet based on information on char dictionary
    >>> character =  {
    ... "name": "dummy",
    ... "max_health": 50,
    ... "health": 50,
    ... "strength": 15,
    ... "defense": 10,
    ... "dexterity": 10,
    ... "level": 1,
    ... "exp": 0,
    ... "goal": False,
    ... "skills": {
    ...     "Basic Attack": attack
    ... }
    ... }
    >>> display_character_info(character)
    <BLANKLINE>
    Character information:
    Name: dummy
    Health: 50
    Strength: 15
    Defense: 10
    Dexterity: 10
    Level: 1
    Skills: ['Basic Attack']
    <BLANKLINE>
    >>> character =  {
    ... "name": "Big Man",
    ... "max_health": 70,
    ... "health": 100,
    ... "strength": 5,
    ... "defense": 20,
    ... "dexterity": 0,
    ... "level": 1,
    ... "exp": 25,
    ... "goal": False,
    ... "skills": {
    ...     "Basic Attack": attack
    ... }
    ... }
    >>> display_character_info(character)
    <BLANKLINE>
    Character information:
    Name: Big Man
    Health: 70
    Strength: 5
    Defense: 20
    Dexterity: 0
    Level: 1
    Skills: ['Basic Attack']
    <BLANKLINE>
    """
    print("\nCharacter information:\n"
          f"Name: {char['name']}\n"
          f"Health: {char['max_health']}\n"
          f"Strength: {char['strength']}\n"
          f"Defense: {char['defense']}\n"
          f"Dexterity: {char['dexterity']}\n"
          f"Level: {char['level']}\n"
          f"Skills: {list(char['skills'].keys())}\n")


def execute_glowup_protocol(char: dict) -> dict:
    """
    Display character increases in stats on level-up.

    Call helper function to increase character attributes.

    :param char: a character dictionary
    :precondition: char must be a dictionary representing a character
    :postcondition: print a character sheet with increased statistics
    :postcondition: return character dictionary with increased statistics using helper function
    :return: a character dictionary with increased attributes
    """
    if char["exp"] >= 50:
        time.sleep(0.25)
        print(f"{char['name']} has leveled up!\n\nNew Stats:\n")
        time.sleep(0.25)
        print(
            f"Name: {char['name']}\n"
            f"Health: {char['max_health']} -> {char['max_health'] * 1.5}\n"
            f"Strength: {char['strength']} -> {char['strength'] * 1.5}\n"
            f"Defense: {char['defense']} -> {char['defense'] * 1.5}\n"
            f"Dexterity: {char['dexterity']} -> {char['dexterity'] * 1.5}\n"
            f"Level: {char['level']} -> {char['level'] + 1}"
        )
        scale_values(char)
        time.sleep(0.25)
    return char


def scale_values(char: dict) -> dict:
    """
    Increase a character's attributes.

    :param char: a character dictionary
    :precondition: char must be a dictionary representing a character
    :postcondition: return character dictionary with increased statistics
    :return: a character dictionary with increased attributes
    """
    char_stats = [integer_key for integer_key in char.keys() if type(char[integer_key]) == int and
                  integer_key != 'level']
    for item in char_stats:
        char[item] *= 1.5
        char[item] = int(char[item])
    char["level"] = char["level"] + 1
    char["exp"] = 0
    if char['level'] == 2:
        print("Skills:%s + ['Double Strike']" % (list(char["skills"].keys())) + "\n")
        char["skills"]["Double Strike"] = double_strike
    if char['level'] == 3:
        print("Skills:%s + ['Guard']" % (list(char["skills"].keys())) + "\n")
        char["skills"]["Guard"] = guard
    return char


def execute_challenge_protocol(char: dict) -> dict:
    """
    Invoke an encounter with an enemy.

    Call helper functions: display_combat_menu
                           validate_move
                           character_enemy_interaction

    :param char: a character dictionary
    :precondition: char must be a dictionary representing a character
    :postcondition: modify character dictionary
    :return: a character dictionary with modified attributes
    """
    enemy = return_entity(char["level"])
    print(f"\n***\nCombat has initiated\n***\n{enemy['name']} glares at you menacingly.")
    while enemy["health"] > 0 and char["health"] > 0:
        display_combat_menu(char, enemy)
        action = input("Please enter an action:")
        if action == '0':
            print("You make a break for it!")
            break
        if not validate_move(action, char, enemy):
            continue
        character_enemy_interaction(char, enemy)
        if char["health"] <= 0:
            char["exp"] -= enemy["exp"]
            print(f"\n{char['name']} has been defeated...\n\n")
            return char
    print("\n***\nCombat has ended\n***\n")
    char["health"] = char["max_health"]
    char["goal"] = enemy["goal"]
    return char


def character_enemy_interaction(char: dict, enemy: dict) -> (dict, None):
    """
    Execute enemy dictionary actions against character dictionary.

    :param char: a character dictionary
    :param enemy: an enemy dictionary
    :precondition: char must be a dictionary representing a character
    :precondition: char must be a dictionary representing a target
    :postcondition: decrease character health values if enemy health value is above 0
    :return: a character dictionary with decreased health values
    """
    if enemy["health"] <= 0:
        char["exp"] += enemy["exp"]
        print(f"\n{enemy['name']} has been defeated!\n")
        return
    attack(enemy, char)
    time.sleep(0.25)
    return char


def display_combat_menu(char: dict, enemy: dict) -> None:
    """
    Display the combat menu.

    Display valid actions, character current health, and enemy current health.

    :param char: a character dictionary
    :param enemy: an enemy dictionary
    :precondition: char must be a dictionary representing a character
    :precondition: char must be a dictionary representing a target
    :postcondition: print the valid user inputs
    :postcondition: print current character and enemy health values
    >>> character =  {
    ... "name": "dummy",
    ... "max_health": 50,
    ... "health": 50,
    ... "strength": 10,
    ... "defense": 10,
    ... "dexterity": 10,
    ... "level": 1,
    ... "exp": 0,
    ... "goal": False,
    ... "skills": {
    ...     "Basic Attack": attack
    ... }
    ... }
    >>> target = {
    ... "name": "Bandit",
    ... "health": 50,
    ... "strength": 10,
    ... "defense": 10,
    ... "dexterity": 10,
    ... "level": 1,
    ... "goal": False,
    ... "exp": 25
    ... }
    >>> display_combat_menu(character, target)
    ***
    Valid Moves:
    0: Flee
    1: Basic Attack
    <BLANKLINE>
    dummy's current HP: 50
    Bandit's current HP: 50
    <BLANKLINE>
    """
    print("***\nValid Moves:")
    print("0: Flee")
    for count, value in enumerate(char['skills'], 1):
        print(f"{count}: {value}")
    print(f"\n{char['name']}'s current HP: {char['health']}\n"
          f"{enemy['name']}'s current HP: {enemy['health']}\n")


def validate_move(action: str, char: dict, enemy: dict) -> (dict, dict):
    """
    Determine if action is a valid move or not.

    Execute the action by invoking a character skill function if the move is valid.

    :param action: a string representing user selected action
    :param char: a character dictionary
    :param enemy: an enemy dictionary
    :precondition: action must be a string representing user selected action
    :precondition: char must be a dictionary representing a character
    :precondition: char must be a dictionary representing a target
    :postcondition: modify character and enemy dictionaries based on action value
    :return: modified character and enemy dictionaries based on action value
    """
    moves = list(map(str, range(1, len(char['skills']) + 1)))
    if action not in moves:
        print("You do not know that move")
        return False
    if action == '1':
        char['skills']["Basic Attack"](char, enemy)
    if action == '2':
        print(f"{char['name']} uses {list(char['skills'].keys())[1]}.")
        char['skills']["Double Strike"](char, enemy)
    if action == '3':
        print(f"{char['name']} uses {list(char['skills'].keys())[2]}.")
        char['skills']["Guard"](char, enemy)
    return char, enemy


def chance_encounter(char: dict) -> None:
    """
    Determine whether run execute challenge protocol.

    :param char: char must be a character dictionary
    :precondition: char must be a dictionary representing a character
    :postcondition: determine if execute challenge protocol executes
    """
    number = random.randint(0, 10)
    if char["level"] == 1 and number <= 2:
        print("You have been spotted!")
        execute_challenge_protocol(char)
    elif char["level"] == 2 and number <= 5:
        print("You have been spotted!")
        execute_challenge_protocol(char)
    elif char["level"] == 3 and number <= 8:
        print("You have been spotted!")
        execute_challenge_protocol(char)
    else:
        print("Nobody notices you.")


def main():
    """
    Drive the program.
    """
    character = make_character()
    while not character['goal'] and character["health"] > 0:
        execute_glowup_protocol(character)
        valid_moves = enumerate(["Display character information", "Pick a fight"], 1)
        print("***\nActions available:\n")
        for count, value in valid_moves:
            print(str(count) + ":", value)
        print("q: Quit")
        move = input("\nPlease enter an action:")
        if move == '1':
            display_character_info(character)
        elif move == '2':
            execute_challenge_protocol(character)
        elif move == 'q':
            break
    if character['goal']:
        end_screen()


if __name__ == "__main__":
    main()
