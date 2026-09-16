class Solution:
    def rob(self, nums: List[int]) -> int:
        max_so_far_start = dict() # At index i, what is the maximum value we have robbed so far.
        max_so_far_no_start = dict()
        # We have 2 possible steps to make here.
        # Either we choose to rob this house, and skip 1 step to the next next house.
        # Or we choose not to rob this house, and go to the next house.
        result = nums[0] + self.recursiveRobAtStart(nums, 2, max_so_far_start)
        result_no_rob_start = self.recursiveRob(nums, 1, max_so_far_no_start)
        print(max_so_far_start, max_so_far_no_start)
        return max(result, result_no_rob_start)

    def recursiveRobAtStart(self, nums: List[int], cur_i: int, max_so_far: dict):
        if cur_i >= len(nums) - 1:
            return 0

        if max_so_far.get(cur_i) is None:
            rob_at_cur_i = nums[cur_i] + self.recursiveRobAtStart(nums, cur_i+2, max_so_far)
            no_rob_at_cur_i = self.recursiveRobAtStart(nums, cur_i+1, max_so_far)
            max_so_far[cur_i] = max(rob_at_cur_i, no_rob_at_cur_i)
            return max_so_far[cur_i]
        else:
            return max_so_far[cur_i]

    def recursiveRob(self, nums: List[int], cur_i: int, max_so_far: dict) -> int:
        if cur_i >= len(nums):
            return 0

        if max_so_far.get(cur_i) is None:
            rob_at_cur_i = nums[cur_i] + self.recursiveRob(nums, cur_i+2, max_so_far)
            no_rob_at_cur_i = self.recursiveRob(nums, cur_i+1, max_so_far)
            max_so_far[cur_i] = max(rob_at_cur_i, no_rob_at_cur_i)
            return max_so_far[cur_i]
        else:
            return max_so_far[cur_i]        