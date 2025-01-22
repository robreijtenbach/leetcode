class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""

        if len(str1) == len(str2):
            return str2

        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str2[len(str1):], str1)

sol = Solution()

s1 = "ABCDEF"
s2 = "ABC"

print(sol.gcdOfStrings(s1,s2))

s1 = "ABCABC"
s2 = "ABC"

print(sol.gcdOfStrings(s1,s2))