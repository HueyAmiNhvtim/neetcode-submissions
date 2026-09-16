from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = dict()
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
            if count[nums[i]] > 1:
                return nums[i]