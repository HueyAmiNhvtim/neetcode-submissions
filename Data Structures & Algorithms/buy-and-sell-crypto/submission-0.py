class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left = buy, right = sell
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:  # If future price is higher than current sell price date
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
            else:  # Update left pointer to the right point because we found a new lower price point to potentially buy
                l = r
            r += 1

        return max_profit