from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rotten_fruit = deque()
        time = 0
        wave_infected = dict()

        num_fruit = 0
        DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # Find all rotten fruits at the initial state to propate first
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_fruit.append((i, j, 0))
                elif grid[i][j] == 1:
                    num_fruit += 1
        # All fruits are already rotten from the get-go
        if num_fruit == 0:
            return 0

        while rotten_fruit:
            infected = False
            cur_row, cur_col, wave = rotten_fruit.popleft()
            print(cur_row, cur_col)

            # Propagate the rotten state to the neighboring fruits.
            for direction in DIRECTIONS:
                i, j = cur_row + direction[0], cur_col + direction[1]
                if -1 < i < len(grid) and -1 < j < len(grid[0]):
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        num_fruit -= 1
                        rotten_fruit.append((i, j, wave+1))
                        infected = True

            if infected:
                wave_infected[wave+1] = True

        for i in range(len(grid)):
            print(grid[i])
        # If after operations, not all fruits are converted to rotten_fruit, is false
        if num_fruit != 0:
            return -1
        return list(wave_infected.keys())[-1]