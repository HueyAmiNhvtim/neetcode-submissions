from heapq import heapify, heappush, heappop


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # min_heap with K Largest integers
        self.min_heap, self.k = nums, k
        heapify(self.min_heap)

        # Continously popping the element off the heap until the heap contains only k-th element.
        # Therefore, the minimum element in the heap is guaranteed to be the kth largest element!
        while len(self.min_heap) > self.k:
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]
        
