class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Cache: At substring of text 1 and substring of text2,
        # what is the longest common subsequence between them?
        storage = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        text1, text2 = list(text1), list(text2)
        def dfs(cur_i: int, cur_j: int) -> int:
            if cur_i >= len(text1) or cur_j >= len(text2):
                return 0
            
            if storage[cur_i][cur_j] != -1:
                return storage[cur_i][cur_j]

            # This doesn't account for strings containing duplicate elements
            if text1[cur_i] == text2[cur_j]:
                LCS = 1 + dfs(cur_i + 1, cur_j + 1)
            else:
                LCS = max(dfs(cur_i + 1, cur_j), dfs(cur_i, cur_j + 1))
            storage[cur_i][cur_j] = LCS
            return LCS
        result = dfs(0, 0)
        return result
            