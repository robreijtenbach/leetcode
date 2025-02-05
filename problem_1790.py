class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        if len(s2) != n:
            return False

        changeletters = ""
        changes = 0
        for i in range(n):
            if s1[i] != s2[i]:
                print(s1[i], s2[i])
                print(changes)
                if changes == 0:
                    changeletters = s1[i] + s2[i]
                elif changes == 1:
                    if changeletters != s2[i] + s1[i]:
                        return False
                else:
                    return False
                changes += 1
        if changes == 1:
            return False
        return True