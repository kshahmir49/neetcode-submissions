"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()
        max_count = 0
        count = 0
        s,e = 0,0
        while s<len(start) and e<len(end):
            if start[s]<end[e]:
                count+=1
                max_count = max(max_count,count)
                s+=1
            else:
                count-=1
                e+=1
        return max_count