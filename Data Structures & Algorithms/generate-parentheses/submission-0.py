class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        result = []
        potential_valid = deque()
        potential_valid.appendleft(("", 0, 0))  # Store the candidate string and the number of left and right parentheses
                                                # used in the string, respectively

        # How do you think about the state transition...?
        # When do you know you should add the left parentheses?
        # When do you know you should close with the right parentheses?
        # So, f
        while potential_valid:
            cur_string, left_p, right_p = potential_valid.popleft()
            if left_p == n and right_p == n:
                result.append(cur_string)
            # Condition to add another left parenthesis as a step
            if left_p < n:
                potential_valid.appendleft((cur_string + "(", left_p+1, right_p))

            # Condition add a right parenthesis as transition step
            if left_p > right_p:
                potential_valid.appendleft((cur_string + ")", left_p, right_p+1))

        return result