#!/usr/bin/python3

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occ = {}

        for num in arr:
            if num in occ.keys():
                occ[num] += 1
            else:
                occ[num] = 0
        return len(occ.values()) == len(set(occ.values()))


s = Solution()

arr = [1,2,2,1,1,3]
print(s.uniqueOccurrences(arr))

arr = [1,2]
print(s.uniqueOccurrences(arr))
