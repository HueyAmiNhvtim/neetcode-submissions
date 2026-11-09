from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visiting = deque()
        visiting_copycat = deque()
        
        # Ah, do you remember the trick of mapping old_node to new_node?
        old_to_new = dict()
        old_to_new[node] = [Node(val=node.val), False] # Map old node to its new node counterpart, and a visited flag
        root = old_to_new[node][0]
        visiting.append(node)
        while visiting:
            cur_node = visiting.popleft()
            cur_new_node, visited = old_to_new[cur_node]
            new_neighbors = []
            if not visited: 
                old_to_new[cur_node][1] = True

                for old_neighbor in cur_node.neighbors:
                    visiting.append(old_neighbor)
                    if not old_to_new.get(old_neighbor, None):
                        old_to_new[old_neighbor] = [Node(old_neighbor.val), False]
                    new_neighbors.append(old_to_new[old_neighbor][0])
                cur_new_node.neighbors = new_neighbors
        return root
                
        


        