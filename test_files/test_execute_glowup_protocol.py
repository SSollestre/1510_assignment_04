from unittest import TestCase
from unittest.mock import patch
import io

from encounter import execute_glowup_protocol, attack, double_strike, guard


class TestExecuteGlowupProtocol(TestCase):
    def setUp(self) -> None:
        self.character_one = {
            "name": "Player",
            "max_health": 50,
            "health": 50,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "exp": 50,
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
            "exp": 50,
            "goal": False,
            "skills": {
                "Basic Attack": attack,
                "Double Strike": double_strike
            }
        }

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_glowup_protocol_level_two(self, mock_output):
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
        expected_display = (f"{self.character_one['name']} has leveled up!\n\nNew Stats:\n\n"
                            f"Name: {self.character_one['name']}\n"
                            f"Health: {self.character_one['max_health']} -> {self.character_one['max_health'] * 1.5}\n"
                            f"Strength: {self.character_one['strength']} -> {self.character_one['strength'] * 1.5}\n"
                            f"Defense: {self.character_one['defense']} -> {self.character_one['defense'] * 1.5}\n"
                            f"Dexterity: {self.character_one['dexterity']} -> {self.character_one['dexterity'] * 1.5}\n"
                            f"Level: {self.character_one['level']} -> {self.character_one['level'] + 1}\n"
                            f"Skills:['Basic Attack'] + ['Double Strike']\n\n")
        actual_return = execute_glowup_protocol(self.character_one)
        actual_display = mock_output.getvalue()
        self.assertEqual(expected_display, actual_display)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_glowup_protocol_level_three(self, mock_output):
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
        expected_display = (f"{self.character_two['name']} has leveled up!\n\nNew Stats:\n\n"
                            f"Name: {self.character_two['name']}\n"
                            f"Health: {self.character_two['max_health']} -> {self.character_two['max_health'] * 1.5}\n"
                            f"Strength: {self.character_two['strength']} -> {self.character_two['strength'] * 1.5}\n"
                            f"Defense: {self.character_two['defense']} -> {self.character_two['defense'] * 1.5}\n"
                            f"Dexterity: {self.character_two['dexterity']} -> {self.character_two['dexterity'] * 1.5}\n"
                            f"Level: {self.character_two['level']} -> {self.character_two['level'] + 1}\n"
                            f"Skills:['Basic Attack', 'Double Strike'] + ['Guard']\n\n")
        actual_return = execute_glowup_protocol(self.character_two)
        actual_display = mock_output.getvalue()
        self.assertEqual(expected_display, actual_display)
        self.assertEqual(expected_return, actual_return)
