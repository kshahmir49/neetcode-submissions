class Solution:
    def isValid(self, s: str) -> bool:
        d = []
        for i in s:
            if d and ((d[-1]=="(" and i==")") or (d[-1]=="{" and i=="}") or (d[-1]=="[" and i=="]")):
                d.pop()
            else:
                d.append(i)
        return not d