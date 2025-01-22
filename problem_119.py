#!/usr/bin/python3

### INEFFICIENT ###
# APPROACH BASED ON 118, COULD BE MADE BETTER

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rowIndex += 1
        if rowIndex == 1:
            return [1]
        l = [[1], [1,1]]


        for i in range(2,rowIndex):
            prev = l[-1]
            curr = [1]
            for j in range(1,1+len(prev)//2):
                curr.append(prev[j]+prev[j-1])

            if len(prev) % 2 == 1:
                curr += curr[::-1]
            else:
                curr += curr[::-1][1::]
            l.append(curr)
        return l[-1]



s = Solution()

nr = 1
#print(nr, s.generate(nr))

nr = 2
#print(nr, s.generate(nr))

nr = 5
print(nr, s.getRow(nr))
