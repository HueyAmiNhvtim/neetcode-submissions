class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potential_targets = dict()
        for i in range(len(nums)):
            if target - nums[i] in potential_targets:
                potential_targets[target - nums[i]].append(i)
                return potential_targets[target - nums[i]]
            else:
                potential_targets[nums[i]] = [i]
        return []