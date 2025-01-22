class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ret = ""
        i = 0

        maxLen = max(len(word1),len(word2))

        while i < maxLen:
            if i < len(word1):
                ret += word1[i]
            if i < len(word2):
                ret += word2[i]
            i += 1
        return ret
    
sol = Solution()

word1 ="abc"
word2 ="abc"

print(sol.mergeAlternately(word1, word2))