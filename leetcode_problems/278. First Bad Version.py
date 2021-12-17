"""
https://leetcode.com/problems/first-bad-version/
""" 

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(version):
    if version > 5:
        return True
    return False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        

        while low<=high:
            mid = (n-low)/2 + low

            mid_is_bad = isBadVersion(mid)

            if mid_is_bad==False and isBadVersion(mid+1)==True:
                return mid
            
            if mid_is_bad==True:
                high = mid -1
            else:
                low = mid+1
        return -1

n = 5
bad = 4

s = Solution()
print(s.firstBadVersion(n))