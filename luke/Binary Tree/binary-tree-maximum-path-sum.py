# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return float('-inf')
        sum = root.val
        # if root.right is not None and root.right.val > 0:
        #     sum += root.right.val
        # if root.left is not None and root.left.val > 0:
        #     sum += root.left.val
        left = self.maxPathSum(root.left)
        right = self.maxPathSum(root.right)
        childMax = max(left, right)
        if left > 0 and right > 0 and sum >= 0:
            childMax = left + right
        maxSum = max(sum, childMax)
        if sum > 0 and childMax > 0:
            maxSum = childMax + sum
        
        return maxSum