A = [1,0.1,-1,-7,3,-5,-2.5,0,1]

# A = [2,2,0,3,-7,3,-5,-2.5,0,1]

def brutal_force(A):
    p=1
    mx=float('-inf')
    i=0
    while i < len(A)-1:
        print(A[i])
        p = A[i]

        for j in range(i+1,len(A)):
            p = A[j] * p
            
            if p ==  0:
                i=j
                break
            print(A[i:j+1])
            print('p at {},{} = {}'.format(i,j, p))
            if p > mx:
                mx = p  
                if mx>1000000000:
                    print('early return ',i,j)
                    return mx

                print('so farr largest ', mx, ' at a[i,j]',i,j, A[i],A[j])
        i+=1
    print(' Largest:', mx)
    return mx
print(brutal_force(A))

# A = [2,2,0,3,-7,0,3,-5,5,100,100,-1,0,4]

# def optimized(A):
#     zeros = []
#     largestExpend = 0
#     for i in range(len(A)):
#         if A[i]==0:
            
#             if zeros == []:
#                 expend = i
#             else:
#                 expend = i - zeros[-1]
#             zeros.append(i)
#             print('zero at index ',i, ' expend ', expend )
#             if  expend > largestExpend:
#                 largestExpend = expend
#                 largestExpendStart = zeros[-2]
#                 largestExpendEnd = zeros[-1]
        


#     print('largestExpend start end', largestExpendStart , largestExpendEnd)

#     return zeros,largestExpend

# print(optimized(A))



print('ok')
