import heapq

class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [(timestamp,value)]
        else:
            self.time_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        else:
            left,right=0,len(self.time_map[key])-1
            res = ""
            while left<=right:
                mid = (left+right)//2
                if self.time_map[key][mid][0] <= timestamp:
                    res = self.time_map[key][mid][-1]
                    left = mid + 1
                else:
                    right = mid - 1
            return res
