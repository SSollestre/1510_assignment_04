"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""


def make_character():
    name = input("What is your name?\n")
    character_board = {
        "name": name,
        "health": 50,
        "strength": 10,
        "vitality": 10,
        "dexterity": 10,
        "level": 1,
        "experience": 0,
        "goal": False
    }
    return character_board


def return_entity(level):
    bandit = {
        "name": "Bandit",
        "health": 50,
        "strength": 10,
        "vitality": 10,
        "dexterity": 10,
        "level": 1,
    }

    bandit_lieutenant = {
        "name": "Bandit Lieutenant",
        "health": 50,
        "strength": 10,
        "vitality": 10,
        "dexterity": 10,
        "level": 2,
    }

    bandit_chief = {
        "name": "Bandit Chief",
        "health": 50,
        "strength": 10,
        "vitality": 10,
        "dexterity": 10,
        "level": 3,
    }

    if level == 1:
        return bandit

    elif level == 2:
        return bandit_lieutenant

    elif level == 3:
        return bandit_chief

def display_character_info(char):
    name = char["name"]
    strength = char["Strength"]
    vitality = char["Vitality"]
    dexterity = char["Dexterity"]
    exp = character["Experience"]
    lvl = character["Level"]
    print("Name:%s\nStrength:%s\nVitality:%s\nDexterity:%s\nLevel:%s\nEXP:%s"
          % (name, strength, vitality, dexterity, lvl, exp) + "\n")


def character_has_leveled(char):
    exp = char["Experience"]
    if exp > 50:
        return True
    return False


def execute_glowup_protocol(char, check):
    if check:
        char["Level"] = char["Level"] + 1
        char["Experience"] = 0


def execute_challenge_protocol(char):
    bandit = {
        "Health": 50,
        "Experience": 25
    }
    while bandit["Health"] > 0 and char["Health"] > 0:
        action = input("What do you want to do?")
        print("You %s" % action)
        bandit["Health"] = 0
        char["Goal"] = True


def check_if_goal_attained(char):
    if char["Goal"]:
        return True
    return False


character = make_character()
display_character_info(character)
character["Experience"] = 51
status = character_has_leveled(character)
goal = check_if_goal_attained(character)
print(goal)

execute_glowup_protocol(character, status)
display_character_info(character)
execute_challenge_protocol(character)
goal = check_if_goal_attained(character)
print(goal)
