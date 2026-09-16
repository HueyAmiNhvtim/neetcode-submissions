class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        cache = dict()
        # At every index, check if substring of s at index i contains a word from word_dict.
        # That's my logic.

        def word_break_recursion(s: str, wordDict: Set[str], l: int) -> bool:
            if l >= len(s):
                return True  # Reached the end!

            if l not in cache:
                viable = False
                for i in range(l, len(s)):
                    if s[l:i + 1] in wordDict:
                        viable = viable or word_break_recursion(s, wordDict, i + 1)
                cache[l] = viable
            return cache[l]

        result = word_break_recursion(s, wordDict, 0)

        return result        