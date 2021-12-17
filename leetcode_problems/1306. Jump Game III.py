# from collections import defaultdict, deque
# class Solution:
#     def canReach(self, arr: list, start: int) -> bool:
#         g = defaultdict(list)
#         visited = set()
#         q = deque( arr[start])
#         for i in range(len(arr)):
#             if 0<=i+arr[i]<len(arr):
#                 g[arr[i]].append(arr[i+arr[i]])
#             if 0<=i-arr[i]<len(arr):
#                 g[arr[i]].append(arr[i-arr[i]])
#         while q:
#             node = q.pop()
#             if node == 0:
#                 return True
#             if node not in visited:
#                 visited.add(node)
#                 for v in g[node]:
#                     q.append(v)
#         return False

# arr = [4,2,3,0,3,1,2]
# start = 5     
# s = Solution()
# print(s.canReach(arr, start ))    

print('ok')