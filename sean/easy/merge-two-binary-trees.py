# 9-10-2020
# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        result = TreeNode()
        result.val += t1.val if t1 else 0
        result.val += t2.val if t2 else 0
        result.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        result.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return result
