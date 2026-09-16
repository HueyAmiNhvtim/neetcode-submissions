from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)] # right, down, left, up
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                node = grid[i][j]
                if node == "1":
                    num_islands += 1
                    visiting = deque()
                    visiting.append((i, j))
                    while visiting:
                        row, col = visiting.popleft()
                        node = grid[row][col]
                        if node == "1":
                            for direction in directions:
                                n_row, n_col = row + direction[0], col + direction[1]
                                if -1 < n_row < len(grid) and -1 < n_col < len(grid[0]):
                                    neighbor_node = grid[n_row][n_col]
                                    if neighbor_node == "1":
                                        visiting.appendleft((n_row, n_col))
                            grid[row][col] = "#"

        # for i in range(len(grid)):
        #     print(" ".join(grid[i]))

        return num_islands