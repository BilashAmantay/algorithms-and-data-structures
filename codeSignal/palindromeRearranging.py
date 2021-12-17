"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
"""

def solution(inputString):
    '''
    cases:
    1. abba -- fully mirror
    2. center point is a single alphabet: aaabbbcbbbaaa. remaining frequency // 2 == 0 
    
    '''
    if len(inputString)==0:
        return False
    if len(inputString)==1:
        return True
        
    freq  = [0] * 26
    
    for a in inputString:
        freq[ord(a) - ord('a')]+=1
    print(freq)
    
    ## it is allowed to have only one alphabet with odd count.
    singleCount = 0
    for i in range(len(freq)):
        if freq[i]%2==1:
            singleCount+=1
            freq[i]+=1
        if singleCount>1:
            return False

    
        
    for v in freq:
        if v%2!=0:
            return False
    return True 

inputString = "ababa"
print(solution(inputString))

## Above are my method, passed in codeSignal, bellow from  mosted voted solution:;
def solution(inputString):
    
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1