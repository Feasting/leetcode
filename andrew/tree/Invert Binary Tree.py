"""

https://leetcode.com/problems/invert-binary-tree/

226. Invert Binary Tree (Easy)

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def invert(node):
            if node == None:
                return
            
            temp = node.left
            node.left = node.right
            node.right = temp
            
            invert(node.left)
            invert(node.right)
            
        invert(root)
        return root