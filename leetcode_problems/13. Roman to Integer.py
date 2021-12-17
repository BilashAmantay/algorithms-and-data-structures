class Solution:
    def romanToInt(self, s: str) -> int:
        ss=0
        dic1= {"I":1,
              "V":5,
              "X":10,
              "L":50,
             "C":100,
             "D":500,
             "M":1000
             }
        dic2 = {"IV":4,"IX":9,"XL":40, "XC":90, "CD":400,"CM":900}


        for k,v in dic2.items():
            if len(s)>0 and s.find(k)>=0:
                s = s.replace(k,"")
                ss+=v
        
        if len(s)>0:
            for c in s:
                s = s.replace(c, "")
                ss+=dic1[c]
        return ss

s = "MCMXCIV"

# sl = Solution()
# print(sl.romanToInt(s))

class Solution:
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
        
rs = Solution()
print(rs.romanToInt(s))
        