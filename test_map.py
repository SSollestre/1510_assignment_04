"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""
from unittest import TestCase
from map import Map


class TestMap(TestCase):

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

    def setUp(self):
        self.create_map = Map(3, 3, 0, 0, paths)

    def test_move(self):
        self.assertEqual(expected, actual)

    def test_print_map(self):
        self.assertEqual(expected, actual)
