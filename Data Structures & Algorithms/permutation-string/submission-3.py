class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        for i in s1:
            d1[i] = 1 + d1.get(i,0)
        for i in range(len(s2)-len(s1)+1):
            d2 = {}
            for j in range(i,i+len(s1)):
                d2[s2[j]] = 1 + d2.get(s2[j],0)
            if d1==d2:
                return True
        return False
