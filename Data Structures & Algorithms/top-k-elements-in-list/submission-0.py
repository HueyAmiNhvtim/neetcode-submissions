class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_num = dict()
        for num in nums:
            count_num[num] = count_num.get(num, 0) + 1
        heap = [(count, num) for num, count in count_num.items()]
        heapq.heapify(heap)
        k_biggest = heapq.nlargest(k, heap, lambda x: x[0])
        result = [res[1] for res in k_biggest]
        return result