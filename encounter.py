"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""
import time
import random
import title_screen


def make_character():
    """
    Generate a dictionary for a player character.

    :return: a dictionary representing a character's attributes
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


def attack(char, enemy):
    """
    Cause damage to an enemy.

    :param char: a character dictionary
    :param enemy: an enemy dictionary
    :return: the enemy dictionary with reduced health
    """
    damage = char["strength"] - (0.25 * enemy["defense"])
    enemy["health"] -= damage
    time.sleep(0.25)
    print(char["name"], "strikes", enemy["name"], "for", damage, "damage!")
    return enemy


def double_strike(char, enemy):
    """
    Cause damage twice to an enemy.

    :param char: a character dictionary
    :param enemy: an enemy dictionary
    :return: the enemy dictionary with reduced health
    """
    damage = (char["strength"] - (0.25 * enemy["defense"])) * 0.75
    enemy["health"] -= damage * 2
    time.sleep(0.25)
    print(char["name"], "strikes", enemy["name"], "for", damage, "damage!")
    time.sleep(0.25)
    print(char["name"], "strikes", enemy["name"], "for", damage, "damage!")
    return enemy


def guard(char, enemy):
    """
    Restore character health.

    :param char: a character dictionary
    :param enemy: an enemy dictionary
    :return: the character dictionary with increased health
    """
    time.sleep(0.25)
    print(f"{char['name']} raises their guard.")
    damage = (enemy["strength"] - (0.25 * char["defense"])) * 1.5
    char["health"] += damage
    return char


def return_entity(level):
    """
    Generates an enemy dictionary based on level.

    :param level: an integer representing a level attribute
    :return: an enemy dictionary
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


def display_character_info(char):
    """
    Display character information.

    :param char: a character dictionary
    """
    print("\nCharacter information:\n"
          f"Name: {char['name']}\n"
          f"Health: {char['max_health']}\n"
          f"Strength: {char['strength']}\n"
          f"Defense: {char['defense']}\n"
          f"Dexterity: {char['dexterity']}\n"
          f"Level: {char['level']}\n"
          f"Skills: {list(char['skills'].keys())}\n")


def execute_glowup_protocol(char):
    """
    Display character increases in stats on level-up.

    Call helper function to increase character attributes.

    :param char: a character dictionary
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


def scale_values(char):
    """
    Increase a character's attributes.

    :param char: a character dictionary
    :return: a character dictionary with increased attributes
    """
    char_stats = [integer_key for integer_key in char.keys() if type(char[integer_key]) == int and
                  integer_key != 'level']
    for item in char_stats:
        char[item] *= 1.5
    char["level"] = char["level"] + 1
    char["exp"] = 0
    if char['level'] == 2:
        print("Skills:%s + ['Double Strike']" % (list(char["skills"].keys())) + "\n")
        char["skills"]["Double Strike"] = double_strike
    if char['level'] == 3:
        print("Skills:%s + ['Guard']" % (list(char["skills"].keys())) + "\n")
        char["skills"]["Guard"] = guard
    return char


def execute_challenge_protocol(char):
    """
    Invoke an encounter with an enemy.

    Call helper functions: display_combat_menu
                           validate_move
                           character_enemy_interaction

    :param char: a character dictionary
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


def character_enemy_interaction(char, enemy):
    """
    Execute enemy dictionary actions against character dictionary.

    :param char: a character dictionary
    :param enemy: an enemy dictionary
    """
    if enemy["health"] <= 0:
        char["exp"] += enemy["exp"]
        print(f"\n{enemy['name']} has been defeated!\n")
        return
    attack(enemy, char)
    time.sleep(0.25)


def display_combat_menu(char, enemy):
    print("***\nValid Moves:")
    print("0: Flee")
    for count, value in enumerate(char['skills'], 1):
        print(str(count) + ":", value)
    print(f"\n{char['name']}'s current HP: {char['health']}\n"
          f"{enemy['name']}'s current HP: {enemy['health']} \n")


def validate_move(action, char, enemy):
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


def check_if_goal_attained(char):
    if char["goal"]:
        return True
    return False


def chance_encounter(char):
    number = random.randint(0, 10)
    if char["level"] == 1 and number <= 2:
        execute_challenge_protocol(char)
    elif char["level"] == 2 and number <= 5:
        execute_challenge_protocol(char)
    elif char["level"] == 3 and number <= 8:
        execute_challenge_protocol(char)
    else:
        print("Nobody notices you.")


def main():
    """
    Drive program.
    """
    character = make_character()
    achieved_goal = False
    while not achieved_goal and character["health"] > 0:
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
        achieved_goal = check_if_goal_attained(character)
    if achieved_goal:
        title_screen.end_screen()


if __name__ == "__main__":
    main()
