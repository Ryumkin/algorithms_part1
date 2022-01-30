import math


def weighted_escape_length(maze,w, i=0, j=0):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:  # if our right item
        return 1
    restored_cell = maze[i][j]
    maze[i][j] = math.inf
    result = math.inf
    current_weight = 1 if restored_cell == 0 else w
    for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= x < n and 0 <= y < m and maze[x][y] != math.inf:
            possible_field = weighted_escape_length(maze, w, x, y)
            result = min(result, possible_field + current_weight)
    maze[i][j] = restored_cell
    return result


# some test code
if __name__ == "__main__":
    test_a = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    # should print 2
    print(weighted_escape_length(test_a, 0))
    test_b = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    # should print 5
    print(weighted_escape_length(test_b, 1))
    # should print 6
    print(weighted_escape_length(test_b, 2))


