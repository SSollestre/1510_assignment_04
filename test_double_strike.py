from unittest import TestCase
from unittest.mock import patch
import io


from encounter import double_strike


class TestDoubleStrike(TestCase):
    def setUp(self) -> None:
        self.character = {
            "name": "Player",
            "max_health": 50 * 1.5,
            "health": 50 * 1.5,
            "strength": 10 * 1.5,
            "defense": 10 * 1.5,
            "dexterity": 10 * 1.5,
            "level": 2,
            "exp": 0,
            "goal": False,
            "skills": {
                "Double Strike": double_strike
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
    def test_double_strike_player_to_bandit(self, mock_output):
        expected_return = {
            "name": "Bandit",
            "health": 31.25,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "goal": False,
            "exp": 25
        }
        damage = (self.character["strength"] - (0.25 * self.bandit["defense"])) * 0.75
        expected_print = (f"{self.character['name']} strikes {self.bandit['name']} for {damage} damage!\n" 
                          f"{self.character['name']} strikes {self.bandit['name']} for {damage} damage!\n")
        actual_return = double_strike(self.character, self.bandit)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_double_strike_player_to_lieutenant(self, mock_output):
        expected_return = {
            "name": "Bandit Lieutenant",
            "health": 31.25,
            "strength": 30,
            "defense": 10,
            "dexterity": 10,
            "level": 2,
            "goal": False,
            "exp": 25
        }
        damage = (self.character["strength"] - (0.25 * self.lieutenant["defense"])) * 0.75
        expected_print = (f"{self.character['name']} strikes {self.lieutenant['name']} for {damage} damage!\n" 
                          f"{self.character['name']} strikes {self.lieutenant['name']} for {damage} damage!\n")
        actual_return = double_strike(self.character, self.lieutenant)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_double_strike_player_to_chief(self, mock_output):
        expected_return = {
            "name": "Bandit Chief",
            "health": 135.0,
            "strength": 30,
            "defense": 20,
            "dexterity": 10,
            "level": 3,
            "goal": True,
            "exp": 25
        }
        damage = (self.character["strength"] - (0.25 * self.chief["defense"])) * 0.75
        expected_print = (f"{self.character['name']} strikes {self.chief['name']} for {damage} damage!\n" 
                          f"{self.character['name']} strikes {self.chief['name']} for {damage} damage!\n")
        actual_return = double_strike(self.character, self.chief)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)
