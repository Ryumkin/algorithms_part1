def valid_parentheses(s):
  stack = []
  open = {')': '(', '}': '{', ']': '['}
  for i in range(len(s)):
    if s[i] in ['(', '[', '{']:
      # push open bracket into the stack
      # your code here
      stack.append(s[i])
    else:
      if len(stack) == 0:
        # stack is empty and there isn't a pair for current close bracket
        # your code here
        return False
      elif stack[-1] == open[s[i]]:
        # top bracket has the same type with current close bracket
        # you don't need this bracket in the stack anymore
        # your code here
        stack.pop()
      else:
        # close bracket has different type with open one on the top of the stack
        # your code here
        return False
  return len(stack) == 0
