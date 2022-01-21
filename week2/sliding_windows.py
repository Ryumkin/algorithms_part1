# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

from collections import deque


def sliding_window_min(a, k):
    result = []
    queue = deque()
    for i in range(k):
        while queue and a[i] < a[queue[-1]]:
            queue.pop()

        queue.append(i);

    for i in range(k, len(a)):
        result.append(a[queue[0]])

        while queue and queue[0] <= i - k:
            queue.popleft()

        while queue and a[i] < a[queue[-1]]:
            queue.pop()

        queue.append(i)

        # Print the maximum element of last window
    result.append(a[queue[0]])
    return result


# some test code
if __name__ == "__main__":
    test_a, test_k = [1, 3, 4, 5, 2, 7], 3
    # should print [1, 3, 2, 2]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [5, 4, 10, 1], 2
    # should print [4, 4, 1]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [10, 20, 6, 10, 8], 5
    # should print [6]
    print(sliding_window_min(test_a, test_k))
