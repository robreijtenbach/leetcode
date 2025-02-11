class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        
        i = s.find(part)

        while i != -1:
            s = s[:i] + s[i+len(part):]
                    
            i = s.find(part)

        return s
        


import unittest
class Test(unittest.TestCase):
    def test1(self):
        s = "daabcbaabcbc" 
        part = "abc"

        output = "dab"
        self.assertEqual(Solution().removeOccurrences(s,part),output)
    
    def test2(self):
        s = "axxxxyyyyb" 
        part = "xy"

        output = "ab"
        self.assertEqual(Solution().removeOccurrences(s,part),output)

unittest.main()