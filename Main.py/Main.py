# main.py
import game
import data_manager

# Load previous game data (if available)
try:
    game_data = data_manager.load_game_data("game_data.json")
    print("Game data loaded:", game_data)
except FileNotFoundError:
    game_data = {"player": {"score": 0, "level": 1}}

# Start the game
if __name__ == "__main__":
    game.game_loop()

    # After the game, save data
    game_data["player"]["score"] = 2000  # Example of updating data
    data_manager.save_game_data("game_data.json", game_data)
