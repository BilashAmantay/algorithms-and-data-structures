"""
2006. Count Number of Pairs With Absolute Difference K
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
"""

from collections import defaultdict, Counter
    
class Solution:
    def countKDifference(self, nums: list, k: int) -> int:
        """
        for each :
            calc complement+- k 
            if complemnts in s, count += s[complement]
        """
        count=0
        freq = defaultdict(int)

        for num in nums:
            complement1 = k+num
            complement2 = num-k

            count+=freq[complement1]
            count+=freq[complement2]

            freq[num]+=1
                
        return count


nums =[7,7,8,3,1,2,7,2,9,5]
k = 6

s = Solution()
print(s.countKDifference(nums, k))


nums = [1,2,2,1]
k=1
s = Solution()
print(s.countKDifference(nums, k))