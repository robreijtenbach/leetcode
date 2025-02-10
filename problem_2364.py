from collections import defaultdict
class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lut = defaultdict(int)

        total = n*(n-1)/2

        i = 0
        while i < n:
            curr = nums[i]-i

            total -= lut[curr]

            lut[curr]+=1

            i+=1        

        return total

import unittest
class Test(unittest.TestCase):
    def test1(self):
        input = [4,1,3,3]
        output = 5

        self.assertEqual(Solution().countBadPairs(input), output)
    def test2(self):
        input = [1,2,3,4,5]
        output = 0

        self.assertEqual(Solution().countBadPairs(input), output)

unittest.main()