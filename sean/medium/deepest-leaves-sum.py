# 9-12-2020
# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        next_level = True
        while next_level:
            next_level = False
            for node in queue:
                if node.left or node.right:
                    level = list(queue)
                    queue = []
                    for n in level:
                        if n.left:
                            queue.append(n.left)
                        if n.right:
                            queue.append(n.right)
                    next_level = True
                    break
        result = 0
        for node in queue:
            result += node.val
        return result
