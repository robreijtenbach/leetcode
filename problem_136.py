#!/usr/bin/python3

class Solution(object):
    def singleNumber(self, nums):
        occ = set()
        for num in nums:
            if num in occ:
                occ.remove(num)
            else:
                occ.add(num)

        return list(occ)[0]

s = Solution()
n = [1,2,2,3,3,4,4]
print(s.singleNumber(n))




n = [1,1,2,2,3,4,4]
print(s.singleNumber(n))

