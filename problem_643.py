class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        cumsum = 0
        for num in nums[0:k]:
            cumsum+=num
        best = cumsum

        for i in range(1,len(nums)-k+1):
            cumsum -= nums[i-1]
            cumsum += nums[i+k-1]
            
            best = max(best, cumsum)
        
        return float(best)/k