# 9-3-2020
# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        visited = {}
        def copy(node: Node) -> Node:
            if node in visited:
                return visited[node]
            result = Node()
            result.val = node.val
            visited[node] = result
            for neighbor in node.neighbors:
                result.neighbors.append(copy(neighbor))
            return result
        return copy(node)
