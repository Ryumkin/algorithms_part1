def not_angry(n):
    # tbl[i] is going to contain the number of possible combinations for i days
    tbl = [0] * (n + 1)
    if n > 0:
        # base case: for just one day, there are ?? options
        tbl[1] = 1
        tbl[0] = 0
        for i in range(2, n + 1):
            tbl[i] = tbl[i-1] + tbl[i-2] + 1
        return tbl[n] +1

# should print 8
print(not_angry(4))
