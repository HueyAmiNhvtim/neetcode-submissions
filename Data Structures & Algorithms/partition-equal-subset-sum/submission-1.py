from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # The steps you can choose:
        # As you move onto each index, you can either choose to include
        # it in this sum, or add it into the next sum

        # Recurrence relation down.
        # Now for memoization.

        # How about a 1D array that stores whether a sublist starting
        # at index

        sum_nums = sum(nums)
        # This one fails because the time complexity is like O(2^n)
        def recursion(s1: int, s2: int, i: int) -> bool:
            if i >= len(nums):
                if s1 == s2:
                    return True
                return False
            

            choose_for_s1 = recursion(s1 + nums[i], s2, i + 1)
            choose_for_s2 = recursion(s1, s2 + nums[i], i + 1)

            return choose_for_s1 or choose_for_s2
        
        cache_table = [[-1] * (sum_nums // 2 + 1) for _ in range(len(nums) + 1)]
        def recursionBetter(cur_sum: int, i: int):
            if i >= len(nums) or cur_sum > sum_nums // 2:
                return False
            if cur_sum == sum_nums / 2:
                return True
            
            if cache_table[i][cur_sum] != -1:
                return cache_table[i][cur_sum]
            retain = recursionBetter(cur_sum + nums[i], i + 1)
            not_retain = recursionBetter(cur_sum, i + 1)
            cache_table[i][cur_sum] = retain or not_retain
            return cache_table[i][cur_sum]


        if sum_nums % 2 == 0:
            return recursionBetter(0, 0)
        else:
            return False # Odd sum can never be partitioned.