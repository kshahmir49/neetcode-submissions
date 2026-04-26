class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1 = {}
        for i in t:
            d1[i] = 1 + d1.get(i,0)
        l,r=0,0
        d2 = {i:0 for i in d1.keys()}
        while l<len(s)-len(t) and s[l] not in d2.keys():
            l+=1
            r+=1
        res = "*"*1001
        prev_r = -1
        while r<len(s):
            if s[r] in d2.keys() and r!=prev_r:
                d2[s[r]] += 1
            valid = True
            prev_r = r
            for i in d2.keys():
                if d2[i] < d1[i]:
                    valid = False
            if not valid:
                r+=1
            else:
                res = s[l:r+1] if len(s[l:r+1]) < len(res) else res
                print(l,r,res,d2)
                if s[l] in d2.keys():
                    d2[s[l]] -= 1
                l+=1
                while l<len(s)-len(t) and s[l] not in d2.keys():
                    l+=1
        return res if res!="*"*1001 else ""
            