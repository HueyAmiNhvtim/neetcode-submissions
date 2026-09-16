class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()     # deque of indices of elements in nums in decreasing order
        l = r = 0

        while r < len(nums):
            # Remove any element in the queue that is smaller than the element that is going to be added.
            # This is because those elements are worthless to be used for comparison!
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]: # Max element fall out of the next window
                q.popleft()

            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1
            r += 1
        return result