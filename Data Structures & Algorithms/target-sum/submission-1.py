from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = [[-1] * target for _ in range(len(nums))]
        # Basically at each index for a given sum, get the number of
        # combo that can already be done at that index to reach the sum
        def dfs(i: int, cur_sum: int) -> int:
            if i >= len(nums):
                if cur_sum == target:
                    return 1
                return 0
                  
            add = dfs(i+1, cur_sum+nums[i])
            minus = dfs(i+1, cur_sum-nums[i])
            return add + minus
        
        return dfs(0, 0)
            