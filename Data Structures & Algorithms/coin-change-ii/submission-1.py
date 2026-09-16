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