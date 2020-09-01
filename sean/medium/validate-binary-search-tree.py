# 8-31-2020
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(node, high, low):
            if node == None:
                return True
            if node.val <= low or node.val >= high:
                return False
            return helper(node.left, node.val, low) and helper(node.right, high, node.val)
            
        return helper(root, float('inf'), float('-inf'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ordered = []
        def inOrder(node: TreeNode):
            if node:
                inOrder(node.left)
                ordered.append(node.val)
                inOrder(node.right)
        
        inOrder(root)

        for i in range(len(ordered) - 1):
            if ordered[i + 1] <= ordered[i]:
                return False
        
        return True
        