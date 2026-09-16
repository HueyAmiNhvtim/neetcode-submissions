class Solution:
    def climbStairs(self, n: int) -> int:
        step_dict = dict()
        return self.climbingStairsRecurse(n, step_dict)

    def climbingStairsRecurse(self, n: int, step_dict: dict[int, int]) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n not in step_dict:
            step_dict[n] = self.climbingStairsRecurse(n - 1, step_dict) + self.climbingStairsRecurse(n - 2, step_dict)
        return step_dict[n]