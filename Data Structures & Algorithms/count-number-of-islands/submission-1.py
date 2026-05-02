from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visit = set()    
        
        # with bfs
        deq = deque()
        def bfs(i,j):
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]
            deq.append((i,j))
            while deq:
                l,r = deq.popleft()
                for a,b in dirs:
                    if (a+l) in range(len(grid)) and (b+r) in range(len(grid[0])) and grid[a+l][b+r]=="1" and (a+l,b+r) not in visit:
                        visit.add((a+l,b+r))
                        deq.append((a+l,b+r))

        # with dfs
        stack = []
        def dfs(i,j):
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]
            stack.append((i,j))
            while stack:
                l,r = stack.pop()
                for a,b in dirs:
                    if (a+l) in range(len(grid)) and (b+r) in range(len(grid[0])) and grid[a+l][b+r]=="1" and (a+l,b+r) not in visit:
                        visit.add((a+l,b+r))
                        stack.append((a+l,b+r))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visit:
                    visit.add((i,j))
                    dfs(i,j)
                    count+=1
        return count

        