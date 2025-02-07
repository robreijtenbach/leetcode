from collections import defaultdict
class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        ret = []

        lut = dict()

        cols = defaultdict(set)

        for ball, color in queries:
            if ball in lut:
                old_col = lut[ball]
                cols[old_col].remove(ball)
                if not cols[old_col]:
                    cols.pop(old_col)
                lut[ball] = color
                cols[color].add(ball)
            else:
                lut[ball] = color
                cols[color].add(ball)
            
            ret.append(len(cols))
        return ret

import unittest
class Test(unittest.TestCase):
    def test1(self):
        limit = 4
        queries = [[1,4],[2,5],[1,3],[3,4]]

        output = [1,2,2,3]

        self.assertEqual(Solution().queryResults(limit, queries), output)
    
    def test2(self):
        limit = 4
        queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

        output = [1,2,2,3,4]

        self.assertEqual(Solution().queryResults(limit, queries), output)

unittest.main()