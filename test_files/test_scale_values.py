from unittest import TestCase
from unittest.mock import patch
import io

from encounter import scale_values, attack, double_strike, guard


class TestScaleValues(TestCase):
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

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_scale_values_level_two(self, mock_output):
        expected_return = {
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
                "Basic Attack": attack,
                "Double Strike": double_strike
            }
        }
        expected_display = "Skills:['Basic Attack'] + ['Double Strike']\n\n"
        actual_return = scale_values(self.character_one)
        actual_display = mock_output.getvalue()
        self.assertEqual(expected_display, actual_display)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_scale_values_level_three(self, mock_output):
        expected_return = {
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
        expected_display = "Skills:['Basic Attack', 'Double Strike'] + ['Guard']\n\n"
        actual_return = scale_values(self.character_two)
        actual_display = mock_output.getvalue()
        self.assertEqual(expected_display, actual_display)
        self.assertEqual(expected_return, actual_return)
