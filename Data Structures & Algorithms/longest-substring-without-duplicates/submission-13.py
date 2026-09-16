class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = dict() # Store last known position of a character
        l = 0
        result = 0

        for r in range(len(s)):
            if s[r] in mp and mp[s[r]] >= l: # Reach the duplicate character
                # Condition explanation:
                # Only shift the left pointer if and only if:
                #   1) There exist a record on a character's last known position
                #   2) That last known position is within the window.
                l = mp[s[r]] + 1 # Move left pointer past that position to prevent duplication
                                 # Also to reset streak
            mp[s[r]] = r
            result = max(result, r-l+1)
        return result
    