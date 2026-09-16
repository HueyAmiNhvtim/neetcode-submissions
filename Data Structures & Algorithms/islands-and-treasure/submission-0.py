from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return []

        visiting = deque()
        lands_to_chest_distance = dict()  # Map the shortest chest distance to land so far

        # loop through the grid, find every instances of the chest.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visiting.append((i, j, 0)) 

        DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        while visiting:
            cur_row, cur_col, distance = visiting.popleft()

            propagate = True
            if grid[cur_row][cur_col] == 2147483647:
                if (cur_row, cur_col) not in lands_to_chest_distance:
                    lands_to_chest_distance[(cur_row, cur_col)] = distance
                else:
                    if distance < lands_to_chest_distance[(cur_row, cur_col)]:
                        lands_to_chest_distance[(cur_row, cur_col)] = distance
                    else:
                        propagate = False
            if propagate:
                for direction in DIRECTIONS:
                    neighbor_row, neighbor_col = cur_row + direction[0], cur_col + direction[1]
                    if -1 < neighbor_row < len(grid) and -1 < neighbor_col < len(grid[0]):
                        neighbor = grid[neighbor_row][neighbor_col]
                        if neighbor != -1 and neighbor != 0:
                            visiting.append((neighbor_row, neighbor_col, distance+1))
        
        for (land_row, land_col) in lands_to_chest_distance:
            grid[land_row][land_col] = lands_to_chest_distance[(land_row, land_col)]
            