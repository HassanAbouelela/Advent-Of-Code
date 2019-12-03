raw = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,5,19,23,2,10,23,27,1,27,5,31,2,9,31,35,1,35,5,39,2,6,39,43,1,43,5,47,2,47,10,51,2,51,6,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,1,71,5,75,1,13,75,79,1,6,79,83,2,83,13,87,1,87,6,91,1,10,91,95,1,95,9,99,2,99,13,103,1,103,6,107,2,107,6,111,1,111,2,115,1,115,13,0,99,2,0,14,0".split(",")


def fun(raw_input: list):
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
