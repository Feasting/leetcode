# 9-16-2020
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        def helper(bits, node):
            n = (bits << 1) | node.val
            if not node.left and not node.right:
                return n
            if not node.left:
                return helper(n, node.right)
            if not node.right:
                return helper(n, node.left)
            return helper(n, node.left) + helper(n, node.right)
        return helper(0, root)
