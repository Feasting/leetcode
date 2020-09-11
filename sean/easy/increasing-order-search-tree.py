# 9-11-2020
# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def inOrder(node):
            if node:
                inOrder(node.left)
                nodes.append(node)
                inOrder(node.right)
        inOrder(root)
        root = nodes[0]
        p = root
        for node in nodes[1:]:
            p.right = TreeNode(node.val)
            p = p.right
        return root
