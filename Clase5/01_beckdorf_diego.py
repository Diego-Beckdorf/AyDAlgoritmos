import sys


def sub_map_paths(map, i, j):
    paths = 0

    if i == 0 and j == 0:
        return 1

    for step in range(1, i + 1):
        if step <= i and map[i-step][j] == step:
            paths += sub_map_paths(map, i-step, j)

    for step in range(1, j + 1):
        if step <= j and map[i][j-step] == step:
            paths += sub_map_paths(map, i, j-step)
    return paths


while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    map = []
    for _ in range(n):
        line = [int(i) for i in sys.stdin.readline()]
        map.append(line)
    m = len(map[0])
    print(sub_map_paths(map, n - 1, m - 1))