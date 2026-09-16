from typing import List
from math import ceil



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We determine the bound of eating rate to be [1, max(piles)] as Koko can only eat at most 1 pile per hour
        max_pile_value = max(piles)
        result = max_pile_value
        l, r = 1, max_pile_value
        while l <= r:
            curr_h = 0
            m = (l + r) // 2
            for i in range(len(piles)):
                curr_h += ceil(piles[i] / m)
            if curr_h <= h:
                result = m
                r = m - 1
            else:
                l = m + 1
        return result