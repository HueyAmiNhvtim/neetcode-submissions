class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # Construct the adjacency list
        adjacency_list = defaultdict(list)
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        visit = [False] * (n + 1)
        cycle = set()
        cycleStart = -1  # For marking the start of a cycle

        # Time & Space Complexity
        #
        #     Time complexity: O(V+E)O(V+E)
        #     Space complexity: O(V+E)O(V+E)
        
        def dfs(node, parent):
            nonlocal cycleStart
            # if we reach a node that has already been visited, mark it as the start of a cycle
            if visit[node]:
                cycleStart = node
                return True

            visit[node] = True
            for neighbor in adjacency_list[node]:
                if neighbor == parent:
                    # If the neighbor of this node is its parent, just don't do anything.
                    continue
                if dfs(neighbor, node):
                    # As you dive out, add the node - the parent of the explored neighbor to the cycle!
                    if cycleStart != -1:
                        cycle.add(node)
                    # If parent is the start of the cycle, then the cycle has been fully detected, stop adding new
                    # node to the cycle set!
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)

        # Scan from the end and grab the first edge with both nodes in the cycle
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []
