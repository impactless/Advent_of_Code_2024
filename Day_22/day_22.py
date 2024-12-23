# Day 22

import re


def read_secret_numbers(file_name):
    with open(file_name, 'r') as file:
        content = file.read()

        numbers = list(map(int, re.findall(r'\d+', content)))

    return numbers


def mix(number, value):
    return number ^ value


def prune(number):
    return number % 16777216


def process_1(number):
    return prune(mix(number, number * 64))


def process_2(number):
    return prune(mix(number, number // 32))


def process_3(number):
    return prune(mix(number, number * 2048))


def evolve_number(number):
    return process_3(process_2(process_1(number)))


def generate_secret_numbers(secret_numbers):
    sum_numbers = 0
    price_list = []
    changes_dict = {}

    for number in secret_numbers:
        secret_number = number
        price = [secret_number % 10]
        changes = []
        for _ in range(2000):
            secret_number = evolve_number(secret_number)
            price.append(secret_number % 10)
            changes.append(price[len(price) - 1] - price[len(price) - 2] + 10)

        f = {}
        for j in range(3, len(changes)):
            idx = changes[j - 3] * 1000000 + changes[j - 2] * 10000 + changes[j - 1] * 100 + changes[j]
            if idx not in f:
                f.update({idx: price[j + 1]})

        for key in f.keys():
            if key not in changes_dict:
                changes_dict.update({key: f.get(key)})
            else:
                changes_dict[key] += f.get(key)

        price_list.append(price)

        sum_numbers += secret_number

    max_bananas = 0
    for key in changes_dict.keys():
        if changes_dict[key] > max_bananas:
            max_bananas = changes_dict[key]

    return sum_numbers, max_bananas


n = read_secret_numbers('input.txt')

s, b = generate_secret_numbers(n)
print(f'The sum of the 2000th secret number generated by each buyer: {s}')
print(f'The most bananas that can be obtained: {b}')
