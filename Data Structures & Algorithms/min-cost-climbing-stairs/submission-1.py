


class Solution:
    def minCostClimbingStairs(self, cost:List[int]) -> int:
        cache = dict()
        cost = min(self.minCostRecursion(cost, 0, cache), self.minCostRecursion(cost, 1, cache))
        return cost

    def minCostRecursion(self, cost: List[int], i, cache: dict):
        if i >= len(cost):
            return 0
        
        # ok, so how do you cache the result?
        # So, the cache will store the minimum cost at the i-th index?
        
        if i in cache:
            return cache[i]

        take_one_step = self.minCostRecursion(cost, i+1, cache)
        take_two_step = self.minCostRecursion(cost, i+2, cache)
        cache[i] = cost[i] + min(take_one_step, take_two_step) 
        
        return cache[i]