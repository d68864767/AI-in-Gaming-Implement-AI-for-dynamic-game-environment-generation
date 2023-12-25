```python
class Utils:
    @staticmethod
    def print_environment(environment):
        """
        Print the current state of the game environment.
        """
        for i, env in enumerate(environment):
            print(f"Position {i}: Terrain - {env['terrain']}, Enemy - {env['enemy']}, Item - {env['item']}")

    @staticmethod
    def print_character_status(character):
        """
        Print the current status of the character.
        """
        if character.is_alive():
            print(f"Character is at position {character.position}.")
            if character.has_reached_goal():
                print("Character has reached the goal.")
            else:
                print("Character is still on the way to the goal.")
        else:
            print("Character is dead.")

    @staticmethod
    def print_game_over_message():
        """
        Print the game over message.
        """
        print("Game Over")

    @staticmethod
    def print_congratulations_message():
        """
        Print the congratulations message.
        """
        print("Congratulations! You have reached the goal.")
```
