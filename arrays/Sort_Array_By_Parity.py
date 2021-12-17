'''
Sort Array By Parity

Solution
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
'''

class Solution:
    def sortArrayByParity(self, nums: list) -> list:
        
        left=0
        right=len(nums)-1

        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[left] , nums[right] = nums[right], nums[left]
                left += 1
        return nums


nums = [3,1,5,2,7]
s = Solution()
print(s.sortArrayByParity(nums))
