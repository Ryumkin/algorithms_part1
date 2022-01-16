# Question 2
# A string is called a palindrome if it reads the same backward as forward, such as madam, racecar.
#
# Given a string that contains lowercase characters a-z and whitespaces. Complete a function that checks if this string is a palindrome ignoring whitespaces.
#
# You are not allowed to use additional string, join and replace methods. Use two pointers to compare a symbol from the beginning of the string to the corresponding symbol from the end of the string and "skip" whitespaces while moving the pointers.
#
# Example:
#
# " mad am    " is a palindrome
#
# "  ma d  " is not

def is_palindrome(s):
  left, right = 0, len(s) - 1
  while left < len(s) and right >= 0:
    if s[left] == ' ':
      left += 1
      continue
    if s[right] == ' ':
      right -= 1
      continue
    if left < len(s) and right >= 0 and s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True
