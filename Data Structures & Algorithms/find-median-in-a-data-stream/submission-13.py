import heapq


#  You should aim for a solution with O(logn) time for addNum(), 
# O(1) time for findMedian(), and O(n) space, where n is the current number of elements. 

# ok, think of a way to use heap.

# both left and partition has to be sorted....being sth like two branches of a binary search tree.
# exactly like what a heap is: a flattened tree.

class MedianFinder:
    def __init__(self):
        # Separate the list using two heaps.....one that is minheap for the right partition.
        #                                                                           another that is maxheap for the left partition.
        #                                                                           That's for the even-length case...
        # For odd case....the element is from the half of larger size.... Yeah, that makes sense?
        self.l_p = []   # Left partition: Maxheap
        self.r_p = []   # Right partition: Minheap.

    def addNum(self, num: int) -> None:
        # Ok, how do you consistently deal with the stream of numbers....?
        # How do you know which partition a number belongs to? 
        # If bigger than the maximum value in the left heap, push into right_partition min_heap instead.
        if self.l_p and num > self.l_p[0]: 
            heapq.heappush(self.r_p, num)
        else:
            heapq.heappush_max(self.l_p, num)

        # Rebalance:
        if len(self.l_p) > len(self.r_p) + 1:
            val = heapq.heappop_max(self.l_p)
            heapq.heappush(self.r_p, val)
        if len(self.r_p) > len(self.l_p) + 1:
            val = heapq.heappop(self.r_p)
            heapq.heappush_max(self.l_p, val)
        return


    def findMedian(self) -> float:
        if len(self.l_p) > len(self.r_p):
            return self.l_p[0]
        elif len(self.r_p) > len(self.l_p):
            return self.r_p[0]
        else:
            return (self.l_p[0] + self.r_p[0]) /  2