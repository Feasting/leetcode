# 9-1-2020
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if len(preorder) == 0:
            return None
        
        self.iPreOrder = 0
        
        def helper(preorder, inorder, start, end):
            
            if start > end:
                return None
            
            node  = TreeNode(preorder[self.iPreOrder])
            self.iPreOrder += 1
            
            if start == end:
                return node
            
            iInOrder = None
            for i in range(start, end + 1):
                if inorder[i] == node.val:
                    iInOrder = i
                    break
            
            node.left = helper(preorder, inorder, start, iInOrder - 1)
            node.right = helper(preorder, inorder, iInOrder + 1, end)
            
            return node
        
        return helper(preorder, inorder, 0, len(inorder) - 1)
