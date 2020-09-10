# 9-10-2020
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original is target:
            return cloned
        result = self.getTargetCopy(original.left, cloned.left, target)
        if not result:
            result = self.getTargetCopy(original.right, cloned.right, target)
        return result
