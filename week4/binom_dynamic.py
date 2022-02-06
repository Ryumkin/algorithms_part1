def binom(n, k):
    # tbl[i][j] is going to contain binom(i, j)
    tbl = [[1 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(1, min(k + 1, i)):
            tbl[i][j] = tbl[i-1][j] + tbl[i-1][j-1]
    return tbl[n][k]

# should print 20
print(binom(6, 3))
# should print 21
print(binom(7, 2))
