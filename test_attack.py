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
        expected_return = {
            "name": "Bandit",
            "health": 42.5,
            "strength": 10,
            "defense": 10,
            "dexterity": 10,
            "level": 1,
            "goal": False,
            "exp": 25
        }
        expected_print = f"{self.character['name']} strikes {self.enemy['name']} for 7.5 damage!\n"
        actual_return = attack(self.character, self.enemy)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_enemy_to_player(self, mock_output):
        expected_return = {
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
        expected_print = f"{self.enemy['name']} strikes {self.character['name']} for 7.5 damage!\n"
        actual_return = attack(self.enemy, self.character)
        system_print = mock_output.getvalue()
        self.assertEqual(expected_print, system_print)
        self.assertEqual(expected_return, actual_return)

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
