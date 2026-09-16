from typing import List
from collections import deque


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cur_i = deque()
        cur_i.appendleft(0)

        while True:
            if len(cur_i)==0:
                return False

            i = cur_i.popleft()
            if i == n-1:
                return True

            for j in range(1, nums[i]+1):
                if i + j <= n-1:
                    cur_i.appendleft(i+j)
        
            