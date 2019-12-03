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


# Counting steps to each intersection
def step_counter(line: str, coords: list):
    """
    Parameters:
        line (str): The raw line input
        coords (list): The intersection coords to count to

    Returns:
        steps (dict): A dict with the steps to each coords
    """
    coord_x = 0
    coord_y = 0
    step = 1
    steps = {}
    raw_input = line.split(",")
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
            if coord in coords:
                if coord in steps.keys():
                    if steps[coord] > step:
                        steps[coord] = step
                    else:
                        pass
                else:
                    steps[coord] = step
            step += 1
    return steps


# Finding the common intersections
intersections = list(set(grid("Line 1", line_1)["Line 1"]).intersection(grid("Line 2", line_2)["Line 2"]))

# Finding the distance to each intersection
steps_line_1 = step_counter(line_1, intersections)
steps_line_2 = step_counter(line_2, intersections)

for value in steps_line_1.keys():
    # Adding steps
    steps_line_1[value] = steps_line_1[value] + steps_line_2[value]
print(min(steps_line_1.values()))
