from typing import List
from collections import deque


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # O(1) space and O(n) time complexity
        # Start at the end of the list, and work backwards.
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            # If we can jump at position i to reach the goal, that means we can use i as a landing node to reach to it!
            if i + nums[i] >= goal:
                goal = i

        if goal != 0:
            return False
        return True
            