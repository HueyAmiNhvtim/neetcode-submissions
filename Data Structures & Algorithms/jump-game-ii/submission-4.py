from typing import List
# You may assume there is always a valid answer.
# You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array. 


class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        step = 0
        while l < len(nums)-1 and r < len(nums)-1:
            furthest_pt = 0
            for i in range(l, r+1):
                furthest_pt = max(furthest_pt, nums[i]+i)
            step += 1
            l, r = r+1, furthest_pt
        return step

    def jumpMySol(self, nums: List[int]) -> int:
        goal = len(nums)-1
        step = 0

        while goal != 0:
            i = goal - 1
            furthest_pt = i
            while i >= 0:
                if nums[i] + i >= goal:
                    furthest_pt = min(furthest_pt, i)
                i -= 1
            goal = furthest_pt
            step += 1

        return step

    