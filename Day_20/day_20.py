# Day 20

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def read_racetrack(file_name):
    matrix = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            row = []
            for i in range(len(line)):
                if line[i] == 'S':
                    row.append(0)
                    start_pos = [len(matrix), i]
                elif line[i] == 'E':
                    row.append(0)
                    exit_pos = [len(matrix), i]
                elif line[i] == '.':
                    row.append(0)
                elif line[i] == '#':
                    row.append(-1)

            matrix.append(row)

    return matrix, start_pos, exit_pos


def is_valid(matrix, pos):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0])


def is_empty(matrix, pos):
    return matrix[pos[0]][pos[1]] == 0


def find_shortest_path(matrix, start_pos, exit_pos):
    queue = [[start_pos, 0]]
    k = 0

    while k < len(queue):
        c_pos = queue[k][0]
        c_time = queue[k][1]

        if c_pos == exit_pos:
            return queue

        for direction in directions:
            n_pos = [c_pos[0] + direction[0], c_pos[1] + direction[1]]

            if is_valid(matrix, n_pos) and is_empty(matrix, n_pos):
                is_absent = True
                for i in range(len(queue)):
                    if n_pos == queue[i][0]:
                        is_absent = False

                if is_absent:
                    queue.append([n_pos, c_time + 1])

        k += 1


def find_cheat_paths(queue, cheat_moves=2, save=100):
    nr_cheats = 0
    for i in range(len(queue) - 1):
        for j in range(i + 1, len(queue)):
            manhattan = abs(queue[j][0][0] - queue[i][0][0]) + abs(queue[j][0][1] - queue[i][0][1])

            if manhattan <= cheat_moves:
                temp_time = queue[j][1] - queue[i][1] - manhattan

                if temp_time >= save:
                    nr_cheats += 1

    return nr_cheats


m, s, e = read_racetrack('input.txt')
q = find_shortest_path(m, s, e)

c = find_cheat_paths(q, 2)
print(f'The number of cheats would save at least 100 picoseconds with 2 cheat moves: {c}')

c = find_cheat_paths(q, 20)
print(f'The number of cheats would save at least 100 picoseconds with 20 cheat moves: {c}')
