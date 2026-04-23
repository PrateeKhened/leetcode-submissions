class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for p in points:
            dist = ((p[0] ** 2) + (p[1] ** 2)) ** 0.5
            heapq.heappush(minHeap, (dist, p))
        
        res = []
        while k > 0:
            _, p = heapq.heappop(minHeap)
            res.append(p)
            k -= 1
        return res