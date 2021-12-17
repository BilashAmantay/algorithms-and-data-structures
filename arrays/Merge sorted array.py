## https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:
'''

nums1 = [3,0,0,0,0]; m = 1; nums2 = [1,2,4,5];n = 4

class List(list):
    pass
        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1=m-1 ## for nums1
        i2=n-1 ## for nums2
        j = m + n -1 

        while i1>=0 and i2>=0:
            if nums1[i1] > nums2[i2]:
                nums1[j] = nums1[i1]
                i1-=1
            else:
                nums1[j] = nums2[i2]
                i2-=1

            j-=1
        while i2>=0:
            nums1[j] = nums2[i2]
            j-=1
            i2-=1
            
        return None

s = Solution()
s.merge(nums1, m, nums2, n)
print(nums1)

#### 0000=------------------------ Another way
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        k = 0
        temp = nums1[:m]
        
        # temp = [4, 5]
        # nums2 = [1, 2, 3]
        
        while i < m and j < n:
            if temp[i] < nums2[j]:
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        while i < m:
            nums1[k] = temp[i]
            i += 1
            k += 1
            
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
