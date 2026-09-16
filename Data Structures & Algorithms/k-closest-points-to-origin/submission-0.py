from heapq import heappush, heappop
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        result = []

        for i in range(len(points)):
            neg_distances = -sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            heappush(distances, [neg_distances, points[i]])

        while len(distances) > k:
            heappop(distances)

        for entries in distances:
            result.append(entries[1])

        return result        