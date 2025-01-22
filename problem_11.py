class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        best = 0

        while left < right:
            area = (right-left)*min(height[left], height[right])
            if area > best:
                best = area
            if height[left] >= height[right]:
                right -= 1
            else:
                left +=1
        return best

        