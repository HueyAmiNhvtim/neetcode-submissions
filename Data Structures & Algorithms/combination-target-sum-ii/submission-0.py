from collections import deque

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        result = []
        candidates = sorted(candidates)
        potential_sum = deque()
        # Add potential states to stack
        for i in range(len(candidates)):
            # Prevent duplicate starting state
            if i > 0 and candidates[i] != candidates[i-1]:
                potential_sum.appendleft(([candidates[i]], candidates[i], i))
            elif i == 0:
                potential_sum.appendleft(([candidates[i]], candidates[i], i))


        while potential_sum:
            candidate_subset, cur_sum, cur_index = potential_sum.popleft()
            if cur_sum == target:
                result.append(candidate_subset) 
            # at each position, append the number to the current subset if and only if the sum is not
            # > target
            for i in range(cur_index+1, len(candidates)):
                # Prevent duplicate transition states
                if i-1 > cur_index:
                    if cur_sum + candidates[i] <= target and candidates[i] != candidates[i-1]:
                        potential_sum.appendleft((candidate_subset + [candidates[i]], cur_sum + candidates[i], i))
                else:
                    potential_sum.appendleft((candidate_subset + [candidates[i]], cur_sum + candidates[i], i))


        return [list(subset) for subset in result]