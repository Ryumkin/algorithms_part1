# Given an array aa sorted in non-decreasing order. Find how many unique elements are there in this array.
#
# Your solution has to work for O(n).
def find_unique(a):
  current_number_index = 0
  unique = 1
  for i in range(1,len(a)):
    if a[current_number_index] != a[i]:
      current_number_index = i
      unique += 1
  return unique

a = [1,2,2,2,3,3]

print(find_unique(a))
