#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self, node, rl):
        if node == None:
            return
        rl.append(node.val)

        self.traverse(node.left, rl)

        self.traverse(node.right, rl)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        retList = []
        self.traverse(root, retList)
        return retList

