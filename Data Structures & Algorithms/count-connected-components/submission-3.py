class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return 0

        components = 0
        adjacency_dict = defaultdict(list)
        for edge in edges:
            adjacency_dict[edge[0]].append(edge[1])
            adjacency_dict[edge[1]].append(edge[0])

        # Adding initial positions
        visited = set()
        for i in range(n):
            jumping = deque()  # Store the currently explored node.
            if i not in visited:
                components += 1
                jumping.append(i)
                while jumping:
                    cur_node = jumping.popleft()
                    if cur_node not in visited:
                        visited.add(cur_node)
                        for neighbor in adjacency_dict[cur_node]:
                            jumping.append(neighbor)

        return components