class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)

        palindromes = []

        if n == 0 or n == 1:
            return s
        
        if n == 2:
            ret = s[0]
            if s[1] == ret:
                ret+=s[1]
            return ret


        #find palindrome middles

        for i in range(n-1):
            if s[i] == s[i+1]:
                palindromes.append((i,i+1))
            if i < n-2 and s[i] == s[i+2]:
                palindromes.append((i,i+2))
        
        print(palindromes)


        for i in range(len(palindromes)):
            l,r = palindromes[i]
            
            while l > 0 and r < n-1 and s[l-1] == s[r+1]:
                l-=1
                r+=1
            
            palindromes[i] = (l,r)
        print(palindromes)
        
        if not palindromes:
            return s[0]

        ret = max(palindromes, key=lambda x: x[1]-x[0])

        return s[ret[0]:ret[1]+1]


import unittest
class Test(unittest.TestCase):
    def test1(self):
        input = "babad"
        output = ["bab", "aba"]

        self.assertIn(Solution().longestPalindrome(input), output)
    
    def test2(self):
        input = "cbbd"
        output = "bb"

        self.assertEqual(Solution().longestPalindrome(input), output)

    def test3(self):
        input = "abb"
        output = "bb"
        
        self.assertEqual(Solution().longestPalindrome(input), output)
    
    def test4(self):
        input = "aaaa"
        output = "aaaa"
        
        self.assertEqual(Solution().longestPalindrome(input), output)


unittest.main()