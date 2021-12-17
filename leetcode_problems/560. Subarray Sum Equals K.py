"""
https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers nums and an integer k, 
return the total number of continuous subarrays whose sum equals to k.
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return count

nums = [1,2,1,2,1]
k = 3

s = Solution()
print(s.subarraySum(nums,k))
        