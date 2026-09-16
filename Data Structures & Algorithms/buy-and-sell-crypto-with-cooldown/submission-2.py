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