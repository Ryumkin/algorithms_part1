import math


def fastest_escape_length(maze, i=0, j=0):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:  # if our right item
        return 1
    restored_cell = maze[i][j]
    maze[i][j] = 1
    result = math.inf
    for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= x < n and 0 <= y < m and maze[x][y] == 0:
            possible_field = fastest_escape_length(maze, x, y)
            result = min(result, possible_field)
    maze[i][j] = restored_cell
    return result + 1


maze = [
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 0, 0],
]

print(fastest_escape_length(maze))
