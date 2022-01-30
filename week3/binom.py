def binom(n, k):
    if k == 0 or k == n:
        return 1
    return binom(n-1, k) + binom(n-1, k-1)

# should print 20
print(binom(6, 3))
# should print 21
print(binom(7, 2))
