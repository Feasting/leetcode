"""

https://leetcode.com/problems/symmetric-tree/

101. Symmetric Tree (Easy)

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        #Traverse down binary tree, compare right and left
        def traverse(node1, node2):
            if node1 == None and node2 == None:
                return True
            #Not Equal / symetric
            if node1 == None or node2 == None:
                return False
            if node1.val != node2.val:
                return False
            
            return traverse(node1.left, node2.right) and traverse(node1.right, node2.left)
        
        return traverse(root.left, root.right)