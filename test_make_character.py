from unittest import TestCase
from unittest.mock import patch

from encounter import make_character, attack


class TestMakeCharacter(TestCase):
    @patch('builtins.input', side_effect=["Player"])
    def test_make_character_standard(self, mock_input):
        actual = make_character()
        expected = {
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
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[""])
    def test_make_character_empty(self, mock_input):
        actual = make_character()
        expected = {
            "name": "",
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
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["P"])
    def test_make_character_one(self, mock_input):
        actual = make_character()
        expected = {
            "name": "P",
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
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Pl"])
    def test_make_character_even(self, mock_input):
        actual = make_character()
        expected = {
            "name": "Pl",
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
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Pla"])
    def test_make_character_odd(self, mock_input):
        actual = make_character()
        expected = {
            "name": "Pla",
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
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["PLAYER"])
    def test_make_character_upper(self, mock_input):
        actual = make_character()
        expected = {
            "name": "PLAYER",
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
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["player"])
    def test_make_character_lower(self, mock_input):
        actual = make_character()
        expected = {
            "name": "player",
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
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["P1@y3r"])
    def test_make_character_special(self, mock_input):
        actual = make_character()
        expected = {
            "name": "P1@y3r",
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
        self.assertEqual(expected, actual)
