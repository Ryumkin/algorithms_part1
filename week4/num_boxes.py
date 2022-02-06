import math


def num_boxes(n):
    tbl = [math.inf] * (n + 1)
    tbl[0] = 0
    for j in range(1, n + 1):
        i = 1
        place = i**3
        while place <= j:
            tbl[j] = min(tbl[j], tbl[j - place] + 1)
            i += 1
            place = i**3
    return tbl[n]

# should print 3
print(num_boxes(10))
