import collections
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        l=0
        while l<len(temperatures):
            while stack and temperatures[l]>stack[-1][1]:
                idx, temp = stack.pop()
                res[idx] = l - idx
            stack.append([l,temperatures[l]])
            l+=1
        return res