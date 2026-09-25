class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = dict()        
        def lcsrecurse(i: int, j: int):
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]

            if text1[i] == text2[j]:
                LCS =  1 + lcsrecurse(i+1, j+1)
            else:
                advance_i = lcsrecurse(i+1, j)
                advance_j = lcsrecurse(i, j+1)
                LCS = max(advance_i, advance_j)
            cache[(i, j)] = LCS
            return LCS

        result = lcsrecurse(0, 0)
        return result
        