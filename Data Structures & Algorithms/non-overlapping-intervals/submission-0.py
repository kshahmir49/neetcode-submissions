class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        end = intervals[0][1]
        for i,j in intervals[1:]:
            if i>=end:
                end = j
            else:
                res += 1
                end = min(end,j)
        return res