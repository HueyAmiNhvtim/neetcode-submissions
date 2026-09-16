class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dicts = dict()
        result = []
        for s in strs:
            freq_dicts[s] = self.freq_dict(s)  # O(m) space

        i = 0
        while i < len(strs):
            s = strs[i]
            count_s = freq_dicts[s]
            counted_in = False
            for group in result:
                if count_s == freq_dicts[group[0]]:
                    group.append(s)
                    counted_in = True
            if not counted_in:
                result.append([s])
            i += 1
        return result

    def freq_dict(self, s: str) -> dict:
        count_s = dict()
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        return count_s