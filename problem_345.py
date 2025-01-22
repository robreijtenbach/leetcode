class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")

        sVow = []

        s = list(s)

        for i in range(len(s)):
            if s[i] in vowels:
                sVow.append(s[i])
                s[i] = '_'
        
        for i in range(len(s)):
            if s[i] == '_':
                s[i] = sVow.pop()
            if sVow == []:
                return "".join(s)
