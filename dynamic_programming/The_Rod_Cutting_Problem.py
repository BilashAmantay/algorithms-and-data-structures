"""
You are given a rod of length n meters. You want to sell the rod and earn revenue. You can cut the rod into multiple smaller pieces of sizes 11 through nn and sell them too. You are given the price of each size of the rod. Since you want to earn more, you will have to look for the optimal cuts on the rod that would earn the most revenue.

Input#
Your function would get as input n, the original length of the rod. You can cut the rod into different pieces of sizes 1,2,1,2, up to nn. The price for each of these pieces is given in a list of size nn called prices.

n = 4
prices = [2,3,7,8]
Output#
Your function should return the optimal amount of revenue you can get out of the rod provided n and prices.

n = 4
prices = [2,3,7,8]
rodCutting(n, prices) = 9
"""

### Solution 1: Simple recursion
"""
Time complexity#
Can you think of the number of combinations of cuts for a rod of length n? It is 2^{n-1}2
​n−1
​​ ! For a rod of length nn, at each position, we have two choices. Either we can make a cut, or we can leave it as it is. All combinations are bounded by O(2^n) as is the time complexity of this solution.
"""
def rodCutting(n, prices):
    if n<0:
        return 0
    max_val = 0
    for i in range(1,n+1):
        
        max_val = max(max_val, prices[i-1] + rodCutting(n - i, prices))
    return max_val

print(rodCutting(3, [3,7,8]))


"""
Solution 2: Top-down dynamic programming

Time and space complexity#
Each problem depends on the smaller subproblems; to evaluate rodCutting(n), 
we need the answer to rodCutting(n-1), rodCutting(n-2), and so on until rodCutting(1). 
Thus, the time complexity would be O(n^2). 
Moreover, we can only have n unique subproblems, making the space complexity of this algorithm O(n).


"""

def rodCutting_(n, prices, memo):
    if n<0:
        return 0
    if n in memo:
        return memo[n]
    max_val = 0
    for i in range(1,n+1):
        max_val = max(max_val, prices[i-1] + rodCutting_(n - i, prices, memo))
    memo[n] = max_val
    
    return memo[n]

def rodCutting(n, prices):
    memo = {}
    return rodCutting_(n, prices, memo)

print(rodCutting(3, [3,7,8]))

"""
Solution 3: Bottom-up dynamic programming#
"""
def rodCutting(n, prices):
      # Create a dp array the size of (n+1)
  dp = [0 for _ in range(n + 1)]  
  # starting from rod of length 1, find optimal answer to all subproblems
  for i in range(1, n + 1):       
    max_val = 0
    # for a rod of length i, we can find what cuts give max answer since we have answer to all smaller cuts
    for j in range(i):            
      max_val = max(max_val, prices[j]+dp[i-j-1])
    dp[i] = max_val
  # return answer to n length rod
  return dp[n]                    

stressTesting = True

n = 4
prices = [2,3,7,8]
print(rodCutting(n, prices))
