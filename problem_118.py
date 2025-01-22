#!/usr/bin/python3

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        l = [[1], [1,1]]


        for i in range(2,numRows):
            prev = l[-1]
            curr = [1]
            print(prev)
            for j in range(1,1+len(prev)//2):
                curr.append(prev[j]+prev[j-1])

            if len(prev) % 2 == 1:
                curr += curr[::-1]
            else:
                curr += curr[::-1][1::]
            l.append(curr)
        return l



s = Solution()

nr = 1
#print(nr, s.generate(nr))

nr = 2
#print(nr, s.generate(nr))

nr = 5
print(nr, s.generate(nr))
