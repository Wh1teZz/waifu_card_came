
import json

def setup_game():
    with open("data/base_game_data.json") as f1:
        data = json.load(f1)
        with open("data/current_game_data.json", "w") as f2:
            json.dump(data, f2)

    with open("data/base_player_data.json") as f3:
        data = json.load(f3)
        with open("data/current_player_data.json", "w") as f4:
            json.dump(data, f4)

    print("Data has successfully been reset!")

if __name__ == "__main__":
    setup_game()