## https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/

'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
'''
from collections import deque

class Solution:
    def thirdMax(self, nums: list) -> int:
        max1 = max2 = max3 = float('-inf')

        for n in nums:
            if n in (max1 , max2 , max3):
                continue
            
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n> max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n       

        if max3 != float('-inf'):
            return max3
        else:
            return max1


nums = [3,2,1,5,2,4,9]

s = Solution()
print(s.thirdMax(nums))

