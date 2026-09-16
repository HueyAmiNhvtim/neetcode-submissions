from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # So the cache would probably be the number of combinations
        # for a given amount of value.

        # At each step, you can either add more of the same coin
        # or move onto the next coin
        amount_cache = dict()
        def recursion(amount, i):
            if amount == 0:
                return 1 # Confirmation of a combination
            
            if (amount, i) in amount_cache:
                return amount_cache[(amount, i)]

            if i >= len(coins) or amount < 0:
                return 0
            # stay
            stay_combo = recursion(amount - coins[i], i)
            move_on = recursion(amount, i+1)
            total = stay_combo + move_on
            amount_cache[(amount, i)] = total
            return total
        
        return recursion(amount, 0)

    def changeTabulation(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort() # Sorted to avoid duplicate combinations and maintain consistent order

        cache = [[0] * (amount + 1) for _ in range(n+1)]
        # dp[i][a]: # ways to form amount a using coins from index i onwards
        # The possible combo of each coin needed to reach 0 is 1
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(n-1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]: 
                    dp[i][a] = dp[i+1][a]
                    dp[i][a] += dp[i][a-coins[i]]

        return dp[0][amount]