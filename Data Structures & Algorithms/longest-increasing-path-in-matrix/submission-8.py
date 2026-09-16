from typing import List


class Solution:
    # OK, recursive solution will not work since in the case of
    # 100 x 100 , the depth is like 10000 times to reach the end
    # for the top-down solution.....
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        result = 0
        # now, time to think of the cache solution...
        cache = dict()

        def dfs(r: int, c: int, pre_val: int):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= pre_val):
                return 0

            if (r, c) in cache:
                return cache[(r, c)]

            lp = 1
            lp = max(lp, 1 + dfs(r + 1, c, matrix[r][c]))
            lp = max(lp, 1 + dfs(r - 1, c, matrix[r][c]))
            lp = max(lp, 1 + dfs(r, c + 1, matrix[r][c]))
            lp = max(lp, 1 + dfs(r, c - 1, matrix[r][c]))
            cache[(r, c)] = lp
            return lp

        for r in range(ROWS):
            for c in range(COLS):
                result = max(result, dfs(r, c, -1))
        return result
        
        