class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        result = set()
        for i in range(len(sorted_nums)):
            all_pairs = self.twoSum(sorted_nums, i + 1, 0 - sorted_nums[i])
            if len(all_pairs) > 0:
                for pair in all_pairs:
                    result.add(tuple([sorted_nums[i], pair[0], pair[1]]))
        result = [list(triplet) for triplet in result]
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
                right -= 1
        return all_pairs