class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        while nums.count(0):
            nums.remove(0)
            zeros += 1

        nums += [0]*zeros    
        