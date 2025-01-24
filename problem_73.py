class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zcols = set()

        for i, row in enumerate(matrix):
            zeros = set([j for j in range(n) if row[j] == 0])
            print(zeros)
            if zeros:
                matrix[i] = [0] * n
                zcols |= zeros
        
        for row in matrix:
            for i in zcols:
                row[i] = 0
        
        return matrix


import unittest
class Test(unittest.TestCase):
    def test1(self):
        case = [[1,1,1],[1,0,1],[1,1,1]]
        out = [[1,0,1],[0,0,0],[1,0,1]]
        
        self.assertEqual(Solution().setZeroes(case), out)
    
    def test2(self):
        case = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        out = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

        self.assertEqual(Solution().setZeroes(case), out)


unittest.main()