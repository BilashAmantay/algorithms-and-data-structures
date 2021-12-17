"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-105 ≤ inputArray[i] ≤ 105.

[output] integer

The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.
"""

def solution(inputArray):
    target = inputArray[0]
    sm=0
    
    for i in range(1,len(inputArray)):
        target +=1 
        if target<inputArray[i]:
            target = inputArray[i]
        elif target > inputArray[i]:
            sm+=abs(inputArray[i]-target)

    return sm
    

inputArray = [-1000, 0, -2, 0]
# inputArray = [1,1,1]
# inputArray = [2,1,0,-1]
inputArray = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]
print(solution(inputArray))