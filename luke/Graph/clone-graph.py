
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        copyGraph = Node()
        visited = {}
        if node == None:
            return
        elif node.neighbors == None:
            copyGraph.val = 1
            return copyGraph
        
        def cloneGraphHelp(node, visited):
            if node.val in visited:
                visited[node.val] = visited.get(node.val) + 1
            else:
                visited[node.val] = 1
            copyGraph = Node()
            copyGraph.val = node.val
            print("copied value: " + str(copyGraph.val))
            for i in range(len(node.neighbors)):
                if not node.neighbors[i].val in visited or visited[node.neighbors[i].val] < len(node.neighbors):
                    copyGraph.neighbors.append(cloneGraphHelp(node.neighbors[i], visited))
                                    
            return copyGraph
        
        copyGraph = cloneGraphHelp(node, visited)
        for x in visited:
            print(visited.get(x))
        
        return copyGraph