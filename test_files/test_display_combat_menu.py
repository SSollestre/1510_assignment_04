from unittest import TestCase
from unittest.mock import patch
import io

from encounter import display_combat_menu, attack, double_strike, guard


class DisplayCombatMenuTest(TestCase):

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
        self.lieutenant = {
            "name": "Bandit Lieutenant",
            "health": 50,
            "strength": 30,
            "defense": 10,
            "dexterity": 10,
            "level": 2,
            "goal": False,
            "exp": 25
        }
        self.chief = {
            "name": "Bandit Chief",
            "health": 150,
            "strength": 30,
            "defense": 20,
            "dexterity": 10,
            "level": 3,
            "goal": True,
            "exp": 25
        }

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_combat_menu_player_level_one(self, mock_stdout):
        display_combat_menu(self.character_one, self.bandit)
        expected = "***\n" \
                   "Valid Moves:\n" \
                   "0: Flee\n" \
                   "1: Basic Attack\n"\
                   "\n"\
                   "Player's current HP: 50\n" \
                   "Bandit's current HP: 50\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_combat_menu_player_level_two(self, mock_stdout):
        display_combat_menu(self.character_two, self.bandit)
        expected = "***\n" \
                   "Valid Moves:\n" \
                   "0: Flee\n" \
                   "1: Basic Attack\n" \
                   "2: Double Strike\n"\
                   "\n"\
                   "Player's current HP: 75\n" \
                   "Bandit's current HP: 50\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_combat_menu_player_level_three(self, mock_stdout):
        display_combat_menu(self.character_three, self.bandit)
        expected = "***\n" \
                   "Valid Moves:\n" \
                   "0: Flee\n" \
                   "1: Basic Attack\n"\
                   "2: Double Strike\n" \
                   "3: Guard\n\n"\
                   "Player's current HP: 112\n" \
                   "Bandit's current HP: 50\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_combat_menu_lieutenant(self, mock_stdout):
        display_combat_menu(self.character_one, self.lieutenant)
        expected = "***\n" \
                   "Valid Moves:\n" \
                   "0: Flee\n" \
                   "1: Basic Attack\n"\
                   "\n"\
                   "Player's current HP: 50\n" \
                   "Bandit Lieutenant's current HP: 50\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_combat_menu_chief(self, mock_stdout):
        display_combat_menu(self.character_one, self.chief)
        expected = "***\n" \
                   "Valid Moves:\n" \
                   "0: Flee\n" \
                   "1: Basic Attack\n"\
                   "\n"\
                   "Player's current HP: 50\n" \
                   "Bandit Chief's current HP: 150\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
