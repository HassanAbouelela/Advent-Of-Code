from intcode_computer import intcode_computer

# Loading the input
with open("input.txt", "r") as input_file:
    raw_data = input_file.read().split(",")

print(intcode_computer(raw_data))
