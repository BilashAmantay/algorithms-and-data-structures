"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
"""

from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph) -1
        
        adjList = defaultdict(list)
        res = []
        
        for i in range(len(graph)):
            adjList[i]=graph[i]
                
        visited = set()
            
        stack = [ (0,[0]) ]
        while stack:
            current, path = stack.pop()
            print('visiting ', current, ' path:', path)
            visited.add(current)

            for nei in adjList[current]:
                # if nei in visited:
                #     print('visited ', nei)
                #     continue
                if nei == n:
                    res.append(path + [nei])
                    # print('found n',nei, path, res)
                else:
                    stack.append( (nei, path + [nei]) )
        return res
    
graph = [[1,2,3],[2],[3],[]] ## expect [[0,1,2,3],[0,2,3],[0,3]] in any order
s = Solution()
print(s.allPathsSourceTarget(graph))   


##### =======>>>>  Backtraking solution <<<< ====== 

from collections import deque 
class Solution:
    def allPathsSourceTarget(self, graph):

        target = len(graph) - 1
        results = []

        def backtrack(currNode, path):
            # if we reach the target, no need to explore further.
            if currNode == target:
                results.append(list(path))
                return
            # explore the neighbor nodes one after another.
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()
        # kick of the backtracking, starting from the source node (0).
        path = deque([0])
        backtrack(0, path)

        return results
graph = [[1,2,3],[2],[3],[]] ## expect [[0,1,2,3],[0,2,3],[0,3]] in any order
s = Solution()
print(s.allPathsSourceTarget(graph))   