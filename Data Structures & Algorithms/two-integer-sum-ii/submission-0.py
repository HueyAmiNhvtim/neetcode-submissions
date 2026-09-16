class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = [0, 0]
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target: # If bigger, decrease.
                right -= 1
            elif numbers[left] + numbers[right] < target: # If smaller, increase
                left += 1
            else:
                indices = [left+1, right+1]
                break
        return indices