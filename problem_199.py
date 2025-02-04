# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.rsv = []
        self.maxlevel = 0
        
        def dfs(node, level):
            if not node:
                return
            if level >= self.maxlevel:
                self.rsv.append(node.val)
                self.maxlevel+=1
            
            dfs(node.right, level+1)
            dfs(node.left, level+1)
            
        dfs(root,0)

        return self.rsv