# Day 14

import re

tails_wide = 101
tails_tall = 103


def read_robots_data(file_name):
    positions = []
    velocities = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            numbers = list(map(int, re.findall(r'-?\d+', line)))
            positions.append([numbers[0], numbers[1]])
            velocities.append([numbers[2], numbers[3]])

    return positions, velocities


def teleport(tails_w, tails_t, pos, vel, t):
    return [(pos[0] + t * (tails_w + vel[0])) % tails_w, (pos[1] + t * (tails_t + vel[1])) % tails_t]


def calculate_safety_factor(p, v, tails_w, tails_t, time=100):
    quadrant = [0 for _ in range(4)]
    safety_factor = -1

    for i in range(len(p)):
        temp_pos = teleport(tails_w, tails_t, p[i], v[i], time)

        q = -1
        if temp_pos[0] > tails_w // 2 and temp_pos[1] < tails_t // 2:
            q = 1
        elif temp_pos[0] < tails_w // 2 and temp_pos[1] < tails_t // 2:
            q = 2
        elif temp_pos[0] < tails_w // 2 and temp_pos[1] > tails_t // 2:
            q = 3
        elif temp_pos[0] > tails_w // 2 and temp_pos[1] > tails_t // 2:
            q = 4

        if q != -1:
            safety_factor = 1
            quadrant[q - 1] += 1

    if safety_factor < 0:
        return 0

    for i in range(4):
        safety_factor *= quadrant[i]

    return safety_factor


def find_christmas_tree(p, v, tails_w, tails_t):
    step = 0
    target_width = 30

    while True:
        grid = [['.'] * tails_w for _ in range(tails_t)]

        for i in range(len(p)):
            p[i] = [p[i][0] + v[i][0], p[i][1] + v[i][1]]

            if not 0 <= p[i][0] < tails_w:
                p[i][0] = p[i][0] % tails_w
            if not 0 <= p[i][1] < tails_t:
                p[i][1] = p[i][1] % tails_t

        for x, y in p:
            grid[y][x] = 'x'

        step += 1
        for row in grid:
            if 'x' * target_width in ''.join(row):
                return step


p, v = read_robots_data('input.txt')

safety_factor = calculate_safety_factor(p, v, tails_wide, tails_tall, 100)
print(f'Safety factor: {safety_factor}')

shortest_time = find_christmas_tree(p, v, tails_wide, tails_tall)
print(f'Shortest time: {shortest_time}')

