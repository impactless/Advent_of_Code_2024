# Day 3

import re


def read_instructions(file_name):
    mul = []
    is_enabled = True

    with open(file_name, 'r') as file:
        content = file.read()

    instructions = re.findall(r"mul+\(+[0-9]+,+[0-9]+\)|do\(\)|don't\(\)", content)

    for i in range(len(instructions)):
        tmp = re.findall(r'[0-9]+', instructions[i])

        if len(tmp) == 2:
            x = int(tmp[0])
            y = int(tmp[1])

            if 0 <= x < 1000 and 0 <= y < 1000:
                mul.append([x, y, is_enabled])
        else:
            tmp = re.findall(r'do\(\)', instructions[i])

            if len(tmp) > 0:
                is_enabled = True
            else:
                is_enabled = False

    return mul


def add_multiplications(mul):
    s = 0

    for i in range(len(mul)):
        s += (mul[i][0] * mul[i][1])

    return s


def add_enabled_multiplications(mul):
    s = 0

    for i in range(len(mul)):
        if mul[i][2] is True:
            s += (mul[i][0] * mul[i][1])

    return s


multiplications = read_instructions('input.txt')
print(f'Sum of multiplications: {add_multiplications(multiplications)}')
print(f'Sum of enabled multiplications: {add_enabled_multiplications(multiplications)}')
