class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        encountered = set()
        for r in range(len(s)):
            char = s[r]
            if char in encountered:
                while l < r and s[r] in encountered:
                    encountered.remove(s[l])
                    l += 1
            encountered.add(char)
            result = max(result, r-l+1)
            print(f"result: {result} l: {l} r: {r}")
        return result