"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.end)
        memo = []
        memo.append(intervals[0])

        for i in range(1,len(intervals)):
            if intervals[i].start < memo[i-1].end:
                return False
            memo.append(intervals[i])
        return True
