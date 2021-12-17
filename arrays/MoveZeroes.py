#https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/


class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        wp  = 0 ## write poritner
        rp = 1 ## read pointer

        for rp in range(1,len(nums)):
            print(nums[rp])
            

            if nums[wp]==0:
                if nums[rp]!=0:
                    nums[wp], nums[rp] = nums[rp], nums[wp]
                    wp+=1
            else:
                wp+=1
            
        return None
        
        


nums = [1,0,1]
s = Solution()
s.moveZeroes(nums)
print(nums)


## solutions from other
class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
        
        for j in range(i,len(nums)):
            nums[j]=0

nums = [1,0,1]
s = Solution()
s.moveZeroes(nums)



## The fastest solution with 28ms 
class Solution:
    def moveZeroes(self, nums: list) -> None:
        count=nums.count(0)
        nums[:]=[i for i in nums if i != 0]
        nums+=[0]*count