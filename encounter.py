"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""
import time


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
    print("Name: %s\n"
          "Health: %s\n"
          "Strength: %s\n"
          "Defense: %s\n"
          "Dexterity: %s\n"
          "Level: %s\n"
          "Skills: %s\n"
          % (char["name"],
             char["max_health"],
             char["strength"],
             char["defense"],
             char["dexterity"],
             char["level"],
             list(char["skills"].keys()),) + "\n")


def character_has_leveled(char):
    exp = char["exp"]
    if exp >= 50:
        return True
    return False


def execute_glowup_protocol(char, check):
    if check:
        print(f"{char['name']} has leveled up!\n\nNew Stats:\n"
              f"Name: {char['name']}\n"
              f"Health: {char['max_health']} -> {char['max_health'] * 1.5}\n"
              f"Strength: {char['strength']} -> {char['strength'] * 1.5}\n"
              f"Defense: {char['defense']} -> {char['defense'] * 1.5}\n"
              f"Dexterity: {char['dexterity']} -> {char['dexterity'] * 1.5}\n"
              f"Level: {char['level']} -> {char['level'] + 1}"
              )
        char["max_health"] *= 1.5
        char["health"] *= 1.5
        char["strength"] *= 1.5
        char["defense"] *= 1.5
        char["dexterity"] *= 1.5
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
    print("\n***\nCombat has initiated\n***\n")
    enemy = return_entity(char["level"])
    while enemy["health"] > 0 and char["health"] > 0:
        moves = []
        moves.extend(char["skills"])
        valid_moves = enumerate(moves, 1)
        print("\n***\nValid Moves:")
        for count, value in valid_moves:
            print(str(count) + ":", value)
        print(f"\n{char['name']}'s current HP:, {char['health']}")
        print(f"{enemy['name']}'s current HP: {enemy['health']} \n")
        action = input("Please enter an action:")
        if action == '1':
            time.sleep(0.5)
            char['skills']["Basic Attack"](char, enemy)
        if action == '2':
            if "Double Strike" not in char["skills"]:
                print("You do not know that move")
                continue
            else:
                time.sleep(0.5)
                print(f"{char['name']} uses {list(char['skills'].keys())[1]}.")
                char['skills']["Double Strike"](char, enemy)
        if action == '3':
            if "Guard" not in char["skills"]:
                print("You do not know that move")
            else:
                time.sleep(0.5)
                print(f"{char['name']} uses {list(char['skills'].keys())[2]}.")
                char['skills']["Guard"](char, enemy)
        if enemy["health"] <= 0:
            char["exp"] += enemy["exp"]
            print(f"\n{enemy['name']} has been defeated!\n")
            break
        time.sleep(0.5)
        attack(enemy, char)
        time.sleep(0.5)
        if char["health"] <= 0:
            char["exp"] -= enemy["exp"]
            print(f"\n{char['name']} has been defeated...\n\n")
            return char
    print("\n***\nCombat has ended\n***\n")
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
        check_level = character_has_leveled(character)
        if check_level:
            execute_glowup_protocol(character, check_level)
        valid_moves = enumerate(["Display character information", "Start encounter"], 1)
        print("Actions available:\n")
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
        print("\nCongratulations! You have successfully escaped the bandits!")


if __name__ == "__main__":
    main()
