class Solution:
    def trap(self, height: List[int]) -> int:
        # Ok...how do we save the results so that next iteration doesn't have to waste time checking for the same lgh and rgh?
        max_area_wata = 0
        lgh_max, rgh_max = 0, 0
        for i in range(len(height)):
            # Get greater elements on both sides of height i
            l, r = i - 1, i + 1
            if height[i] < lgh_max and height[i] < rgh_max:
                lgh, rgh = lgh_max, rgh_max
            else:
                lgh, rgh = 0, 0
                while l > -1:
                    if height[l] > height[i] and height[l] > lgh:
                        lgh = height[l]
                    l -= 1

                while r < len(height):
                    if height[r] > height[i] and height[r] > rgh:
                        rgh = height[r]
                    r += 1
                lgh_max, rgh_max = lgh, rgh

            if lgh == 0 or rgh == 0:
                max_area_wata += 0
            else:
                max_area_wata += min(lgh, rgh) - height[i]
        return max_area_wata
        