class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len, i = 0, 0

        nums_sorted = sorted(nums)
        while i < len(nums_sorted):
            j = i
            cur_len = 1
            while j < len(nums_sorted) - 1:
                if nums_sorted[j+1] - nums_sorted[j] == 1:
                    cur_len += 1
                elif nums_sorted[j+1] - nums_sorted[j] > 1:
                    break
                j += 1
            if cur_len > max_len:
                max_len = cur_len
            i += 1

        return max_len
        