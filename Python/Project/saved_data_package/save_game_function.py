import json

def save_game(items):

    with open("Project/saved_data_package/saved_game_data.json", "r") as file:
        save_data = json.load(file)

    save_data["items"] = items

    with open("Project/saved_data_package/saved_game_data.json", "w") as file:
        json.dump(save_data, file)

    with open("Project/saved_data_package/saved_game_data.json", "w") as file:
        json.dump(save_data, file)