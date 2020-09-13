# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = [root]
        while q:
            curr = q.pop(0)
            if curr is None:
                continue
            q.append(curr.left)
            q.append(curr.right)
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            
        return root
        
# https://leetcode.com/problems/invert-binary-tree/
