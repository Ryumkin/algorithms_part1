import math


def filter_result(maze, list_to_filter, w):
    result = []
    min_len = math.inf
    for path in list_to_filter:
        length_of_path = 0
        for x, y in path:
            length_of_path += 1 if maze[x][y] == 0 else w
        if length_of_path < min_len:
            result = [path]
            min_len = length_of_path
        elif length_of_path == min_len:
            result.append(path)
    return result


def weighted_escapes(maze, w,  i=0, j=0):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:  # if our right item
        return[[(i,j)]]
    restored_cell = maze[i][j]
    maze[i][j] = math.inf
    result = []
    for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= x < n and 0 <= y < m and  maze[x][y] != math.inf:
            possible_paths = weighted_escapes(maze, w,  x, y)
            if possible_paths:
                result = [*result,*possible_paths]
            for path in result:
                if (i, j) not in path:
                    path.insert(0, (i, j))
    maze[i][j] = restored_cell

    if result:
        if i == 0 and j == 0 :
            result = filter_result(maze,result, w)
    return result


# some test code
if __name__ == "__main__":
    test_a = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]

    test_b = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]

    # should print [[(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]]
    print(weighted_escapes(test_b, 0))
    # should print [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
    # the order of the paths within the list might be different
    print(weighted_escapes(test_b, 2))
