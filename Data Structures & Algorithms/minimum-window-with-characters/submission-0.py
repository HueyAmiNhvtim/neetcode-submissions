class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        res, res_len = [-1, -1], float("inf")
        matches = 0
        count_t = dict()
        count_s = dict()

        for i in range(len(t)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        l = 0

        for r in range(0, len(s)):
            c = s[r]
            count_s[c] = count_s.get(c, 0) + 1
            if c in count_t and count_s[c] == count_t[c]:
                matches += 1

            while matches == len(count_t):
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    matches -= 1
                l += 1
        l, r = res
        if res_len != float("inf"):
            return s[l:r+1]
        else:
            return ""