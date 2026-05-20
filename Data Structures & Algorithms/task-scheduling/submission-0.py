import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        q = [-i for i in c.values()]
        heapq.heapify(q)
        deq = deque()
        time = 0
        while q or deq:
            time += 1
            if q:
                cnt = 1+ heapq.heappop(q)
                if cnt:
                    deq.append((cnt,time+n))
            if deq and deq[0][1]==time:
                el = deq.popleft()
                heapq.heappush(q,el[0])
        return time
