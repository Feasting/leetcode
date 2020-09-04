"""

https://leetcode.com/problems/binary-tree-level-order-traversal/

102. Binary Tree Level Order Traversal (Medium)

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root == None:
            return []
        
        level = [root]
        output = []
        
        #Breadth First Search
        while level:
            outLevel = []
            nextLevel = []
            for i in level:
                outLevel.append(i.val)
                if i.left:
                    nextLevel.append(i.left)
                if i.right:
                    nextLevel.append(i.right)
            output.append(outLevel)
            level = nextLevel
            
        return output