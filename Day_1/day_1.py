# Day 1

import re

left_list = []
right_list = []


def read_location_id(file_name):
    with open(file_name, 'r') as file:
        content = file.read()

    numbers = re.findall(r'(\d+)', content)

    length_list = len(numbers) // 2

    for i in range(length_list):
        left_list.append(int(numbers[2 * i]))
        right_list.append(int(numbers[2 * i + 1]))

    # print(left_list)
    # print(right_list)


def find_total_distance():
    total_distance = 0

    for i in range(len(left_list)):
        total_distance = total_distance + abs(left_list[i] - right_list[i])

    return total_distance


def find_similarity_score():
    similarity_score = 0

    for i in range(len(left_list)):
        frequency = 0

        for j in range(len(right_list)):
            if left_list[i] == right_list[j]:
                frequency += 1

        similarity_score = similarity_score + left_list[i] * frequency

    return similarity_score


read_location_id('input.txt')
left_list.sort()
right_list.sort()
print(f'Total distance: {find_total_distance()}')
print(f'Similarity score: {find_similarity_score()}')
