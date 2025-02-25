# Attempt at problem 1524 but has some error I don't want to keep looking for
from math import factorial

class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        num_evens = 1
        num_odds = 0

        for n in arr:
            num_evens += (n+1)%2
            num_odds += n%2
        
        even_combs = 2**num_evens

        n = num_odds
        odd_combs = []
        for k in range(1,n+1,2):
            odd_combs.append(factorial(n)//(factorial(k)*factorial(n-k)))
        
        print(odd_combs)
        
        print(even_combs)
        ret = sum([x * even_combs for x in odd_combs])

        return ret