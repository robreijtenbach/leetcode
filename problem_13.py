#!/usr/bin/python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }

        val = 0
        for i in range(len(s)):
            if i < len(s)-1 and rom[s[i]] < rom[s[i+1]]:
                val -= rom[s[i]]
            else:
                val += rom[s[i]]
        return val
              








sol = Solution()

string = 'LVIII'
print("BLA", string, sol.romanToInt(string), 58)

string = 'MCMXCIV'
print("BLA", string, sol.romanToInt(string), '1994')

string = 'IIC'
print("BLA", string, sol.romanToInt(string))
