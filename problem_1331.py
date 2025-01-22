class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        lut = dict()

        j = 1
        
        for num in sorted(set(arr)):
            if not num in lut:
                lut[num] = j
                j += 1

        for i in range(len(arr)):
            arr[i] = lut[arr[i]]
        
        return arr