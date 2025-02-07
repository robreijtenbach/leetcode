class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        ret = ""

        palindromes = []

        #find palindrome middles

        for i in range(n-2):
            if s[i] == s[i+1]:
                palindromes.append((i,i+1))
            elif s[i] == s[i+2]:
                palindromes.append((i,i+2))
        
        ## TODO grow palindromes and return longest

        return ret




import unittest
class Test(unittest.TestCase):
    def test1(self):
        input = "babad"
        output = ["bab", "aba"]

        self.assertIn(Solution().longestPalindrome(input), output)
    
    def test1(self):
        input = "cbbd"
        output = "bb"

        self.assertEqual(Solution().longestPalindrome(input), output)

unittest.main()