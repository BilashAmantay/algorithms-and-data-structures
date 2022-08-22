numCourses = 4
prerequisites = [[1, 2], [1, 0], [2, 0], [0, 3]]

queries = [[1,0],[1,2],[1,3]]

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites, queries):
        res = []

        adj = [[False] * numCourses for _ in range(numCourses)]
        
        for u, v in prerequisites:
            print(u,v)
            adj[u][v] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    adj[i][j] = adj[i][j] or (adj[i][k] and adj[k][j])
        
        for u,v in queries:
            res.append(adj[u][v])
        return res

        

s = Solution()
r = s.checkIfPrerequisite(numCourses, prerequisites, queries)
print(r)

## test 2
numCourses = 4
prerequisites = [[1, 2], [1, 0], [0, 3]]

queries = [[1,0],[1,2],[1,3],[2,0],[2,3]]
r = s.checkIfPrerequisite(numCourses, prerequisites, queries)
print(r)

# test 3
prerequisites = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]]

r = s.checkIfPrerequisite(numCourses, prerequisites, queries)
print(r)
    
        
        
        
            
        
            