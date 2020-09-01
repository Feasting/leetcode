# 8-31-2020
# https://leetcode.com/problems/reorder-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        ordered = []
        def inOrderTraversal(node: TreeNode):
            if node == None:
                return None
            
            inOrderTraversal(node.left)
            ordered.append(node.val)
            inOrderTraversal(node.right)
        
        inOrderTraversal(root)
        
        return ordered[k - 1]
