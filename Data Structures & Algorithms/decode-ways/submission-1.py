class Solution:
    def numDecodings(self, s: str) -> int:
        result = 0


        # We know that you can only reach to at maximum 2 digits.
        # And you cannot start at digit 0.
        store = dict()
        result = self.numDecodingsRecurse(0, s, cache=store)

        return result

    def numDecodingsRecurse(self, i: int, s: str, cache: dict) -> int:
        if i >= len(s):
            cache[i] = 1
            return 1

        if s[i] == "0":
            return 0

        if i not in cache:
            # Convert now
            convert_now_result = self.numDecodingsRecurse(i + 1, s, cache)
            convert_later_result = 0

            if i + 1 < len(s):
                concatenated = int(s[i] + s[i+1])
                if concatenated <= 26:
                    convert_later_result = self.numDecodingsRecurse(i + 2, s, cache)
            cache[i] = convert_now_result + convert_later_result
        return cache[i]