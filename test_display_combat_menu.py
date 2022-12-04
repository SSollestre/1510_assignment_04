from unittest import TestCase
from unittest.mock import patch
import io

from encounter import display_combat_menu, attack


class DisplayCombatMenuTest(TestCase):

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
        self.bandit = {
            "name": "Bandit",
            "health": 50,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "goal": False,
            "exp": 25
        }

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_combat_menu(self, mock_stdout):
        display_combat_menu(self.character, self.bandit)
        expected = "***\n" \
                   "Valid Moves:\n" \
                   "0: Flee\n" \
                   "1: Basic Attack\n"\
                   "\n"\
                   "Player's current HP: 50\n" \
                   "Bandit's current HP: 50\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
