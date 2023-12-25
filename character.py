```python
class Character:
    def __init__(self):
        self.alive = True
        self.goal_reached = False
        self.position = 0

    def is_alive(self):
        """
        Check if the character is still alive.
        """
        return self.alive

    def has_reached_goal(self):
        """
        Check if the character has reached the goal.
        """
        return self.goal_reached

    def move(self, steps):
        """
        Move the character by a certain number of steps.
        """
        self.position += steps

    def interact_with_environment(self, environment):
        """
        Interact with the environment. This could involve fighting enemies, picking up items, etc.
        """
        # Get the current environment
        current_environment = environment[self.position]

        # Interact with the enemy
        if 'enemy' in current_environment:
            self.fight(current_environment['enemy'])

        # Interact with the item
        if 'item' in current_environment:
            self.pick_up_item(current_environment['item'])

        # Check if the goal has been reached
        if self.position == len(environment) - 1:
            self.goal_reached = True

    def fight(self, enemy):
        """
        Fight an enemy. This could involve losing health, etc.
        """
        # For simplicity, let's say that the character dies if they encounter an enemy
        self.alive = False

    def pick_up_item(self, item):
        """
        Pick up an item. This could involve gaining health, etc.
        """
        # For simplicity, let's say that the character gains health if they pick up an item
        pass
```
