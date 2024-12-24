# Day 24

import re


def read_device(file_name):
    device_input = {}
    device_gates = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        is_wire = True
        for line in lines:
            line = line.strip()

            if len(line) == 0:
                is_wire = False
                continue

            if is_wire:
                wire = re.findall(r'[a-z][0-9]+', line)
                value = re.findall(r': [0-1]', line)

                if int(value[0][2]):
                    device_input[wire[0]] = True
                else:
                    device_input[wire[0]] = False

            else:
                wires = re.findall(r'[a-z]+[0-9]+|[a-z]+|[0-9]+', line)
                gate = re.findall(r'AND|OR|XOR', line)

                logic_gate = [gate[0]]

                for wire in wires:
                    logic_gate.append(wire)

                device_gates.append(logic_gate)

    return device_input, device_gates


def convert_number(device_wires, char='z'):
    array = []
    keys = device_wires.keys()
    for key in keys:
        if key[0] == char and ord('0') <= ord(key[1]) <= ord('9') and ord('0') <= ord(key[2]) <= ord('9'):
            array.append(key)

    result = 0
    aux = 1
    array.sort()
    for key in array:
        result += device_wires[key] * aux
        aux *= 2

    return result


def system_calculation(device_input, device_gates):
    device_wires = device_input.copy()
    visited = [False for _ in range(len(device_gates))]
    nr_calculations_done = 0
    different = -1

    while len(visited) > nr_calculations_done != different:
        different = nr_calculations_done

        for i in range(len(visited)):
            if not visited[i]:
                keys = device_wires.keys()
                if device_gates[i][1] in keys and device_gates[i][2] in keys:
                    output = device_gates[i][3]
                    gate = device_gates[i][0]

                    if gate == 'AND':
                        device_wires[output] = device_wires[device_gates[i][1]] and device_wires[device_gates[i][2]]
                    elif gate == 'OR':
                        device_wires[output] = device_wires[device_gates[i][1]] or device_wires[device_gates[i][2]]
                    elif gate == 'XOR':
                        device_wires[output] = device_wires[device_gates[i][1]] ^ device_wires[device_gates[i][2]]

                    visited[i] = True
                    nr_calculations_done += 1

    return convert_number(device_wires, 'z')


di, dg = read_device('input.txt')

r = system_calculation(di, dg)
print(f"The decimal number that it outputs on the wires starting with 'z': {r}")
