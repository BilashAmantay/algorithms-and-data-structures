
from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: list, src: int, dst: int, k: int) -> int:
        
        edges = defaultdict(list)
        for u,v,w in flights:
            edges[u].append((v,w))
        cheapest = float('inf')
        visited = set()
        minHeap = [(float('inf'),src)]
        stops=0

        while minHeap:
            if stops>k:
                return cheapest
            cost, dist = heapq.heappop(minHeap)

            if dist in visited:
                continue
            visited.add(dist)
            cheapest = min(cheapest, cost)

            for dist2,cost2 in edges[dist]:
                if dist2 not in visited:
                    heapq.heappush(minHeap, (cost2 + cost2, dist2))
                    stops+=1
        return cheapest if len(visited) == n else -1

n = 3; flights = [[0,1,100],[1,2,100],[0,2,500]]; src = 0; dst = 2; k = 1

s = Solution()
print(s.findCheapestPrice(n,flights, src, dst, k))

n = 3; flights = [[0,1,100],[1,2,100],[0,2,500]]; src = 0; dst = 2; k = 0
s = Solution()
print(s.findCheapestPrice(n,flights, src, dst, k))


        
        