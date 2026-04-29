"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: return True

        intervals.sort(key=lambda i: i.start)

        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            j = i + 1
            while( j < len(intervals) and intervals[j].start >= end):
                end = intervals[j].end
                j += 1

            if j == len(intervals):
                return True
            else:
                return False
            




