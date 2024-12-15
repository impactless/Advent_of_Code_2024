# Day 15

import re

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def read_map_movements(file_name):
    matrix = []
    moves = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        is_map = True
        for line in lines:
            line = line.strip()

            if len(line) == 0:
                is_map = False
            elif is_map:
                row = list(re.findall(r'[#.O@]', line))

                matrix.append(row)
            else:
                for i in range(len(line)):
                    if line[i] == '^':
                        moves.append(0)
                    elif line[i] == '>':
                        moves.append(1)
                    elif line[i] == 'v':
                        moves.append(2)
                    elif line[i] == '<':
                        moves.append(3)
    # print(matrix)
    return matrix, moves


def transform_map(matrix):
    new_matrix = []
    start = []

    for line in matrix:
        row = []
        for i in range(len(line)):
            if line[i] == '@':
                start = [len(new_matrix), i]
                row.append(0)
            elif line[i] == '#':
                row.append(-1)
            elif line[i] == '.':
                row.append(0)
            elif line[i] == 'O':
                row.append(1)

        new_matrix.append(row)

    return new_matrix, start


def change_map(matrix):
    new_matrix = []
    start = []

    new_matrix = []
    start = []

    for line in matrix:
        row = []
        for i in range(len(line)):
            if line[i] == '@':
                start = [len(new_matrix), len(row)]
                row.append(0)
                row.append(0)
            elif line[i] == '#':
                row.append(-1)
                row.append(-1)
            elif line[i] == '.':
                row.append(0)
                row.append(0)
            elif line[i] == 'O':
                row.append(1)
                row.append(2)

        new_matrix.append(row)

    return new_matrix, start


def is_valid(matrix, pos):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0])


def is_obstacle(matrix, pos):
    return matrix[pos[0]][pos[1]] != -1


def is_box(matrix, pos):
    return matrix[pos[0]][pos[1]] == 1 or matrix[pos[0]][pos[1]] == 2


def is_empty(matrix, pos):
    return matrix[pos[0]][pos[1]] == 0


def move_robot(matrix, moves, start):
    current = [start[0], start[1]]

    for move in moves:
        temp_pos = [current[0] + directions[move][0], current[1] + directions[move][1]]

        if is_valid(matrix, temp_pos) and is_obstacle(matrix, temp_pos):
            if is_empty(matrix, temp_pos):
                current = temp_pos
            else:
                while is_valid(matrix, temp_pos) and is_box(matrix, temp_pos):
                    temp_pos = [temp_pos[0] + directions[move][0], temp_pos[1] + directions[move][1]]
                if is_valid(matrix, temp_pos) and is_empty(matrix, temp_pos):
                    matrix[temp_pos[0]][temp_pos[1]] = 1
                    temp_pos = [current[0] + directions[move][0], current[1] + directions[move][1]]
                    matrix[temp_pos[0]][temp_pos[1]] = 0
                    current = temp_pos


def calculate_gps_coordinates(matrix):
    gps_sum = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                gps_sum += (100 * i + j)

    return gps_sum


matrix, moves = read_map_movements('input.txt')

matrix_1, start = transform_map(matrix)

move_robot(matrix_1, moves, start)
sum_boxes = calculate_gps_coordinates(matrix_1)
print(f"The sum of all boxes' GPS coordinates: {sum_boxes}")

# matrix_2, start = change_map(matrix)
# move_robot(matrix_2, moves, start)
# sum_boxes = calculate_gps_coordinates(matrix_2)
# print(f"The sum of all boxes' GPS coordinates: {sum_boxes}")