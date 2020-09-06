"""

https://leetcode.com/problems/subtree-of-another-tree/

572. Subtree of Another Tree (Easy)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        #A tree is a subtree of another tree if it contains
        #When we see root node of second tree, we can compare if same tree
        
        #traverse the first tree and check if the tree equals to t
        
        #Check if subtree
        def isEqual(s, t):
            if s == None and t == None:
                return True
            if s == None and t != None:
                return False
            if s != None and t == None:
                return False
            if s.val != t.val:
                return False
        
            return isEqual(s.right, t.right) and isEqual(s.left, t.left)
        
        #Traverse s and check if t is subtree
        def traverse(s, t):
            if s == None:
                return False
            if isEqual(s,t):
                return True    
            return traverse(s.left, t) or traverse(s.right, t)
        
        return traverse(s, t)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        #A tree is a subtree of another tree if it contains
        #When we see root node of second tree, we can compare if same tree
        
        #traverse the first tree and check if the tree equals to t
        
        #Check if subtree
        def isEqual(s, t):
            if s == None and t == None:
                return True
            if s == None and t != None:
                return False
            if s != None and t == None:
                return False
            if s.val != t.val:
                return False
        
            return isEqual(s.right, t.right) and isEqual(s.left, t.left)
        
        #Traverse s and check if t is subtree
        def traverse(s, t):
            if s == None:
                return False
            if isEqual(s,t):
                return True    
            return traverse(s.left, t) or traverse(s.right, t)
        
        return traverse(s, t)