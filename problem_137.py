#!/usr/bin/python3

class Solution(object):
    def singleNumber(self, nums):
        occ = {}
        for num in nums:
            occ[num] = 1 + occ.get(num, 0)
            if occ[num] == 3:
                del occ[num]
        return list(occ.keys())[0]


s = Solution()
n = [1,2,2,2,3,3,3,4,4,4]
print(s.singleNumber(n))

n = [2,2,3,2]
print(s.singleNumber(n))




