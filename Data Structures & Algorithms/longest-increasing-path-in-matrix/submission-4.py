from typing import List


class Solution:
    # OK, recursive solution will not work since in the case of
    # 100 x 100 , the depth is like 10000 times to reach the end
    # for the top-down solution.....
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    #     DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    #     m_y, m_x = len(matrix), len(matrix[0])
    #     result = 0
    #     # now, time to think of the cache solution...
    #     cache = [[dict() for _ in range(m_x)] for _ in range(m_y)]
    #     def dfs(i: int, j: int, direction) -> int:  
    #         if direction in cache[i][j]:
    #             return cache[i][j][direction] 

    #         lp = 1
    #         lp_dir = (0, 0)
    #         for y, x in DIRECTIONS:
    #             n_y, n_x = i + y, j + x
    #             if (-1 < n_y < m_y and -1 < n_x < m_x): 
    #                 if matrix[n_y][n_x] > matrix[i][j]:
    #                     lp = max(lp, 1 + dfs(n_y, n_x, (y, x)))
    #                     lp_dir = (y, x)
            
    #         cache[i][j][lp_dir] = lp
    #         return lp
        
    #     for s_y in range(m_y):
    #         for s_x in range(m_x):
    #             result = max(result, dfs(s_y, s_x, (0, 0)))
    #     return result

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or matrix[r][c] <= prevVal
            ):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())
        
        