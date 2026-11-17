class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights) - 1
        while left < right:
            container_area = min(heights[left], heights[right]) * (right - left)
            if container_area > max_area:
                max_area = container_area
            if heights[left] < heights[right]:  # Only move the pointer where the lower value is because the area formula is dependent on the lower values
                left += 1
            else:
                right -= 1
        return max_area