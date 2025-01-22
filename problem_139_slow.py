#!/usr/bin/python

class Solution(object):
    # Assumes sorted wordDict and is called recursively
    def helper(self, s, wordDict): 
        if len(s) == 0:
            return True
        for word in wordDict:
            if s.find(word) == 0:
                if self.helper(s[len(word):], wordDict) == True:
                    return True
        return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not set(s).issubset(set("".join(wordDict))):
            return False
        wordDict.sort(key = len, reverse = True)

        return self.helper(s, wordDict)



        

sol = Solution()

s = "leetcode" 
wordDict = ["leet","code"]
print(sol.wordBreak(s, wordDict))


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
print(sol.wordBreak(s, wordDict))

