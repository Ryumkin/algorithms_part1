import math


def tj_cost(L, W):
    n = len(W)
    tbl = [math.inf] * (n + 1)
    tbl[0] = 0
    for i in range(1, n + 1):
        length = -1
        for j in range(i - 1, -1, -1):
            length += len(W[j]) + 1
            penalty = 0
            if length > L:
                penalty = math.inf
            else:
                if i != n:
                    penalty = (L - length) ** 3
            tbl[i] = min(tbl[i], tbl[j] + penalty)
    return tbl[n]


def tj(L, W):
    n = len(W)
    tbl = [math.inf] * (n + 1)
    tbl[0] = 0
    lines = [0] * (n + 1)
    for i in range(1, n + 1):
        length = -1
        for j in range(i - 1, -1, -1):
            length += len(W[j]) + 1
            if length > L:
                penalty = math.inf
            else:
                if i != n:
                    penalty = (L - length) ** 3
                else:
                    penalty = 0
            if tbl[i] > tbl[j] + penalty:
                tbl[i] = tbl[j] + penalty
                lines[i] = j

    strings = []
    index = n
    while index > 1:
        strings.append(W[lines[index]:index])
        index = lines[index]

    result = ""
    for i in range(len(strings) - 1, -1, -1):
        result += " ".join(strings[i]) + "\n"
    return result[:-1]


if __name__ == "__main__":
    W_example = ["jars", "jaws", "joke", "jury", "juxtaposition"]
    L_example = 15
    # should print 432
    print(tj_cost(L_example, W_example))
    # should print:
    # jars jaws
    # joke jury
    # juxtaposition
    print(tj(L_example, W_example))
