# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        levelOrder = []
        q = []
        if root == None:
            return levelOrder
        
        q.append(root)
        while True:
            tempList = []
            while len(q) > 0:
                node = q.pop(0)
                if node != None:
                    tempList.append(node)
            if len(tempList) == 0:
                break    
            levelOrder.append([])
            for node in tempList:
                    levelOrder[len(levelOrder) - 1].append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        
        return levelOrder