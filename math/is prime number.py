from math import ceil, sqrt

from sympy import prevprime
def prime_number_less_than_n(n):
    if n < 2: return []
    isPrime =  [True] * n
    isPrime[0] = isPrime[1] = False

    for i in range(2, ceil(sqrt(n))):
        if isPrime[i] == True:
            for x in range(i*i, n, i):
                isPrime[x] = False
    
    return [i for i in range(n) if isPrime[i]]

print(prime_number_less_than_n(10))











