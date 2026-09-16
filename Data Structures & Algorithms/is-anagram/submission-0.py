class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_dict = dict()
        for char in s:
            freq_dict[char] = freq_dict.get(char, 0) + 1
        for char in t:
            freq = freq_dict.get(char, -1)
            if freq == -1:
                return False
            freq_dict[char] -= 1
            if freq_dict[char] < 0:
                return False
        for char in freq_dict:
            if freq_dict[char] != 0:
                return False
        return True