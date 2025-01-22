class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        zeros = 0
        j = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+=1
            else:
                zeros+=1
            i+=1
        if zeros != 0:
            nums[-zeros:] = [0]*zeros
        