# Day 12

Directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def read_garden(file_name):
    garden = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            garden.append(list(line))

    return garden


def is_valid(matrix, pos):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0])


def visit_region(matrix, visited, pos):
    stack = [pos]
    visited[pos[0]][pos[1]] = True
    area = 0
    perimeter = 0

    while stack:
        current = stack.pop()
        area += 1

        for direction in Directions:
            next_pos = [current[0] + direction[0], current[1] + direction[1]]

            if is_valid(matrix, next_pos) and matrix[next_pos[0]][next_pos[1]] == matrix[pos[0]][pos[1]]:
                if not visited[next_pos[0]][next_pos[1]]:
                    stack.append(next_pos)
                    visited[next_pos[0]][next_pos[1]] = True
            else:
                perimeter += 1

    return area, perimeter


def calculate_price(matrix, discount=False):
    total_price = 0
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    if not discount:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not visited[i][j]:
                    region_area, region_perimeter = visit_region(matrix, visited, [i, j])
                    total_price += region_area * region_perimeter

    return total_price


garden = read_garden('input.txt')

full_price = calculate_price(garden, False)
print(f'Total full price: {full_price}')

discounted_price = calculate_price(garden, True)
print(f'Total discounted price: {discounted_price}')
