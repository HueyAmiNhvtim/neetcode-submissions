class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        store = dict()
        store[0] = 0
        num_coins = self.coin_change_recursion(coins, amount, len(coins) - 1, store)


        return num_coins

    def coin_change_recursion(self, coins: List[int], amount: int, current_coin_index: int, cache: dict) -> int:
        if amount == 0:
            return 0
        # Too much coins of a type. Return -1 for an infeasible solution
        if amount < 0:
            return -1

        # Exhaust all options. Return -1 for an infeasible solution
        if current_coin_index == -1:
            return -1

        if amount not in cache:
            retain = self.coin_change_recursion(coins, amount - coins[current_coin_index], current_coin_index, cache)
            skip_coin = self.coin_change_recursion(coins, amount, current_coin_index - 1, cache)

            if retain == -1 or skip_coin == -1:
                if retain >= 0:
                    cache[amount] = 1 + retain
                elif skip_coin >= 0:
                    cache[amount] = skip_coin
                else:
                    cache[amount] = -1
            else:
                cache[amount] = min(1 + retain, skip_coin)
        return cache[amount]