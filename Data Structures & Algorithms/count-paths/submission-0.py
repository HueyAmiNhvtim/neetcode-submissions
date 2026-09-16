

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        def dfs(cur_i: int, cur_j: int) -> int:
            if cur_i >= m or cur_j >= n:
                return 0
            
            if cache[cur_i][cur_j] != -1:
                return cache[cur_i][cur_j]
            
            if cur_i == m-1 and cur_j == n-1:
                return 1

            # You can only move either down or to the right
            # So no up or left.
            cur_num_paths = dfs(cur_i, cur_j + 1) + dfs(cur_i + 1, cur_j)
            cache[cur_i][cur_j] = cur_num_paths
            return cur_num_paths

        return dfs(0, 0)