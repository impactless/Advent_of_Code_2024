# Day 17

import re


def read_registers_and_program(file_name):
    registers = []

    with open(file_name, 'r') as file:
        content = file.read().strip()

        temp = list(map(int, re.findall(r'\d+', content)))

        registers.append(temp[0])
        registers.append(temp[1])
        registers.append(temp[2])
        program = temp[3:]

    return registers, program


def dv(registers, combo_operand):
    numerator = registers[0]
    denominator = 1

    if 0 <= combo_operand <= 3:
        denominator = 2 ** combo_operand
    if 4 <= combo_operand <= 6:
        denominator = 2 ** registers[combo_operand - 4]

    return numerator // denominator


def bxl(registers, literal_operand):
    return registers[1] ^ literal_operand


def bst(registers, combo_operand):
    result = 0

    if 0 <= combo_operand <= 3:
        result = combo_operand % 8
    if 4 <= combo_operand <= 6:
        result = registers[combo_operand - 4] % 8

    return result


def jnz(registers, literal_operand, instruction_pointer):
    if registers[0] == 0:
        return instruction_pointer
    return literal_operand - 2


def bxt(registers):
    return registers[1] ^ registers[2]


def out(registers, combo_operand):
    result = 0

    if 0 <= combo_operand <= 3:
        result = combo_operand % 8
    if 4 <= combo_operand <= 6:
        result = registers[combo_operand - 4] % 8

    return result


def run_program(registers, program):
    output = []

    i = 0
    while i < len(program):
        a = registers[0]
        b = registers[1]
        c = registers[2]

        if program[i] == 0:
            a = dv(registers, program[i + 1])
        elif program[i] == 1:
            b = bxl(registers, program[i + 1])
        elif program[i] == 2:
            b = bst(registers, program[i + 1])
        elif program[i] == 3:
            i = jnz(registers, program[i + 1], i)
        elif program[i] == 4:
            b = bxt(registers)
        elif program[i] == 5:
            output.append(out(registers, program[i + 1]))
        elif program[i] == 6:
            b = dv(registers, program[i + 1])
        elif program[i] == 7:
            c = dv(registers, program[i + 1])

        i += 2
        registers = [a, b, c]

    return output


def copy_program(registers, program):
    a = sum(7 * 8 ** i for i in range(len(program) - 1)) + 1

    while True:
        output = run_program([a, registers[1], registers[2]], program)

        if program == output:
            return a

        if len(output) <= len(program):
            for i in range(len(output) - 1, -1, -1):
                if program[i] != output[i]:
                    a += 8 ** i
                    break


def print_output(output):
    for i in range(len(output) - 1):
        print(output[i], end=',')
    print(output[len(output) - 1])


r, p = read_registers_and_program('input.txt')

o = run_program(r, p)
print('Output: ', end='')
print_output(o)

register_a = copy_program(r, p)
print(f'Register A: {register_a}')
