from unittest import TestCase
from unittest.mock import patch

from encounter import make_character, attack


@patch('builtins.input', side_effect=["Player"])
class TestMakeCharacter(TestCase):
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
