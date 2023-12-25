```python
import unittest
from unittest.mock import Mock
from game_environment import GameEnvironment
from ai import AI
from character import Character

class TestGameEnvironment(unittest.TestCase):
    def setUp(self):
        self.game_env = GameEnvironment()
        self.ai = AI()
        self.character = Character()

    def test_generate(self):
        self.game_env.generate(self.ai)
        self.assertIsNotNone(self.game_env.environment)

    def test_start_without_generate(self):
        with self.assertRaises(Exception):
            self.game_env.start(self.character)

    def test_start_with_generate(self):
        self.game_env.generate(self.ai)
        self.character.is_alive = Mock(return_value=True)
        self.character.has_reached_goal = Mock(return_value=False)
        with self.assertRaises(StopIteration):
            self.game_env.start(self.character)

    def test_start_with_character_dead(self):
        self.game_env.generate(self.ai)
        self.character.is_alive = Mock(return_value=False)
        self.character.has_reached_goal = Mock(return_value=False)
        with self.assertRaises(StopIteration):
            self.game_env.start(self.character)

    def test_start_with_character_reached_goal(self):
        self.game_env.generate(self.ai)
        self.character.is_alive = Mock(return_value=True)
        self.character.has_reached_goal = Mock(return_value=True)
        with self.assertRaises(StopIteration):
            self.game_env.start(self.character)

if __name__ == '__main__':
    unittest.main()
```
