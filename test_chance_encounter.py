import io
from unittest import TestCase
from unittest.mock import patch

from encounter import chance_encounter


class ChanceEncounterTest(TestCase):

    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_chance_encounter_one(self, mock_output, random_number_generator):
        char = {"level": 1}
        chance_encounter(char)
        actual = mock_output.getvalue()
        expected = "Nobody notices you.\n"
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_chance_encounter_two(self, mock_output, random_number_generator):
        char = {"level": 2}
        chance_encounter(char)
        actual = mock_output.getvalue()
        expected = "You have been spotted!\n"
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_chance_encounter_three(self, mock_output, random_number_generator):
        char = {"level": 3}
        chance_encounter(char)
        actual = mock_output.getvalue()
        expected = "You have been spotted!\n"
        self.assertEqual(expected, actual)
