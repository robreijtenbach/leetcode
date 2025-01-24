class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        lut = dict()

        for s in strs:
            sorts = "".join(sorted(s))
            if sorts in lut:
                lut[sorts].append(s)
            else:
                lut[sorts] = [s]
        
        return list(lut.values())



