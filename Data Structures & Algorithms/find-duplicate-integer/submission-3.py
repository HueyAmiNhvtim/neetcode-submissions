from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # Use the list itself as a hashset.
            if nums[abs(nums[i]) - 1] < 0:
                # Sth has already operated on this particular member.
                return abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] *= -1