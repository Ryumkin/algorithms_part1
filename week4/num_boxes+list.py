import math


def num_boxes(n):
    tbl = [math.inf] * (n + 1)
    tbl[0] = 0
    last = [0] * (n + 1)
    for j in range(1, n + 1):
        i = 1
        place = i**3
        while i ** 3 <= j:
            if tbl[j] > tbl[j-place]+1:
                tbl[j] = tbl[j-place]+1
                last[j] = i
            i += 1
            place = i**3
    cubes = []
    current = n
    while current > 0:
        cubes.append(last[current])
        current -= last[current] **3
    return (tbl[-1], cubes)

# should print (3, [1, 1, 2])
# the order of boxes might be different
print(num_boxes(10))
