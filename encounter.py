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
        "goal": False,
        "skills": {
            "Basic Attack": attack
        }
    }
    return character_board


def attack(char, enemy):
    damage = char["strength"] - (0.25 * enemy["defense"])
    enemy["health"] -= damage
    print(char["name"], "strikes", enemy["name"], "for", damage, "damage!")
    return enemy


def double_strike(char, enemy):
    damage = (char["strength"] - (0.25 * enemy["defense"])) * 0.75
    enemy["health"] -= damage * 2
    print(char["name"], "strikes", enemy["name"], "for", damage, "damage!")
    print(char["name"], "strikes", enemy["name"], "for", damage, "damage!")
    return enemy


def guard(char, enemy):
    print(char["name"], "braces themselves")
    damage = (enemy["strength"] - (0.25 * char["defense"])) * 1.5
    char["health"] += damage
    return char


def return_entity(level):
    bandit = {
        "name": "Bandit",
        "health": 50,
        "strength": 5,
        "defense": 10,
        "dexterity": 10,
        "level": 1,
        "goal": False,
        "exp": 25
    }

    bandit_lieutenant = {
        "name": "Bandit Lieutenant",
        "health": 50,
        "strength": 30,
        "defense": 10,
        "dexterity": 10,
        "level": 2,
        "goal": False,
        "exp": 25
    }

    bandit_chief = {
        "name": "Bandit Chief",
        "health": 150,
        "strength": 30,
        "defense": 20,
        "dexterity": 10,
        "level": 3,
        "goal": True,
        "exp": 25
    }

    if level == 1:
        return bandit

    elif level == 2:
        return bandit_lieutenant

    elif level == 3:
        return bandit_chief


def display_character_info(char):
    print("\nCharacter information:\n")
    name = char["name"]
    strength = char["strength"]
    defense = char["defense"]
    dexterity = char["dexterity"]
    exp = char["exp"]
    lvl = char["level"]
    skills = char["skills"]
    print("Name:%s\nStrength:%s\ndefense:%s\nDexterity:%s\nLevel:%s\nSkills:%s\nEXP:%s"
          % (name, strength, defense, dexterity, lvl, list(skills.keys()), exp) + "\n")


def character_has_leveled(char):
    exp = char["exp"]
    if exp >= 50:
        return True
    return False


def execute_glowup_protocol(char, check):
    if check:
        print(char["name"], "has leveled up!\n\nNew stats:")
        char["max_health"] *= 1.5
        char["health"] *= 1.5
        char["strength"] *= 1.5
        char["defense"] *= 1.5
        char["dexterity"] *= 1.5
        char["level"] = char["level"] + 1
        char["exp"] = 0
        if char['level'] == 2:
            char["skills"]["Double Strike"] = double_strike
        display_character_info(char)
        if char['level'] == 3:
            char["skills"]["Guard"] = guard
        display_character_info(char)
    return char


def execute_challenge_protocol(char):
    print("\n***\nCombat has initiated\n***\n")
    enemy = return_entity(char["level"])
    while enemy["health"] > 0 and char["health"] > 0:
        moves = []
        moves.extend(char["skills"])
        valid_moves = enumerate(moves, 1)
        print("\nValid Moves:")
        for count, value in valid_moves:
            print(count, value)
        print("\n" + char['name'], "current HP:", char["health"])
        print(enemy['name'], "current HP:", str(enemy["health"]) + '\n')
        action = input("Please enter an action:")
        if action == '1':
            char['skills']["Basic Attack"](char, enemy)
        if action == '2':
            if "Double Strike" not in char["skills"]:
                print("You do not know that move")
            else:
                print(char['name'], "uses", list(char['skills'].keys())[1])
                char['skills']["Double Strike"](char, enemy)
        if action == '3':
            if "Guard" not in char["skills"]:
                print("You do not know that move")
            else:
                print(char['name'], "uses", list(char['skills'].keys())[1])
                char['skills']["Guard"](char, enemy)
        if enemy["health"] <= 0:
            char["exp"] += enemy["exp"]
            print("\n" + enemy["name"], "has been defeated\n")
            break
        attack(enemy, char)
        if char["health"] <= 0:
            char["exp"] -= enemy["exp"]
            print("\n" + char["name"], "has been defeated\n\n")
            return char
    print("\n***\nCombat had ended\n***\n")
    char["health"] = char["max_health"]
    char["goal"] = enemy["goal"]
    return char


def check_if_goal_attained(char):
    if char["goal"]:
        return True
    return False


def main():
    character = make_character()
    achieved_goal = False
    while not achieved_goal and character["health"] > 0:
        valid_moves = enumerate(["Display character information", "Start encounter"], 1)
        print("Actions available:\n")
        for count, value in valid_moves:
            print(count, value)
        check_level = character_has_leveled(character)
        if check_level:
            execute_glowup_protocol(character, check_level)
            continue
        move = input("\nPlease enter an action:")
        if move == '1':
            display_character_info(character)
        elif move == '2':
            execute_challenge_protocol(character)
        elif move == 'q':
            break
        achieved_goal = check_if_goal_attained(character)
    print("\nCongratulations! You have escaped the bandits!")


if __name__ == "__main__":
    main()
