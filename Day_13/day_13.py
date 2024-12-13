# Day 13

import re


def read_data(file_name):
    buttons_a = []
    buttons_b = []
    prizes = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for i in range(0, len(lines), 4):
            temp_a = lines[i].strip()
            temp_b = lines[i + 1].strip()
            temp_p = lines[i + 2].strip()

            buttons_a.append(list(map(int, re.findall(r'\d+', temp_a))))
            buttons_b.append(list(map(int, re.findall(r'\d+', temp_b))))
            prizes.append(list(map(int, re.findall(r'\d+', temp_p))))

    return buttons_a, buttons_b, prizes


def least_possible_tokens(button_a, button_b, prize):
    x_a, y_a = button_a
    x_b, y_b = button_b
    x_prize, y_prize = prize

    determinant = x_a * y_b - x_b * y_a

    if determinant == 0:
        ans = float('inf')
        for a in range(x_prize // x_a + 1):
            b = (x_prize - a * x_a) // x_b
            if a * x_a + b * x_b == x_prize:
                ans = min(ans, a * 3 + b)
        return ans if ans != float('inf') else 0

    a = (y_b * x_prize - x_b * y_prize) // determinant
    b = (x_a * y_prize - y_a * x_prize) // determinant

    if min(a, b) >= 0 and (a * x_a + b * x_b == x_prize) and (a * y_a + b * y_b == y_prize):
        return a * 3 + b

    return 0


def calculate_tokens(buttons_a, buttons_b, prizes):
    total_tokens = 0
    length = len(prizes)

    for i in range(length):
        total_tokens += least_possible_tokens(buttons_a[i], buttons_b[i], prizes[i])

    return total_tokens


buttons_a, buttons_b, prizes = read_data('input.txt')

fewest_tokens = calculate_tokens(buttons_a, buttons_b, prizes)
print(f'Tokens: {fewest_tokens}')

for i in range(len(prizes)):
    prizes[i][0] += 10000000000000
    prizes[i][1] += 10000000000000

error_tokens = calculate_tokens(buttons_a, buttons_b, prizes)
print(f'Tokens: {error_tokens}')
