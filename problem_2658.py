
class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        m = len(grid)
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        seen = set()

        lut = dict()

        def dfs(i,j, start):
            if not grid[i][j] or (i,j) in seen:
                return
            seen.add((i,j))
            lut[start].append((i,j))
            for d in directions:
                target_i = i+d[0]
                target_j = j+d[1]
                if 0 <= target_i < m and 0 <= target_j < n and not (target_i, target_j) in seen:
                    dfs(target_i,target_j, start)
        
        for i in range(m):
            for j in range(n):
                lut[(i,j)] = []
                dfs(i,j,(i,j))
        
        best = 0
        for key, value in lut.items():
            if not value:
                continue
            else:
                ssum = 0
                for cell in value:
                    ssum += grid[cell[0]][cell[1]]

                best = max(ssum,best)

        return best    


import unittest
class Test(unittest.TestCase):
    def test1(self):
        grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
        output = 7

        self.assertEqual(Solution().findMaxFish(grid), output)

    def test2(self):
        grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
        output = 1

        self.assertEqual(Solution().findMaxFish(grid), output)

unittest.main()