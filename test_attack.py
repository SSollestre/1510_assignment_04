from unittest import TestCase
from unittest.mock import patch
import io


from encounter import attack


class TestAttack(TestCase):

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
    def test_attack_player_to_bandit(self, mock_output):
        expected_return = {
            "name": "Bandit",
            "health": 42.5,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "goal": False,
            "exp": 25
        }
        damage = self.character["strength"] - (0.25 * self.bandit["defense"])
        expected_print = f"{self.character['name']} strikes {self.bandit['name']} for {damage} damage!\n"
        actual_return = attack(self.character, self.bandit)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_bandit_to_player(self, mock_output):
        expected_return = {
            "name": "Player",
            "max_health": 50,
            "health": 42.5,
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
        damage = self.bandit["strength"] - (0.25 * self.character["defense"])
        expected_print = f"{self.bandit['name']} strikes {self.character['name']} for {damage} damage!\n"
        actual_return = attack(self.bandit, self.character)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_lieutenant_to_player(self, mock_output):
        expected_return = {
            "name": "Player",
            "max_health": 50,
            "health": 22.5,
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
        damage = self.lieutenant["strength"] - (0.25 * self.character["defense"])
        expected_print = f"{self.lieutenant['name']} strikes {self.character['name']} for {damage} damage!\n"
        actual_return = attack(self.lieutenant, self.character)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_chief_to_player(self, mock_output):
        expected_return = {
            "name": "Player",
            "max_health": 50,
            "health": 22.5,
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
        damage = self.chief["strength"] - (0.25 * self.character["defense"])
        expected_print = f"{self.chief['name']} strikes {self.character['name']} for {damage} damage!\n"
        actual_return = attack(self.chief, self.character)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)
