import unittest

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        safeSet = set()

        changed = True
        while changed:
            changed = False
            for i, node in enumerate(graph):
                if set(node) <= safeSet:
                    safeSet.add(i)
                    node.append(-1) # cant be added to safeset again
                    changed = True
        
        return sorted(safeSet)

class Test(unittest.TestCase):
    def test1(self):
        case = [[1,2],[2,3],[5],[0],[5],[],[]]
        
        self.assertEqual(Solution().eventualSafeNodes(case), [2,4,5,6])

    def test2(self):
        case = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
        
        self.assertEqual(Solution().eventualSafeNodes(case), [4])

unittest.main()