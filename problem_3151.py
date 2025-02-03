class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 2:
            return True
        
        for i in range(len(nums)-1):
            n1,n2 = nums[i]%2, nums[i+1]%2

            if (n1 and n2) or (not n1 and not n2):
                return False
        return True
        