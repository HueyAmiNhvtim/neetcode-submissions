from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # The step you can use... Whether to remove the num
        # or include it in the sequence
        cache = [-1] * len(nums)

        def recursion(i):
            if cache[i] != -1:
                return cache[i]

            LIS = 1 # Min subsequence length is always 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + recursion(j))

            cache[i] = LIS
            return LIS
        
        return max(recursion(i) for i in range(len(nums)))