# Day 7

import re


def read_equations(file_name):
    equations = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            if re.match(r'\d+:.*', line):
                numbers = list(map(int, re.findall(r'\d+', line)))
                equations.append(numbers)

    return equations


def possible_calibration(target, nums, index=1, current_value=0, can_concatenate=False):
    if index == len(nums):
        return current_value == target

    if possible_calibration(target, nums, index + 1, current_value + nums[index], can_concatenate):
        return True

    if possible_calibration(target, nums, index + 1, current_value * nums[index], can_concatenate):
        return True

    if can_concatenate:
        concat_value = int(f"{current_value}{nums[index]}")
        if possible_calibration(target, nums, index + 1, concat_value, can_concatenate):
            return True

    return False


def determine_total_calibration_result(equations):
    calibration_result_2_operators = 0
    calibration_result_3_operators = 0

    for equation in equations:
        target = equation[0]
        nums = tuple(equation[1:])

        if possible_calibration(target, nums, 1, nums[0], False):
            calibration_result_2_operators += target

        if possible_calibration(target, nums, 1, nums[0], True):
            calibration_result_3_operators += target

    return calibration_result_2_operators, calibration_result_3_operators


equ = read_equations('input.txt')
total_2_operators, total_3_operators = determine_total_calibration_result(equ)
print(f"Total calibration result with 2 operators: {total_2_operators}")
print(f"Total calibration result with 3 operators: {total_3_operators}")
