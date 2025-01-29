class Solution(object):
    def findRedundantConnection(self, edges):
        parent = {} 

        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node]) 
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return False  
            parent[root2] = root1
            return True

        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):  
                return [u, v]

        return []

import unittest
class Test(unittest.TestCase):
    def test1(self):
        edges = [[1,2],[1,3],[2,3]]
        output = [2,3]

        self.assertEqual(Solution().findRedundantConnection(edges), output)

    def test2(self):
        edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        output = [1,4]

        self.assertEqual(Solution().findRedundantConnection(edges), output)
        
    def test3(self):
        edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
        output = [2,5]

        self.assertEqual(Solution().findRedundantConnection(edges), output)


unittest.main()
