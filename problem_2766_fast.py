#!/usr/bin/python

class Solution(object):
    def relocateMarbles(self, nums, moveFrom, moveTo):
        """
        :type nums: List[int]
        :type moveFrom: List[int]
        :type moveTo: List[int]
        :rtype: List[int]
        """
        nums = set(nums)

        moves = zip(moveFrom, moveTo)
        
        for fr, to in moves:
            nums.remove(fr)
            nums.add(to)

        return sorted(list(nums))



sol = Solution()

nums = [1,6,7,8]
moveFrom = [1,7,2]
moveTo = [2,9,5]

print(sol.relocateMarbles(nums, moveFrom, moveTo))
