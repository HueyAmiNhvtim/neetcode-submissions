class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_dict = dict()
        if len(s2) < len(s1):
            return False

        for char in s1:
            freq_dict[char] = freq_dict.get(char, 0) + 1

        # Set up 2 pointers, only move l if the value of freq_dict at r goes below 0.
        l, r = 0, 0
        while l < len(s2) and r < len(s2):
            if s2[r] in freq_dict:
                freq_dict[s2[r]] = freq_dict[s2[r]] - 1
                if freq_dict[s2[r]] < 0:  # More than what is needed, move l until that problem is resolved
                    while freq_dict[s2[r]] < 0:
                        freq_dict[s2[l]] += 1
                        l += 1

                r += 1
            else:  # lost cause, move l to r + 1 and reset
                while l < r + 1 and l < len(s2):
                    if s2[l] in freq_dict:
                        freq_dict[s2[l]] += 1
                    l += 1
                r = l

            if sum(freq_dict.values()) == 0:
                return True
        return False