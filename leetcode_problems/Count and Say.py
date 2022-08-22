"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/
"""
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s

# s = Solution()
# print(s.countAndSay(4))

## recursion method. 32ms
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        num = self.countAndSay(n-1)
        c_digit = num[0]
        c_count = 0
        ans = ''
        for digit in num:
            if c_digit == digit:
                c_count += 1
            else:
                ans += str(c_count) + c_digit
                c_digit = digit
                c_count = 1
        ans += str(c_count) + c_digit
        return ans

s = Solution()
print(s.countAndSay(4))