class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        len_longest_sub = 0
        l, r = 0, 0
        unique_chars = set()
        while True:
            if r == len(s):
                if (cur_len := r - l) > len_longest_sub:
                    len_longest_sub = cur_len
                break # We know we have gotten the longest substring length from this point on, so we can just break
            # Continue advancing the window when the current character is not in the set.
            if s[r] not in unique_chars:
                unique_chars.add(s[r])
                r += 1
            else:
                if (cur_len := r - l) > len_longest_sub:
                    len_longest_sub = cur_len
                l += 1
                r = l
                unique_chars = set()
        return len_longest_sub