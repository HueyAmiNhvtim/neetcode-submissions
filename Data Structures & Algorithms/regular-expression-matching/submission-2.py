class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recursion(i: int, j: int) -> False:
            if i == len(s) and j == len(p):
                return True

            if j == len(p) and i < len(s):
                return False
            
            match = False
            # Check for the wildcard pattern
            if j + 1 < len(p) and p[j+1] == "*":
                i_l = i
                # The "zero" part of the wild card
                match = match or recursion(i_l, j+2)
                # The "more" part of the wild card
                while i_l < len(s) and (s[i_l] == p[j] or p[j] == ".") and not match:
                    i_l += 1
                    match = match or recursion(i_l, j+2)
            else:
                if (i < len(s) and s[i] == p[j]) or p[j] == ".":
                    match = recursion(i+1, j+1)
            return match
        
        match = recursion(0, 0)
        return match