import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            if len(heap) < k:
                heapq.heappush(heap, (-dist, point))
            else:
                heapq.heappushpop(heap, (-dist, point))
        return [i[1] for i in heap]

    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        """One-liner naive solution, terrible performance"""
        return sorted(points, key=lambda i: i[0] ** 2 + i[1] ** 2)[:k]
