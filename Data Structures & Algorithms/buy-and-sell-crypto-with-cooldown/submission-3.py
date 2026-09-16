from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = dict()
        cache[True] = [-1] * len(prices)
        cache[False] = [-1] * len(prices)

        def recursion(coin: bool, i: int, j_b: int) -> int:
            if i >= len(prices):
                return 0  # No profit at this window if it is over there.

            if cache[coin][i] != -1:
                return cache[coin][i]

            MP = 0
            if coin:
                for j in range(i, len(prices)):
                    if prices[j] > prices[j_b]:
                        MP = max(MP, prices[j] - prices[j_b] + recursion(False,j+2,-1))
            else:
                for j in range(i, len(prices)):
                    MP = max(MP, recursion(True,j+1,j))
            cache[coin][i] = MP
            return MP
        return recursion(False, 0, -1)

    def maxProfitBetter(self, prices: List[int]) -> int:
        dp = {}  # key=(i, buying) val=max_profit

        # This return the total profit gained so far using DFS
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)

    def maxProfitTabulation(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        # In Python True is 1, False is 0. bruh.
        for i in range(n - 1, -1, -1):
            # Cycle through all states of buying
            for buying in [True, False]:
                if buying:
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown) # max profit when allowed to buy
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][False] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown) # Max profit when holding the stock
        return dp[0][1]