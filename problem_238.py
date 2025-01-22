class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if nums.count(0) > 1:
            return [0] * (len(nums))
        
        zeroPos = -1
        if nums.count(0) == 1:
            zeroPos = nums.index(0)

            nums.remove(0)
        prod = 1
        for num in nums:
            prod *= num
        print(prod)

        if zeroPos != -1:
            ret = [0] * (1+len(nums))
            ret[zeroPos] = prod
            return ret
        
        
        return [prod//num for num in nums]
        
