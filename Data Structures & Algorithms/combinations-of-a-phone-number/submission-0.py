class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        result = []
        # Dictionary mapping number to the string of characters it could represent
        num_to_chars_str = ["+", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        # Implicitly map number to the potential list of characters it could represent
        potential_combination = deque()
        # Add initial state
        potential_combination.appendleft((f"", 0))

        while potential_combination:
            cur_str, cur_pos = potential_combination.popleft()
            if cur_pos == len(digits):
                result.append(cur_str)
                continue

            digit = int(digits[cur_pos])
            for i in range(len(num_to_chars_str[digit])):
                # State transition, just move onto the next digit
                potential_combination.appendleft((cur_str + f"{num_to_chars_str[digit][i]}", cur_pos+1))

        return result        