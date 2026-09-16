class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = dict() # Store last known position of a character
        l = 0
        result = 0

        for r in range(len(s)):
            if s[r] in mp and mp[s[r]] >= l: # Reach the duplicate character
                # print(f"Duplicate {s[r]} detected at {r}")
                # print(f"Last known {s[r]} at {mp[s[r]]}")
                l = mp[s[r]] + 1 # Move left pointer past that position to prevent duplication
                                 # Also to reset streak
            mp[s[r]] = r
            # print(s[r], mp[s[r]])
            result = max(result, r-l+1)

        return result
    