class Solution:
    def searchInsert(self, nums: list, target: int) -> int:

        low, high = 0, len(nums)-1
        
        while low<=high:
            mid = (high - low)  // 2 + low
            if nums[mid] == target:
                return mid
            if nums[mid]<target:
                low = mid+1
            else:
                high = mid -1
        # print(low)
        # print(mid)
        return low

            

nums = [1,3,5,7]
target =6
s = Solution()
print(s.searchInsert(nums, target))

nums = list(range(-7,15,3))
for i in range(-10,18):
    r = s.searchInsert(nums, i)
    print(i,r, i==r)

        