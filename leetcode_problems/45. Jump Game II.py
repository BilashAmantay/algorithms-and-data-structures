"""
nums[-1] is the target

i is the latest position jump to target, keep i as minimum as possible

"""
class Solution:
    def jump(self, nums: list) -> int:
        i=0
        c = 1
        while i < len(nums):
            if c+nums[i]== nums[-1]:
                return c
            i+=1
            c+=1
        return -1


nums = [2,3,1,1,4] # 2
nums = [2,3,0,1,4] # 2
# nums = [1,2] # 1
s = Solution()
print(s.jump(nums))