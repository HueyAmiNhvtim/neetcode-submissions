node_visited = 0

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        directed_edges = defaultdict(set) # Turn each undirected edge into 2 directed edges
        for edge in edges:
            directed_edges[edge[0]].add(edge[1])
            directed_edges[edge[1]].add(edge[0])

        # A tree does not contain any cycles!
        # I guess assume that some nodes can be disconnected from the "big" tree.
        visited_node_in_path = set()
        visited_total = set()
        def dfs(node: int, parent):
            if node in visited_node_in_path:
                return False # Node visited twice => Not a tree
            if not directed_edges[node]:
                return True # Reach leaf or the sub-graph that has already been checked to be a tree
            visited_node_in_path.add(node) # Record the node
            for neighbor in directed_edges[node]:
                if neighbor != parent: # Do not allow the node to go back to its parent
                    if not dfs(neighbor, node):
                        return False
            directed_edges[node] = set()
            visited_node_in_path.remove(node)
            visited_total.add(node)
            return True
        # How to know if every node is connected? Well, count the number of node in the path!
        for i in range(n):
            if not dfs(i, -1):
                return False
            if len(visited_total) != n:
                return False
            else:
                return True
        return True