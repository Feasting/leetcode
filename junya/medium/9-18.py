# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q=[root]
        ret=[]
        while q:
            ret.append([])
            lenq = len(q)
            for i in range(0, lenq):
                cur=q.pop(0)
                ret[-1].append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        
        return ret
        
# https://leetcode.com/problems/binary-tree-level-order-traversal/
