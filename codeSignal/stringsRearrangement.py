"""
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
solution(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
solution(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.

"""
from itertools import product


import itertools

def solution(inputArray):
    
    ln = len(inputArray)
    perms = list(itertools.permutations(inputArray))
    
    for perm in perms:
        for i in range(len(perm)-1):
            if sum([perm[i][j] != perm[i+1][j] for j in range(len(perm[i]))])!=1:
                break
            if i==len(perm)-2:
                return True
    return False

inputArray = ["ab", "bb", "aa"]
inputArray = ["aba", "bbb", "bab"]
print(solution(inputArray))

