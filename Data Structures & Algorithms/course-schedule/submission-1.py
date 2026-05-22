class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # d = {i:set() for i in range(numCourses)}
        # for i,j in prerequisites:
        #     d[i].add(j)
        # visited = set()
        # def dfs(course):
        #     if course in visited:
        #         return False
        #     if d[course] == []:
        #         return True
        #     visited.add(course)
        #     for i in d[course]:
        #         if not dfs(i): return False
        #     visited.remove(course)
        #     d[course] = []
        #     return True
        # for i in range(numCourses):
        #     if not dfs(i): return False
        # return True

        d = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            d[i].append(j)
        visited = set()
        memo = {}
        def dfs(course):
            if d[course] == []:
                return True
            if course in visited:
                return False
            if course in memo:
                return memo[course]
            visited.add(course)
            res = True
            for i in d[course]:
                if not dfs(i): return False
                memo[i] = res
            visited.remove(course)
            return True
        res = True
        for i in range(numCourses):
            res = res and dfs(i)
        return res