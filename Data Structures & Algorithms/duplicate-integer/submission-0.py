class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_dict = dict()
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
            if freq_dict[num] > 1:
                return True
        return False