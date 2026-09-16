class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:  # Nums[m] is part of left sorted set
                if target < nums[l] or target > nums[m]:  # target is in the right sorted set
                    # as the left sorted set is guaranteed to be bigger the target
                    l = m + 1
                else:
                    r = m - 1  # target is in the left sorted set as it is possibly sandwiched between nums[l] and nums[m]
            else:  # middle is in the right sorted set
                if target > nums[r] or target < nums[m]:  # target is in the left sorted set
                    r = m - 1
                else:  # target is in the right sorted set
                    l = m + 1
        return -1
        