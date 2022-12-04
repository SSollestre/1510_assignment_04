from unittest import TestCase

from encounter import return_entity


class ReturnEntityTest(TestCase):

    def setUp(self):
        enemies = [
            {
                "name": "Bandit",
                "health": 50,
                "strength": 10,
                "defense": 10,
                "dexterity": 10,
                "level": 1,
                "goal": False,
                "exp": 25
            },

            {
                "name": "Bandit Lieutenant",
                "health": 50,
                "strength": 30,
                "defense": 10,
                "dexterity": 10,
                "level": 2,
                "goal": False,
                "exp": 25
            },

            {
                "name": "Bandit Chief",
                "health": 150,
                "strength": 30,
                "defense": 20,
                "dexterity": 10,
                "level": 3,
                "goal": True,
                "exp": 25
            }]

    def test_return_entity_1(self):
        expected = {
            "name": "Bandit",
            "health": 50,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "goal": False,
            "exp": 25
        }
        actual = return_entity(1)
        self.assertEqual(expected, actual)

    def test_return_entity_two(self):
        expected = {
            "name": "Bandit Lieutenant",
            "health": 50,
            "strength": 30,
            "defense": 10,
            "dexterity": 10,
            "level": 2,
            "goal": False,
            "exp": 25
        }
        actual = return_entity(2)
        self.assertEqual(expected, actual)

    def test_return_entity_three(self):
        expected = {
            "name": "Bandit Chief",
            "health": 150,
            "strength": 30,
            "defense": 20,
            "dexterity": 10,
            "level": 3,
            "goal": True,
            "exp": 25
        }
        actual = return_entity(3)
        self.assertEqual(expected, actual)
