"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""


def make_character():
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
        "goal": False
    }
    return character_board


def attack(char, enemy):
    damage = char["strength"] - (0.25 * enemy["defense"])
    enemy["health"] -= damage
    print(char["name"], "strikes", enemy["name"], "for", damage, "damage!")
    return enemy


def return_entity(level):
    bandit = {
        "name": "Bandit",
        "health": 50,
        "strength": 5,
        "defense": 10,
        "dexterity": 10,
        "level": 1,
        "exp": 25
    }

    bandit_lieutenant = {
        "name": "Bandit Lieutenant",
        "health": 50,
        "strength": 10,
        "defense": 10,
        "dexterity": 10,
        "level": 2,
        "exp": 25
    }

    bandit_chief = {
        "name": "Bandit Chief",
        "health": 50,
        "strength": 10,
        "defense": 10,
        "dexterity": 10,
        "level": 3,
        "exp": 25
    }

    if level == 1:
        return bandit

    elif level == 2:
        return bandit_lieutenant

    elif level == 3:
        return bandit_chief


def display_character_info(char):
    name = char["name"]
    strength = char["strength"]
    defense = char["defense"]
    dexterity = char["dexterity"]
    exp = character["exp"]
    lvl = character["level"]
    print("Name:%s\nStrength:%s\ndefense:%s\nDexterity:%s\nLevel:%s\nEXP:%s"
          % (name, strength, defense, dexterity, lvl, exp) + "\n")


def character_has_leveled(char):
    exp = char["exp"]
    if exp >= 50:
        return True
    return False


def execute_glowup_protocol(char, check): #
    if check:
        print(char["name"], "has leveled up!\n\nNew stats:")
        char["max_health"] *= 0.5
        char["health"] *= 0.5
        char["strength"] *= 0.5
        char["defense"] *= 0.5
        char["dexterity"] *= 0.5
        char["level"] = char["level"] + 1
        char["exp"] = 0
        display_character_info(char)
    return char


def execute_challenge_protocol(char): #
    print("\n***\nCombat has initiated\n***\n")
    enemy = return_entity(char["level"])
    while enemy["health"] > 0 and char["health"] > 0:
        print("\n" + char['name'], "current HP:", char["health"])
        print(enemy['name'], "current HP:", str(enemy["health"]) + '\n')
        action = input("Please enter an action:")
        if action == '1':
            attack(char, enemy)
        if enemy["health"] <= 0:
            char["exp"] += enemy["exp"]
            print("\n" + enemy["name"], "had been defeated\n")
            break
        attack(enemy, char)
    print("\n***\nCombat had ended\n***\n")
    char["health"] = char["max_health"]
    return char


def check_if_goal_attained(char):
    if char["goal"]:
        return True
    return False


character = make_character()
while True:
    check_level = character_has_leveled(character)
    execute_glowup_protocol(character, check_level)
    move = input("Please enter an action:")
    if move == '1':
        display_character_info(character)
    elif move == '2':
        execute_challenge_protocol(character)
    elif move == 'q':
        break




