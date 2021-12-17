##https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

class Solution:
    def validMountainArray(self, arr: list) -> bool:
        i=0
        j=1
        direct =[]
        last = None
        while j<len(arr):
            if arr[j] == arr[i]:
                return False 
            dir = arr[j] > arr[i]
            if dir != last:
                direct.append(dir)
                last = dir
            if direct == [False]:
                return False
            
            i+=1
            j+=1
        return direct == [True, False]


arr = [2,1,2,3,5,7,9,10,12,14,15,16,18,14,13]
s = Solution()
print(s.validMountainArray(arr))



