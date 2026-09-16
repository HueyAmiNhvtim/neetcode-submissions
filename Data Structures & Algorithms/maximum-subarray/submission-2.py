from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, n = nums[0], len(nums)
        cur_sum = 0
        
        
        for i in range(n):
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += nums[i]
            res = max(res, cur_sum)

        return res

