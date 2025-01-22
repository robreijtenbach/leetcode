class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums.count(0) <= k:
            return len(nums)

        best = 0
        i=0
        j=0
        while i < len(nums):
            j = i + best
            while j <= len(nums):
                print(nums[i:j])
                if nums[i:j].count(0) <= k:
                    best = j-i
                else:
                    break
                j+=1
            i+=1
        return best
        