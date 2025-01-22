#!/usr/bin/python3

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref = ""
        
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs:
                if i > len(s) or s[i] != c:
                    return pref
            else:
                pref += c

        return pref



s = Solution()

strs = ["flower","flow","flight"]
print(s.longestCommonPrefix(strs))


strs = ["dog","racecar","car"]
print(s.longestCommonPrefix(strs))
