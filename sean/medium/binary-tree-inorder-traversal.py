# 9-7-2020
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            result.append(node.val)
            helper(node.right)
            
        helper(root)
            
        return result
