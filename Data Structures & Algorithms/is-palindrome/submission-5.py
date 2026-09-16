class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()
        while left <= right:
            while left <= len(s) - 1 and (s[left] == " " or not(s[left].isdigit() or s[left].isalpha())):
                left += 1
            while right >= 0 and (s[right] == " " or not(s[right].isdigit() or s[right].isalpha())):
                right -= 1
            if not(left <= len(s) - 1 and right >= 0):
                break
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        