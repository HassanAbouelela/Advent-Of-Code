import re

with open("input.txt", "r") as file:
    raw_range = file.read()

passwords = []
for number in range(int(raw_range[:re.search("[-]", raw_range).start()]), int(raw_range[re.search("[-]", raw_range).end():])):
    previous = [0]
    valid = False
    for part in str(number):
        if list(str(number)).count(part) == 2:
            valid = True
        else:
            pass
        if int(part) >= previous[-1]:
            previous.append(int(part))
        else:
            valid = False
            break
    if valid and len(previous) == 7:
        passwords.append(number)

print(len(passwords))
