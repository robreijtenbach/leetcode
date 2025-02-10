class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ret = []

        for c in s:
            if c.isdigit():
                ret.pop()
            else:
                ret.append(c)
        
        return "".join(ret)