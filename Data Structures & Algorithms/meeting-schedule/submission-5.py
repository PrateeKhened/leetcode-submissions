"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        if not intervals:
            return True
        for i in intervals:
            print(i.start, i.end)
        prev = intervals[0].end
        for i in range(1, len(intervals)):
            s, e = intervals[i].start, intervals[i].end
            if s < prev:
                return False 
            prev = e
        return True 