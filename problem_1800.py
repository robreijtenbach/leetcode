class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = nums[0]

        cursum = nums[0]
        prev = nums[0]

        for i in range(1,len(nums)):
            if nums[i] <= prev:
                cursum = nums[i]
            else:
                cursum += nums[i]
            
            best = max(best, cursum)    

            prev = nums[i]

        return best


import unittest
class Test(unittest.TestCase):
    def test1(self):
        input = [10,20,30,5,10,50]
        out = 65

        self.assertEqual(Solution().maxAscendingSum(input), out)

    def test2(self):
        input = [10,20,30,40,50]
        out = 150

        self.assertEqual(Solution().maxAscendingSum(input), out)

    def test3(self):
        input = [12,17,15,13,10,11,12]
        out = 33
        
        self.assertEqual(Solution().maxAscendingSum(input), out)


    def test4(self):
        input = [100,10,1]
        out = 100
        
        self.assertEqual(Solution().maxAscendingSum(input), out)



unittest.main()