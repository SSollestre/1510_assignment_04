"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""


def make_character():
    name = input("What is your name?\n")
    character_board = {
        "name": name,
        "Strength": 10,
        "Vitality": 10,
        "Dexterity": 10,
        "Level": 1,
        "Experience": 0
    }
    return character_board


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


character = make_character()
display_character_info(character)
character["Experience"] = 51
status = character_has_leveled(character)
execute_glowup_protocol(character, status)
display_character_info(character)
