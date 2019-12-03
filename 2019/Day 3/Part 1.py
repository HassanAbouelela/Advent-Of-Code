import re

# Loading the raw input
with open("input.txt", "r") as input_file:
    line_1 = input_file.readline()
    line_2 = input_file.readline()


# Making grid system
def grid(line_name: str, raw_input: str):
    """
    Parameters:
        line_name (str): The name of the line
        raw_input (str): The raw line input

    Returns:
        coords (dict): A dict of all the coordinates the wire touched
    """
    import utils

    coords = {}
    coord_x = 0
    coord_y = 0
    raw_input = raw_input.split(",")
    for instruction in raw_input:
        for number in range(int(instruction[re.search("[1-9]", instruction).start():])):
            if "R" in instruction:
                coord_x += 1
            elif "L" in instruction:
                coord_x -= 1
            elif "U" in instruction:
                coord_y += 1
            elif "D" in instruction:
                coord_y -= 1
            coord = f"{coord_x}, {coord_y}"
            utils.DataMethods.DictionaryMethods.update_dict(coords, line_name, coord)
    return coords


# Manhattan distance between two coordinates
def man_dist_calc(coords: str):
    """
    Parameters:
        coords (str): The coordinates to check distance to

    Returns:
        (int): Manhattan distance between two points
    """
    coords = coords.split(",")
    return int(coords[0]) + int(coords[1])


# Finding the shortest manhattan distance
print(min(
    map(man_dist_calc,
        list(set(grid("Line 1", line_1)["Line 1"]).intersection(grid("Line 2", line_2)["Line 2"])))))
