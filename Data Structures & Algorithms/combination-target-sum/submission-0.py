class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        # How do you remove duplicate solution again...?

        result = []
        nums = sorted(nums) # Sorted to make it easier to prune early
        potential_sum = deque()
        # Add the possible starting states
        for i in range(len(nums)):
            potential_sum.appendleft(([nums[i]], nums[i], i)) # Save the current sum + the current index of potential member to be added

        # All elements of nums are distinct => Starting with nothing the choice is either: ...stay and add or move to the new number and begin anew
        # Because of the all-unique elements, that means all solutions paths do not overlap with one another.
        while potential_sum:
            cur_subset, cur_sum, cur_index = potential_sum.popleft()

            if cur_sum == target: # Valid target
                result.append(cur_subset)
            elif cur_sum < target: # Potential to dive
                for i in range(cur_index, len(nums)):
                    if cur_sum + nums[i] <= target: # Only add if the new sum is <= target  => Prune cases where sum is guaranteed to be big
                        potential_sum.appendleft((cur_subset + [nums[i]], cur_sum + nums[i], i))
        return result