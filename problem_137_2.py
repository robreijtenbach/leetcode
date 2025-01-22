#!/usr/bin/python3

class Solution(object):
    def singleNumber(self, nums):
        if len(nums) < 3:
            return nums[0]
        nums.sort()
        
        for i in range(0,len(nums)-3, 3):
            if nums[i] != nums[i+1] and nums[i] != nums[i+2]:
                return nums[i]
        return nums[-1]


s = Solution()
n = [1,2,2,2,3,3,3,4,4,4]
print(s.singleNumber(n))

n = [2,2,3,2]
print(s.singleNumber(n))




