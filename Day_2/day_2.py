# Day 2

import re


def read_data(file_name):
    reports = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            numbers = list(map(int, re.findall(r'\d+', line)))
            reports.append(numbers)

    return reports


def check_safety(report):
    if len(report) < 2:
        return False

    is_increasing = report[0] < report[1]
    for i in range(len(report) - 1):
        if is_increasing and report[i] >= report[i + 1]:
            return False
        if not is_increasing and report[i] <= report[i + 1]:
            return False
        if abs(report[i] - report[i + 1]) < 1 or abs(report[i] - report[i + 1]) > 3:
            return False

    return True


def check_tolerated_safety(report):
    for i in range(len(report)):
        tmp_report = report[:i] + report[i+1:]
        if check_safety(tmp_report):
            return True

    return False


def find_report_safety(reports):
    return sum(1 for report in reports if check_safety(report))


def find_tolerated_report_safety(reports):
    return sum(1 for report in reports if check_tolerated_safety(report))


Reports = read_data('input.txt')
print(f'Safe reports: {find_report_safety(Reports)}')
print(f'Tolerated safe reports: {find_tolerated_report_safety(Reports)}')
