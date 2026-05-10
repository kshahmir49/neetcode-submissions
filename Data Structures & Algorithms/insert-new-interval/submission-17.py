class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            print(newInterval,intervals[i])
            if ((newInterval[0]<=intervals[i][1]) and (newInterval[0]>=intervals[i][0])) or ((newInterval[1]<=intervals[i][1]) and (newInterval[1]>=intervals[i][0])):
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
            if ((intervals[i][0]<=newInterval[1]) and (intervals[i][0]>=newInterval[0])) or ((intervals[i][1]<=newInterval[1]) and (intervals[i][1]>=newInterval[0])):
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
            else:
                res.append(intervals[i])
        res.append(newInterval)
        res.sort(key=lambda x:x[0])
        return res