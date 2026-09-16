from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # The step you can use... Whether to remove the num
        # or include it in the sequence

        # At index i, store the longest increasing subsequence  at that index
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
        
        # Have to loop through the whole thing to define the start of the chain.
        return max(recursion(i) for i in range(len(nums)))