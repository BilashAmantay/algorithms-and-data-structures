## https://leetcode.com/problems/3sum/

nums = [-1,0,1,2,-1,-4]

class Solution:
    def threeSum(self, nums: list):
        l2dic = {}
        l1dic={}
        res = []


        for i in range(len(nums)):
            l1complement = 0 - nums[i]

            l1dic[nums[i]]=i

            for j in range(i,len(nums)):
                l2complement = l1complement - nums[j]

                if l2complement in l2dic and i!=j and i!=l2dic[l2complement] and j!=l2dic[l2complement]:
                    r =[i,j,l2dic[l2complement]]
                    print('r=',r)
                    if r not in res:
                        res.append(r)
                
                l2dic[nums[j]] = j
        return res

nums = [-1,0,1,2,-1,-4]
s  = Solution()
res = s.threeSum(nums)
for r in res:
    # print('-----------------')
    r.sort()
    [i,j,k] = r
    print(i,j,k)
    # print(nums[i],nums[j],nums[k])
    # print(sum([nums[i],nums[j],nums[k]]))