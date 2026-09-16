class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0
        count = 0
        l1, l2 = 0, 0
        result = []
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] <= nums2[l2]:
                result.append(nums1[l1])
                l1 += 1
            else:
                result.append(nums2[l2])
                l2 += 1

        if l1 == len(nums1):
            result += nums2[l2:]
        elif l2 == len(nums2):
            result += nums1[l1:]
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            median = (result[total_len // 2] + result[total_len //2 - 1]) / 2
        else:
            median = result[total_len // 2]
        return median