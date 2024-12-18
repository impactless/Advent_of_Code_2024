# Day 18

import re

dim = 71
corrupted_bytes = 1024
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def read_bytes(file_name):
    bytes_list = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            bytes_list.append(list(map(int, re.findall(r'\d+', line))))

    return bytes_list


def generate_map(bytes_list):
    matrix = [[0 for _ in range(dim)] for _ in range(dim)]

    for i in range(len(bytes_list)):
        x, y = bytes_list[i]
        if matrix[y][x] == 0:
            matrix[y][x] = i + 1

    return matrix


def is_valid(pos):
    return 0 <= pos[0] < dim and 0 <= pos[1] < dim


def is_empty(matrix, pos, nr_bytes):
    if matrix[pos[0]][pos[1]] == 0:
        return True
    return nr_bytes < matrix[pos[0]][pos[1]]


def find_shortest_path(matrix, nr_bytes):
    start_pos = [0, 0]
    exit_pos = [dim - 1, dim - 1]
    steps = 1000000001

    visited = [[0 for _ in range(dim)] for _ in range(dim)]

    queue = [[start_pos, 1, -1]]
    k = 0
    while k < len(queue):
        c_pos = queue[k][0]
        c_step = queue[k][1]
        visited[c_pos[0]][c_pos[1]] = c_step

        if c_pos == exit_pos:
            steps = min(steps, c_step)

        for direction in directions:
            next_pos = [c_pos[0] + direction[0], c_pos[1] + direction[1]]

            if is_valid(next_pos):
                if is_empty(matrix, next_pos, nr_bytes):
                    add_in_queue = True

                    for i in range(len(queue)):
                        if queue[i][0] == next_pos:
                            add_in_queue = False
                            break

                    if add_in_queue:
                        queue.append([next_pos, c_step + 1, k])

        k += 1

    return steps - 1


def find_byte(matrix, bytes_list):
    start = corrupted_bytes
    end = len(bytes_list) - 1

    middle = (start + end) // 2
    result = find_shortest_path(matrix, nr_bytes=middle)

    while start < end:
        if result == 1000000000:
            end = middle
        else:
            start = middle + 1

        middle = (start + end) // 2
        result = find_shortest_path(matrix, nr_bytes=middle)

    for y in range(dim):
        for x in range(dim):
            if matrix[y][x] == middle:
                return [x, y]

    return [-1, -1]


b = read_bytes('input.txt')
m = generate_map(b)

min_steps = find_shortest_path(m, corrupted_bytes)
print(f'Minimum number of steps: {min_steps}')

byte_pos = find_byte(m, b)
print(f'The coordinates of the first byte that will prevent the exit from being reachable: {byte_pos[0]},{byte_pos[1]}')
