class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using division version
        prefixes_prods = [1 for i in range(len(nums))]
        suffixes_prods = [1 for i in range(len(nums))]
        result = []
        for i in range(1, len(nums)):
            prefixes_prods[i] = prefixes_prods[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            suffixes_prods[i] = suffixes_prods[i+1] * nums[i+1]

        for i in range(len(nums)):
            result.append(prefixes_prods[i] * suffixes_prods[i])

        return result