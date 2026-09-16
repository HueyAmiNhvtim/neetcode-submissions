class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()
        while left < right:
            while left < right and  (s[left] == " " or not(s[left].isdigit() or s[left].isalpha())):
                left += 1
            while right > left and (s[right] == " " or not(s[right].isdigit() or s[right].isalpha())):
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        