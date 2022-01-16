#https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/?ref=lbp
def check_palindrome(left, right, s):
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def largest_palindrome(s):
    n = len(s)
    maxlength = 1
    start = 0
    for i in range(n):
        for j in range(i,n):

            if check_palindrome(i, j, s):
                if j - i + 1 > maxlength:
                    start = i
                    maxlength = j -i + 1

    return s[start:start+maxlength]


# some test code
if __name__ == "__main__":
    test_s = 'ABBCB'
    # should print BCB
    print(largest_palindrome(test_s))

    test_s = 'ABACABAD'
    # should print ABACABA
    print(largest_palindrome(test_s))

    test_s = 'ABCDE'
    # should print A
    print(largest_palindrome(test_s))

