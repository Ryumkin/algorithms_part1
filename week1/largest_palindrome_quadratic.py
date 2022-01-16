#https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/?ref=lbp
def largest_palindrome(s):
    n = len(s)
    table = [[0 for x in range(n)] for y in range(n)]

    max_length = 1

    for i in range(n):
        table[i][i] = True

    start = 0
    i = 0

    while i < n-1:
        if s[i] == s[i+1]:
            table[i][i+1] = True
            start = i
            max_length = 2
        i += 1

    k = 3
    while k <= n:
        i = 0
        while i < (n - k + 1) :
            j = i + k -1
            if table[i+1][j-1] and s[i] == s[j]:
                table[i][j] = True

                if k > max_length:
                    max_length = k
                    start = i
            i += 1
        k += 1
    return s[start:start+max_length]


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

