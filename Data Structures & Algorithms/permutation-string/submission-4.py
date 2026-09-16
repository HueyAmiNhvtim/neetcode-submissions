class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_freq = dict()
        for i in range(len(s1)):
            window_freq[s1[i]] = window_freq.get(s1[i], 0) + 1
        
        l, r = 0, 0
        while l < len(s2) and r < len(s2):
            if s2[r] in window_freq:
                window_freq[s2[r]] -= 1
                if window_freq[s2[r]] < 0: # Too many count of one letter compared to s1, move l until stabilized
                    while window_freq[s2[r]] < 0:
                        window_freq[s2[l]] += 1
                        l += 1
                r += 1
            else: # A lone character not in s1 is in the window. Window is useless now. Move l, r to r + 1
                while l < r + 1 and l < len(s2):
                    if s2[l] in window_freq:
                        window_freq[s2[l]] += 1
                    l += 1
                r = l
            
            if sum(window_freq.values()) == 0:
                return True
        return False
