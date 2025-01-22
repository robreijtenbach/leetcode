class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")

        s = list(s)

        l, r = 0, len(s)-1
        lock,rock = False, False

        while l<r:
            if s[l] in vowels:
                lock = True
            if s[r] in vowels:
                rock = True
            
            if lock and rock:
                s[l], s[r] = s[r], s[l]
                lock, rock = False, False
            
            l += 0 if lock else 1

            r -= 0 if rock else 1
        
        return "".join(s)
