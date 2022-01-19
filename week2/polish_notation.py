# https://danishmujeeb.com/blog/2014/12/parsing-reverse-polish-notation-in-python/
# Question 2
# In reverse Polish notation for mathematical expressions, the operators follow their operands. For instance
#
# 3 + 4 would be written like 3 4 +
#
# 3 − 4 * 5 would be written like 3 4 5 * −
#
# To calculate reverse Polish notation expression stack data structure will be helpful. Read the expression from the left to right, if you meet operand push it into stack, otherwise execute an operation.
#
# Fulfil reverse\_notationreverse_notation function.
#
# Input format: ss is a list consisting of floats and symbols "+", "-", "*", "/".
#
# s = [4, 3, "-", 2, "*"]
def reverse_notation(s):
    stack = []
    for i in range(len(s)):
        if not s[i] in ['+', '-', '*', '/']:
            # add operand to stack
            # your code here
            stack.append(int(s[i]))
        else:
            # to execute operation get operands from the stack
            # be careful with operands order during execution
            # your code here
            var1 = stack.pop()
            var2 = stack.pop()
            if s[i] == "-":
                stack.append(var2 - var1)
            if s[i] == "+":
                stack.append(var2 + var1)
            if s[i] == "*":
                stack.append(var2 * var1)
            if s[i] == "/":
                stack.append(var2 / var1)
    return stack.pop()


print(reverse_notation([5, 6, '-']))
