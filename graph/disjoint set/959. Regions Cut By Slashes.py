"""
https://leetcode.com/problems/regions-cut-by-slashes/
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

Example 1:


Input: grid = [" /","/ "]
Output: 2
Example 2:


Input: grid = [" /","  "]
Output: 1
Example 3:


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
"""

class Solution:
    def regionsBySlashes(self, grid ) -> int:
        f = {}
        count = len(grid) * len(grid[0]) * 4
        print('count ',  count)

        def find(x):
            f.setdefault(x,x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x] 

        def union(x, y):
            nonlocal count
            if find(x) != find(y):
                count = count - 1 

            f[find(x)] = find(y)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0: union((i-1,j,2), (i,j,0))
                if j > 0: union((i,j-1,1), (i,j,3))

                if grid[i][j] != "/": #// if it is "\\" or empty, apply common operations
                    union((i,j,0), (i,j,1))
                    union((i,j,2), (i,j,3))
                
                if grid[i][j] != "\\":  #if it is "/" or empty, apply common operations.
                    union((i,j,1), (i,j,2))
                    union((i,j,0), (i,j,3))
                
        return len(set(map(find,f))), count 

s = Solution()

grid = [" /","/ "]
print(s.regionsBySlashes(grid))


## solution 2, a little bit optimized
from collections import defaultdict 
def one():
    return 1
class Solution:
    def regionsBySlashes(self, grid) -> int:
        f = {}
        width = len(grid)
        hight = len(grid[0])
        self.count = width * hight * 4
        
        
        self.rank = defaultdict(one)
        
        
        def find(x):
            f.setdefault(x,x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                self.count -= 1
                if self.rank[rootX] > self.rank[rootY]:
                    f[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    f[rootX] = rootY
                else:
                    f[rootY] = rootX
                    self.rank[rootX] += self.rank[rootY]
                    
        
        for i in range(width):
            for j in range(hight):
                if i > 0: union((i-1,j,2), (i,j,0))
                if j > 0: union((i,j-1,1), (i,j,3))
                    
                if grid[i][j] != "/": # means \ or empty
                    union( (i,j,0), (i,j,1))
                    union( (i,j,2), (i,j,3))
                
                if grid[i][j] != "\\": # means / or empty
                    union( (i,j,0), (i,j,3))
                    union( (i,j,1), (i,j,2))
                    
        # return len(set(map(find,f)))
        return self.count


s = Solution()

grid = [" /","/ "]
print(s.regionsBySlashes(grid))