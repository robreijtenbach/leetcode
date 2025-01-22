class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zeros = 0
        left = right = 0
        best = 0

        window = 0
        while right < len(nums):
            if nums[right] ==0:
                zeros += 1
            
            while left <= right and zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                window -= 1
                left += 1
                
            window += 1
            best = max(best, window)
            right += 1
    
        return best