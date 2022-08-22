from collections import defaultdict

class Solution:
    def countSubIslands(self, grid1, grid2) -> int:
        m, n = len(grid1), len(grid1[0])

        def union(uf, x, y):
            uf[find(uf, x)] = find(uf, y)
            
        def find(uf, x):
			# the root of all 0s is (-1, -1)
            if x == (-1, -1):
                return x
            if uf[x] != x:
                uf[x] = find(uf, uf[x])
            return uf[x]
        
		# connect all adjacent 1s for a given grid
        def process_grid(g):
            uf = {
                (r, c): (r, c) if g[r][c] else (-1, -1)
                for r in range(m)
                for c in range(n)
            }
            
            for r in range(m):
                for c in range(n):
                    if g[r][c]:
                        for nr, nc in [(r+1, c), (r, c+1)]:
                            if 0 <= nr < m and 0 <= nc < n and g[nr][nc]:
                                union(uf, (r, c), (nr, nc))
                                
            return uf
        
		# group all land that belongs to the same island
        uf1, uf2 = process_grid(grid1), process_grid(grid2)
        islands2 = defaultdict(set)
        for r in range(m):
            for c in range(n):
                if grid2[r][c]:
                    root = find(uf2, (r, c))
                    islands2[root].add((r, c))
					
		# find sub island
        res = 0
        for cells in islands2.values():
			# for all cell of a island in grid2, 
			# if the corresponding cells in grid1 are also a land and belong to the same island, 
			# we found an island
            islands1 = set(find(uf1, (r, c)) for r, c in cells)
			
			# a water cell is found in grid1
            if (-1, -1) in islands1:
                continue
            # all cells belong to the same island
            if len(islands1) == 1:
                res += 1
        return res

# grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

# s = Solution()
# print(s.countSubIslands(grid1, grid2))

grid1 = [[1,1,0,1,0,1,1,1],[0,1,1,1,1,0,1,1],[1,1,1,1,0,1,0,1],[1,1,1,0,1,1,1,1],[1,1,1,1,0,1,1,0],[1,1,1,1,0,1,0,0],[1,0,1,1,1,1,0,0],[1,0,0,1,1,1,1,1]]
grid2 = [[1,1,1,1,0,0,0,0],[0,1,1,1,0,0,1,1],[1,1,1,1,0,1,1,1],[1,1,0,1,1,1,1,0],[1,0,0,1,0,1,1,1],[1,1,0,1,1,1,1,0],[1,0,1,0,1,1,1,1],[1,1,1,1,1,0,1,1]]

s = Solution()
print(s.countSubIslands(grid1, grid2))      
      
            
        