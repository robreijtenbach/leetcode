class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        
        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr+=1
        best = curr

        for i in range(k, len(s)):
            if best == k:
                return k
            if s[i - k] in vowels:
                curr -= 1
            if s[i] in vowels:
                curr += 1
            best = max(best, curr)
        return best