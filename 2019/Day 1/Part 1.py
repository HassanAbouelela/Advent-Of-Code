import math

# Loading the raw input
with open("input.txt", "r") as input_file:
    raw_input = input_file.readlines()

numbers = []
# Calculating individual fuel requirements
for number in raw_input:
    numbers.append(math.floor(int(number)/3) - 2)

# Summing the individual fuel requirements
print(sum(numbers))
