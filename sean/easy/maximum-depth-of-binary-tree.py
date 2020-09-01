# 8-31-2020
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def helper(depth, node):
            if node == None:
                return depth
            return max(helper(depth + 1, node.left), helper(depth + 1, node.right))
        
        return helper(0, root)
