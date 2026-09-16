from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def recursion(i: int):
            if i > len(nums)-1:
                return 0
            
            max_val = max(nums[i], nums[i]+recursion(i+1))
            return max_val
        
        res = float("-inf")
        for i in range(len(nums)):
            res = max(res, recursion(i))

        return res

