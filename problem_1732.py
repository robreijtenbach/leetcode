class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = best = 0
        for i in range(len(gain)):
            alt += gain[i]
            best = max(best,alt)
        return best
        