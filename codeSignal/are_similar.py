"""
Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

Array of integers.

Guaranteed constraints:
3 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 1000.

[input] array.integer b

Array of integers of the same length as a.

Guaranteed constraints:
b.length = a.length,
1 ≤ b[i] ≤ 1000.

[output] boolean

true if a and b are similar, false otherwise.
"""
def solution(a, b):
    switchIdx=[]
    if a==b:
        return True
    else:
        for i in range(len(a)):
            if a[i]!=b[i]:
                switchIdx.append(i)

                if len(switchIdx)>2:
                    print(switchIdx)
                    return False
        
        if a[switchIdx[0]] == b[switchIdx[1]] and a[switchIdx[1]] == b[switchIdx[0]]:
            return True
        else:
            return False



a =[1, 1, 4]
b =[1, 2, 3]

print(solution(a,b))