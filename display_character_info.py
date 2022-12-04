from unittest import TestCase
from unittest.mock import patch
import io

from encounter import display_character_info, attack


class DisplayCharacterInfoTest(TestCase):

    def setUp(self) -> None:
        self.character = {
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

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_info(self, mock_stdout):
        display_character_info(self.character)
        expected = "Character information:\n" \
                   "Name: Player\n" \
                   "Health: 50\n" \
                   "Strength: 10\n" \
                   "Defense: 10\n" \
                   "Dexterity: 10\n" \
                   "Level: 1\n" \
                   "Skills: ['Basic Attack']\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
