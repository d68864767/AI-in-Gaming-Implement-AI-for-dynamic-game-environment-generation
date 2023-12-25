```python
import unittest
from character import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character()

    def test_is_alive(self):
        self.assertEqual(self.character.is_alive(), True)

    def test_has_reached_goal(self):
        self.assertEqual(self.character.has_reached_goal(), False)

    def test_move(self):
        self.character.move(5)
        self.assertEqual(self.character.position, 5)

    def test_interact_with_environment(self):
        # Test interaction with an enemy
        environment = [{'terrain': 'grass', 'enemy': 'goblin', 'item': None}]
        self.character.interact_with_environment(environment)
        self.assertEqual(self.character.is_alive(), False)

        # Reset character
        self.character = Character()

        # Test interaction with an item
        environment = [{'terrain': 'grass', 'enemy': None, 'item': 'sword'}]
        self.character.interact_with_environment(environment)
        self.assertEqual(self.character.is_alive(), True)

        # Test reaching the goal
        environment = [{'terrain': 'grass', 'enemy': None, 'item': None}]
        self.character.interact_with_environment(environment)
        self.assertEqual(self.character.has_reached_goal(), True)

if __name__ == '__main__':
    unittest.main()
```
