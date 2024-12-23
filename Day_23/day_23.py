# Day 23

import re
import itertools


def read_connections(file_name):
    connections = {}

    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            computers = list(map(str, re.findall(r'[a-z]+', line)))

            if computers[0] not in connections:
                connections.update({computers[0]: [computers[1]]})
            else:
                if computers[1] not in connections[computers[0]]:
                    connections[computers[0]].append(computers[1])

            if computers[1] not in connections:
                connections.update({computers[1]: [computers[0]]})
            else:
                if computers[0] not in connections[computers[1]]:
                    connections[computers[1]].append(computers[0])

    return connections


def find_three_lan_connections(connections):
    result = 0
    already_found = []
    for p_key in connections.keys():
        if p_key[0] == 't':
            for s_key in connections[p_key]:
                for t_key in connections[s_key]:
                    if p_key in connections[t_key]:
                        is_connections_found = False
                        for i in range(len(already_found)):
                            if p_key in already_found[i] and s_key in already_found[i] and t_key in already_found[i]:
                                is_connections_found = True
                                break

                        if not is_connections_found:
                            already_found.append([p_key, s_key, t_key])
                            result += 1

    return result


def all_connected(connections, computers):
    for c_1 in computers:
        for c_2 in computers:
            if c_1 != c_2 and c_1 not in connections[c_2]:
                return False

    return True


def generate_combinations(connections):
    combs = []
    for key in connections.keys():
        computers = [key]
        computers.extend(connections[key])
        for i in range(1, len(computers) + 1):
            els = [list(x) for x in itertools.combinations(computers, i)]
            combs.extend(els)

    return combs


def find_largest_connection(connections):
    combinations = generate_combinations(connections)

    max_idx = -1
    for i in range(len(combinations)):
        if all_connected(connections, combinations[i]):
            if max_idx == -1:
                max_idx = i
            elif len(combinations[max_idx]) < len(combinations[i]):
                max_idx = i

    lan_party = combinations[max_idx]
    lan_party.sort()

    password = ''
    for i in range(len(lan_party)):
        password += lan_party[i]
        if i < len(lan_party) - 1:
            password += ','

    return password


c = read_connections('input.txt')

t = find_three_lan_connections(c)
print(f"The number of connections that contain at least one computer with a name that starts with 't': {t}")

p = find_largest_connection(c)
print(f"The password to get into the LAN party: {p}")
