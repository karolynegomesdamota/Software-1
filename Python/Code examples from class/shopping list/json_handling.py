# This for creating and saving json file:

"""
import json

save_data = {
    "player":"Karo",
    "level":"15",
    "items":["sword, potion"]
}

with open("save_data.json", "w") as file:
    json.dump(save_data, file)
"""
# This for reading json file:

"""
import json

save_data = {
    "player":"Karo",
    "level":"15",
    "items":["sword, potion"]
}

with open("save_data.json", "r") as file:
    file_data = json.load(file)
print(f"Player: {file_data["player"]}")

"""

#Exercise 1

# Create dictionary and save it to a file

import json

movies = {
    "movie_name":"Name 1",
    "movie_year":"2000",
    "movie_actor":"Actor A and Actor B"
}

with open("movie_exercise.json", "w") as file:
    json.dump(movies, file)

# Read it back and print the title, year and actors.

with open("movie_exercise.json", "r") as file:
    file_data = json.load(file)

print(f'Movie: {file_data["movie_name"]}')
print(f'Movie: {file_data["movie_year"]}')
print(f'Movie: {file_data["movie_actor"]}')