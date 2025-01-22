#!/usr/bin/python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        valDict = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if nums[i] in valDict:
                return [i, valDict[nums[i]]]
            valDict[val] = i
                
            print(valDict)

s = Solution()

nums = [2,7,11,15] 
target = 9
print(s.twoSum(nums, target))

nums = [3,2,4] 
target = 6
print(s.twoSum(nums, target))

nums = [3,3] 
target = 6
print(s.twoSum(nums, target))
