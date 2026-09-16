from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Choose the last balloon to burst in a subarray
        # Why this helps:
        #     If balloon i is the last one to burst between indices l and r, then at that moment:
        #         everything inside (l..r) except i is already gone
        #         the neighbors of i are fixed: nums[l - 1] on the left and nums[r + 1] on the right
        #     So the coins gained from bursting i last are:
        #         nums[l - 1] * nums[i] * nums[r + 1]
        #     And the remaining work splits cleanly into two independent parts:
        #         best coins from (l..i-1)
        #         best coins from (i+1..r)

        # This creates overlapping subproblems, so we store results in a memo table dp keyed by (l, r).
        # Maybe the cache will store 
        nums = [1] + nums + [1]  # Add 1 to the edges of the list so that
                                 # we don't have to constantly check for boundaries!
        cache = dict()
        n = len(nums)
        def recursion(l: int, r: int):
            if l > r:
                return 0
            
            if (l, r) in cache:
                return cache[(l, r)]
            res = 0
            for i in range(l, r+1):
                # Since we consider coin at i to be the last popped one within
                # l and r range (inclusive), we know the neighbor of nums[i] is l-1 and r+1 !
                coins = nums[l-1] * nums[i] * nums[r+1]
                # Now we have 2 distinct subproblems that do not overlap with one another!
                # And those subproblems can reappear multiple times! => easy cache solution!
                coins += recursion(l, i-1) + recursion(i+1, r)
                res = max(res, coins)
            cache[(l, r)] = res
            return res
            
        max_coin = recursion(1, n-2)
        return max_coin