"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

class Solution:
    def singleNumber(self, nums) -> int:
        res=0
        
        for i in nums:
            res^=i
            print('Num={}, res={}'.format(i, res))
        return res


##  Above solution got worst performence when compared to other python solution. 
## Here is the top solution

class Solution:
    def singleNumber(self, nums) -> int:
        res=0
        
        for i in nums:
            res^=i
        
        return res


nums = [2,3,5,6,2,3,6,5,1]

s = Solution()
print(s.singleNumber(nums))