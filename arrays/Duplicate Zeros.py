## source https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/


#Python 3 real in-place solution
class Solution:
    def duplicateZeros(self, arr) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0


arr = [1,0,2,3,0,4]

s = Solution()
s.duplicateZeros(arr)