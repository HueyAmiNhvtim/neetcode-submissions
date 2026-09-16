from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)] # Left, up, right, down
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                node = grid[i][j]
                if node == 1:
                    # Dive time
                    visiting = deque()
                    visiting.appendleft((i, j))
                    area = 0
                    while visiting:
                        cur_row, cur_col = visiting.popleft()
                        cur_node = grid[cur_row][cur_col]
                        if cur_node == 1:
                            area += 1
                            grid[cur_row][cur_col] = -1
                            for direction in directions:
                                n_row, n_col = cur_row + direction[0], cur_col + direction[-1]
                                if -1 < n_row < ROWS and -1 < n_col < COLS:
                                    if grid[n_row][n_col] == 1:
                                        visiting.appendleft((n_row, n_col))
                    
                    if area > max_area:
                        max_area = area

        return max_area
