"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        cloned_graph = {}

        if node == None:
            return None
        
        def dfs(node):
            if node in cloned_graph:
                return cloned_graph[node]
            
            cloned_copy = Node(node.val)
            cloned_graph[node] = cloned_copy

            for neighbor in node.neighbors:
                if neighbor in cloned_graph:
                    cloned_copy.neighbors.append(cloned_graph[neighbor])
                else:
                    cloned_copy.neighbors.append(dfs(neighbor))
            
            return cloned_copy
        
        return dfs(node)





        
    
        
        

        
        