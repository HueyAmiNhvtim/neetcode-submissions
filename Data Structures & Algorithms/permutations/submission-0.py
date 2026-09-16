class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        candidate_permutations = deque()
        result = []
        # Add the initial states:
        for i in range(len(nums)):
            candidate_permutations.appendleft(([nums[i]], i))
        while candidate_permutations:
            candidate_perm, cur_index = candidate_permutations.popleft()

            # Now...how do we define the state transitions?
            # Part of a single step of state transition would be to append a single number at a time...
            # But how do we choose the number...?
            if len(candidate_perm) == len(nums):
                result.append(candidate_perm)
            # We know that the list contains only unique numbers...
            candidate_set = set(candidate_perm)
            for i in range(cur_index+1, cur_index+len(nums)):
                num = nums[i%len(nums)]
                if num not in candidate_set:
                    candidate_permutations.appendleft((candidate_perm + [num], i%len(nums)))

        return result