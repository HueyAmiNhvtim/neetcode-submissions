class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if target < nums[l]: # target is in the right sorted
                                     # as the left sorted set is guaranteed to be bigger the target
                    l = m + 1
                else:
                    if target >= nums[m]:  # target is part of left sorted set
                        l = m + 1
                    else:
                        r = m - 1 # target is in the left sorted set as it is possibly sandwiched between nums[l] and nums[m]
            else: # middle is in the right sorted set
                if target > nums[r]: # target is in the left sorted set
                    r = m - 1
                else: # target is in the right sorted set
                    if target <= nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
        return -1
        