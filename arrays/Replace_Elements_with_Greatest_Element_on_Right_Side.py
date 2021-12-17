## https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/

## my solution:

class Solution:
    def replaceElements(self, arr: list) -> list:
        ln = len(arr)

        if ln==0:
            return arr
        if ln==1:
            return [-1]

        max=-1

        for i in range(ln-1,-1,-1):
            # print(i, ' -> ',arr[i])
            old = max
            if arr[i]>max:
                max=arr[i]
            arr[i] = old
        return arr

## better solution
class Solution:
    def replaceElements(self, arr: list) -> list:

        max_value=-1

        for i in range(len(arr)-1, -1, -1):
            if arr[i] > max_value:
                arr[i], max_value = max_value, arr[i]
            else:
                arr[i] = max_value
        return arr
        

arr = [17,18,5,4,6,1]
s  = Solution()
r = s.replaceElements(arr)

print(r)      

print(s.replaceElements([4]))

    