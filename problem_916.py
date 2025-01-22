#!/usr/bin/python3

class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        universals = []
        maxCounts = {}
        for word in words2:
            for ch in list(set(word)):
                charCount = word.count(ch)
                if charCount > maxCounts.get(ch, 0):
                    maxCounts[ch] = charCount

        for word in words1:
            for ch,occ in maxCounts.items():
                if word.count(ch) < occ:
                    break
            else:
                universals.append(word)
        return universals


sol = Solution()


w1 = ["amazon","apple","facebook","google","leetcode"]
w2 = ["e","o"]

print(sol.wordSubsets(w1,w2))
