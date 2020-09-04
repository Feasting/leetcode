"""

https://leetcode.com/problems/same-tree/

100. Same Tree (Easy)

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        #Traverse down both trees
        #if they dont equal return false, if they do then return true
        
        
        def traverse(p, q):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False
            elif p.val != q.val:
                return False
            
            return traverse(p.left,q.left) and traverse(p.right,q.right)
        
        return traverse(p, q)