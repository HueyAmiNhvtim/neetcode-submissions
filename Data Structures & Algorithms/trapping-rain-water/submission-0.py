class Solution:
    def trap(self, height: List[int]) -> int:
        # Ok...how do we save the results so that next iteration doesn't have to waste time checking for the same lgh and rgh?
        max_area_wata = 0
        lgh_rgh_arr = []
        for i in range(len(height)):
            # Get greater elements on both sides of height i
            l, r = i - 1, i + 1
            if len(lgh_rgh_arr) > 0 and height[i] < lgh_rgh_arr[-1][0] and height[i] < lgh_rgh_arr[-1][1]:
                lgh, rgh = lgh_rgh_arr[-1][0], lgh_rgh_arr[-1][1]
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
                lgh_rgh_arr.append(tuple([lgh, rgh]))

            if lgh == 0 or rgh == 0:
                max_area_wata += 0
            else:
                max_area_wata += min(lgh, rgh) - height[i]
        return max_area_wata
        