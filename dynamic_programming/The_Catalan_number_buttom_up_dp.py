def catalan_memo(n, memo):

    if n == 0:          # base case; C(0) = 1
        return 1
    elif n in memo:       # if n already evaluated, return from dp
        return memo[n]
    sum = 0
    # iterate from 1...n to evaluate: C(0)*C(n-1) + C(1)*C(n-2) ... + C(n-1)*C(0)
    for i in range(n):  
        sum += (catalan_memo(i, memo) * catalan_memo(n-1-i, memo))  # C(i)*C(n-1-i)
        memo[n] = sum         # store result in dp
    return memo[n]

"""
If you plug a bigger number (say 1000) into above solution 
it will not evaluate due to RecursionError. 
Also, we have seen that recursion can be expensive as well, 
so let’s look at a bottom-up solution to this problem.
"""


def catalan(n):
  memo = {}
  return catalan_memo(n, memo)

print(catalan(400))

def catalan(n):
    table = [None] * (n+1)  # tabulating 
    table[0] = 1            # handling the base case
    for i in range(1,n+1):  # iterating to fill up the tabulation table
        table[i] = 0          # initializing the i-th value to 0
        # iterate from 0 to i; according to formula of catalan i.e. 
        # C0*Ci + C1*Ci-1 + ... Ci*C0
        for j in range(i):    
            table[i] += (table[j] * table[i-j-1]) # C(j) * C(i-j-1)
    return table[n]         

print(catalan(6))