class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        if not intervals:
            return [] 
        intervals.sort(key = lambda x : x[0] - x[1] + 1)
        res = [] 
        for q in queries:
            subRes = float("inf")
            for i in range(len(intervals)):
                if intervals[i][0] <= q <= intervals[i][1]:
                    subRes = min(subRes, intervals[i][1] - intervals[i][0] + 1)
            if subRes != float("inf"):
                res.append(subRes)
            else:
                res.append(-1)
        return res