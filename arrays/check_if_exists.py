## https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/

class Solution:
    def checkIfExist(self, arr: list) -> bool:
        seen = set()
        for i in arr:
          # if 2 * i in seen or i % 2 == 0 and i // 2 in seen:
            if 2 * i in seen or i / 2 in seen: # credit to @PeterBohai
                return True
            seen.add(i)
        return False

nums=[0,10,2,5,3]

s = Solution()
print(s.checkIfExist(nums))
