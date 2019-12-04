# These are all meant to test the limits of what we can do, hence esocentricity. These aren't highly efficient,
# they aren't beautiful, and they aren't always *guaranteed* to work, but I do test them to some extent.

# Day 1

# Day 2

# Day 3
# Part 1 - WIP:
# Have to add all values between each point
# Have to find intersections and calc manhattan distance
# Have to remove all semi-colons
x, y = [[0, 0]], [[0, 0]]; list(map(lambda coord: x.append([x[-1][0] + int(coord[1:]), x[-1][1]]) if "R" in coord else x.append([x[-1][0] - int(coord[1:]), x[-1][1]]) if "L" in coord else x.append([x[-1][0], x[-1][1] + int(coord[1:])]) if "U" in coord else x.append([x[-1][0], x[-1][1] - int(coord[1:])]) if "D" in coord else 0, [i for i in open("input.txt", "r").readlines()[0].split(",")])); list(map(lambda coord: y.append([y[-1][0] + int(coord[1:]), y[-1][1]]) if "R" in coord else y.append([y[-1][0] - int(coord[1:]), y[-1][1]]) if "L" in coord else y.append([y[-1][0], y[-1][1] + int(coord[1:])]) if "U" in coord else y.append([y[-1][0], y[-1][1] - int(coord[1:])]) if "D" in coord else 0, [i for i in open("input.txt", "r").readlines()[1].split(",")]))#; x = list(map(lambda z: str(z), x)); y = list(map(lambda z: str(z), y)); print([z for z in x if z in y])
# Part 2

# Day 4
# Part 1 - Working
print(len(list(filter(lambda x: True if True in [True if len(__import__("re").findall(f"{z}", str(x))) >= 2 else False for z in range(1, 10)] else False, filter(lambda x: True if False not in [True if str(x)[y] >= str(x)[y-1] else False for y in range(1, 6)] else False, [i for i in range(int(open("input.txt", "r").read()[:__import__("re").search("-", open("input.txt", "r").read()).start()]), int(open("input.txt", "r").read()[__import__("re").search("-", open("input.txt", "r").read()).end():]))])))))
# Part 2 - Working
print(len(list(filter(lambda x: True if True in [True if len(__import__("re").findall(f"{z}", str(x))) == 2 else False for z in range(1, 10)] else False, filter(lambda x: True if False not in [True if str(x)[y] >= str(x)[y-1] else False for y in range(1, 6)] else False, [i for i in range(int(open("input.txt", "r").read()[:__import__("re").search("-", open("input.txt", "r").read()).start()]), int(open("input.txt", "r").read()[__import__("re").search("-", open("input.txt", "r").read()).end():]))])))))

# Day 5
