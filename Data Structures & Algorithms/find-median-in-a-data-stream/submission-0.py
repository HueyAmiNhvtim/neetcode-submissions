import heapq


class MedianFinder:
    def __init__(self):
        self.vals = []

    def addNum(self, num: int) -> None:
        self.vals.append(num)

    def findMedian(self) -> float:
        self.vals = sorted(self.vals)
        if len(self.vals) % 2 == 1:
            return self.vals[len(self.vals) // 2]
        else:
            left = self.vals[len(self.vals)//2-1] 
            right = self.vals[len(self.vals)//2]
            return (left+right) / 2