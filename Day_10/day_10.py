# Day 10

import re

Directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def read_topographic_map(file_name):
    topographic_map = []
    beginning_pos = []
    ending_pos = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            numbers = list(map(int, re.findall(r'\d', line)))
            topographic_map.append(numbers)

            for i in range(len(numbers)):
                if numbers[i] == 0:
                    beginning_pos.append([len(topographic_map) - 1, i])
                if numbers[i] == 9:
                    ending_pos.append([len(topographic_map) - 1, i])

    return topographic_map, beginning_pos, ending_pos


def is_valid(matrix, pos):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0])


def find_path(matrix, frequency, pos, ending):
    if matrix[pos[0]][pos[1]] == 9:
        for i in range(len(ending)):
            if ending[i] == pos:
                frequency[i] += 1

                if frequency[i] == 1:
                    return 1, 1

                return 0, 1

        return 0, 0

    trail_score = 0
    trail_rating = 0
    for direction in Directions:
        temp_pos = [pos[0] + direction[0], pos[1] + direction[1]]

        if is_valid(matrix, temp_pos) and matrix[pos[0]][pos[1]] + 1 == matrix[temp_pos[0]][temp_pos[1]]:
            temp_score, temp_rating = find_path(matrix, frequency, temp_pos, ending)

            trail_score += temp_score
            trail_rating += temp_rating

    return trail_score, trail_rating


def determine_trailhead_score_rating(matrix, beginning, ending):
    trailhead_score = 0
    trailhead_rating = 0

    for pos in beginning:
        frequency = [0 for _ in range(len(ending))]

        temp_score, temp_rating = find_path(matrix, frequency, pos, ending)

        trailhead_score += temp_score
        trailhead_rating += temp_rating

    return trailhead_score, trailhead_rating


topographic_map, beginning_pos, ending_pos = read_topographic_map('input.txt')

trailhead_score, trailhead_rating = determine_trailhead_score_rating(topographic_map, beginning_pos, ending_pos)
print(f"Trailhead score: {trailhead_score}")
print(f"Trailhead rating: {trailhead_rating}")
