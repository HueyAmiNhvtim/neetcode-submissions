class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            string = strs[i]
            # Number of letters followed by the # delimiter. When decoding, the thing will read the number of letter,
            # then read the delimiter to make sure it's valid, then extract the read number of letters followed after.
            encoded += f"{len(string)}#{string}"
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        if len(s) == 1:
            return result  # Invalid encoded message
        i = 0
        while i < len(s):
            if s[i].isdigit():
                str_len = ""
                # Continually scan for the digit and stop if reaching the delimiter:
                while s[i] != "#":
                    str_len += s[i]
                    i += 1
                steps = int(str_len)
                result.append(s[i+1:i+1+steps])
                i += 1 + steps
        return result
