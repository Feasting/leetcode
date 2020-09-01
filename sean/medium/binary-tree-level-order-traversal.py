# 8-31-2020
# https://leetcode.com/problems/binary-tree-level-order-traversal/

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
        
        result = []
        queue = [root]
        while len(queue) > 0:
            level = list(queue)
            queue = []
            values = []
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                values.append(node.val)
            result.append(values)
        
        return result
