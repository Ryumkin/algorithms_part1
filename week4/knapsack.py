def knapsack_dynamic(W, V, C):  # O(nC)
    n = len(W)
    tbl = [[0] * (C + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(C + 1):
            tbl[i][j] = tbl[i - 1][j]
            if j >= W[i - 1]:
                tbl[i][j] = max(
                    tbl[i][j],
                    tbl[i - 1][j - W[i - 1]] + V[i - 1]
                )
    # print("\n".join([str(l) for l in tbl]))
    return tbl[-1][-1]


if __name__ == '__main__':
    W_example = [4, 1, 6, 9]
    V_example = [6, 17, 9, 10]
    C = 12
    print(knapsack_dynamic(W_example, V_example, C))
