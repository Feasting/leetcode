# 9-11-2020
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.result = 0
        def helper(node):
            if not node:
                return
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        self.result += node.left.left.val
                    if node.left.right:
                        self.result += node.left.right.val
                if node.right:
                    if node.right.left:
                        self.result += node.right.left.val
                    if node.right.right:
                        self.result += node.right.right.val
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return self.result
