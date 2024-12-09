# Day 9


def read_disk_map(file_name):
    disk_map = []
    disk_array = []

    with (open(file_name, 'r') as file):
        content = file.read()

        file_id = 0
        is_file = True
        for i in range(len(content)):
            if is_file:
                disk_map += [file_id for _ in range(int(content[i]))]
                disk_array.append([file_id, int(content[i])])
                file_id += 1
                is_file = False
            else:
                disk_map += [-1 for _ in range(int(content[i]))]
                disk_array.append([-1, int(content[i])])
                is_file = True

    return disk_map, disk_array


def transform_disk_map(disk_map):
    left = 0
    while left < len(disk_map) and disk_map[left] != -1:
        left += 1

    right = len(disk_map) - 1
    while right >= 0 and disk_map[right] == -1:
        right -= 1

    while left < right:
        if disk_map[left] == -1 and disk_map[right] != -1:
            disk_map[left] = disk_map[right]
            disk_map[right] = -1

        if disk_map[left] != -1:
            left += 1

        if disk_map[right] == -1:
            right -= 1


def rearrange_disk_map(disk_map, disk_array):
    right = len(disk_array) - 1
    while right >= 0 and disk_array[right][0] == -1:
        right -= 1

    while right > 0:
        left = 0
        while left < len(disk_array) and (disk_array[left][0] != -1 or disk_array[left][1] < disk_array[right][1]):
            left += 1

        if left < len(disk_array) and left < right:
            disk_array.insert(left, disk_array[right])
            disk_array[left + 1][1] -= disk_array[left][1]

            disk_array.pop(right + 1)
            disk_array.insert(right + 1, [-1, disk_array[left][1]])

            if disk_array[left + 1][1] == 0:
                disk_array.pop(left + 1)

        right -= 1
        while right >= 0 and disk_array[right][0] == -1:
            right -= 1

    disk_map.clear()
    for i in range(len(disk_array)):
        disk_map += [disk_array[i][0] for _ in range(disk_array[i][1])]


def filesystem_checksum(disk_map):
    checksum = 0

    for i in range(len(disk_map)):
        if disk_map[i] != -1:
            checksum += i * disk_map[i]

    return checksum


disk_map, disk_array = read_disk_map('input.txt')

transform_disk_map(disk_map)
checksum = filesystem_checksum(disk_map)
print(f"Filesystem fragmentation checksum: {checksum}")

rearrange_disk_map(disk_map, disk_array)
checksum = filesystem_checksum(disk_map)
print(f"Filesystem with whole files checksum: {checksum}")
