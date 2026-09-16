class Solution:
    def jump(self, nums: List[int]) -> int:
        # So it's kinda like a sliding window one.
        l, r = 0, 0
        result = 0
        # Stop when the window reaches the end
        while l < len(nums) - 1 and r < len(nums)-1:
            furthest_pt = 0 # Furthest point that can be reached within this window.
            for i in range(l, r+1):
                furthest_pt = max(furthest_pt, i+nums[i]) 
            result += 1
            l, r = r+1, furthest_pt
        return result