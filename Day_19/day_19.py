# Day 19

import re


def read_towels(file_name):
    with open(file_name, 'r') as file:
        line = file.readline().strip()
        patterns = list(map(str, re.findall(r'[wubrg]+', line)))

        content = file.read().strip()
        designs = list(map(str, re.findall(r'[wubrg]+', content)))

    return patterns, designs


def find_possible_designs(patterns, designs, part=1):
    nr_possible_designs = 0

    for design in designs:
        dynamic_programming = [0] * (len(design) + 1)
        dynamic_programming[0] = 1

        for i in range(len(design)):
            if dynamic_programming[i]:
                for pattern in patterns:
                    if i + len(pattern) <= len(design) and design[i:i + len(pattern)] == pattern:
                        dynamic_programming[i + len(pattern)] += dynamic_programming[i]

        if dynamic_programming[len(design)]:
            if part == 1:
                nr_possible_designs += 1
            elif part == 2:
                nr_possible_designs += dynamic_programming[len(design)]

    return nr_possible_designs


towel_patterns, desired_designs = read_towels('input.txt')

possible_designs = find_possible_designs(towel_patterns, desired_designs, 1)
print(f'The number of possible designs: {possible_designs}')

different_designs = find_possible_designs(towel_patterns, desired_designs, 2)
print(f'The number of different possible designs: {different_designs}')
