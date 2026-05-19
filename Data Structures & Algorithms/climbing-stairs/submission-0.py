class Solution:
    def climbStairs(self, n: int) -> int:
        d = {1:1,2:2}
        def dp(n):
            if n in d:
                return d[n]
            else:
                d[n] = dp(n-1) + dp(n-2)
                return d[n]
        return dp(n)
