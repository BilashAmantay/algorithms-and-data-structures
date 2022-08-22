"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""

class Solution(object):
        
    def find(self, i):
        if self.parent[i] == -1: return i
        return self.find(self.parent[i])
    
    def union(self,x,y):
        parentX = self.find(x)
        parentY = self.find(y)
        
        if parentX != parentY:
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentY] = parentX
            elif self.rank[parentX] < self.rank[parentY]:
                self.parent[parentX] = parentY
            else:
                self.parent[parentY] = parentX
                self.rank[parentX] += 1
            
            # self.parent[parentX] = parentY
    
    
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        size = len(isConnected)
        self.parent = [-1 for i in range(size)]
        self.rank = [1] * size
                
        for i in range(size):
            for j in range(size):
                if isConnected[i][j] == 1 and i != j:
                    self.union(i,j)
        
        count = 0
        print(self.parent)
        for i in range(size):
            
            if self.parent[i] == -1:
                count += 1
        return count

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,1,0,0],[1,1,0,0],[0,0,1,0],[0,0,0,1]]

# isConnected = [[1,0,0],[0,1,0],[0,0,1]]

isConnected =  [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
                [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
                [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
                [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]


s = Solution()
print(s.findCircleNum(isConnected))
