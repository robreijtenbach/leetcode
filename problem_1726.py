from collections import defaultdict
from math import factorial
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        lut = defaultdict(list)

        for i in range(n):
            for j in range(i+1,n):
                n1, n2= nums[i], nums[j]
                if n1 > n2:
                    continue
                lut[n1*n2].append((n1,n2))
        
        products = []
        for k,v in lut.items():
            if len(v) > 1:
                products.append(v)

        ret = 0
        for p in products:
            addd = 8*((factorial(len(p)))//(2*factorial((len(p)-2))))
            ret += addd

        return ret

import unittest
class Test(unittest.TestCase):
    def test1(self):
        input = [2,3,4,6]
        output = 8

        self.assertEqual(Solution().tupleSameProduct(input), output)

    def test2(self):
        input = [1,2,4,5,10]
        output = 16

        self.assertEqual(Solution().tupleSameProduct(input), output)

    def test3(self):
        input = [2,3,4,6,8,12]
        output = 40

        self.assertEqual(Solution().tupleSameProduct(input), output)

    def test4(self):
        input = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]
        output = 1288

        self.assertEqual(Solution().tupleSameProduct(input), output)

    def test5(self):
        input = [20,10,6,24,15,5,4,30]
        output = 48

        self.assertEqual(Solution().tupleSameProduct(input), output)

unittest.main()