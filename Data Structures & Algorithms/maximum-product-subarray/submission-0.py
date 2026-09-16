class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # Initialize to the maximum value in array. Can't be 1 because the array can just contain all negatives
        cur_min, cur_max = 1, 1 # Neutral value

        # BOTTOM-UP APPROACH
        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1  # Reset upon encountering 0 to avoid the death spiral
                continue
            tmp_max, tmp_min = cur_max, cur_min
            cur_max = max(n * tmp_max, n * tmp_min, n)  # n can be negative and cur_min can be negative, hence potential bigger positive value.
                                                        # n itself can be considered as the start of the new subarray starting at n! Also consider the case of [-1, 8]
            cur_min = min(n * tmp_max, n * tmp_min, n)  # Consider the case of [-1, -8]. -8 itself can be considered the start of a new subarray start at its place!
                                                        # n * cur_max and n * cur_min is for continuing the streak of the current subarray!
            res = max(res, cur_max)
        return res