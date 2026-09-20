class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            result += self.twoSum(nums, target, i+1, nums[i]) # start with a progressively smaller window 
                                                              # to prevent duplicate result from left side

        return result

    def twoSum(self, nums: List[int], target: int, start: int, original: int):
        result = []
        l = start
        r = len(nums) - 1
        while l < r:
            two_sum = nums[l] + nums[r]
            if two_sum == target:
                result.append([original, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
            elif two_sum > target: # Too big, move the r pointer back
                r -= 1
            else: # Too small, move l forward
                l += 1
        return result            

