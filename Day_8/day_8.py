# Day 8


def read_map(file_name):
    matrix = []
    antennas = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            matrix.append(line)

            for i in range(len(line)):
                if line[i] != '.':
                    antenna_exists = False
                    for j in range(len(antennas)):
                        if antennas[j][0] == line[i]:
                            antenna_exists = True
                            antennas[j].append([len(matrix) - 1, i])
                            break

                    if antenna_exists is False:
                        antennas.append([line[i], [len(matrix) - 1, i]])

    return matrix, antennas


def is_valid(matrix, pos):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0])


def mark_antinode(antinode_map, pos):
    if antinode_map[pos[0]][pos[1]] == 0:
        antinode_map[pos[0]][pos[1]] = 1
        return 1

    return 0


def determine_unique_locations(matrix, antennas, resonant_harmonics=False):
    locations = 0
    antinode_map = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for antenna in antennas:
        positions = tuple(antenna[1:])

        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                dist = [positions[i][0] - positions[j][0], positions[i][1] - positions[j][1]]

                pos = [positions[i][0] + dist[0], positions[i][1] + dist[1]]
                while is_valid(matrix, pos):
                    locations += mark_antinode(antinode_map, pos)

                    if resonant_harmonics:
                        pos = [pos[0] + dist[0], pos[1] + dist[1]]
                    else:
                        break

                pos = [positions[j][0] - dist[0], positions[j][1] - dist[1]]
                while is_valid(matrix, pos):
                    locations += mark_antinode(antinode_map, pos)

                    if resonant_harmonics:
                        pos = [pos[0] - dist[0], pos[1] - dist[1]]
                    else:
                        break

                if resonant_harmonics:
                    locations += mark_antinode(antinode_map, positions[i])
                    locations += mark_antinode(antinode_map, positions[j])

    return locations


matrix, antennas = read_map('input.txt')
nr_locations = determine_unique_locations(matrix, antennas, False)
print(f"Number of unique locations without resonant harmonics: {nr_locations}")
nr_locations = determine_unique_locations(matrix, antennas, True)
print(f"Number of unique locations with resonant harmonics: {nr_locations}")
