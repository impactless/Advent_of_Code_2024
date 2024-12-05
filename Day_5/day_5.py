# Day 5

from collections import defaultdict, deque
import re


def read_manual(file_name):
    page_rules = []
    page_update = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

        is_rules = True
        for line in lines:
            line = line.strip()
            if not line:
                is_rules = False
                continue

            numbers = list(map(int, re.findall(r'\d+', line)))
            if is_rules is True:
                page_rules.append(numbers)
            else:
                page_update.append(numbers)

    return page_rules, page_update


def build_graph(page_rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for rule in page_rules:
        x, y = rule
        graph[x].append(y)
        in_degree[y] += 1
        in_degree[x] += 0

    return graph, in_degree


def topological_sort(graph, in_degree):
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_order) != len(in_degree):
        raise ValueError('Cycle detected in the rules graph.')

    return sorted_order


def validate_update(update, graph):
    position = {page: idx for idx, page in enumerate(update)}
    for x, neighbors in graph.items():
        if x in position:
            for y in neighbors:
                if y in position and position[x] > position[y]:
                    return False
    return True


def reorder_update(update, graph):
    update_set = set(update)
    subgraph = {node: [n for n in neighbors if n in update_set] for node, neighbors in graph.items() if node in
                update_set}
    in_degree = {node: 0 for node in update_set}

    for node, neighbors in subgraph.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    return topological_sort(subgraph, in_degree)


def process_updates(page_rules, page_updates):
    graph, in_degree = build_graph(page_rules)

    correct_sum = 0
    incorrect_sum = 0
    for update in page_updates:
        if validate_update(update, graph):
            correct_sum += update[len(update) // 2]
        else:
            reordered_update = reorder_update(update, graph)
            incorrect_sum += reordered_update[len(reordered_update) // 2]

    return correct_sum, incorrect_sum


Page_rules, Page_update = read_manual('input.txt')
Correct_sum, Incorrect_sum = process_updates(Page_rules, Page_update)
print(f'Sum of middle page numbers for correctly ordered updates: {Correct_sum}')
print(f'Sum of middle page numbers for corrected updates: {Incorrect_sum}')
