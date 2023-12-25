```python
import unittest
from unittest.mock import patch
from io import StringIO
from utils import Utils
from character import Character

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.environment = [
            {'terrain': 'grass', 'enemy': None, 'item': None},
            {'terrain': 'water', 'enemy': 'shark', 'item': 'boat'},
            {'terrain': 'mountain', 'enemy': 'dragon', 'item': 'sword'}
        ]
        self.character = Character()

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_environment(self, mock_stdout):
        Utils.print_environment(self.environment)
        expected_output = "Position 0: Terrain - grass, Enemy - None, Item - None\n" \
                          "Position 1: Terrain - water, Enemy - shark, Item - boat\n" \
                          "Position 2: Terrain - mountain, Enemy - dragon, Item - sword\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_character_status_alive(self, mock_stdout):
        self.character.position = 1
        Utils.print_character_status(self.character)
        expected_output = "Character is at position 1.\nCharacter is still on the way to the goal.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_character_status_dead(self, mock_stdout):
        self.character.alive = False
        Utils.print_character_status(self.character)
        expected_output = "Character is dead.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_game_over_message(self, mock_stdout):
        Utils.print_game_over_message()
        expected_output = "Game Over\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_congratulations_message(self, mock_stdout):
        Utils.print_congratulations_message()
        expected_output = "Congratulations! You have reached the goal.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
```
