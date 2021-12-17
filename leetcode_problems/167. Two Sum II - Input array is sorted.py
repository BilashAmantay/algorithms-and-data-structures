"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        l = 0
        r = len(numbers)-1

        while l<r:
            sm = numbers[l] + numbers[r]

            if sm == target:
                return [l+1,r+1]
            elif sm > target:
                r-=1
                
            else:
                l+=1
        


        

numbers = [2,7,11,15]
target = 9

s = Solution()
print(s.twoSum(numbers,target))