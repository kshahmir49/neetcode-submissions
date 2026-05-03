from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        deq = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh +=1     
                if grid[i][j] == 2:
                    deq.append((i,j))
        time = 0
        while deq and fresh>0:
            for _ in range(len(deq)):
                x,y = deq.popleft()
                for a,b in dirs:
                    nx, ny = x+a, y+b
                    if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != 1:
                        continue
                    grid[x+a][y+b]=2
                    fresh-=1
                    deq.append((x+a,y+b))
            time+=1
        
        return time if fresh==0 else -1
        