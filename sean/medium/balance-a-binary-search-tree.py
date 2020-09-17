# 9-16-2020
# https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        arr = []
        def inOrder(node):
            if node:
                inOrder(node.left)
                arr.append(node)
                inOrder(node.right)
        inOrder(root)
        
        def constructTree(arr):
            if len(arr) == 0:
                return None
            mid = len(arr) // 2
            arr[mid].left = constructTree(arr[:mid])
            arr[mid].right = constructTree(arr[mid+1:])
            return arr[mid]
        
        root = constructTree(arr)
        
        return root
