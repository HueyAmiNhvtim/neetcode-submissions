class Solution:
  def longestPalindrome(self, s: str) -> str:
        result = ""
        result_len = 0

        for i in range(len(s)):
            # Expand in the case of odd length palindrome
            cur_len = 1
            cur_str = s[i]
            l, r = i - 1, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                cur_len += 2
                if cur_len > result_len:
                    result_len = cur_len
                    result = s[l:r+1]
                l -= 1
                r += 1

            # Expand in the case of even length palindrome
            if i + 1 < len(s):
                l, r = i, i + 1
                cur_len = 0
                while l > -1 and r < len(s) and s[l] == s[r]:
                    cur_len += 2
                    if cur_len > result_len:
                        result_len = cur_len
                        result = s[l:r+1]
                    l -= 1
                    r += 1

            if len(result) == 0:
                result = cur_str

        return result
    
        