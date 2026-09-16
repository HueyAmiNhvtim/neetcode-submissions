class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums = sorted(nums)

        potential_subsets = deque()
        result = [[]]
        # Adding initial state:
        for i in range(len(nums)):
            # Prevent adding duplicate initial states
            if (i == 0) or (i > 0 and nums[i] != nums[i-1]):
                potential_subsets.appendleft(([nums[i]], i))

        while potential_subsets:
            subset, cur_index = potential_subsets.popleft()
            result.append(subset)

            # Avoid adding duplicate transition states
            for i in range(cur_index+1, len(nums)):
                if (i == cur_index+1) or (i > cur_index+1 and nums[i] != nums[i-1]):
                    potential_subsets.appendleft((subset + [nums[i]], i))

        return result