class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        
        # 3 possible operations at any position
        # Insertion
        # Deletion of the current character
        # Replacement of the character
        # So the cache would be sth like for 2 given substrings, what are the minimum #
        # operations to change from ss1 to ss2

        cache = dict()

        def recursion(i: int, j: int) -> int:
            if i == len(word1):
                return len(word2) - j # Insert this many characters of word2 into word1

            if j == len(word2):
                return len(word1) - i # Delete this many characters of word1
            
            if (i, j) in cache:
                return cache[(i, j)]

            min_ops  = 0
            if word1[i] == word2[j]:
                min_ops = recursion(i+1, j+1)
            else:
                # 3 CHOICES
                # Replacement
                replace = recursion(i+1, j+1)
                
                # Deletion
                delete = recursion(i+1, j)

                # Insertion
                insert = recursion(i, j+1)

                min_ops = 1 + min(replace, delete, insert)
            cache[(i, j)] = min_ops
            return min_ops
        
        min_ops = recursion(0, 0)
        return min_ops