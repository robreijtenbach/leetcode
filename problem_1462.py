class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
        # dict for which courses depend on course key
        preqCourses = dict()

        for pre, course in prerequisites:
            if pre in preqCourses:
                preqCourses[pre].add(course)
            else:
                preqCourses[pre] = {course}
        
        changed = True
        while changed:
            changed = False
            for key, value in preqCourses.items():
                for v in list(value):
                    if v not in preqCourses:
                        continue
                    elif (preqCourses[v] | value) != value:
                        preqCourses[key] |= preqCourses[v]
                        changed = True
                    else:
                        continue

        ret = []
        for qPreq, qCourse in queries:
            if qPreq not in preqCourses:
                ret.append(False)
            elif qCourse in preqCourses[qPreq]:
                ret.append(True)
            else:
                ret.append(False)

        return ret
                        
import unittest
class Test(unittest.TestCase):
    def test1(self):
        numCourses = 2
        prerequisites = [[1,0]]
        queries = [[0,1],[1,0]]

        output = [False,True]

        self.assertEqual(Solution().checkIfPrerequisite(numCourses, prerequisites, queries), output)

    def test2(self):
        numCourses = 2
        prerequisites = []
        queries = [[1,0],[0,1]]

        output = [False,False]

        self.assertEqual(Solution().checkIfPrerequisite(numCourses, prerequisites, queries), output)

    def test3(self):
        numCourses = 3
        prerequisites = [[1,2],[1,0],[2,0]]
        queries = [[1,0],[1,2]]

        output = [True,True]

        self.assertEqual(Solution().checkIfPrerequisite(numCourses, prerequisites, queries), output)

unittest.main()