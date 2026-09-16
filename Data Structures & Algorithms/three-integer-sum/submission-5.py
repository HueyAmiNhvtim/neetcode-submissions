class Solution:
    def threeSum(self, nums: List[int], target: int=0) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            all_pairs = self.twoSum(sorted_nums, i + 1, target - sorted_nums[i])
            if len(all_pairs) > 0:
                for pair in all_pairs:
                    result.append([sorted_nums[i], pair[0], pair[1]])
        return result

    def twoSum(self, nums, start_index, target):
        left, right = start_index, len(nums) - 1
        all_pairs = []
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                all_pairs.append(tuple([nums[left], nums[right]]))
                left += 1  # Move both pointers to force the algo to find a different triplet.
                right -= 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
        return all_pairs