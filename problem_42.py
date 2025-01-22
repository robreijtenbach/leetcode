#!/usr/bin/python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_height = max(height)

        def find_bins(height, h):
            start = -1
            end = -1
            res = 0
            for i in range(len(height)):
                v = height[i]
                if v >= h:
                    if start == -1:
                        start = i
                    end = i
                if height[i] < h:
                    res+=1
            return res-(start-1)-(len(height)-end)

        res = 0
        for h in range(max_height+1):
            res += find_bins(height, h)
        return res


            


s = Solution()


height = [4,2,0,3,2,5]
print(s.trap(height))

height = [2,0,2]
print(s.trap(height))

