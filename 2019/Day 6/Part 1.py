import utils
import re

# Importing raw data
with open("input.txt", "r") as file:
    raw = file.read()

# Making planets list
planets = utils.DataMethods.StringMethods.multi_term_split(raw, "\n", ")")
raw = raw.splitlines()
planets.remove("COM")

# This can be sped up by counting the orbits of the planets as we reach them, and removing them from the list
# instead of checking them all
orbits = 0
for planet in planets:
    try:
        current = [i for i in raw if f"){planet}" in i][0]
    except IndexError:
        continue

    new_planet = ""
    while "COM" not in new_planet:
        orbits += 1
        new_planet = current[:re.search('\)', current).start()]
        try:
            current = [i for i in raw if f"){new_planet}" in i][0]
        except IndexError:
            continue

print(orbits)
