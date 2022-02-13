import math

def edistance(A, B):
    n = len(A)
    m = len(B)
    tbl = [[0 for о in range(m+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(m + 1):
            if i == 0:
                tbl[i][j] = j
                continue
            if j == 0:
                tbl[i][j] = i
                continue
            if A[i - 1] == B[j - 1]:
                tbl[i][j] = tbl[i - 1][j - 1]
            else:
                tbl[i][j] = min(tbl[i - 1][j],
                                tbl[i][j - 1],
                                tbl[i - 1][j - 1]) + 1
    return tbl[-1][-1]

def weighted_edistance(A, B, wdel, wins, wsub):
    n = len(A)
    m = len(B)
    tbl = [[0 for о in range(m + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                tbl[i][j] = j * wins
                continue
            if j == 0:
                tbl[i][j] = i * wdel
                continue
            if A[i - 1] == B[j - 1]:
                tbl[i][j] = tbl[i - 1][j - 1]
            else:
                tbl[i][j] = min(tbl[i - 1][j] + wdel,
                                tbl[i][j - 1] + wins,
                                tbl[i - 1][j - 1] + wsub)
    return tbl[-1][-1]

def edistance_substring(A, B):
    n = len(A)
    m = len(B)
    tbl = [[0 for о in range(m + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                tbl[i][j] = j
                continue
            if j == 0:
                tbl[i][j] = 0
                continue
            if A[i - 1] == B[j - 1]:
                tbl[i][j] = tbl[i - 1][j - 1]
            else:
                tbl[i][j] = min(tbl[i - 1][j],
                                tbl[i][j - 1],
                                tbl[i - 1][j - 1]) + 1
    return tbl[-1][-1]

if __name__ == "__main__":
    # should print 3
    print(edistance("good", "bad"))
    # should print 7
    print(weighted_edistance("good", "bad", 1, 2, 5))
