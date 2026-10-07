# Import
import json

# This function serves as a game saver.

def save_game(items):

    # This reads the already created file and converts the JSON data back to Python, assigning it to a variable.

    with open("Project/saved_data_package/saved_game_data.json", "r") as file:
        save_data = json.load(file)

    # This updates the items with the new version of items that has been passed to the function:

    save_data["items"] = items

    # This overwrites the file with the new updated items:

    with open("Project/saved_data_package/saved_game_data.json", "w") as file:
        json.dump(save_data, file)
