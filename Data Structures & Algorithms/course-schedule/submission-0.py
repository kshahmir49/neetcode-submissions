class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i:set() for i in range(numCourses)}
        for i,j in prerequisites:
            d[i].add(j)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if d[course] == []:
                return True
            visited.add(course)
            for i in d[course]:
                if not dfs(i): return False
            visited.remove(course)
            d[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True