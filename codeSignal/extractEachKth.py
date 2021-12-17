def solution(inputArray, k):
    res = []
    for i in range(len(inputArray)):
        if (i+1)%k!=0:
            res.append(inputArray[i])
    return res
            
inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(inputArray,3))