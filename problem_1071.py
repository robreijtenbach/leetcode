class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        def divides(s1, s2):
            if len(s1) % len(s2) != 0:
                return False

            for i in range(0,len(s1),len(s2)):
                if s1[i:i+len(s2)] != s2:
                    return False
            return True

        ret = [""]
        minLen = min(len(str1),len(str2))
        div = ""
        for i in range(minLen):
            if str1[i] == str2[i]:
                div += str1[i]
                if divides(str1,div) and divides(str2,div):
                    ret.append(div)
            else:
                break
        

        return ret[-1]
        


sol = Solution()

s1 = "ABCDEF"
s2 = "ABC"

print(sol.gcdOfStrings(s1,s2))