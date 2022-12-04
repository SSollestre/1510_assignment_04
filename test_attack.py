from unittest import TestCase
from unittest.mock import patch
import io


from encounter import attack


class TestAttack(TestCase):

    def setUp(self) -> None:
        character = {
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

        enemy = {
            "name": "Bandit",
            "health": 50,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "goal": False,
            "exp": 25
        }

        self.character = character
        self.enemy = enemy

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_player_to_enemy(self, mock_output):
        character = self.character
        enemy = self.enemy
        actual = attack(character, enemy)
        system_print = mock_output.getvalue()
        expected_print = "Player strikes Bandit for 7.5 damage!\n"

        expected = {
            "name": "Bandit",
            "health": 42.5,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "goal": False,
            "exp": 25
        }

        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_enemy_to_player(self, mock_output):
        character = {
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

        enemy = {
            "name": "Bandit",
            "health": 50,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "goal": False,
            "exp": 25
        }

        actual = attack(enemy, character)
        system_print = mock_output.getvalue()
        expected_print = "Bandit strikes Player for 7.5 damage!\n"

        expected = {
            "name": "Player",
            "max_health": 50,
            "health": 42.5,
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

        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_no_damage(self, mock_output):
        character = {
            "name": "Player",
            "max_health": 50,
            "health": 50,
            "strength": 0,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "exp": 0,
            "goal": False,
            "skills": {
                "Basic Attack": attack
            }
        }

        enemy = {
            "name": "Bandit",
            "health": 50,
            "strength": 10,
            "defense": 0,
            "dexterity": 10,
            "level": 1,
            "goal": False,
            "exp": 25
        }

        actual = attack(character, enemy)

        expected = {
            "name": "Bandit",
            "health": 50,
            "strength": 10,
            "defense": 0,
            "dexterity": 10,
            "level": 1,
            "goal": False,
            "exp": 25
        }

        self.assertEqual(expected, actual)
