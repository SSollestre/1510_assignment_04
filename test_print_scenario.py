from unittest import TestCase
from unittest.mock import patch
import io
from map import Map
from game import print_scenario


class PrintScenarioTest(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario(self, mock_stdout):
        print_scenario(Map(2, 2, 0, 0, [((0, 0), (0, 1)), ((0, 0), (1, 0)), ((1, 0), (1, 1)), ((0, 1), (1, 1))]))
        expected = 'Current location (0, 0)''you wake up in a dark damp cave.''You remember being knocked out.''It seems that you have been kidnapped.'
        self.assertEqual(mock_stdout.getvalue(), expected)
