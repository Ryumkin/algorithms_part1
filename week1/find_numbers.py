#https://afteracademy.com/blog/check-for-pair-in-an-array-with-a-given-sum
# Given an array aa and a number kk. An array is sorted in increasing order.
# Check if there are two elements xx and yy in the array such that they add up to kk.

# Your solution has to work for O(n)O(n).

def find_numbers(a, k):
  left, right = 0, len(a) - 1
  while left < right:
    possible_value = a[left] + a[right]
    if possible_value == k:
      return True
    if possible_value < k:
      left += 1
      continue
    right -= 1
  return False
