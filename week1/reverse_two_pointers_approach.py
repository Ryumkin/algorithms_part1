# Complete a function that reverses an array.
#
# For [1, 2, 4, 6] you have to get [6, 4, 2, 1].
#
# Do not allocate extra space for another array, you must do this in-place with O(1)O(1) extra memory.
#
# Use two pointers approach
#
# left points to the beginning of the array
#
# right points to the end of the array

def reverse(a):
  left, right = 0, len(a) - 1
  while left < right:
    a[left], a[right] = a[right], a[left]
    left += 1
    right -= 1
