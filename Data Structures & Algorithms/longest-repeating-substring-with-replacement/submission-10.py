class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        d = {}
        res = 0
        while r<len(s):
            d[s[r]] = 1 + d.get(s[r],0)
            length = r-l+1
            f = max(d.values())
            if length - f > k:
                d[s[l]] -= 1
                l+=1
            length = r-l+1
            res = max(res,length)
            print(l,r,res)
            r+=1
        return res

        