class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1,max(piles)
        res = end
        while start<=end:
            mid = (start+end)//2
            tot = 0	
            for p in piles:
                tot+= math.ceil(p/mid)
            if tot<=h:
                res = mid
                end =mid-1
            else: start = mid+1
        return res