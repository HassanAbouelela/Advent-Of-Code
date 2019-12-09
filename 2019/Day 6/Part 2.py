import utils
import re

# Importing raw data
with open("input.txt", "r") as file:
    raw = file.read()

# Making planets list
planets = utils.DataMethods.StringMethods.multi_term_split(raw, "\n", ")")
raw = raw.splitlines()
planets.remove("COM")


# Finding path from objects to COM
def path_finder(search_object: str):
    path = []
    try:
        current = [i for i in raw if f"){search_object}" in i][0]
        new_planet = ""
        while "COM" not in new_planet:
            new_planet = current[:re.search('\)', current).start()]
            path.append(new_planet)
            current = [i for i in raw if f"){new_planet}" in i][0]
    except IndexError:
        pass
    return path


you_path = path_finder("YOU")
santa_path = path_finder("SAN")

# Finding First Common Intersection
common = [i for i in you_path if i in santa_path][0]

print(you_path.index(common) + santa_path.index(common))
