import math

# Loading the raw input
with open("input.txt", "r") as input_file:
    raw_input = input_file.readlines()


fuel = []


# Run the math calculations
def cal(number: int):
    """
    Parameters:
        number (int): The number to do the calculations on

    Returns:
        (int): The final number
    """
    if math.floor((number/3)) - 2 > 0:
        return math.floor(number/3) - 2
    else:
        return 0


# Run individual components till required fuel is reached
for module in raw_input:
    module = int(module)
    module_fuel = cal(module)
    fuel_total = module_fuel
    while module_fuel > 0:
        module_fuel = cal(module_fuel)
        fuel_total += module_fuel
    fuel.append(fuel_total)

# Sum individual fuel requirements
print(sum(fuel))
