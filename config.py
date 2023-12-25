```python
class Config:
    def __init__(self):
        # Define the size of the game environment
        self.environment_size = 100

        # Define the possible terrain types
        self.terrain_types = ['grass', 'sand', 'water', 'mountain']

        # Define the possible enemy types
        self.enemy_types = ['goblin', 'orc', 'dragon', None]

        # Define the possible item types
        self.item_types = ['sword', 'shield', 'potion', None]
```
