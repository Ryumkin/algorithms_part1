#https://youtu.be/hI0A_UOgdD8
# A landscape in a Flat World consists of blocks size 1 by 1 meter.

# The island is a set of different height columns consist of stone and surrounded by the sea.
#
# Heavy rain have fallen over the island, and filled all the lowlands with water. Extra water has gone back into the sea, without increasing its level. According to the landscape of the island, determine how many blocks of water remain after rain in the lowlands on the island.
#
# Implement a function calc_rain_water(h) which takes the landscape of the island and returns the number of remaining water blocks.
#
# One integer — remaining water blocks number.
#
# Example:
#
# Input: h = [2, 5, 2, 3, 6, 9, 1, 3, 4, 6, 1]Input:h=[2,5,2,3,6,9,1,3,4,6,1]
#
# Output: 15Output:15

def calc_rain_water(h):
    size = len(h)
    left = size * [0]
    right = size * [0]
    left[0] = h[0]
    max_from_left = h[0]
    for i in range(1, size):
        max_from_left = max(max_from_left, h[i])
        left[i] = max_from_left

    max_from_right = h[size - 1]
    right[size - 1] = h[size - 1]
    for i in range(size - 2, -1, -1):
        max_from_right = max(max_from_right, h[i])
        right[i] = max_from_right

    result = 0
    for i in range(size):
        result += min(left[i], right[i]) - h[i]
    return result


# some test code
if __name__ == "__main__":
    test_h = [2, 5, 2, 3, 6, 9, 1, 3, 4, 6, 1]
    # should print 15
    print(calc_rain_water(test_h))

    test_h = [2, 4, 6, 8, 6, 4, 2]
    # should print 0
    print(calc_rain_water(test_h))

    test_h = [8, 6, 4, 2, 4, 6, 8]
    # should print 18
    print(calc_rain_water(test_h))
