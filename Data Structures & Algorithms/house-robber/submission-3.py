class Solution:
    def rob(self, nums: List[int]) -> int:
        max_so_far = dict() # At index i, what is the maximum value we have robbed so far.
        # We have 2 possible steps to make here.
        # Either we choose to rob this house, and skip 1 step to the next next house.
        # Or we choose not to rob this house, and go to the next house.
        return self.recursiveRob(nums, 0, max_so_far)

    def recursiveRob(self, nums: List[int], cur_i: int, max_so_far: dict) -> int:
        if cur_i >= len(nums):
            return 0

        if max_so_far.get(cur_i) is None:
            rob_at_cur_i = nums[cur_i] + self.recursiveRob(nums, cur_i+2, max_so_far)
            no_rob_at_cur_i = self.recursiveRob(nums, cur_i+1, max_so_far)
            max_so_far[cur_i] = max(rob_at_cur_i, no_rob_at_cur_i)
        return max_so_far[cur_i]