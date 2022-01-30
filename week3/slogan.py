# Y​ou would like to write a slogan with length exactly LL symbols (this is a width of a billboard you have payed for). You have a nonempty list of distinct words characterizing your product (e.g., ["modern", "cool", "abysmal"]). The slogan is several of these words separated by commas (repetitions are not allowed).
#
# F​or example if the words are ["modern", "cool", "abysmal"] and L = 12L=12, then "cool,abysmal" would be a feasible slogan.
#
# Complete the code below to produce a recursive function slogan(words, L) that returns True if there is a feasible slogan and False otherwise

def slogan(words, L):
    if len(words) == 1 or len(words[-1]) == L:
        return len(words[-1]) == L
    last_word = words[-1]
    without_last_word = words[:-1]
    return slogan(without_last_word, L) or slogan(without_last_word, L - len(last_word) - 1)

# should print True
print(slogan(["modern", "cool", "abysmal"], 12))
# should print False
print(slogan(["modern", "cool", "abysmal"], 13))
