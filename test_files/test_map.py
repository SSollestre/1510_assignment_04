from unittest import TestCase
from unittest.mock import patch
import io

from map import Map


class TestMap(TestCase):
    def setUp(self):
        paths = [((0, 0), (0, 1)),
                 ((0, 0), (1, 0)),
                 ((0, 1), (0, 2)),
                 ((0, 1), (1, 1)),
                 ((0, 2), (1, 2)),
                 ((1, 0), (1, 1)),
                 ((1, 1), (1, 2)),
                 ((1, 0), (2, 0)),
                 ((2, 0), (2, 1)),
                 ((2, 1), (2, 2)),
                 ((1, 1), (2, 1)),
                 ((1, 2), (2, 2))]
        self.chart = Map(3, 3, 1, 1, paths)

    def test_move_up(self):
        self.chart.move('w')
        expected = 0
        actual = self.chart.row
        self.assertEqual(expected, actual)

    def test_move_down(self):
        self.chart.move('s')
        expected = 2
        actual = self.chart.row
        self.assertEqual(expected, actual)

    def test_move_left(self):
        self.chart.move('a')
        expected = 0
        actual = self.chart.column
        self.assertEqual(expected, actual)

    def test_move_right(self):
        self.chart.move('d')
        expected = 2
        actual = self.chart.column
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map(self, mock_output):
        self.chart.print_map()
        expected = "[ ]-[ ]-[ ] \n" \
                   " |   |   |  \n" \
                   "[ ]-[x]-[ ] \n" \
                   " |   |   |  \n" \
                   "[ ]-[ ]-[ ] \n" \
                   "            \n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
