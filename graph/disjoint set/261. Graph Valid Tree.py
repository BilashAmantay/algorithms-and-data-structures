"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
"""

List = list

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, A, B):
        rootA = self.find(A)
        rootB = self.find(B)
        
        if rootA == rootB:
            return False
        
        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += self.rank[rootB]
        
        return True
        
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n -1 : return False
        
        uf = UnionFind(n)
        
        for A,B in edges:
            if not uf.union(A,B):
                return False
        
        return True
        
# n = 6
# edges = [[5,0], [0,4], [2,1], [3,1], [2,3]]

# S = Solution()
# print(S.validTree(n, edges))

n = 5; edges = [[0,1],[0,2],[0,3],[1,4]] # True

n = 5; edges = [[0,1],[1,2],[2,3],[1,3],[1,4]] # False

S = Solution()
print(S.validTree(n, edges))