import io
from unittest import TestCase
from unittest.mock import patch

from encounter import chance_encounter, attack


class ChanceEncounterTest(TestCase):
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
                "Double Strike": attack
            }
        }

    @patch('builtins.input', side_effect=["0"])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_chance_encounter_one(self, mock_output, random_number_generator, mock_input):
        chance_encounter(self.character)
        actual = mock_output.getvalue()
        expected = "Nobody notices you.\n"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["0"])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_chance_encounter_two(self, mock_output, random_number_generator, mock_input):
        chance_encounter(self.character)
        actual = mock_output.getvalue()
        expected = "You have been spotted!\n"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["0"])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_chance_encounter_three(self, mock_output, random_number_generator, mock_input):
        chance_encounter(self.character)
        actual = mock_output.getvalue()
        expected = "You have been spotted!\n"
        self.assertEqual(expected, actual)
