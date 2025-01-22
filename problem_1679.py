class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lut = dict()

        ret = 0
        for num in nums:
            if num in lut and lut[num] > 0:
                lut[num] -= 1
                ret +=1
            else:
                lut[k-num] = 1+lut.get(k-num, 0)

        return ret

        