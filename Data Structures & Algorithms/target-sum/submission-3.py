from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = dict()
        # Basically at each index for a given sum, get the number of
        # combo that can already be done at that index to reach the sum
        def dfs(i: int, cur_sum: int) -> int:
            if i >= len(nums):
                if cur_sum == target:
                    return 1
                return 0
            
            if (i, cur_sum) in cache:
                return cache[(i, cur_sum)]

            add = dfs(i+1, cur_sum+nums[i])
            minus = dfs(i+1, cur_sum-nums[i])
            cache[(i, cur_sum)] = add + minus
            return add + minus

        result = dfs(0, 0)
        return result
        