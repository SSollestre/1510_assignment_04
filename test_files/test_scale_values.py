from unittest import TestCase

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

    def test_scale_values_level_two(self):
        expected = {
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
        actual = scale_values(self.character_one)
        self.assertEqual(expected, actual)

    def test_scale_values_level_three(self):
        expected = {
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
        actual = scale_values(self.character_two)
        self.assertEqual(expected, actual)
