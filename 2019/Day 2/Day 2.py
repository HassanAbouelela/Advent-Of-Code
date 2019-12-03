# Loading the raw input
with open("input.txt", "r") as input_file:
    raw = input_file.readline().split(",")


def fun(raw_input: list):
    func = "addition"
    i = 0
    li = []
    for number in raw_input:
        number = int(number)
        if i < 4:
            if i == 0:
                if number == 1:
                    func = "addition"
                elif number == 2:
                    func = "multiplication"
                elif number == 99:
                    break
                else:
                    i = 4
            elif i == 3:
                i = -1
                if func == "addition":
                    raw_input[number] = li[0] + li[1]
                elif func == "multiplication":
                    raw_input[number] = li[0] * li[1]
                li = []
            else:
                li.append(int(raw_input[number]))
            i += 1
    return raw_input


noun = 0
verb = 0
while noun <= 99:
    while verb <= 99:
        raw_modified = []
        raw_modified.extend(raw)
        raw_modified[1] = noun
        raw_modified[2] = verb
        if int(fun(raw_modified)[0]) == 19690720:
            print(noun, verb)
            break
        verb += 1
    noun += 1
    verb = 0
