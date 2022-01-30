import math


def fastest_escapes(maze, i=0, j=0):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:  # if our right item
        return[[(i,j)]]
    restored_cell = maze[i][j]
    maze[i][j] = 1
    result = []
    for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= x < n and 0 <= y < m and maze[x][y] == 0:
            possible_paths = fastest_escapes(maze, x, y)
            if possible_paths:
                result = [*result,*possible_paths]
            for path in result:
                if (i, j) not in path:
                    path.insert(0, (i, j))
    maze[i][j] = restored_cell

    if i == 0 and j == 0:
        min_length = min([len(path) for path in result]) if result else math.inf
        result = list(filter(lambda path: len(path) <= min_length, result))
    return result



def fastest_escape_length(maze, i=0, j=0):
    pass


def weighted_escape_length(maze, w, i=0, j=0):
    pass


def weighted_escapes(maze, w, i=0, j=0):
    pass


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

    # should print [[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
    print(fastest_escapes(test_a))
    # should print []
    print(fastest_escapes(test_b))
    # should print [5, 5, 5, 5, 5, 5]
    print(list(map(len, fastest_escapes([[0 for _ in range(3)] for _ in range(3)]))))
