import math
from heapq import merge


def find_percentile(a, b, p):
    k = (p / 100) * (len(a) + len(b))
    return find_kth_element(a, len(a), b, len(b), math.ceil(k))


def find_kth_element(arr1, end1, arr2, end2, k, start1=0, start2=0):
    if k > (end1 + end2) or k < 1:
        return -1

    # first array should be less then second
    if end1 > end2:
        return find_kth_element(arr2, end2, arr1, end1, k, start2, start1)

    # Check if arr1 is empty returning k-th element of arr2 + initial index
    if end1 == 0:
        return arr2[k + start2 - 1]

    # Check if k = 1 return minimum of first two elements of both arrays
    # + initial index
    if k == 1:
        return min(arr1[start1], arr2[start2])

    # binary search approach (divide and conquer)
    i = min(end1, k // 2)
    j = min(end2, k // 2)

    if arr1[i + start1 - 1] > arr2[j + start2 - 1]:

        # Now we need to find only k-j th element since we
        # have found out the lowest j
        return find_kth_element(arr1, end1, arr2, end2 - j, k - j, start1, start2 + j)
    else:

        # Now we need to find only k-i th element since we
        # have found out the lowest i
        return find_kth_element(arr1, end1 - i, arr2, end2, k - i, start1 + i, start2)


def find_percentile_initial_approach(a, b, p):
    merged_array = list(merge(a, b))
    k = (p / 100) * len(merged_array)
    return merged_array[math.ceil(k) - 1]


# some test code
if __name__ == "__main__":
    test_a, test_b, test_p = [1, 2, 7, 8, 10], [6, 12], 50
    # should print 7
    print(find_percentile(test_a, test_b, test_p))

    test_a, test_b, test_p = [1, 2, 7, 8], [6, 12], 50
    # should print 6
    print(find_percentile(test_a, test_b, test_p))

    test_a, test_b, test_p = [15, 20, 35, 40, 50], [], 30
    # should print 20
    print(find_percentile(test_a, test_b, test_p))

    test_a, test_b, test_p = [15, 20], [25, 40, 50], 40
    # should print 20
    print(find_percentile(test_a, test_b, test_p))


# The idea is the same as binary search approach or divide and conquer approach
#
