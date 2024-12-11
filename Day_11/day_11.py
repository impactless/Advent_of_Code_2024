# Day 11

import re
import math


def read_stones(file_name):
    stone_counts = {}

    with open(file_name, 'r') as file:
        content = file.read()
        stones = list(map(int, re.findall(r'\d+', content)))

        for stone in stones:
            if stone in stone_counts:
                stone_counts[stone] += 1
            else:
                stone_counts[stone] = 1

    return stone_counts


def transform_stones(stones, nr_of_blinks):
    for blink in range(nr_of_blinks):
        new_stones = {}

        for stone, count in stones.items():
            # Rule 1
            if stone == 0:
                if 1 in new_stones:
                    new_stones[1] += count
                else:
                    new_stones[1] = count
                continue

            # Rule 2
            nr_of_digits = int(math.log10(stone)) + 1 if stone > 0 else 1
            if nr_of_digits % 2 == 0:
                pow_10 = 10 ** (nr_of_digits // 2)
                first_half = stone // pow_10
                second_half = stone % pow_10

                if first_half in new_stones:
                    new_stones[first_half] += count
                else:
                    new_stones[first_half] = count

                if second_half in new_stones:
                    new_stones[second_half] += count
                else:
                    new_stones[second_half] = count
            else:
                # Rule 3
                new_stone = stone * 2024
                if new_stone in new_stones:
                    new_stones[new_stone] += count
                else:
                    new_stones[new_stone] = count

        stones = new_stones

    return sum(stones.values())


stone_counts = read_stones('input.txt')

stone_counts_copy = stone_counts.copy()
nr_of_stones = transform_stones(stone_counts_copy, 25)
print(f'Number of stones after 25 blinks: {nr_of_stones}')

stone_counts__copy = stone_counts.copy()
nr_of_stones = transform_stones(stone_counts_copy, 75)
print(f'Number of stones after 75 blinks: {nr_of_stones}')
