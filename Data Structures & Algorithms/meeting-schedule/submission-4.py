"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res = []
        for i in range(len(intervals)):
            res.append([intervals[i].start,intervals[i].end])
        res.sort(key=lambda i:i[0])
        for i in range(1,len(res)):
            if res[i-1][1]>res[i][0]:
                return False
        return True