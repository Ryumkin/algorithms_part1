# Given an array aa, a sliding window of size kk  is moving from the very left of the array to the very right. Each time the sliding window moves right by one position. For each sliding window position return average value of all numbers inside the sliding window.
#
# Use two pointers to determine current sliding window position, you are not allowed to use loops inside the given whilewhile loop.
#
# Input example
#
# a = [1, 2, 3, 4, 8], \space k = 3a=[1,2,3,4,8], k=3

def moving_average(a, k):
  sum = 0
  for i in range(k):
    sum += a[i]
  window_sum = [sum]
  left, right = 0, k - 1
  while right + 1 < len(a):
    left += 1
    right += 1
    window_sum.append(window_sum[-1] + a[right] - a[left-1])
  return [x * 1.0 / k for x in window_sum]


# a = [3, 10, 14, 5, 11, 13, 14, 10, 11, 12]
# k = 1
k = 10
a = [8, 3, 4, 15, 7, 8, 6, 9, 7, 1, 5, 14, 11, 15, 11, 5]
print(moving_average(a,k))
