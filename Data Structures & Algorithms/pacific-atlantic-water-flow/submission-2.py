from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        res = []
        def dfs(i,j):
            deq = deque()
            deq.append((i,j))
            pac = False
            atl = False
            visited = set()
            while deq:
                a,b = deq.pop()
                if (a,b) not in visited:
                    visited.add((a,b))
                if (a == 0 and b in range(len(heights[0]))) or (a in range(len(heights)) and b==0):
                    pac = True
                if (a == len(heights)-1 and b in range(len(heights[0]))) or (a in range(len(heights)) and b==len(heights[0])-1):
                    atl = True
                if (a,b)==(2,0):
                    print(pac,atl)
                if pac and atl:
                    return True
                for x,y in dirs:
                    if (a+x) in range(len(heights)) and (b+y) in range(len(heights[0])) and heights[a][b]>=heights[a+x][b+y] and (a+x,b+y) not in visited:
                        deq.append((a+x,b+y))
            return False
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if dfs(i,j): res.append([i,j])
        return res