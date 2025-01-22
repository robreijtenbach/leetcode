#!/usr/bin/python

class Solution(object):
    def relocateMarbles(self, nums, moveFrom, moveTo):
        """
        :type nums: List[int]
        :type moveFrom: List[int]
        :type moveTo: List[int]
        :rtype: List[int]
        """
        nums = list(set(nums))

        moves = zip(moveFrom, moveTo)
        
        occupied = {}
        for num in nums:
            occupied[num] = True

        for fr, to in moves:
            occupied[fr] = False
            occupied[to] = True

        return sorted([x for x in list(occupied.keys()) if occupied[x] == True])



sol = Solution()

nums = [1,6,7,8]
moveFrom = [1,7,2]
moveTo = [2,9,5]

print(sol.relocateMarbles(nums, moveFrom, moveTo))
