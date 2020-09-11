# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depHelper(node):
            return 0 if node is None else max(depHelper(node.right), depHelper(node.left)) + 1
        return depHelper(root)
        
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
