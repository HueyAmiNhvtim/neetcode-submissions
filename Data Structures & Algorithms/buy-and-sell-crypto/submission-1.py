class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 # Left is buy, right is sell
        max_profit = 0
        while left < right and right < len(prices): 
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right]-prices[left])
                right += 1
            else: # if prices is either smaller or equal to the current buying price
                  # Move left to right pointer, and increment right pointer by 1
                left = right
                right += 1
        return max_profit