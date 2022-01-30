# You would like to find your neighbour's password. You know its length and know that it consists only of letters A and B (your neighbor is not good in cybersecurity).
#
# Complete the code below to produce a recursive function passwords(n) that would produce a set of all words in letters A and B with n letters.
#
# F​or example passwords(2) should return {"AA", "AB", "BA", "BB"}.

def passwords(n):
    if n == 0:
        return {""}
    prev = passwords(n - 1)
    result = set()
    for p in prev:
        result.add(p + "A")
        result.add(p + "B")
        result.add("A" + p)
        result.add("B" + p)
    return result

    # should print {"AA", "AB", "BA", "BB"}
    # the elements in the set can be printed in different order
print(passwords(2))
