# 9-12-2020
# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return None
        def helper(value, node):
            if not node:
                return True
            if node.val is not value:
                return False
            return helper(value, node.left) and helper(value, node.right)
        return helper(root.val, root.left) and helper(root.val, root.right)
