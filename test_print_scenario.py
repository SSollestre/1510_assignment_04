from unittest import TestCase
from unittest.mock import patch
import io
from map import Map
from game import print_scenario


class PrintScenarioTest(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_zero(self, mock_stdout):
        print_scenario(Map(2, 2, 0, 0, [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((1, 0), (1, 1)), ((0, 1), (1, 1))]))
        expected = 'Current location (0, 0)\n' \
                   'You wake up in a dark damp cave. You remember being knocked out.' \
                   ' It seems that you have been kidnapped.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_column(self, mock_stdout):
        print_scenario(Map(2, 2, 1, 0, [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((1, 0), (1, 1)), ((0, 1), (1, 1))]))
        expected = 'Current location (0, 1)\nYou hear scuffling and voices.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_row(self, mock_stdout):
        print_scenario(Map(2, 2, 0, 1, [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((1, 0), (1, 1)), ((0, 1), (1, 1))]))
        expected = 'Current location (1, 0)\nYou hear scuffling and voices.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_both_even(self, mock_stdout):
        print_scenario(Map(2, 2, 2, 2, [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((1, 0), (1, 1)), ((0, 1), (1, 1))]))
        expected = 'Current location (2, 2)\nIt`s very dark, you can`t make out anything.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_both_odd(self, mock_stdout):
        print_scenario(Map(2, 2, 1, 1, [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((1, 0), (1, 1)), ((0, 1), (1, 1))]))
        expected = 'Current location (1, 1)\nYou hear scuffling and voices.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)
