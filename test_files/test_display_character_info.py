from unittest import TestCase
from unittest.mock import patch
import io

from encounter import display_character_info, attack, double_strike, guard


class DisplayCharacterInfoTest(TestCase):

    def setUp(self) -> None:
        self.character_one = {
            "name": "Player",
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

        self.character_two = {
            "name": "Player",
            "max_health": int(50 * 1.5),
            "health": int(50 * 1.5),
            "strength": int(10 * 1.5),
            "defense": int(10 * 1.5),
            "dexterity": int(10 * 1.5),
            "level": 2,
            "exp": 0,
            "goal": False,
            "skills": {
                "Basic Attack": attack,
                "Double Strike": double_strike
            }
        }

        self.character_three = {
            "name": "Player",
            "max_health": int((50 * 1.5) * 1.5),
            "health": int(((50 * 1.5) * 1.5)),
            "strength": int((10 * 1.5) * 1.5),
            "defense": int((10 * 1.5) * 1.5),
            "dexterity": int((10 * 1.5) * 1.5),
            "level": 3,
            "exp": 0,
            "goal": False,
            "skills": {
                "Basic Attack": attack,
                "Double Strike": double_strike,
                "Guard": guard
            }
        }

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_info_level_one(self, mock_stdout):
        display_character_info(self.character_one)
        actual = mock_stdout.getvalue()
        expected = ("\nCharacter information:\n"
                    "Name: Player\n"
                    "Health: 50\n"
                    "Strength: 10\n"
                    "Defense: 10\n"
                    "Dexterity: 10\n"
                    "Level: 1\n"
                    "Skills: ['Basic Attack']\n\n")
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_info_level_two(self, mock_stdout):
        display_character_info(self.character_two)
        actual = mock_stdout.getvalue()
        expected = ("\nCharacter information:\n"
                    "Name: Player\n"
                    "Health: 75\n"
                    "Strength: 15\n"
                    "Defense: 15\n"
                    "Dexterity: 15\n"
                    "Level: 2\n"
                    "Skills: ['Basic Attack', 'Double Strike']\n\n")
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_info_level_three(self, mock_stdout):
        display_character_info(self.character_three)
        actual = mock_stdout.getvalue()
        expected = ("\nCharacter information:\n"
                    "Name: Player\n"
                    "Health: 112\n"
                    "Strength: 22\n"
                    "Defense: 22\n"
                    "Dexterity: 22\n"
                    "Level: 3\n"
                    "Skills: ['Basic Attack', 'Double Strike', 'Guard']\n\n")
        self.assertEqual(expected, actual)
