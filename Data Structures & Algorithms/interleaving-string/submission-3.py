class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = dict()

        def recursion(i: int, j: int, k: int) -> str:
            if i >= len(s1):
                for pos in range(j, len(s2)):
                    if s2[pos] != s3[k]:
                        return False
                    k += 1
                return True
            if j >= len(s2):
                for pos in range(i, len(s1)):
                    if s1[pos] != s3[k]:
                        return False
                    k += 1
                return True
            
            if (i, k) in cache:
                return cache[(i, k)]

            if s1[i] == s3[k] and s2[j] == s3[k]:
                result = recursion(i+1, j, k+1) or recursion(i, j+1, k+1)
            elif s1[i] == s3[k]:
                result = recursion(i+1, j, k+1) 
            elif s2[j] == s3[k]:
                result = recursion(i, j+1, k+1)
            else:
                result = False
            
            cache[(i, k)] = result

            return result
        
        return recursion(0, 0, 0)

# Intuition

# We need to check whether the string s3 can be formed by interleaving s1 and s2, while keeping the relative order of characters from both strings.

# Instead of recursion, we can solve this using bottom-up dynamic programming.
# The idea is to determine, for every possible pair of positions (i, j), whether it is possible to form the suffix of s3 starting at position i + j using:

#     the substring s1[i:]
#     the substring s2[j:]

# If either taking the next character from s1 or from s2 leads to a valid state, then the current state is also valid.
# Algorithm

#     First, check if the lengths of s1 and s2 add up to the length of s3:
#         If not, return false
#     Create a 2D DP table dp of size (len(s1) + 1) x (len(s2) + 1):
#         dp[i][j] is true if s3[i + j:] can be formed using s1[i:] and s2[j:]
#     Initialize the base case:
#         dp[len(s1)][len(s2)] = true because empty strings can form an empty string
#     Fill the table in reverse order (from bottom-right to top-left):
#     For each position (i, j):
#         If the next character of s1 matches s3[i + j] and dp[i + 1][j] is true, then set dp[i][j] = true
#         If the next character of s2 matches s3[i + j] and dp[i][j + 1] is true, then set dp[i][j] = true
#     After filling the table, the answer is stored in dp[0][0]
#     Return dp[0][0]

        def isInterleaveTabulation(self, s1: str, s2: str, s3: str) -> bool:
            if len(s1) + len(s2) != len(s3):
                return False

            dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
            dp[len(s1)][len(s2)] = True

            for i in range(len(s1), -1, -1):
                for j in range(len(s2), -1, -1):
                    if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                        dp[i][j] = True
                    if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                        dp[i][j] = True
            return dp[0][0]