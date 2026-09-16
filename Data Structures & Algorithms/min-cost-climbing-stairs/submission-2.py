class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        cost_dict = dict()
        min_cost = min(self.minCostClimbingStairsRecurse(len(cost) - 1, cost, cost_dict), self.minCostClimbingStairsRecurse(len(cost)-2, cost, cost_dict))
        return min_cost

    def minCostClimbingStairsRecurse(self, step: int, cost: List[int], min_cost_dict: dict[int, int]) -> int:
        if step <= 1:
            return cost[step]

        if min_cost_dict.get(step) is None:
            min_cost_dict[step] = cost[step]+ min(self.minCostClimbingStairsRecurse(step-1, cost, min_cost_dict),
                                                  self.minCostClimbingStairsRecurse(step-2, cost, min_cost_dict))

        return min_cost_dict[step]        