class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        lut = set()
        
        while not n in lut:
            lut.add(n)
            n = sum([int(x)**2 for x in str(n)])
            if n == 1:
                return True
        
        return False





import unittest
class Test(unittest.TestCase):
    def test1(self):
        case = 19
        out = True

        self.assertEqual(Solution().isHappy(case), out)
        
    def test2(self):
        case = 2
        out = False

        self.assertEqual(Solution().isHappy(case), out)

unittest.main()