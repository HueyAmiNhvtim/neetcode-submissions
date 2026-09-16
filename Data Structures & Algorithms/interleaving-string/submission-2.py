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