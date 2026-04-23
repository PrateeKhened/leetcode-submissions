class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for p in points:
            d = (p[0] ** 2 + p[1] ** 2) ** 0.5
            heapq.heappush(max_heap, (-d, p))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [p[1] for p in max_heap]