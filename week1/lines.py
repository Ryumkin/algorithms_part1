def lines(a: list):
    a = a.copy()
    destroyed = 0
    left = right = 0

    while right+1 < len(a):
        right += 1
        if a[left] != a[right]:
            if right - left > 2:
                destroyed += right - left
                del a[left:right]
                left, right = 0, 0
            else:
                left = right
            continue
        if right == len(a) - 1:
            if left == 0 and right - left >= 2:
                destroyed += right - left + 1
            else:
                if right - left >= 2:
                    destroyed += right - left + 1
    return destroyed


if __name__ == "__main__":
    test_a = [2, 2, 1, 1, 1, 2, 1]
    # should print 6
    print(lines(test_a))

    test_a = [0, 0, 0, 0, 0]
    # should print 5
    print(lines(test_a))

    test_a = [2, 3, 1, 4]
    # should print 0
    print(lines(test_a))

    test_a = [1, 3, 3, 3]
    # should print 0
    print(lines(test_a))
