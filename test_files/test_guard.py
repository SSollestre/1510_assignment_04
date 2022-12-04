from unittest import TestCase
from unittest.mock import patch
import io


from encounter import guard


class TestGuard(TestCase):
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
    def test_guard_bandit(self, mock_output):
        expected_return = {
            "name": "Player",
            "max_health": 50,
            "health": 61.25,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "exp": 0,
            "goal": False,
            "skills": {
                "Guard": guard
            }
        }
        expected_print = f"{self.character['name']} raises their guard.\n"
        actual_return = guard(self.character, self.bandit)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guard_lieutenant(self, mock_output):
        expected_return = {
            "name": "Player",
            "max_health": 50,
            "health": 91.25,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "exp": 0,
            "goal": False,
            "skills": {
                "Guard": guard
            }
        }
        expected_print = f"{self.character['name']} raises their guard.\n"
        actual_return = guard(self.character, self.lieutenant)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guard_chief(self, mock_output):
        expected_return = {
            "name": "Player",
            "max_health": 50,
            "health": 91.25,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "exp": 0,
            "goal": False,
            "skills": {
                "Guard": guard
            }
        }
        expected_print = f"{self.character['name']} raises their guard.\n"
        actual_return = guard(self.character, self.chief)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)
