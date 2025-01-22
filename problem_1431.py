class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        target = max(candies)-extraCandies

        ret = []

        for kid in candies:
            if kid >= target:
                ret.append(True)
            else:
                ret.append(False)
        
        return ret

        
