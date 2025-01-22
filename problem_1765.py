from collections import deque

class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(isWater), len(isWater[0])
        res = [[-1]*n for _ in range(m)]
        
        q = deque()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for y in range(m):
            for x in range(n):
                if isWater[y][x] == 1:
                    res[y][x] = 0
                    q.append((x,y))
        
        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                cur_x = x + dx
                cur_y = y + dy

                if  not (0 <= cur_x < n) or not (0 <= cur_y < m):
                    continue

                if res[cur_y][cur_x] == -1:
                    res[cur_y][cur_x] = res[y][x] + 1
                    q.append((cur_x,cur_y))

        return res

s = Solution()

inputs = [
    [[0,1],[0,0]],
    [[0,0,1],[1,0,0],[0,0,0]]
]

def pprint(grid):
    for r in grid:
        print(r)

for i in inputs:
    pprint(s.highestPeak(i))