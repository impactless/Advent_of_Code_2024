# Day 16

import re

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def read_maze(file_name):
    matrix = []
    start_pos = []
    exit_pos = []
    start_dir = 1

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            symbols = list(re.findall(r'[#.SE]', line))
            row = []

            for i in range(len(symbols)):
                if symbols[i] == 'S':
                    start_pos = [len(matrix), i]
                    row.append(0)
                elif symbols[i] == 'E':
                    exit_pos = [len(matrix), i]
                    row.append(0)
                elif symbols[i] == '.':
                    row.append(0)
                elif symbols[i] == '#':
                    row.append(-1)

            matrix.append(row)

    return matrix, start_pos, exit_pos, start_dir


def is_valid(matrix, pos):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0]) and matrix[pos[0]][pos[1]] != -1


def find_best_path(matrix, pos, exit_pos, direction):
    score = 100000000000

    queue = [[pos, direction, 0, -1]]
    k = 0
    while k < len(queue):
        c_pos = queue[k][0]
        c_dir = queue[k][1]
        c_score = queue[k][2]

        matrix[c_pos[0]][c_pos[1]] = c_score

        if c_pos == exit_pos:
            if c_score < score:
                score = c_score

        next_pos = [c_pos[0] + directions[c_dir][0], c_pos[1] + directions[c_dir][1]]

        if (is_valid(matrix, next_pos) and
                (matrix[next_pos[0]][next_pos[1]] == 0 or matrix[next_pos[0]][next_pos[1]] >= c_score + 1)):
            queue.append([next_pos, c_dir, c_score + 1, k])

        next_pos = [c_pos[0] + directions[(c_dir + 5) % 4][0], c_pos[1] + directions[(c_dir + 5) % 4][1]]

        if (is_valid(matrix, next_pos) and
                (matrix[next_pos[0]][next_pos[1]] == 0 or matrix[next_pos[0]][next_pos[1]] >= c_score + 1001)):
            queue.append([next_pos, (c_dir + 5) % 4, c_score + 1001, k])

        next_pos = [c_pos[0] + directions[(c_dir + 3) % 4][0], c_pos[1] + directions[(c_dir + 3) % 4][1]]

        if (is_valid(matrix, next_pos) and
                (matrix[next_pos[0]][next_pos[1]] == 0 or matrix[next_pos[0]][next_pos[1]] >= c_score + 1001)):
            queue.append([next_pos, (c_dir + 3) % 4, c_score + 1001, k])

        k += 1

    paths = []
    for u in range(len(queue)):
        if queue[u][2] == score:
            q = u
            path = []

            while q > -1:
                path.append(queue[q][0])
                q = queue[q][3]

            paths.append(path)

    return score, paths


def find_tiles_part_of_best_paths(matrix, paths):
    tiles = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            is_part_of_best_path = False
            for path in paths:
                if [i, j] in path:
                    is_part_of_best_path = True

            if is_part_of_best_path:
                tiles += 1

    return tiles


maze, start, e, d = read_maze('input.txt')

lowest_score, best_paths = find_best_path(maze, start, e, d)
print(f'Lowest score: {lowest_score}')

nr_tiles = find_tiles_part_of_best_paths(maze, best_paths)
print(f'The number of tiles that are part of at least one of the best paths through the maze: {nr_tiles}')
