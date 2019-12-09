def intcode_computer(int_program: list, *args, output: bool = True, user_input: bool = True):

    arg_number = 0
    if args:
        user_input = False
    returns = list()

    int_program = list(map(int, int_program))
    pointer_pos = 0
    halt = False
    while not halt:
        if int_program[pointer_pos] == 1:
            # Adding input in spot 1 and 2, and storing them in spot 3
            int_program[int_program[pointer_pos + 3]] = int_program[int_program[pointer_pos + 1]] + \
                                                        int_program[int_program[pointer_pos + 2]]
            pointer_pos += 4

        elif int_program[pointer_pos] == 2:
            # Multiplying input in spot 1 and 2, and storing them in spot 3
            int_program[int_program[pointer_pos + 3]] = int_program[int_program[pointer_pos + 1]] * \
                                                        int_program[int_program[pointer_pos + 2]]
            pointer_pos += 4

        elif int_program[pointer_pos] == 3:
            # Input
            if user_input:
                int_program[int_program[pointer_pos + 1]] = int(input("Enter a single integer input: "))
            else:
                int_program[int_program[pointer_pos + 1]] = int(args[arg_number])
                arg_number += 1

            pointer_pos += 2

        elif int_program[pointer_pos] == 4:
            # Output
            if output:
                print(int_program[int_program[pointer_pos + 1]])
            else:
                returns.append(int_program[int_program[pointer_pos + 1]])

            pointer_pos += 2

        elif int_program[pointer_pos] == 5:
            # Jump if True
            if int_program[int_program[pointer_pos + 1]] != 0:
                pointer_pos = int_program[int_program[pointer_pos + 2]]
            else:
                pointer_pos += 3

        elif int_program[pointer_pos] == 6:
            # Jump if false
            if int_program[int_program[pointer_pos + 1]] == 0:
                pointer_pos = int_program[int_program[pointer_pos + 2]]
            else:
                pointer_pos += 3

        elif int_program[pointer_pos] == 7:
            # Less than
            if int_program[int_program[pointer_pos + 1]] < int_program[int_program[pointer_pos + 2]]:
                int_program[int_program[pointer_pos + 3]] = 1
            else:
                int_program[int_program[pointer_pos + 3]] = 0
            pointer_pos += 4

        elif int_program[pointer_pos] == 8:
            # Equals
            if int_program[int_program[pointer_pos + 1]] == int_program[int_program[pointer_pos + 2]]:
                int_program[int_program[pointer_pos + 3]] = 1
            else:
                int_program[int_program[pointer_pos + 3]] = 0
            pointer_pos += 4

        elif int_program[pointer_pos] == 99:
            halt = True

        else:
            # Getting and executing instruction
            instruction = int(str(int_program[pointer_pos])[-2:])
            get_1, get_2, get_3 = False, False, False
            if instruction in [1, 2, 7, 8]:
                get_1, get_2, get_3 = True, True, True
            elif instruction in [5, 6]:
                get_1, get_2, get_3 = True, True, False
            elif instruction in [3, 4]:
                get_1, get_2, get_3 = True, False, False
            elif instruction == 99:
                halt = True

            # Getting the values
            value_1, value_2, value_3 = 0, 0, 0
            if get_1:
                try:
                    if int(str(int_program[pointer_pos])[-3]) == 0:
                        value_1 = int_program[int_program[pointer_pos + 1]]
                    elif int(str(int_program[pointer_pos])[-3]) == 1:
                        value_1 = int_program[pointer_pos + 1]
                except IndexError:
                    value_1 = int_program[int_program[pointer_pos + 1]]

            if get_2:
                try:
                    if int(str(int_program[pointer_pos])[-4]) == 0:
                        value_2 = int_program[int_program[pointer_pos + 2]]
                    elif int(str(int_program[pointer_pos])[-4]) == 1:
                        value_2 = int_program[pointer_pos + 2]
                except IndexError:
                    value_2 = int_program[int_program[pointer_pos + 2]]
            if get_3:
                try:
                    if int(str(int_program[pointer_pos])[-5]) == 0:
                        value_3 = int_program[pointer_pos + 3]
                    elif int(str(int_program[pointer_pos])[-5]) == 1:
                        value_3 = int_program[int_program[pointer_pos + 3]]
                except IndexError:
                    value_3 = int_program[pointer_pos + 3]

            if instruction == 1:
                # Addition
                int_program[value_3] = value_1 + value_2

                # Going to next intcode
                pointer_pos += 4

            elif instruction == 2:
                # Multiplication
                int_program[value_3] = value_1 * value_2

                # Going to next intcode
                pointer_pos += 4

            elif instruction == 3:
                # Input
                if user_input:
                    int_program[value_2] = int(input("Enter a single integer input: "))
                else:
                    int_program[value_2] = int(args[arg_number])
                    arg_number += 1

                # Going to next intcode
                pointer_pos += 2

            elif instruction == 4:
                # Output
                if output:
                    print(value_1)
                else:
                    returns.append(value_1)

                # Going to next intcode
                pointer_pos += 2

            elif instruction == 5:
                # Jump if true
                if value_1 != 0:
                    pointer_pos = value_2
                else:
                    pointer_pos += 3

            elif instruction == 6:
                # Jump if false
                if value_1 == 0:
                    pointer_pos = value_2
                else:
                    pointer_pos += 3

            elif instruction == 7:
                # Less than
                if value_1 < value_2:
                    int_program[value_3] = 1
                else:
                    int_program[value_3] = 0
                pointer_pos += 4

            elif instruction == 8:
                # Equal to
                if value_1 == value_2:
                    int_program[value_3] = 1
                else:
                    int_program[value_3] = 0
                pointer_pos += 4

            elif instruction == 99:
                halt = True

    if not output:
        return returns
