class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  
        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                result = (result + odd_count) % MOD
                even_count += 1
            else:
                result = (result + even_count) % MOD
                odd_count += 1

        return result