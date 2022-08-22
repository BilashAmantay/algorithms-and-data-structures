a = [3,5,1,1,6,3,3,5]
import numpy as np
a = np.random.randint(10,size=1000000)


def solution(A):
    # write your code in Python 3.6
    count =0

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if a[i] == a[j]:
                # print('a[{}]={}, a[{}]={}'.format(i,A[i], j, A[j]))
                count+=1

                # if count >= 1000000000:
                if count >= 200:                    
                    return count
    return count

print(solution(a))