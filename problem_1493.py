class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = nums.count(0)
        if zeros == 0 or zeros == 1:
            return len(nums) - 1

        best = sub_old = sub_new = 0
        for num in nums:
            if num == 1:
                sub_new += 1
                best = max(best, sub_old + sub_new)
            else:
                sub_old = sub_new
                sub_new = 0

        return best