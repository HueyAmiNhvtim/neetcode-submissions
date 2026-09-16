class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                # We have reached the sorted portion of the array from l to r
                result = min(result, nums[l])
                break
            m = (l + r) // 2
            result = min(result, nums[m])
            if nums[m] >= nums[l]: # Min element in Right sorted part as all elements in left part is guaranteed to be bigger than everything in right also due to nums[l] >= nums[r]
                l = m + 1
            else: # Min element in left sorted part
                r = m - 1
        # print(l, r)
        return result