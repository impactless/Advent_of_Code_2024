# Day 6

Directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def read_lab(file_name):
    matrix = []
    start_pos = None
    start_dir = -1

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for row in range(len(lines)):
            temp_row = []

            for col in range(len(lines[row])):
                if lines[row][col] == '#':
                    temp_row.append(-1)
                elif lines[row][col] == '.':
                    temp_row.append(0)
                elif lines[row][col] != '\n':
                    temp_row.append(0)
                    start_pos = [row, col]

                    if lines[row][col] == '^':
                        start_dir = 0
                    elif lines[row][col] == '>':
                        start_dir = 1
                    elif lines[row][col] == 'v':
                        start_dir = 2
                    elif lines[row][col] == '<':
                        start_dir = 3

            matrix.append(temp_row)

    return matrix, start_pos, start_dir


def is_within_bounds(matrix, pos):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0])


def predict_guard_path(matrix, start_pos, start_dir):
    visited = set()
    current_pos = start_pos[:]
    current_dir = start_dir
    state_history = set()

    while is_within_bounds(matrix, current_pos):
        state = (current_pos[0], current_pos[1], current_dir)
        if state in state_history:
            return visited, True
        state_history.add(state)

        visited.add(tuple(current_pos))

        next_pos = [current_pos[0] + Directions[current_dir][0], current_pos[1] + Directions[current_dir][1]]

        if is_within_bounds(matrix, next_pos) and matrix[next_pos[0]][next_pos[1]] != -1:
            current_pos = next_pos
        else:
            while is_within_bounds(matrix, next_pos) and matrix[next_pos[0]][next_pos[1]] == -1:
                current_dir = (current_dir + 1) % 4
                next_pos = [current_pos[0] + Directions[current_dir][0], current_pos[1] + Directions[current_dir][1]]

            if not is_within_bounds(matrix, next_pos) or matrix[next_pos[0]][next_pos[1]] == -1:
                break

    return visited, False


def count_loop_positions(matrix, visited_positions, start_pos, start_dir):
    loop_count = 0

    for pos in visited_positions:
        if pos == tuple(start_pos):
            continue

        temp_matrix = [row[:] for row in matrix]
        temp_matrix[pos[0]][pos[1]] = -1

        _, loop_detected = predict_guard_path(temp_matrix, start_pos, start_dir)
        if loop_detected:
            loop_count += 1

    return loop_count


lab_matrix, guard_start_pos, guard_start_dir = read_lab('input.txt')

visited_positions, _ = predict_guard_path(lab_matrix, guard_start_pos, guard_start_dir)
print(f'Number of distinct positions: {len(visited_positions)}')
loop_positions_count = count_loop_positions(lab_matrix, visited_positions, guard_start_pos, guard_start_dir)
print(f'Number of possible loops: {loop_positions_count}')
