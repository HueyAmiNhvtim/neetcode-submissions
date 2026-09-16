class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        for n in nums:
            # check if its the start of the sequence
            if (n-1) not in num_set:
                cur_len = 1
                while (n + 1) in num_set:
                    cur_len += 1
                    n += 1
                if cur_len > max_len:
                    max_len = cur_len
        return max_len
        