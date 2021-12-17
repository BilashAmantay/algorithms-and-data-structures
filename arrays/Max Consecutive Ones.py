### https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ml = None
        
        for n in nums:
            if n==1:
                if ml:
                    ml+=1
                else:
                    ml=1
            else:
                ml=0
        return ml

nums = [1,1,0,1,1,1]
s = Solution()
r = s.findMaxConsecutiveOnes(nums)
print(r)
        

### fastest solution in leedcode
import itertools
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max((sum(t[1]) for t in itertools.groupby(nums) if t[0] > 0), default=0)
