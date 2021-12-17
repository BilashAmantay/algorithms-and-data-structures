## https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) == 0:
            return 
        i = 0
        curr_value = nums[0]
        
        for j in range(1, len(nums)):
            if nums[j] != curr_value:
                i+=1
                nums[i] = nums[j]
                curr_value = nums[j]
            print(' '.join([str(n) for n in nums]))
        
        return i + 1


nums = [1,1,2,3,3,3,4]
s = Solution()
k = s.removeDuplicates(nums)


print(nums)
print(k)
print(nums[:k])