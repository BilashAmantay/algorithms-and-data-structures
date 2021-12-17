"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters and the characters ( and ). It is guaranteed that all parentheses in inputString form a regular bracket sequence.

Guaranteed constraints:
0 ≤ inputString.length ≤ 50.

[output] string

Return inputString, with all the characters that were in parentheses reversed.
"""

def solution(inputString):
    ps, pe = [],[] # paranthesis start and end
    
    i=0
    res = ''
    tmp=''
    while i<len(inputString):
        if inputString[i] not in ['(',')']:
            res+=inputString[i]
        elif inputString[i]=='(':
            ps.append(i)
            i+=1
            while ps:
                if inputString[i]=='(':
                    ps.append(i)
                    
                elif inputString[i]==')':
                    ## now, goingg backword
                    pe = i
                    inputString = inputString[:i] + inputString[i+1:]
                    i-=1
                    
                    while inputString[i]!='(':
                        tmp+=inputString[i]
                        i-=1
                    inputString = inputString[:ps.pop()] + tmp + inputString[pe:]
                    tmp=''
                    i-=1

                i+=1
            i-=1
            
        i+=1
    return res
    
inputString = "foo(bar(baz))blim"
# inputString = "abc(def(xyz(uvw)))1234"
s = solution(inputString)
print(s)
print(s == "foobazrabblim")
            
            
        
            

