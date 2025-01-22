class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {
            ']':'[',
            ')':'(',
            '}':'{'
               }

        stack = []
        for c in s:
            if c in dic:
                if stack == [] or stack.pop() != dic[c]:
                    return False
            else:
                stack.append(c)
                
        if stack != []:
            return False
        return True
        
