class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        frequency_dict = dict()
        l, r = 0, 0
        r_unchanged = False
        while r < len(s):
            if not r_unchanged:
                frequency_dict[s[r]] = frequency_dict.get(s[r], 0) + 1
            most_frequent_char, freq = max(frequency_dict.items(), key=lambda x: x[1])
            if (r - l + 1 - freq) <= k: # If we can replace non-frequent character within the substring with the most frequent character while remaining under k replacement limit, it's valid!
                res = max(res, r - l + 1)
                r += 1
                r_unchanged = False
            else: # If not, we advance the l instead
                if s[l] in frequency_dict:
                    frequency_dict[s[l]] -= 1
                l += 1
                r_unchanged = True
        return res