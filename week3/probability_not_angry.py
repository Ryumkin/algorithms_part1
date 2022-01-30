#https://stackoverflow.com/questions/65964996/recursion-function-to-calculate-the-probability

def probability_not_angry(n, p):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return (1-p)*probability_not_angry(n-1, p) + p*(1-p)*probability_not_angry(n-2, p)

# should print 0.5
print(probability_not_angry(4, 0.5))
# should print 0.4375
print(probability_not_angry(2, 0.75))
