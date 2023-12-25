```python
import unittest
from ai import AI
from game_environment import GameEnvironment
from config import Config

class TestAI(unittest.TestCase):
    def setUp(self):
        self.ai = AI()
        self.game_env = GameEnvironment()
        self.config = Config()

    def test_generate_environment(self):
        # Generate the game environment
        self.ai.generate_environment(self.game_env)

        # Check if the environment has been generated
        self.assertIsNotNone(self.game_env.environment)

        # Check if the environment size is correct
        self.assertEqual(len(self.game_env.environment), self.config.environment_size)

        # Check if the environment contains the correct keys
        for env in self.game_env.environment:
            self.assertIn('terrain', env)
            self.assertIn('enemy', env)
            self.assertIn('item', env)

            # Check if the terrain, enemy, and item types are correct
            self.assertIn(env['terrain'], self.config.terrain_types)
            self.assertIn(env['enemy'], self.config.enemy_types)
            self.assertIn(env['item'], self.config.item_types)

if __name__ == '__main__':
    unittest.main()
```
