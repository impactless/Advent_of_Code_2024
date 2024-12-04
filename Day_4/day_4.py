# Day 4

Directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1)]

X_Directions = [(-1, -1), (1, 1),
                (-1, 1), (1, -1)]


def read_data(file_name):
    matrix = []

    with open(file_name, 'r') as file:
        for line in file:
            matrix.append(list(line.strip()))

    return matrix


def is_valid(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def search(matrix, row, col, word, index, direction):
    if index == len(word):
        return True

    new_row = row + direction[0]
    new_col = col + direction[1]
    if is_valid(matrix, new_row, new_col) and matrix[new_row][new_col] == word[index]:
        if search(matrix, new_row, new_col, word, index + 1, direction):
            return True

    return False


def find_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == word[0]:
                for direction in Directions:
                    if search(matrix, row, col, word, 1, direction):
                        count += 1

    return count


def find_x_word(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'A':
                positions = []

                for direction in X_Directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if is_valid(matrix, new_row, new_col):
                        positions.append((new_row, new_col))

                if len(positions) == 4:
                    chars = [matrix[r][c] for r, c in positions]

                    if ((chars[0] == 'M' and chars[1] == 'S' or chars[0] == 'S' and chars[1] == 'M') and
                            (chars[2] == 'M' and chars[3] == 'S' or chars[2] == 'S' and chars[3] == 'M')):
                        count += 1

    return count


Matrix = read_data('input.txt')
print(f'XMAS search: {find_word(Matrix, 'XMAS')}')
print(f'X-MAS search: {find_x_word(Matrix)}')
