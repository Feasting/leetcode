# 9-6-2020
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None

        queue = [root]
        
        while len(queue) > 0:
            level = list(queue)
            queue = []
            size = len(level)
            for i in range(size):
                node = level[i]
                if i != size - 1:
                    node.next = level[i + 1]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return root
