import random
# size=100
# nums = list(set([random.randint(1,size) for x in range(size)]))
# nums.sort()
# target=54
# res={}


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        res = {}

        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in res:
                return i,res[complement]
            res[nums[i]]=i

# s = Solution()
# i,j = s.twoSum(nums,target)
# print(nums[i])
# print(nums[j])

nums=[3,2,1,0,4,5]
target=6

s = Solution()

i,j = s.twoSum(nums,target)
print(i,j)
print(i,nums[i])
    print(j,nums[j])
          





