#!/usr/bin/python

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        if not set(s).issubset("".join(wordDict)):
            return False

        breakable = [False] * (len(s)+1)
        breakable[0] = True

        for i in range(len(breakable)):
            for w in wordDict:
                start = i-len(w)
                if start >= 0 and len(w) == i - start and breakable[start] == True and w == s[start:i]:
                    breakable[i] = True

        return breakable[-1]


        

sol = Solution()

s = "leetcode" 
wordDict = ["leet","code"]
print(sol.wordBreak(s, wordDict))


s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(sol.wordBreak(s, wordDict))

