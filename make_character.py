"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""


def make_character():
    name = input("What is your name?\n")
    character_board ={
        "name": name,
        "Strength": 10,
        "Vitality": 10,
        "Dexterity": 10,
        "EXP": 0
    }
    return character_board


def display_character_info(char):
    name = character["name"]
    strength = character["Strength"]
    vitality = character["Vitality"]
    dexterity = character["Dexterity"]
    exp = character["EXP"]
    print("Name:%s\nStrength:%s\nVitality:%x\nDexterity:%s\nEXP:%s" % (name, strength, vitality, dexterity, exp))


def character_has_leveled(char):
    exp = char["EXP"]
    if exp > 50:
        return True
    return False






character = make_character()
display_character_info(character)
