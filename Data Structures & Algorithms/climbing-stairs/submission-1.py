from collections import deque

class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = dict() # Map stairs to number of steps
        return self.climbStairsRecurse(n, stairs)
 
    def climbStairsRecurse(self, n, steps_dict):
        if n == 1:
            steps_dict[n] = 1
            return 1
        if n == 2:
            steps_dict[n] = 2
            return 2
        
        if n in steps_dict:
            return steps_dict[n]
        else:
            steps = self.climbStairsRecurse(n-1, steps_dict) + self.climbStairsRecurse(n-2, steps_dict)
            steps_dict[n] = steps
            return steps