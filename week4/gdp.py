def gdp(n):
    tbl = [1] * (n + 1)
    for i in range(2, n + 1):
        tbl[i] = 2*tbl[i-1] + tbl[i-2]
    return tbl[n]
