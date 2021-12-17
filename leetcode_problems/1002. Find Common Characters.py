'''
https://leetcode.com/problems/find-common-characters/
'''


from collections import Counter
class Solution:
    def commonChars(self, words):
        counter = Counter(words[0])
        for word in words:
            counter &= Counter(word)
        return list(counter.elements())
        

words = ["bella","label","roller"]
s = Solution()
print(s.commonChars(words))
        
        