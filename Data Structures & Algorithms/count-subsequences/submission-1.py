class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = dict() # Key: The number of subsequences starting at index s_i and index t_i
        def recursion(i: int, j: int) -> int:
            if i >= len(s) and j < len(t):
                return 0
            
            if j >= len(t):
                return 1

            if (i, j) in cache:
                return cache[(i, j)]

            res = 0
            if s[i] == t[j]:
                res += recursion(i+1, j+1) + recursion(i+1, j)
            else:
                res += recursion(i+1, j)
            cache[(i, j)] = res
            return res

        subsequences = 0
        for s_i in range(len(s)):
            if s[s_i] == t[0]:
                subsequences_at_s_i = recursion(s_i+1, 1)
                print(subsequences_at_s_i, s_i)
                subsequences += subsequences_at_s_i

        return subsequences