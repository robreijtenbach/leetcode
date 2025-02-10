class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ret = []

        i = 0
        while i < n:
            if s[i].isdigit():
                ret.pop()
            else:
                ret.append(s[i])
            i+=1

        return "".join(ret)